import io

from patcher.helper.patttern_handler import parse_pattern_bytes, \
    search_pattern
from patcher.models.DOL import DOL
from patcher.models.models import PatchPattern, Instruction, Patch, MemoryData


def compute_addi_to_target(data, matches: dict[int, MemoryData], base_identifier: int, target_identifier: int,
                           src_reg: int, dest_reg: int, ):
    base_offset = matches.get(base_identifier).address

    target_offset = matches.get(target_identifier).address

    # Calculate the offset needed
    offset = get_branch_offset(base_offset, data, target_offset)

    # Check if offset fits in 16-bit signed immediate
    if not (-32768 <= offset <= 32767):
        raise ValueError(f"Offset {offset} out of range for addi instruction (±32KB)")

    # addi opcode = 14
    opcode = 14
    imm = offset & 0xFFFF  # Handle negative offsets properly

    instruction = (opcode << 26) | (dest_reg << 21) | (src_reg << 16) | imm

    print(
        f"ADDI r{dest_reg}, r{src_reg}, {offset} "
        f"(0x{base_offset:08X} + {offset} = 0x{target_offset:08X}) "
        f"→ instruction 0x{instruction:08X}"
    )

    return instruction.to_bytes(4, 'big')


def get_offset_from_patch_pattern(data: bytearray, target_function_pattern: PatchPattern, identifier: int):
    target_function_match = search_pattern(data, target_function_pattern.patternJP)
    if not target_function_match:
        raise ValueError("Target function not found in pattern match: ", target_function_pattern.name)
    if len(target_function_match) > 1:
        raise ValueError(
            f"ERROR: Ambiguous match ({len(target_function_match)}) for pattern: {target_function_pattern.name}"
        )

    return target_function_match[0].matched_instructions[identifier].address


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
                                                           matches: dict[int, MemoryData], condition: str):
    target_offset = matches.get(target_identifier).address
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


def compute_b_instruction_from_identifier(offset: int, data: bytearray, target_identifier: int,
                                          matches: dict[int, MemoryData]):
    target_offset = matches.get(target_identifier).address
    branch_offset = get_branch_offset(offset, data, target_offset)

    instruction = get_b_instruction(branch_offset)

    return instruction.to_bytes(4, 'big')


def compute_bl_to_function(offset: int, data: bytearray, target_function_pattern: PatchPattern, identifier: int):
    target_offset = get_offset_from_patch_pattern(data, target_function_pattern, identifier)

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


def compute_bl_to_function_with_target_identifier(offset: int, data: bytearray, target_identifier: int,
                                                  matches: dict[int, MemoryData]):
    target_offset = matches.get(target_identifier).address
    branch_offset = get_branch_offset(offset, data, target_offset)

    instruction = get_bl_instruction_from_branch_offset(branch_offset)

    return instruction.to_bytes(4, 'big')


def get_player_name_from_dict(plando_dict):
    player_name: str = plando_dict["Name"]
    player_name_bytes = player_name.encode('utf-8')
    return (player_name_bytes + b'\x00' * 0x40)[:0x40]


def write_zone_change_string() -> bytes:
    zone_change_bytes = "ZoneChange".encode('utf-8')
    return zone_change_bytes + b'\x00'


def write_address_of_target_patch(data: bytearray, target_identifier: int,
                                  matches: dict[int, MemoryData]) -> bytes:
    target_offset = matches.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    return target_address.to_bytes(4, 'big')


def write_address_of_target_patch_by_pattern(data: bytearray, target_pattern: PatchPattern,
                                             target_identifier: int) -> bytes:
    target_offset = get_offset_from_patch_pattern(data, target_pattern, target_identifier)
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    return target_address.to_bytes(4, 'big')


def make_lis(reg: int, imm16: int) -> int:
    return 0x3C000000 | (reg << 21) | (imm16 & 0xFFFF)


def make_ori(reg: int, imm16: int) -> int:
    return 0x60000000 | (reg << 21) | (reg << 16) | (imm16 & 0xFFFF)


def li_upper_address_from_identifier(data: bytearray, target_identifier: int,
                                     matches: dict[int, MemoryData], register: int):
    target_offset = matches.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    upper = ((target_address + 0x8000) >> 16) & 0xFFFF

    instruction = make_lis(register, upper)
    return instruction.to_bytes(4, 'big')


def ori_lower_address_from_identifier(data: bytearray, target_identifier: int,
                                      matches: dict[int, MemoryData], register: int):
    target_offset = matches.get(target_identifier).address
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    lower = target_address & 0xFFFF

    instruction = make_ori(register, lower)
    return instruction.to_bytes(4, 'big')


