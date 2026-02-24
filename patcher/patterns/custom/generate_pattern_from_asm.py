#!/usr/bin/env python3
"""
AI-generated script to parse PowerPC assembly from objdump and generate PatchPattern objects.
still needs a lot of work for full automation, but good enough to remove most manual work

for compiling the out.s use:
cargo build --release
${DEVKITPPC}/bin/powerpc-eabi-objdump -Drh target/powerpc-unknown-eabi/release/libcustom_functions.a > out.s
"""

import re
import sys
from pathlib import Path


class DisassemblyParser:
    def __init__(self, asm_file_path):
        self.asm_file_path = Path(asm_file_path)
        self.object_files = []  # List of object file contexts
        self.current_object = None
        self.current_section = None
        self.current_function = None
        self.current_data_section = None

    def parse(self):
        """Parse the disassembly file."""
        # Try to read with UTF-16 first, fallback to UTF-8
        try:
            with open(self.asm_file_path, 'r', encoding='utf-16') as f:
                content = f.read()
        except:
            try:
                with open(self.asm_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                print("Error: Cannot read file with UTF-16 or UTF-8 encoding")
                return

        lines = content.split('\n')

        for line_num, line in enumerate(lines, 1):
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Detect object file header: "filename.o:     file format elf32-powerpc"
            obj_match = re.match(r'^(.+\.o):\s+file format\s+(.+)$', line)
            if obj_match:
                obj_name = obj_match.group(1)
                file_format = obj_match.group(2)
                self.current_object = {
                    'name': obj_name,
                    'format': file_format,
                    'sections': {},
                    'functions': [],
                    'data_sections': {}
                }
                self.object_files.append(self.current_object)
                self.current_section = None
                self.current_function = None
                self.current_data_section = None
                continue

            # Detect section header: "Disassembly of section .text.functionName:"
            section_match = re.match(r'^Disassembly of section (.+):\s*$', line)
            if section_match:
                self.current_section = section_match.group(1)
                continue

            # Detect function start: looks like "00000000 <functionName>:"
            func_match = re.match(r'^[0-9a-fA-F]+\s+<([^>]+)>:\s*$', line)
            if func_match:
                func_name = func_match.group(1)
                # Skip section headers, data sections, and buffers
                # Data sections typically start with . or contain certain keywords
                is_data_section = (
                        func_name.startswith('.') or
                        func_name.endswith('_buffer') or
                        func_name.endswith('_data') or
                        'rodata' in func_name.lower() or
                        'comment' in func_name.lower() or
                        '.data' in func_name.lower() or
                        '.bss' in func_name.lower()
                )

                if not is_data_section:
                    self.current_function = {
                        'name': func_name,
                        'instructions': [],
                        'section': self.current_section,
                        'object_file': self.current_object['name'] if self.current_object else None
                    }
                    if self.current_object:
                        self.current_object['functions'].append(self.current_function)
                    self.current_data_section = None
                else:
                    # Track data section
                    self.current_function = None
                    self.current_data_section = func_name
                    if self.current_object and func_name not in self.current_object['data_sections']:
                        self.current_object['data_sections'][func_name] = []
                continue

            # Parse instruction line
            # Format: "  offset: hex bytes  instruction  # comment"
            # Example: "   0:  7c 08 02 a6   mflr r0"
            # Hex bytes and instruction are separated by tab(s) in objdump output
            inst_match = re.match(r'^\s*([0-9a-fA-F]+):\s+([0-9a-fA-F ]+)\t+(.+?)(?:\s*$)', line)
            if inst_match:
                offset = inst_match.group(1)
                hex_bytes = inst_match.group(2).replace(' ', '')
                instruction = inst_match.group(3).strip()

                # Handle data sections
                if self.current_data_section and self.current_object:
                    # Skip .long pseudo-instructions and just store hex
                    if '.long' in instruction or '...' in instruction:
                        # Store the data bytes
                        if hex_bytes and len(hex_bytes) == 8:
                            self.current_object['data_sections'][self.current_data_section].append(
                                {
                                    'offset': offset,
                                    'hex': hex_bytes
                                }
                            )
                    continue

                # Handle code functions
                if self.current_function:
                    # Skip .long pseudo-instructions in data sections
                    if '.long' in instruction:
                        continue

                    inst_data = {
                        'offset': offset,
                        'hex': hex_bytes,
                        'instruction': instruction,
                        'relocation': None
                    }

                    self.current_function['instructions'].append(inst_data)
                    continue

            # Check for relocation lines (they have R_PPC in them and tabs/lots of whitespace)
            if 'R_PPC' in line and self.current_function and self.current_function['instructions']:
                self._process_relocation(line, self.current_function['instructions'][-1])

    def _process_relocation(self, reloc_line, instruction):
        """Process relocation information and attach to instruction."""
        # Extract relocation type and symbol
        # Format: "R_PPC_REL24  symbolName" or "e: R_PPC_ADDR16_HA  symbol"
        reloc_match = re.search(r'R_PPC_(\w+)\s+(.+)', reloc_line)
        if not reloc_match:
            return

        reloc_type = reloc_match.group(1)
        symbol = reloc_match.group(2).strip()

        instruction['relocation'] = {
            'type': reloc_type,
            'symbol': symbol
        }

    def _sanitize_variable_name(self, name):
        """Convert function name to valid Python variable name."""
        # Replace common problematic characters
        sanitized = name.replace('.', '_')
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', sanitized)

        # Ensure it doesn't start with a number
        if sanitized and sanitized[0].isdigit():
            sanitized = '_' + sanitized

        # Handle empty result
        if not sanitized:
            sanitized = 'unnamed_function'

        return sanitized

    def _get_object_prefix(self, object_name):
        """
        Generate a short prefix from object file name for namespacing.
        Example: 'custom_functions-...cgu.0.rcgu.o' -> 'custom_functions_cgu0'
        """
        # Extract meaningful parts before hash
        # Pattern: name-hash.name.hash-cgu.N.rcgu.o -> name_cguN
        match = re.match(r'([^-]+)', object_name)
        if match:
            base = match.group(1)
        else:
            base = object_name.replace('.o', '')

        # Find cgu number
        cgu_match = re.search(r'cgu\.(\d+)', object_name)
        if cgu_match:
            return f"{self._sanitize_variable_name(base)}_cgu{cgu_match.group(1)}"

        return self._sanitize_variable_name(base)

    def _parse_symbol_with_offset(self, symbol):
        """
        Parse a symbol that may have an offset like 'symbol+0x4'.
        Returns: (base_symbol, offset_hex, target_identifier)

        target_identifier calculation:
        - Each data word is 4 bytes
        - Identifiers start at 1
        - So offset 0x0 -> identifier 1, offset 0x4 -> identifier 2, etc.
        """
        # Check for offset pattern like "symbol+0x4"
        offset_match = re.match(r'(.+?)\+0x([0-9a-fA-F]+)$', symbol)
        if offset_match:
            base_symbol = offset_match.group(1)
            offset_hex = offset_match.group(2)
            offset_bytes = int(offset_hex, 16)
            # Calculate target identifier: offset / 4 + 1 (since identifiers start at 1)
            target_identifier = (offset_bytes // 4) + 1
            # Strip section prefix from base_symbol
            base_symbol = self._strip_section_prefix(base_symbol)
            return base_symbol, offset_hex, target_identifier
        else:
            # No offset, target identifier is 1
            # Strip section prefix
            symbol = self._strip_section_prefix(symbol)
            return symbol, None, 1

    def _strip_section_prefix(self, symbol):
        """
        Strip section prefixes like '.text.unlikely.' from symbol names.
        Examples:
        - '.text.unlikely._ZN4core...' -> '_ZN4core...'
        - '.text._ZN4core...' -> '_ZN4core...'
        - 'regular_symbol' -> 'regular_symbol'
        """
        # Match section patterns like .text.something.functionName
        section_match = re.match(r'^\.(?:text|rodata|data|bss)(?:\.[^.]+)?\.(.+)$', symbol)
        if section_match:
            return section_match.group(1)
        return symbol

    def _detect_instruction_relocation(self, inst_text, hex_bytes):
        """Detect relocation based on instruction type."""
        inst_lower = inst_text.lower()

        # Branch and link
        if inst_lower.startswith('bl '):
            target = inst_text.split(None, 1)[1].strip() if len(inst_text.split(None, 1)) > 1 else ""

            # Skip if empty
            if not target:
                return None

            # Extract function name from different formats:
            # Format 1: "bl memcpy" - direct name
            # Format 2: "bl 5c <print_archipelago_text+0x5c>" - local offset, ignore
            # Format 3: "bl c <memcpy>" - external function with offset
            if '<' in target and '>' in target:
                # Extract what's inside the angle brackets
                match = re.search(r'<([^>]+)>', target)
                if match:
                    inner = match.group(1)
                    # If it contains '+' it's a local offset like "print_archipelago_text+0x5c", skip it
                    if '+' in inner:
                        return None
                    # Otherwise it's a function name like "memcpy"
                    target = inner

            # Check if it's a symbolic target (not a hex address)
            if target and not target.startswith('0x') and not (target[0].isdigit() and len(target) <= 4):
                return {'type': 'bl', 'target': target}

        # Load immediate shifted
        if inst_lower.startswith('lis '):
            match = re.match(r'lis\s+r(\d+),\s*(.+?)(?:@ha?)?$', inst_lower)
            if match:
                register = int(match.group(1))
                target = match.group(2).strip()
                if not target.startswith('0x') and not target.lstrip('-').isdigit():
                    return {'type': 'lis', 'register': register, 'target': target}

        # OR immediate
        if inst_lower.startswith('ori '):
            match = re.match(r'ori\s+r(\d+),\s*r\d+,\s*(.+?)(?:@l)?$', inst_lower)
            if match:
                register = int(match.group(1))
                target = match.group(2).strip()
                if not target.startswith('0x') and not target.isdigit():
                    return {'type': 'ori', 'register': register, 'target': target}

        return None

    def generate_patch_patterns(self):
        """Generate PatchPattern code for all functions, organized by object file."""
        all_outputs = []

        for obj in self.object_files:
            outputs = []

            # Add comment header for this object file
            outputs.append(f"# From object file: {obj['name']}")
            outputs.append(f"# Format: {obj['format']}\n")

            # Build a set of all function names in THIS object for reference checking
            self.function_names = {func['name'] for func in obj['functions'] if func['instructions']}

            # Track all referenced symbols within THIS object
            self.referenced_symbols = set()
            self.symbol_name_map = {}  # Map stripped_name -> original_name for data sections
            self.data_sections = obj['data_sections']  # Use this object's data sections

            # Get object file prefix for namespacing
            obj_prefix = self._get_object_prefix(obj['name'])

            for func in obj['functions']:
                if not func['instructions']:
                    continue

                output = []
                # Create a valid Python variable name from function name with object prefix
                var_name = f"{obj_prefix}_{self._sanitize_variable_name(func['name'])}"
                output.append(f'{var_name} = PatchPattern(')
                output.append(f'    name=f"{obj_prefix}_{func["name"]}",')
                output.append("    patchMapJP=[")

                for idx, inst in enumerate(func['instructions'], start=1):
                    hex_bytes = inst['hex']
                    instruction = inst['instruction']
                    reloc_info = inst['relocation']

                    # Check for relocation from objdump
                    if reloc_info:
                        reloc_type = reloc_info['type']
                        symbol = reloc_info['symbol']

                        if reloc_type == 'REL24':
                            # Branch to function
                            original_symbol = symbol  # Keep original before stripping
                            base_symbol, offset_hex, target_id = self._parse_symbol_with_offset(symbol)
                            symbol_var = f"{obj_prefix}_{self._sanitize_variable_name(base_symbol)}"
                            self.referenced_symbols.add(base_symbol)
                            # Map stripped name to original for data section lookup
                            if base_symbol != original_symbol.split('+')[0]:
                                self.symbol_name_map[base_symbol] = original_symbol.split('+')[0]
                            pattern_ref = f"{symbol_var}.name"
                            patch_func = (
                                f"lambda offset, data, plando_dict, patch_patterns, pattern_name: "
                                f"compute_bl_to_function(offset, data, patch_patterns, {pattern_ref}, {target_id})"
                            )
                            readable = f"bl {symbol}"

                        elif reloc_type == 'ADDR16_HA':
                            # Upper 16 bits of address
                            # Extract register from instruction
                            reg_match = re.search(r'r(\d+)', instruction)
                            register = int(reg_match.group(1)) if reg_match else 3
                            original_symbol = symbol
                            base_symbol, offset_hex, target_id = self._parse_symbol_with_offset(symbol)
                            symbol_var = f"{obj_prefix}_{self._sanitize_variable_name(base_symbol)}"
                            self.referenced_symbols.add(base_symbol)
                            if base_symbol != original_symbol.split('+')[0]:
                                self.symbol_name_map[base_symbol] = original_symbol.split('+')[0]
                            pattern_ref = f"{symbol_var}.name"
                            patch_func = (
                                f"lambda offset, data, plando_dict, patch_patterns, pattern_name: "
                                f"bytes.fromhex('{hex_bytes[:4]}') + get_addr16_ha(data, patch_patterns, {pattern_ref}, {target_id})"
                            )
                            readable = instruction

                        elif reloc_type == 'ADDR16_LO':
                            # Lower 16 bits of address
                            reg_match = re.search(r'r(\d+)', instruction)
                            register = int(reg_match.group(1)) if reg_match else 3
                            original_symbol = symbol
                            base_symbol, offset_hex, target_id = self._parse_symbol_with_offset(symbol)
                            symbol_var = f"{obj_prefix}_{self._sanitize_variable_name(base_symbol)}"
                            self.referenced_symbols.add(base_symbol)
                            if base_symbol != original_symbol.split('+')[0]:
                                self.symbol_name_map[base_symbol] = original_symbol.split('+')[0]
                            pattern_ref = f"{symbol_var}.name"
                            patch_func = (
                                f"lambda offset, data, plando_dict, patch_patterns, pattern_name: "
                                f"bytes.fromhex('{hex_bytes[:4]}') + get_addr16_lo(data, patch_patterns, {pattern_ref}, {target_id})"
                            )
                            readable = instruction

                        else:
                            # Unknown relocation type, use hex
                            patch_func = f"lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('{hex_bytes}')"
                            readable = instruction

                    else:
                        # No relocation - check instruction pattern anyway
                        auto_reloc = self._detect_instruction_relocation(instruction, hex_bytes)

                        if auto_reloc:
                            if auto_reloc['type'] == 'bl':
                                target = auto_reloc['target']
                                base_symbol, offset_hex, target_id = self._parse_symbol_with_offset(target)
                                target_var = self._sanitize_variable_name(base_symbol)
                                pattern_ref = f"{target_var}.name"
                                patch_func = (
                                    f"lambda offset, data, plando_dict, patch_patterns, pattern_name: "
                                    f"compute_bl_to_function(offset, data, patch_patterns, {pattern_ref}, {target_id})"
                                )
                                readable = f"bl {target}"
                            elif auto_reloc['type'] == 'lis':
                                target = auto_reloc['target']
                                base_symbol, offset_hex, target_id = self._parse_symbol_with_offset(target)
                                target_var = self._sanitize_variable_name(base_symbol)
                                pattern_ref = f"{target_var}.name"
                                patch_func = (
                                    f"lambda offset, data, plando_dict, patch_patterns, pattern_name: "
                                    f"li_upper_address_from_identifier(data, patch_patterns, {pattern_ref}, {target_id},"
                                    f" {auto_reloc['register']})"
                                )
                                readable = instruction
                            elif auto_reloc['type'] == 'ori':
                                target = auto_reloc['target']
                                base_symbol, offset_hex, target_id = self._parse_symbol_with_offset(target)
                                target_var = self._sanitize_variable_name(base_symbol)
                                pattern_ref = f"{target_var}.name"
                                patch_func = (
                                    f"lambda offset, data, plando_dict, patch_patterns, pattern_name: "
                                    f"ori_lower_address_from_identifier(data, patch_patterns, {pattern_ref}, {target_id},"
                                    f" {auto_reloc['register']})"
                                )
                                readable = instruction
                        else:
                            # Regular instruction with hex bytes
                            if len(hex_bytes) == 8:
                                patch_func = f"lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('{hex_bytes}')"
                            else:
                                patch_func = f"lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('00000000')  # TODO: Invalid hex length"
                            readable = instruction

                    output.append("        Patch(")
                    output.append(f"            identifier={idx},")
                    output.append(f"            patch_function={patch_func},")
                    output.append(f'            new_instruction_readable="{readable}"')
                    output.append("        ),")

                output.append("    ],")
                output.append("    patternJP=[],")
                output.append(")")
                outputs.append('\n'.join(output))

            # Generate placeholder PatchPattern objects for referenced data buffers
            data_symbols = self.referenced_symbols - self.function_names
            if data_symbols:
                outputs.append("\n# Data buffer placeholders")
                for symbol in sorted(data_symbols):
                    var_name = f"{obj_prefix}_{self._sanitize_variable_name(symbol)}"

                    # Get original name for data section lookup (before section prefix was stripped)
                    original_name = self.symbol_name_map.get(symbol, symbol)

                    # Check if we have data for this symbol (use original name)
                    if original_name in self.data_sections and self.data_sections[original_name]:
                        # Generate patches for the data bytes
                        patches = []
                        for idx, data_item in enumerate(self.data_sections[original_name], start=1):
                            hex_bytes = data_item['hex']
                            patch = (
                                f"        Patch(\n"
                                f"            identifier={idx},\n"
                                f"            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('{hex_bytes}'),\n"
                                f'            new_instruction_readable=".long 0x{hex_bytes}"\n'
                                f"        ),"
                            )
                            patches.append(patch)

                        placeholder = (
                                f'{var_name} = PatchPattern(\n'
                                f'    name=f"{obj_prefix}_{symbol}",\n'
                                f'    patchMapJP=[\n'
                                + '\n'.join(patches) + '\n'
                                                       f'    ],\n'
                                                       f'    patternJP=[],\n'
                                                       f')'
                        )
                    else:
                        # No data (BSS or not found), empty placeholder
                        placeholder = f'{var_name} = PatchPattern(\n    name=f"{obj_prefix}_{symbol}",\n    patchMapJP=[],\n    patternJP=[],\n)'

                    outputs.append(placeholder)

                # Add this object's outputs to the collection
                all_outputs.append('\n\n'.join(outputs))

        # Return all object files combined
        return '\n\n\n'.join(all_outputs)


def main(asm_file):
    if not Path(asm_file).exists():
        print(f"Error: File '{asm_file}' not found")
        sys.exit(1)

    parser = DisassemblyParser(asm_file)
    parser.parse()

    if not parser.object_files:
        print("Warning: No object files found in file")
        sys.exit(0)

    total_functions = sum(len(obj['functions']) for obj in parser.object_files)
    print(f"Found {len(parser.object_files)} object file(s) with {total_functions} total function(s)")
    for obj in parser.object_files:
        print(f"\n  Object: {obj['name']}")
        for func in obj['functions']:
            print(f"    - {func['name']}: {len(func['instructions'])} instructions")

    output = parser.generate_patch_patterns()

    # Save to output file
    output_file = Path(asm_file).stem + "_patches.py"
    with open(output_file, 'w') as f:
        f.write("# Generated from disassembly\n")
        f.write("# Import required functions:\n")
        f.write(
            "# from patch_functions import compute_bl_to_function, li_upper_address_from_identifier, ori_lower_address_from_identifier\n\n"
        )
        f.write(output)

    print(f"\n✓ Output saved to: {output_file}")
    total_patches = sum(len(func['instructions']) for obj in parser.object_files for func in obj['functions'])
    print(f"  Total patches generated: {total_patches}")


if __name__ == "__main__":
    main("../custom-functions/out.s")
