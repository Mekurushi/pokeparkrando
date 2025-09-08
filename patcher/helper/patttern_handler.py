from typing import Literal, Union

from patcher.models.models import Instruction, PatternMatch, MemoryData, PatchPattern


def parse_pattern_bytes(pattern_str: str):
    return [int(b, 16) if b != "??" else None for b in pattern_str.strip().split()]


def match_at(data: bytearray, offset: int, pattern: list[int | None]):
    for i, pat_byte in enumerate(pattern):
        if pat_byte is not None and data[offset + i] != pat_byte:
            return False
    return True


def search_pattern(data: bytearray, pattern_def: list[Instruction]):
    matches: list[PatternMatch] = []
    max_offset = max(pattern.offset + len(pattern.pattern) for pattern in pattern_def)
    anchor_pattern = next(
        (pattern for pattern in pattern_def
         if pattern.offset == 0),
        None
    )
    anchor_pattern_bytes = bytes(anchor_pattern.pattern)
    start_offset = 0
    while True:
        base = data.find(anchor_pattern_bytes, start_offset)
        if base == -1:  # No more occurrences found
            break

        if base + max_offset > len(data):
            break

        matched = {}
        for pattern in pattern_def:
            if base + pattern.offset + len(pattern.pattern) <= len(data) and match_at(
                    data, base + pattern.offset,
                    pattern.pattern
            ):
                matched[pattern.identifier] = MemoryData(
                    address=base + pattern.offset,
                    value=data[base + pattern.offset:base + pattern.offset + 0x4]
                )

            else:
                break
        else:
            matches.append(
                PatternMatch(
                    base_address=base,
                    matched_instructions=matched
                )
            )

        # Move to next potential position
        start_offset = base + 1

    return matches


def search_all_pattern(data: bytearray, patch_def: PatchPattern):
    patch_def.matchesJP = search_pattern(data, patch_def.patternJP)
    patch_def.matchesPAL = search_pattern(data, patch_def.patternPAL)
    patch_def.matchesNA = search_pattern(data, patch_def.patternNA)

    if not patch_def.matchesJP and not patch_def.matchesPAL and not patch_def.matchesNA:
        print(f"ERROR: No match found for pattern: {patch_def.name}")
        raise ValueError(f"ERROR: No match found for pattern: {patch_def.name}")

    ambiguous_regions = []
    if len(patch_def.matchesJP) > 1:
        ambiguous_regions.append(f"JP({len(patch_def.matchesJP)})")
    if len(patch_def.matchesPAL) > 1:
        ambiguous_regions.append(f"PAL({len(patch_def.matchesPAL)})")
    if len(patch_def.matchesNA) > 1:
        ambiguous_regions.append(f"NA({len(patch_def.matchesNA)})")

    if ambiguous_regions:
        error_msg = f"ERROR: Ambiguous matches for pattern: {patch_def.name} - {', '.join(ambiguous_regions)}"
        print(error_msg)
        raise ValueError(error_msg)

    print(f"Pattern {patch_def.name} matched in region: {patch_def.get_matched_region()}")


def compute_bl_to_function_script(offset: int, data: bytearray, target_function_pattern: PatchPattern):
    target_function_match = search_pattern(data, target_function_pattern.patternJP)
    new_function_address = target_function_match[0].base_address
    branch_offset = new_function_address - (offset + 0x4)
    operand = branch_offset // 4

    if not (-0x8000 <= operand <= 0x7FFF):
        raise ValueError(f"Operand out of 16-bit signed range: {operand:#x}")

    operand_bytes = operand.to_bytes(2, 'big', signed=True)
    instruction_bytes = operand_bytes + b'\x00\x03'

    print(
        f"call from offset 0x{offset:08X} to 0x{new_function_address:08X} "
        f"→ offset 0x{branch_offset & 0xFFFFFFFF:08X} "
        f"→ instruction 0x{int.from_bytes(instruction_bytes, 'big'):08X}"
    )
    return instruction_bytes


def get_num_battle_count_from_dict_as_instruction(plando_dict):
    battle_count: int = plando_dict["Options"]["num_required_battle_count"]
    if not (0x0000 <= battle_count <= 0xFFFF):
        raise ValueError(f"Invalid Battle Count: {battle_count}")
    battle_count_as_bytes = battle_count.to_bytes(2, byteorder="big")
    battle_count_instruction = battle_count_as_bytes + b'\x00\x10'
    print(f"writing battle Count: {battle_count}")
    return battle_count_instruction