def li_upper_address_from_pattern(data: bytearray, target_pattern: PatchPattern, target_identifier: int, register: int):
    target_offset = get_offset_from_patch_pattern(data, target_pattern, target_identifier)
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    upper = ((target_address + 0x8000) >> 16) & 0xFFFF

    instruction = make_lis(register, upper)
    return instruction.to_bytes(4, 'big')


def ori_lower_address_from_pattern(data: bytearray, target_pattern: PatchPattern,
                                   target_identifier: int,
                                   register: int):
    target_offset = get_offset_from_patch_pattern(data, target_pattern, target_identifier)
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    target_address: int = dol.convert_offset_to_address(target_offset)
    lower = target_address & 0xFFFF

    instruction = make_ori(register, lower)
    return instruction.to_bytes(4, 'big')


def setup_global_manager_syscall_handler_r12_upper_address(data: bytearray):
    data_init_function_match = search_pattern(data, global_manager_syscall_handler.patternJP)
    if not data_init_function_match:
        raise ValueError("Target function not found in pattern match.")
    if len(data_init_function_match) > 1:
        raise ValueError(
            f"ERROR: Ambiguous match ({len(data_init_function_match)}) for pattern: {data_init_function_match.name}"
        )
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    address = dol.convert_offset_to_address(data_init_function_match[0].base_address)
    address_bytes = address.to_bytes(4, 'big')
    upper_bits = int.from_bytes(address_bytes[:2], 'big')
    result = 0x3D800000 | upper_bits
    print(
        f"upper address for global Manager r12 Register is 0x{upper_bits:04X} instruction is: 0x{result.to_bytes(4, 'big').hex()}"
    )
    return result.to_bytes(4, 'big')


def setup_global_manager_syscall_handler_r12_lower_address(data: bytearray):
    data_init_function_match = search_pattern(data, global_manager_syscall_handler.patternJP)
    if not data_init_function_match:
        raise ValueError("Target function not found in pattern match.")
    if len(data_init_function_match) > 1:
        raise ValueError(
            f"ERROR: Ambiguous match ({len(data_init_function_match)}) for pattern: {data_init_function_match.name}"
        )

    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    address = dol.convert_offset_to_address(data_init_function_match[0].base_address)
    address_bytes = address.to_bytes(4, 'big')

    lower_bits = int.from_bytes(address_bytes[-2:], 'big')
    result = 0x618C0000 | lower_bits
    print(
        f"lower address for global Manager r12 Register is 0x{lower_bits:04X} instruction is: 0x{result.to_bytes(4, 'big').hex()}"
    )
    return result.to_bytes(4, 'big')


def get_global_manager_syscall_handler_wrapper(data: bytearray):
    data_init_function_match = search_pattern(data, custom_global_manager_syscall_handler_wrapper.patternJP)
    if not data_init_function_match:
        raise ValueError("Target function not found in pattern match.")
    if len(data_init_function_match) > 1:
        raise ValueError(
            f"ERROR: Ambiguous match ({len(data_init_function_match)}) for pattern: {data_init_function_match.name}"
        )

    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    address = dol.convert_offset_to_address(data_init_function_match[0].base_address)
    return address.to_bytes(4, 'big')


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


module_lookup = PatchPattern(
    name="module lookup function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("7c 64 1b 78"),
            instruction_readable="or r4,r4,r4"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("80 6d bb a0"),
            instruction_readable="lwz r3, -0x4460(r13)"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("80 84 00 00"),
            instruction_readable="lwz r4, 0x0 (r4)"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("48 ?? ?? ??"),
            instruction_readable="b search_module"
        ),
    ],
)

stage_setup_new_file_pattern = PatchPattern(
    name="Stage Setup new File",
    description="changing start zone to 02010005 (Treehouse Drifblim)",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("38 a0 00 63"),
            instruction_readable="li r5, 0x63"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="li r4, 0x1"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="li r0, 0x0"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("98 a3 00 20"),
            instruction_readable="stb r5, 0x20 (r3)"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("98 83 00 21"),
            instruction_readable="stb r4, 0x21 (r3)"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("b0 03 00 22"),
            instruction_readable="sth r0, 0x22 (r3)"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="blr"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x38a00002).to_bytes(4, 'big'),
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x38000005).to_bytes(4, 'big'),
            new_instruction_readable="push 0x5"
        ),

    ],
)

