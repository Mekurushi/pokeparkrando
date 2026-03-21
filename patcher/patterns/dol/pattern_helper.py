import io

from patcher.helper.patttern_handler import find_pattern_by_name
from patcher.models.DOL import DOL
from patcher.models.models import PatchPattern


def get_bl_instruction_from_branch_offset(branch_offset: int):
    # Check if within ±32MB range (signed 26-bit / 4 = 24-bit signed)
    if not (-0x02000000 <= branch_offset <= 0x01FFFFFF):
        raise ValueError("Target out of range for 'bl' instruction (±32MB)")

    # Extract the 24-bit immediate
    imm = branch_offset >> 2 & 0x00FFFFFF

    # Construct bl: opcode = 18 (0x12), LK = 1
    instruction = (18 << 26) | (imm << 2) | 1

    print(f"→ offset 0x{branch_offset:08X} → instruction 0x{instruction:08X}")
    return instruction


def get_conditional_branch_instruction(branch_offset: int, condition: str, predict_not_taken: bool = False):
    # Check 14-bit range (±32KB)
    if not (-0x8000 <= branch_offset <= 0x7FFF):
        raise ValueError("Target out of range for conditional branch (±32KB)")

    # Extract 14-bit immediate
    imm = (branch_offset >> 2) & 0x3FFF

    conditions = {
        'beq': (12, 2),  # BO=12 (if true), BI=2 (EQ bit)
        'bne': (4, 2),  # BO=4 (if false), BI=2 (EQ bit)
        'blt': (12, 0),  # BO=12 (if true), BI=0 (LT bit)
        'bgt': (12, 1),  # BO=12 (if true), BI=1 (GT bit)
    }
    BO, BI = conditions[condition]

    y_bit = 1 if predict_not_taken else 0  # Prediction hint

    instruction = (16 << 26) | (BO << 21) | (BI << 16) | (imm << 2) | (y_bit << 1)
    return instruction


def compute_conditional_branch_instruction_from_identifier(offset: int, data: bytearray, target_identifier: int,
                                                           patch_patterns: list[PatchPattern], pattern_name: str,
                                                           condition: str):
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address
    branch_offset = get_branch_offset(offset, data, target_offset)

    instruction = get_conditional_branch_instruction(branch_offset, condition)

    return instruction.to_bytes(4, 'big')


def get_b_instruction(branch_offset: int):
    # Check 24-bit range (±32MB)
    if not (-0x2000000 <= branch_offset <= 0x1FFFFFF):
        raise ValueError("Target out of range for unconditional branch (±32MB)")

    # Extract 24-bit immediate
    imm = (branch_offset >> 2) & 0xFFFFFF

    # Construct b: opcode=18, AA=0 (relative), LK=0 (no link)
    instruction = (18 << 26) | (imm << 2)
    return instruction


def compute_b_instruction_from_identifier(offset: int, data: bytearray, pattern_name: str,
                                          patch_patterns: list[PatchPattern], target_identifier: int):
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address

    branch_offset = get_branch_offset(offset, data, target_offset)

    instruction = get_b_instruction(branch_offset)

    return instruction.to_bytes(4, 'big')


def compute_bl_to_function(offset: int, data: bytearray, patch_patterns: list[PatchPattern], pattern_name: str,
                           target_identifier: int):
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address

    branch_offset = get_branch_offset(offset, data, target_offset)

    instruction = get_bl_instruction_from_branch_offset(branch_offset)

    return instruction.to_bytes(4, 'big')


def get_branch_offset(offset: int, data: bytearray, target_offset: int):
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    instr_offset = dol.convert_offset_to_address(offset)
    new_function_address = dol.convert_offset_to_address(target_offset)

    # Compute the relative offset from PC
    branch_offset = new_function_address - instr_offset

    print(f"BL/branch from offset 0x{instr_offset:08X} to 0x{new_function_address:08X} ")
    return branch_offset


def get_player_name_from_dict(plando_dict):
    player_name: str = plando_dict["Name"]
    player_name_bytes = player_name.encode('utf-8')
    return (player_name_bytes + b'\x00' * 0x40)[:0x40]


def write_address_of_target_patch(data: bytearray, patch_patterns: list[PatchPattern], pattern_name: str,
                                  target_identifier: int) -> bytes:
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    return target_address.to_bytes(4, 'big')


def get_addr16_ha(data: bytearray, patch_patterns: list[PatchPattern], pattern_name: str,
                  target_identifier: int) -> bytes:
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    upper = (target_address + 0x8000) >> 16
    return (upper & 0xFFFF).to_bytes(2, 'big')


def get_addr16_lo(data: bytearray, patch_patterns: list[PatchPattern], pattern_name: str,
                  target_identifier: int) -> bytes:
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    lower = target_address & 0xFFFF
    return lower.to_bytes(2, 'big')


def make_lis(reg: int, imm16: int) -> int:
    return 0x3C000000 | (reg << 21) | (imm16 & 0xFFFF)


def make_ori(reg: int, imm16: int) -> int:
    return 0x60000000 | (reg << 21) | (reg << 16) | (imm16 & 0xFFFF)


def get_upper_address(address: int) -> int:
    return (address >> 16) & 0xFFFF


def get_lower_address(address: int) -> int:
    return address & 0xFFFF


def li_upper_address_from_pattern(data: bytearray, patch_patterns: list[PatchPattern], pattern_name: str,
                                  target_identifier: int, register: int):
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    upper = get_upper_address(target_address)

    instruction = make_lis(register, upper)
    return instruction.to_bytes(4, 'big')


def ori_lower_address_from_pattern(data: bytearray, patch_patterns: list[PatchPattern], pattern_name: str,
                                   target_identifier: int,
                                   register: int):
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_offset = pattern.matched_instructions.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    lower = get_lower_address(target_address)

    instruction = make_ori(register, lower)
    return instruction.to_bytes(4, 'big')


def get_enemy_ai_option(plando_dict):
    enemy_ai_option: str = plando_dict["Options"]["harder_enemy_ai"]
    if enemy_ai_option == 0:
        return (0x38600000).to_bytes(4, 'big')
        # li r3, 0
    if enemy_ai_option == 1:
        return (0x38600001).to_bytes(4, 'big')
        # li r3, 1
    raise ValueError(
        f"unknown option value for harder_enemy_ai value: {enemy_ai_option}"
    )


def should_print_client_text(plando_dict):
    should_print: int = plando_dict["Options"]["show_client_text_ingame"]
    return should_print.to_bytes(1, 'big')


def should_print_ap_buffer():
    return True.to_bytes(0x4, 'big')