def get_attraction_id_from_dict(plando_dict, entrance: str):
    exit_to_id: dict[str, int] = {
        "Bulbasaur's Daring Dash Attraction": 0xf,
        "Venusaur's Vine Swing Attraction": 0x2,
        "Pelipper's Circle Circuit Attraction": 0x6,
        "Gyarado's Aqua Dash Attraction": 0x5,
        "Empoleon's Snow Slide Attraction": 0x8,
        "Bastiodon's Panel Crush Attraction": 0x9,
        "Rhyperior's Bumper Burn Attraction": 0xa,
        "Blaziken's Boulder Bash Attraction": 0xb,
        "Dusknoir's Speed Slam Attraction": 0x4,
        "Tangrowth's Swing-Along Attraction": 0x3,
        "Rotom's Spooky Shoot-'em-Up Attraction": 0xc,
        "Absol's Hurdle Bounce Attraction": 0x0,
        "Salamence's Sky Race Attraction": 0xe,
        "Rayquaza's Balloon Panic Attraction": 0x1
    }

    exit: str = plando_dict["Entrances"][entrance]

    id = exit_to_id[exit]
    attractionid_as_bytes = id.to_bytes(2, byteorder="big")
    attractionid_instruction = attractionid_as_bytes + b'\x00\x10'
    print(f"writing attraction Id: {id}")
    return attractionid_instruction


def get_num_skygarden_prisma_count_from_dict_as_instruction(plando_dict):
    prisma_count: int = plando_dict["Options"]["num_required_prisma_count_skygarden"]
    if not (0x0000 <= prisma_count <= 0xe):
        raise ValueError(f"Invalid prisma Count: {prisma_count}")
    prisma_count_as_bytes = prisma_count.to_bytes(2, byteorder="big")
    prisma_count_instruction = prisma_count_as_bytes + b'\x00\x10'
    print(f"writing prisma Count from option: {prisma_count}")
    return prisma_count_instruction


def fill_with_delay_instructions_script(start_offset: int, end_offset: int):
    num_bytes = end_offset - start_offset

    if num_bytes % 4 != 0:
        raise ValueError("The offset range must be a multiple of 4 bytes")

    repeats = num_bytes // 4

    byte_sequence = (0x00000002).to_bytes(4, 'big') * repeats

    # Optional: Print or use the bytes
    print(byte_sequence)
    return byte_sequence


def create_lstr_script(data: bytearray, start_string_section_pattern: PatchPattern,
                       target_string_pattern: PatchPattern):
    start_string_section_match = search_pattern(data, start_string_section_pattern.patternJP)
    target_string_match = search_pattern(data, target_string_pattern.patternJP)
    if not start_string_section_match or not target_string_match:
        print(f"ERROR: No match found for pattern: {start_string_section_pattern.name} or {target_string_pattern.name}")
        raise Exception(
            f"ERROR: No match found for pattern: {start_string_section_pattern.name} or {target_string_pattern.name}"
        )

    if len(start_string_section_match) > 1 or len(target_string_match) > 1:
        print(
            f"ERROR: Ambiguous match ({len(start_string_section_match)}) for pattern: {start_string_section_pattern.name}"
        )
        print(f"ERROR: Ambiguous match ({len(target_string_match)}) for pattern: {target_string_pattern.name}")
        raise Exception(
            f"non unique pattern"
        )

    string_offset = target_string_match[0].base_address - start_string_section_match[0].base_address
    string_offset_as_bytes = string_offset.to_bytes(3, "big")
    lstr_instruction = string_offset_as_bytes + b'\x13'
    print(f"writing lstr instruction: 0x{int.from_bytes(lstr_instruction, 'big'):08X}")

    return lstr_instruction


def create_jmp_instruction_script(offset: int, target_identifier: int, matches: dict[int, MemoryData],
                                  condition: Literal["jmp"] | Literal["jnz"] | Literal["jz"] = "jmp"):
    target_address = matches.get(target_identifier).address
    branch_offset = target_address - (offset + 0x4)
    operand = branch_offset // 4

    if not (-0x8000 <= operand <= 0x7FFF):
        raise ValueError(f"Operand out of 16-bit signed range: {operand:#x}")
    condition_dict = {
        "jmp": b'\x00',
        "jnz": b'\x01',
        "jz": b'\x02'
    }
    condition_bit = condition_dict.get(condition)
    operand_bytes = operand.to_bytes(2, 'big', signed=True)
    instruction_bytes = operand_bytes + condition_bit + b'\x08'

    print(
        f"jmp from offset 0x{offset:08X} to 0x{target_address:08X} "
        f"→ offset 0x{branch_offset & 0xFFFFFFFF:08X} "
        f"→ instruction 0x{int.from_bytes(instruction_bytes, 'big'):08X}"
    )
    return instruction_bytes