load_file_spawn_position = PatchPattern(
    name="load file spawn position",
    description="overwrites the vanilla hardcoded spawn point inside of zones with the saved one in the save file",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="li r0, 0x0"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("98 7f 5f 41"),
            instruction_readable="stb r3, 0x5f41 (r31)"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="or r3, r30, r30"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("b0 1f 5f 42"),
            instruction_readable="sth r0, 0x5f42 (r31)"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("81 9e 00 04"),
            instruction_readable="lwz r12,0x4(r30)"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("81 8c 00 44"),
            instruction_readable="lwz r12, 0x44(r12)"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7d 89 03 a6"),
            instruction_readable="mtspr CTR, r12"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0xA01F5F02).to_bytes(4, 'big'),
            new_instruction_readable="lhz r0, 0x5F02 (r31)"
        ),

    ],
)

prep_global_manager_data_struc_address = PatchPattern(
    name="set up data structure that is necessary for the global manager",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("40 82 00 30"),
            instruction_readable="bne"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("3f e0 80 ??"),
            instruction_readable="lis r31,-0x7fc9"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 7f ?? ??"),
            instruction_readable="addi r3, r31, 0x4fe0"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("48 ?? ?? ??"),
            instruction_readable="bl FUN_??????"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("3c 80 80 03"),
            instruction_readable="lis r4, -0x7ffd"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("3c a0 80 37"),
            instruction_readable="lis r5, -0x7fc9"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 7f ?? ??"),
            instruction_readable="addi r3, r31, 0x4fe0"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 84 ?? ??"),
            instruction_readable="subi r4, r4, 0x1930"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 a5 ?? ??"),
            instruction_readable="addi r5, r5, 0x1270"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("48 ?? ?? ??"),
            instruction_readable="bl FUN_??????"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="li r0, 0x1"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("98 0d ?? ??"),
            instruction_readable="stb r0, -0x5485 (r13)"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="lwz r31, local_4 (r1)"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("3c 60 80 ??"),
            instruction_readable="lis r3, -0x7fc9"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="lwz r0, local_res4 (r1)"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("38 63 ?? ??"),
            instruction_readable="addi r3, r3, 0x4fe0"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="mtspr LR, r0"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="addi r1, r1, 0x10"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="blr"
        ),
        # taking part of the next function to find unique match (order identical between versions)
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="- - -"
        ),
    ],
)

global_manager_syscall_handler_pattern = PatchPattern(
    name="Global Manager Function entry that allows with opcode to run code",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff b0"),
            instruction_readable="stwu r1, -0x50 (r1)"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="mfspr r0, LR"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("28 04 00 cf"),
            instruction_readable="cmplwi e4, 0xcf"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 54"),
            instruction_readable="stw r0, 0x54 (r1)"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 4c"),
            instruction_readable="stw r31, 0x4c (r1)"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("3b e0 00 7c"),
            instruction_readable="li r31, 0x7c"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 48"),
            instruction_readable="stw r30, 0x48 (r1)"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
            instruction_readable="or r30, r3, r3"
        ),
    ],
)

mnFieldInfo_syscall_handler = PatchPattern(
    name="mnFieldInfo module syscall handler",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff c0"),
            instruction_readable="stwu r1, -0x40 (r1)"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="mfspr r0, LR"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 44"),
            instruction_readable="stw r0, 0x44 (r1)"
        ),
        Instruction(
            identifier=5, offset=0x0c, pattern=parse_pattern_bytes("39 61 00 30"),
            instruction_readable="addi r11,r1, 0x30"
        ),
        Instruction(
            identifier=6, offset=0x10, pattern=parse_pattern_bytes("db e1 00 30"),
            instruction_readable="stfd f31, 0x30 (r1)"
        ),
        Instruction(
            identifier=7, offset=0x14, pattern=parse_pattern_bytes("f3 e1 00 38"),
            instruction_readable="psq_st f31, 0x38(r1), 0x0, GQR0"
        ),
        Instruction(
            identifier=8, offset=0x18, pattern=parse_pattern_bytes("48 ?? ?? ??"),
            instruction_readable="bl ???"
        ),
        Instruction(
            identifier=9, offset=0x1c, pattern=parse_pattern_bytes("28 04 00 3c"),
            instruction_readable="cmplwi r4, 0x3c"
        ),
    ],
)

data_space = PatchPattern(
    name="data space",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 e5 d8"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("e5 cf 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("e5 d9 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("e5 db 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 94 ed"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("e5 d7 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("e5 dc e5 de"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("8c d1 e5 d2"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("00 00 88 bf"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 e5 dd"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 8d d9"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("97 f4 e5 df"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("e5 e0 91 95"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("00 00 97 a0"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("e5 e1 97 54"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("e5 e2 e5 e3"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("95 e2 e5 e4"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("00 00 8d be"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("00 00 97 a1"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("e5 e9 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("e5 ea 8f d6"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("e5 e8 fb a2"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("97 87 e5 e5"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("e5 e7 90 bb"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("90 9e 00 00"),
            instruction_readable="- - -"
        ),
    ],
    patchMapJP=[
        # strings + pointers
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: "GlobalManager".encode('utf-8') + b'\x00',
            new_instruction_readable="GlobalManager string"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: write_address_of_target_patch(
                data, 1,
                matches
            ),
            new_instruction_readable="GlobalManager string pointer"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: "SceneManager".encode('utf-8') + b'\x00',
            new_instruction_readable="SceneManager string"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: write_address_of_target_patch(
                data, 6,
                matches
            ),
            new_instruction_readable="SceneManager string pointer"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: "mnFieldInfo".encode('utf-8') + b'\x00',
            new_instruction_readable="mnFieldInfo string"
        ),

        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: write_address_of_target_patch(
                data, 11,
                matches
            ),
            new_instruction_readable="mnFieldInfo string pointer"
        ),

        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: "mnLobby".encode('utf-8') + b'\x00',
            new_instruction_readable="mnLobby string"
        ),

        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: write_address_of_target_patch(
                data, 16,
                matches
            ),
            new_instruction_readable="mnLobby string pointer"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, matches: "mnAtInfo".encode('utf-8') + b'\x00',
            new_instruction_readable="mnAtInfo string"
        ),

        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: write_address_of_target_patch(
                data, 20,
                matches
            ),
            new_instruction_readable="mnAtInfo string pointer"
        ),
        # misc strings
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: bytes([0xFF] * 28),
            new_instruction_readable="flag names"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, matches: "ZoneChange".encode('utf-8') + b'\x00',
            new_instruction_readable="Scene Name String"  # 12 bytes
        ),
        Patch(
            identifier=35,
            patch_function=lambda offset, data, plando_dict, matches: get_player_name_from_dict(plando_dict),
            new_instruction_readable="PlayerName String"  # 0x40 bytes
        ),
        # up to idx 51

    ]
)

main_routine = PatchPattern(
    name="main_routine",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("e5 e6 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("e5 eb 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 95 a1"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("e5 ed 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("e5 ec 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("8a 8c 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("96 4a e5 ee"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("fa 5d e5 fa"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("e5 f0 00 00"),
            instruction_readable="- - -"
        ),
    ],
    patchMapJP=[
        # function header
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x9421FFE0).to_bytes(4, 'big'),
            new_instruction_readable="stwu sp, -0x0020 (sp)"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0802a6).to_bytes(4, 'big'),
            new_instruction_readable="mflr r0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x9001001C).to_bytes(4, 'big'),
            new_instruction_readable="stw r0, 0x001c (sp)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x90610014).to_bytes(4, 'big'),
            new_instruction_readable="stw r3, 0x0014 (sp)"
        ),

        # function body
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                global_manager_interface, 1
            ),
            new_instruction_readable="call GlobalManagerInterface"
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                scene_manager_interface, 1
            ),
            new_instruction_readable="call SceneManagerInterface"
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                mn_field_info_interface, 1
            ),
            new_instruction_readable="call mnFieldInfoInterface"
        ),

        # function footer
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x80610014).to_bytes(4, 'big'),
            new_instruction_readable="lwz r3, 0x0014 (sp)"
        ),

        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x8001001C).to_bytes(4, 'big'),
            new_instruction_readable="lwz r0, 0x001c (sp)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0803a6).to_bytes(4, 'big'),
            new_instruction_readable="mtlr r0"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x38210020).to_bytes(4, 'big'),
            new_instruction_readable="addi sp, sp, 32"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x4e800020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        )

    ]
)

global_manager_interface = PatchPattern(
    name="GlobalManagerInterface",
    patternJP=[
        Instruction(
            identifier=0, offset=0x00, pattern=parse_pattern_bytes("e5 b8 e5 b9"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=1, offset=0x04, pattern=parse_pattern_bytes("00 00 8a 49"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=2, offset=0x08, pattern=parse_pattern_bytes("00 00 8b 61"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=3, offset=0x0c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("e5 b7 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("00 00 e5 a2"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("00 00 fb a1"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("00 00 e5 b6"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("e5 ba e5 b5"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("00 00 e5 bc"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=14, offset=0x38, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=15, offset=0x3c, pattern=parse_pattern_bytes("00 00 e5 be"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=16, offset=0x40, pattern=parse_pattern_bytes("e5 bd 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=17, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=18, offset=0x48, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=19, offset=0x4c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=20, offset=0x50, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=21, offset=0x54, pattern=parse_pattern_bytes("00 00 e5 c0"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=22, offset=0x58, pattern=parse_pattern_bytes("e5 bf e5 79"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=23, offset=0x5c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=24, offset=0x60, pattern=parse_pattern_bytes("00 00 e5 c4"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=25, offset=0x64, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=26, offset=0x68, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=27, offset=0x6c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=28, offset=0x70, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=29, offset=0x74, pattern=parse_pattern_bytes("00 00 e5 c1"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=30, offset=0x78, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),

    ],
    patchMapJP=[
        # function header
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x9421FFF0).to_bytes(4, 'big'),
            new_instruction_readable="stwu sp, -0x0010 (sp)"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0802a6).to_bytes(4, 'big'),
            new_instruction_readable="mflr r0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x9001000C).to_bytes(4, 'big'),
            new_instruction_readable="stw r0, 0x000c (sp)"
        ),
        # function body
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_identifier(
                data, 28,
                matches, 30
            ),
            new_instruction_readable="li r30, parameter1_upper"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_identifier(
                data, 28,
                matches, 30
            ),
            new_instruction_readable="ori r30, parameter1_lower"
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x809EFFFC).to_bytes(4, 'big'),
            new_instruction_readable="lwz r4, -0x4 (r30)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x811E0000).to_bytes(4, 'big'),
            new_instruction_readable="lwz r8, 0 (r30)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x2C04FFFF).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r4, 0xffff"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict,
                                  matches: compute_conditional_branch_instruction_from_identifier(
                offset, data, 23, matches, "beq"
            ),
            new_instruction_readable="beq-"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x2c07ffff).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r8, 0xffff"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict,
                                  matches: compute_conditional_branch_instruction_from_identifier(
                offset, data, 23, matches, "beq"
            ),
            new_instruction_readable="beq-"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_pattern(
                data, data_space, 5, 3
            ),
            new_instruction_readable="lis r3, GlobalManager string pointer"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_pattern(
                data, data_space, 5, 3
            ),
            new_instruction_readable="ori r3, r3, module_name_pointer_lower"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                module_lookup, 1
            ),
            new_instruction_readable="bl lookup_module"
        ),

        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x809EFFFC).to_bytes(4, 'big'),
            new_instruction_readable="lwz r4, -0x4 (r30)"
        ),

        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x7FC5F378).to_bytes(4, 'big'),
            new_instruction_readable="mr r5, r30"
        ),

        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                global_manager_syscall_handler_pattern, 1
            ),
            new_instruction_readable="bl GlobalManager syscall"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: (0x38e0ffff).to_bytes(4, 'big'),
            new_instruction_readable="li r7, 0xffff"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: (0x90FE0008).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, 0x8 (r30)"  # cleanup parameter3
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, matches: (0x90FE0004).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, 0x4 (r6)"  # cleanup parameter2
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, matches: (0x90FE0000).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, 0x0 (r6)"  # cleanup parameter1
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, matches: (0x90FEFFFC).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, -0x4 (r6)"  # cleanup opcode
        ),

        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x8001000C).to_bytes(4, 'big'),
            new_instruction_readable="lwz r0, 0x000c (sp)"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0803a6).to_bytes(4, 'big'),
            new_instruction_readable="mtlr r0"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x38210010).to_bytes(4, 'big'),
            new_instruction_readable="addi sp, sp, 16"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x4e800020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        # data
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="opcode"
        ),
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="parameter1"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="parameter2"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="parameter3"
        ),
    ]
)

scene_manager_interface = PatchPattern(
    name="SceneManagerInterface",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00, pattern=parse_pattern_bytes("8c be 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=2, offset=0x04, pattern=parse_pattern_bytes("92 f9 e6 5d"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=3, offset=0x08, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=4, offset=0x0c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("8c 76 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("90 75 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("e6 60 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("93 a2 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("e6 5f 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("fb a3 8c 50"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("e6 5e 91 f5"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("8b 4c 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 e6 61"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("00 00 e6 62"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("00 00 8f d7"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 8c 8d"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 00 e6 63"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("96 4b 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("00 00 90 dd"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("00 00 8b 96"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("00 00 96 f3"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("91 69 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("e6 64 fb a4"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("90 66 92 90"),
            instruction_readable="- - -"
        ),
    ],
    patchMapJP=[
        # function header
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x9421FFF0).to_bytes(4, 'big'),
            new_instruction_readable="stwu sp, -0x0010 (sp)"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0802a6).to_bytes(4, 'big'),
            new_instruction_readable="mflr r0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x9001000C).to_bytes(4, 'big'),
            new_instruction_readable="stw r0, 0x000c (sp)"
        ),
        # Check the address
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_identifier(
                data, 30,
                matches, 3
            ),
            new_instruction_readable="lis r3, parameter1"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_identifier(
                data, 30,
                matches, 3
            ),
            new_instruction_readable="ori r3, r3, parameter1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x80830000).to_bytes(4, 'big'),
            new_instruction_readable="lwz r4, 0 (r3)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x2C040001).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r4, 1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict,
                                  matches: compute_conditional_branch_instruction_from_identifier(
                offset, data, 25, matches, "bne"  # Skip to end if not equal to 1
            ),
            new_instruction_readable="bne- to_end"
        ),
        # get SceneManager module
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_pattern(
                data, data_space, 10, 3
            ),
            new_instruction_readable="lis r3, SceneManager string pointer"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_pattern(
                data, data_space, 10, 3
            ),
            new_instruction_readable="ori r3, r3, SceneManager string pointer"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                module_lookup, 1
            ),
            new_instruction_readable="bl lookup_module"
        ),

        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x38800006).to_bytes(4, 'big'),
            new_instruction_readable="li r4, 0x6"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_identifier(
                data, 29,
                matches, 5
            ),
            new_instruction_readable="lis r5, SceneName pointer"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_identifier(
                data, 29,
                matches,
                5
            ),
            new_instruction_readable="ori r5, r5, SceneName pointer"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                scene_manager_syscall_handler, 1
            ),
            new_instruction_readable="bl SceneManager syscall handler"
        ),

        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_pattern(
                data, data_space, 10, 3
            ),
            new_instruction_readable="lis r3, SceneManager string pointer"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_pattern(
                data, data_space, 10, 3
            ),
            new_instruction_readable="ori r3, r3, SceneManager string pointer"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                module_lookup, 1
            ),
            new_instruction_readable="bl lookup_module"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: (0x38800003).to_bytes(4, 'big'),
            new_instruction_readable="li r4, 0x3"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                scene_manager_syscall_handler, 1
            ),
            new_instruction_readable="bl SceneManager syscall handler"
        ),
        # Set value back to 0xFF
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_identifier(
                data, 30,
                matches, 3
            ),
            new_instruction_readable="lis r3, parameter1"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_identifier(
                data, 30,
                matches, 3
            ),
            new_instruction_readable="ori r3, r3, parameter1"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x3880FFFF).to_bytes(4, 'big'),
            new_instruction_readable="li r4, 0xFFFF"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x90830000).to_bytes(4, 'big'),
            new_instruction_readable="stw r4, 0 (r3)"
        ),

        # Restore and return
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x8001000C).to_bytes(4, 'big'),
            new_instruction_readable="lwz r0, 0x000c (sp)"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0803a6).to_bytes(4, 'big'),
            new_instruction_readable="mtlr r0"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0x38210010).to_bytes(4, 'big'),
            new_instruction_readable="addi sp, sp, 16"
        ),
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0x4e800020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        # data
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: write_address_of_target_patch_by_pattern(
                data,
                data_space, 31
            ),
            new_instruction_readable="SceneName string pointer"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="parameter1"
        ),
    ]
)

mn_field_info_interface = PatchPattern(
    name="mnFieldInfoInterface",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00, pattern=parse_pattern_bytes("8c ea 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=2, offset=0x04, pattern=parse_pattern_bytes("90 bd e6 72"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=3, offset=0x08, pattern=parse_pattern_bytes("00 00 e6 77"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=4, offset=0x0c, pattern=parse_pattern_bytes("8c eb e6 74"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("e6 75 fb a6"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("e6 71 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("90 e0 93 c7"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("92 4e 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("89 db 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 94 ee"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("8b 62 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("fb a7 92 b2"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("e6 7a 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("e6 78 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 92 6b"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("00 00 90 bf"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("8a d0 e6 79"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("00 00 90 7a"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("97 c8 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("98 5f 00 00"),
            instruction_readable="- - -"
        ),
    ],
    patchMapJP=[
        # function header
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x9421FFF0).to_bytes(4, 'big'),
            new_instruction_readable="stwu sp, -0x0010 (sp)"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0802a6).to_bytes(4, 'big'),
            new_instruction_readable="mflr r0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x9001000C).to_bytes(4, 'big'),
            new_instruction_readable="stw r0, 0x000c (sp)"
        ),
        # function body
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_identifier(
                data, 28,
                matches, 30
            ),
            new_instruction_readable="li r30, parameter1_upper"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_identifier(
                data, 28,
                matches, 30
            ),
            new_instruction_readable="ori r30, parameter1_lower"
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x809EFFFC).to_bytes(4, 'big'),
            new_instruction_readable="lwz r4, -0x4 (r30)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x811E0000).to_bytes(4, 'big'),
            new_instruction_readable="lwz r8, 0 (r30)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x2C04FFFF).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r4, 0xffff"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict,
                                  matches: compute_conditional_branch_instruction_from_identifier(
                offset, data, 23, matches, "beq"
            ),
            new_instruction_readable="beq-"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x2c07ffff).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r8, 0xffff"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict,
                                  matches: compute_conditional_branch_instruction_from_identifier(
                offset, data, 23, matches, "beq"
            ),
            new_instruction_readable="beq-"
        ),

        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: li_upper_address_from_pattern(
                data, data_space, 15, 3
            ),
            new_instruction_readable="lis r3, mnFieldInfo string pointer"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: ori_lower_address_from_pattern(
                data, data_space, 15, 3
            ),
            new_instruction_readable="ori r3, r3, mnFieldInfo string pointer"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                module_lookup, 1
            ),
            new_instruction_readable="bl lookup_module"
        ),

        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x809EFFFC).to_bytes(4, 'big'),
            new_instruction_readable="lwz r4, -0x4 (r30)"
        ),

        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x7FC5F378).to_bytes(4, 'big'),
            new_instruction_readable="mr r5, r30"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0x38e0ffff).to_bytes(4, 'big'),
            new_instruction_readable="li r7, 0xffff"
        ),

        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: (0x90FEFFFC).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, -0x4 (r30)"  # block usage during execution
        ),

        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                mnFieldInfo_syscall_handler, 1
            ),
            new_instruction_readable="bl mnFieldInfo syscall"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, matches: (0x38e0ffff).to_bytes(4, 'big'),
            new_instruction_readable="li r7, 0xffff"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, matches: (0x90FE0000).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, 0x0 (r30)"  # cleanup parameter1
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, matches: (0x90FE0004).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, 0x4 (r30)"  # cleanup parameter2
        ),
        # function ending
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x8001000C).to_bytes(4, 'big'),
            new_instruction_readable="lwz r0, 0x000c (sp)"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0803a6).to_bytes(4, 'big'),
            new_instruction_readable="mtlr r0"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x38210010).to_bytes(4, 'big'),
            new_instruction_readable="addi sp, sp, 16"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x4e800020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        # data
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="opcode"
        ),
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="parameter1"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0xFFFFFFFF).to_bytes(4, 'big'),
            new_instruction_readable="parameter2"
        )
    ]
)

inject_custom_function = PatchPattern(
    name="Call for custom give item function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("7f 83 e3 78"),
            instruction_readable="mr r3, r30"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7f e5 fb 78"),
            instruction_readable="bl FUN_??????"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("4b ff ?? ??"),
            instruction_readable="mr r3, r30"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("7f 83 e3 78"),
            instruction_readable="lwz r0, 0x0014 (sp)"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7f a4 eb 78"),
            instruction_readable="lwz r31, 0x000c (sp)"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7f c5 f3 78"),
            instruction_readable="lwz r30, 0x0008 (sp)"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("4b ff ?? ??"),
            instruction_readable="mtlr r0"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="addi sp, sp, 16"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("80 01 00 24"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("83 e1 00 1c"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("83 c1 00 18"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("83 a1 00 14"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 81 00 10"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("38 21 00 20"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="blr"
        ),
    ], patchMapJP=[
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(
                offset, data,
                main_routine, 1
            ),
            new_instruction_readable="bl main_routine"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x080010024).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="lwz r0, 0x0014 (sp)"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x83e1001c).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="lwz r31, 0x000C (sp)"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x83c10018).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="lwz r30, 0x0008 (sp)"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x83a10014).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="mtlr r0"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x83810010).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="addi sp, sp, 16"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0803a6).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0x38210020).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: (0x4e800020).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="blr"
        ),
    ]
)

custom_global_manager_syscall_handler_wrapper = PatchPattern(
    name="Wrapper for the global Manager syscall handler",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00, pattern=parse_pattern_bytes("e6 6c e6 6b"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=2, offset=0x04, pattern=parse_pattern_bytes("91 46 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=3, offset=0x08, pattern=parse_pattern_bytes("8b 6c 98 62"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=4, offset=0x0c, pattern=parse_pattern_bytes("8a 59 8f da"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 fb a5"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("e6 6a 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("e6 6f 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("e6 70 e6 6e"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 8c d6"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("00 00 97 5f"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("8e 8f 94 46"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 00 e6 73"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 90 be"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 92 61"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("97 55 00 00"),
            instruction_readable="- - -"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("e6 76 00 00"),
            instruction_readable="- - -"
        ),
    ], patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x7C0802A6).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="mflr r0"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x9421FFEC).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="stwu r1, -0x14(r1)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x90010018).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="stw r0, 0x18(r1)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x2C04003C).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="cmpwi r4, 0x3c"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches:
            compute_conditional_branch_instruction_from_identifier(offset, data, 8, matches, "bne"),
            new_instruction_readable="bne check_28"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x3880004A).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="li r4, 0x4a"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: compute_b_instruction_from_identifier(
                offset,
                data, 10,
                matches
            ),
            new_instruction_readable="b global_manager_syscall_handler"
        ),

        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x2C040028).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="cmpwi r4, 0x28"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches:
            compute_conditional_branch_instruction_from_identifier(offset, data, 14, matches, "beq"),
            new_instruction_readable="beq skip_global_manager_syscall_handler"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches:
            setup_global_manager_syscall_handler_r12_upper_address(data),
            new_instruction_readable="lis r12, 0x8018"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches:
            setup_global_manager_syscall_handler_r12_lower_address(data),
            new_instruction_readable="ori r12, r12, 0x0790"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x7D8903A6).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="mtctr r12"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x4E800421).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="bctrl"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x80010018).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="lwz r0, 0x18(r1)"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x38210014).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="addi r1, r1, 0x14"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x7C0803A6).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="mtlr r0"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0x4E800020).to_bytes(length=4, byteorder='big'),
            new_instruction_readable="blr"
        ),
    ]
)

scene_manager_syscall_handler = PatchPattern(
    name="SceneManager syscall Handler",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="stwu r1,-0x50(r1)"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="mfspr r0, LR"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 04 00 06"),
            instruction_readable="cmplwi r4, 0xcf"
        ),

    ],
)

global_manager_syscall_handler = PatchPattern(
    name="GlobalManager syscall Handler",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff b0"),
            instruction_readable="stwu r1,-0x50(r1)"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="mfspr r0, LR"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("28 04 00 cf"),
            instruction_readable="cmplwi r4, 0xcf"
        ),

    ],
)

global_manager_v_table = PatchPattern(
    name="GlobalManager v table",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes(
                "6e 73 44 65 6c 68 69 3a 3a 6e 73 47 6c 6f 62 61 6c 3a 3a 47 6c 6f 62 61 6c 4d 61 6e 61 67 65 72 00"
            ),
            instruction_readable="ds nsDelhi::nsGlobal::GlobalManager"
        ),

        Instruction(
            identifier=2, offset=-0x14, pattern=parse_pattern_bytes("80 ?? ?? ??"),
            instruction_readable="call global_manager_syscall_handler"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: get_global_manager_syscall_handler_wrapper(data),
            new_instruction_readable="blr"
        ),
    ]
)

ai_difficulty_logic = PatchPattern(
    name="ai difficulty",
    description="modifying ai difficulty based on option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff e0"),
            instruction_readable="stwu r1,local_20(r1)"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="mfspr r0,LR"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 24"),
            instruction_readable="stw r0,local_res4(r1)"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 1c"),
            instruction_readable="stw r31,local_4(r1)"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 c1 00 18"),
            instruction_readable="stw r30,local_8(r1)"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c 9e 23 78"),
            instruction_readable="or r30,r4,r4"
        ),
        Instruction(
            identifier=7, offset=0x4c, pattern=parse_pattern_bytes("48 ?? ?? ??"),
            instruction_readable="bl get_friendship"
        ),
        Instruction(
            identifier=8, offset=0xa4, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="blr"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: get_enemy_ai_option(plando_dict),
            new_instruction_readable="li r3, 0|1"
        )

    ],
)

attraction_record_unlock = PatchPattern(
    name="attraction record unlock",
    description="removing skip for removed attractions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 60"),
            instruction_readable="stwu r1,local_a0(r1)"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="mfspr r0,LR"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 a4"),
            instruction_readable="stw r0,local_res4(r1)"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 9c"),
            instruction_readable="stw r31,local_4(r1)"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="mr r31, r3"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("93 c1 00 98"),
            instruction_readable="stw r30,local_8(r1)"
        ),
        Instruction(
            identifier=7, offset=0x144, pattern=parse_pattern_bytes("2c 1e 00 07"),
            instruction_readable="cmpwi r30,0x7"
        ),
        Instruction(
            identifier=8, offset=0x14c, pattern=parse_pattern_bytes("2c 1e 00 0d"),
            instruction_readable="cmpwi r30,0xd"
        ),
        Instruction(
            identifier=9, offset=0x1dc, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="blr"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x2c1e00ff).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r30,0xff"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x2c1e00ff).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r30,0xff"
        )

    ],
)

main_dol_pattern = [
    inject_custom_function,
    stage_setup_new_file_pattern,
    load_file_spawn_position,
    ai_difficulty_logic,
    attraction_record_unlock,

    global_manager_v_table,
    custom_global_manager_syscall_handler_wrapper,

    main_routine,
    global_manager_interface,
    scene_manager_interface,
    mn_field_info_interface,
    data_space,
]
