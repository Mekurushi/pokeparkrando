import io

from patcher.helper.patttern_handler import parse_pattern_bytes, \
 search_pattern
from patcher.models.DOL import DOL
from patcher.models.models import PatchPattern, Instruction, Patch

def setup_global_manager_r3_lower_address(data: bytearray):
    data_init_function_match = search_pattern(data, prep_global_manager_data_struc_address.pattern)
    if not data_init_function_match:
        raise ValueError("Target function not found in pattern match.")
    suffix = int.from_bytes(data_init_function_match[0].matched_instructions[3].value[-2:], 'big')
    result = 0x60630000 | suffix
    print(
        f"lower address for global Manager r3 Register is 0x{suffix:08X} instruction is: 0x{result.to_bytes(4, 'big').hex()}")
    return result.to_bytes(4, 'big')


def compute_bl_to_function(offset: int, data: bytearray, target_function_pattern: PatchPattern, identifier: int):
    target_function_match = search_pattern(data, target_function_pattern.pattern)
    if not target_function_match:
        raise ValueError("Target function not found in pattern match.")
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    instr_offset = dol.convert_offset_to_address(offset)
    new_function_address = dol.convert_offset_to_address(target_function_match[0].matched_instructions[identifier].address)

    # Compute the relative offset from PC
    branch_offset = new_function_address - instr_offset

    # Check if within ±32MB range (signed 26-bit / 4 = 24-bit signed)
    if not (-0x02000000 <= branch_offset <= 0x01FFFFFF):
        raise ValueError("Target out of range for 'bl' instruction (±32MB)")

    # Extract the 24-bit immediate
    imm = branch_offset >> 2 & 0x00FFFFFF

    # Construct bl: opcode = 18 (0x12), LK = 1
    instruction = (18 << 26) | (imm << 2) | 1

    print(f"BL from offset 0x{instr_offset:08X} to 0x{new_function_address:08X} "
          f"→ offset 0x{branch_offset:08X} → instruction 0x{instruction:08X}")

    return instruction.to_bytes(4, 'big')

def compute_bl_to_function_with_target_offset(offset: int, data: bytearray, target_offset:int):
    dol = DOL()
    stream = io.BytesIO(data)
    dol.read(stream)
    instr_offset = dol.convert_offset_to_address(offset)
    new_function_address = dol.convert_offset_to_address(target_offset)

    # Compute the relative offset from PC
    branch_offset = new_function_address - instr_offset

    # Check if within ±32MB range (signed 26-bit / 4 = 24-bit signed)
    if not (-0x02000000 <= branch_offset <= 0x01FFFFFF):
        raise ValueError("Target out of range for 'bl' instruction (±32MB)")

    # Extract the 24-bit immediate
    imm = branch_offset >> 2 & 0x00FFFFFF

    # Construct bl: opcode = 18 (0x12), LK = 1
    instruction = (18 << 26) | (imm << 2) | 1

    print(f"BL from offset 0x{instr_offset:08X} to 0x{new_function_address:08X} "
          f"→ offset 0x{branch_offset:08X} → instruction 0x{instruction:08X}")

    return instruction.to_bytes(4, 'big')


def get_player_name_from_dict(plando_dict):
    player_name: str = plando_dict["Name"]
    player_name_bytes = player_name.encode('utf-8')
    return (player_name_bytes + b'\x00' * 0x40)[:0x40]

stage_setup_new_file_pattern = PatchPattern(
    name="Stage Setup new File",
    description="changing start zone to 02010005 (Treehouse Drifblim)",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("38 a0 00 63"),
                    instruction_readable="li r5, 0x63"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 80 00 01"),
                    instruction_readable="li r4, 0x1"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 00 00 00"),
                    instruction_readable="li r0, 0x0"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("98 a3 00 20"),
                    instruction_readable="stb r5, 0x20 (r3)"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("98 83 00 21"),
                    instruction_readable="stb r4, 0x21 (r3)"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("b0 03 00 22"),
                    instruction_readable="sth r0, 0x22 (r3)"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("4e 80 00 20"),
                    instruction_readable="blr"),
    ],
    patchMap=[
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

setup_new_file_pattern = PatchPattern(
    name="Setup on new file load",
    description="patching new file setup to load position 0005 (drifblim), because it is here overwritten again",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("38 00 00 00"),
                    instruction_readable="li r0, 0x0"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("98 7f 5f 41"),
                    instruction_readable="stb r3, 0x5f41 (r31)"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("7f c3 f3 78"),
                    instruction_readable="or r3, r30, r30"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("b0 1f 5f 42"),
                    instruction_readable="sth r0, 0x5f42 (r31)"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("81 9e 00 04"),
                    instruction_readable="lwz r12,0x4(r30)"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("81 8c 00 44"),
                    instruction_readable="lwz r12, 0x44(r12)"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("7d 89 03 a6"),
                    instruction_readable="mtspr CTR, r12"),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x38000005).to_bytes(4, 'big'),
            new_instruction_readable="li r0, 0x0005"
        ),

    ],
)


prep_global_manager_data_struc_address = PatchPattern(
    name="set up data structure that is necessary for the global manager",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("40 82 00 30"),
                    instruction_readable="bne"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("3f e0 80 ??"),
                    instruction_readable="lis r31,-0x7fc9"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 7f ?? ??"),
                    instruction_readable="addi r3, r31, 0x4fe0"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("48 ?? ?? ??"),
                    instruction_readable="bl FUN_??????"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("3c 80 80 03"),
                    instruction_readable="lis r4, -0x7ffd"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("3c a0 80 37"),
                    instruction_readable="lis r5, -0x7fc9"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 7f ?? ??"),
                    instruction_readable="addi r3, r31, 0x4fe0"),
        Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 84 ?? ??"),
                    instruction_readable="subi r4, r4, 0x1930"),
        Instruction(identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 a5 ?? ??"),
                    instruction_readable="addi r5, r5, 0x1270"),
        Instruction(identifier=10, offset=0x24, pattern=parse_pattern_bytes("48 ?? ?? ??"),
                    instruction_readable="bl FUN_??????"),
        Instruction(identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 00 00 01"),
                    instruction_readable="li r0, 0x1"),
        Instruction(identifier=12, offset=0x2c, pattern=parse_pattern_bytes("98 0d ?? ??"),
                    instruction_readable="stb r0, -0x5485 (r13)"),
        Instruction(identifier=13, offset=0x30, pattern=parse_pattern_bytes("83 e1 00 0c"),
                    instruction_readable="lwz r31, local_4 (r1)"),
        Instruction(identifier=14, offset=0x34, pattern=parse_pattern_bytes("3c 60 80 ??"),
                    instruction_readable="lis r3, -0x7fc9"),
        Instruction(identifier=15, offset=0x38, pattern=parse_pattern_bytes("80 01 00 14"),
                    instruction_readable="lwz r0, local_res4 (r1)"),
        Instruction(identifier=16, offset=0x3c, pattern=parse_pattern_bytes("38 63 ?? ??"),
                    instruction_readable="addi r3, r3, 0x4fe0"),
        Instruction(identifier=17, offset=0x40, pattern=parse_pattern_bytes("7c 08 03 a6"),
                    instruction_readable="mtspr LR, r0"),
        Instruction(identifier=18, offset=0x44, pattern=parse_pattern_bytes("38 21 00 10"),
                    instruction_readable="addi r1, r1, 0x10"),
        Instruction(identifier=19, offset=0x48, pattern=parse_pattern_bytes("4e 80 00 20"),
                    instruction_readable="blr"),
        # taking part of the next function to find unique match (order identical between versions)
        Instruction(identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 00 00"),
                    instruction_readable="- - -"),
        Instruction(identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 00 00"),
                    instruction_readable="- - -"),
        Instruction(identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 00 00"),
                    instruction_readable="- - -"),
        Instruction(identifier=23, offset=0x58, pattern=parse_pattern_bytes("94 21 ff f0"),
                    instruction_readable="- - -"),
        Instruction(identifier=24, offset=0x5c, pattern=parse_pattern_bytes("7c 08 02 a6"),
                    instruction_readable="- - -"),
        Instruction(identifier=25, offset=0x60, pattern=parse_pattern_bytes("2c 03 00 00"),
                    instruction_readable="- - -"),
        Instruction(identifier=26, offset=0x64, pattern=parse_pattern_bytes("90 01 00 14"),
                    instruction_readable="- - -"),
        Instruction(identifier=27, offset=0x68, pattern=parse_pattern_bytes("93 e1 00 0c"),
                    instruction_readable="- - -"),
        Instruction(identifier=28, offset=0x6c, pattern=parse_pattern_bytes("7c 9f 23 78"),
                    instruction_readable="- - -"),
    ],
)


global_manager_function_pattern = PatchPattern(
    name="Global Manager Function entry that allows with opcode to run code",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff b0"),
                    instruction_readable="stwu r1, -0x50 (r1)"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
                    instruction_readable="mfspr r0, LR"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("28 04 00 cf"),
                    instruction_readable="cmplwi e4, 0xcf"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 54"),
                    instruction_readable="stw r0, 0x54 (r1)"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 4c"),
                    instruction_readable="stw r31, 0x4c (r1)"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("3b e0 00 7c"),
                    instruction_readable="li r31, 0x7c"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 48"),
                    instruction_readable="stw r30, 0x48 (r1)"),
        Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
                    instruction_readable="or r30, r3, r3"),
    ],
)

custom_give_item_function_pattern = PatchPattern(
    name="give item that runs GlobalManager Syscalls",    # for displaying client text in-game banner syscall is opcode 0x11 address: 8011a3ec
    pattern=[Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("e5 f9 e8 b5"),
                         instruction_readable="- - -"),
             Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("89 a6 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=12, offset=0x2c, pattern=parse_pattern_bytes("e5 fc 8b dd"),
                         instruction_readable="- - -"),
             Instruction(identifier=13, offset=0x30, pattern=parse_pattern_bytes("e5 fb 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=15, offset=0x38, pattern=parse_pattern_bytes("e6 41 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=16, offset=0x3c, pattern=parse_pattern_bytes("e6 40 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=17, offset=0x40, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=18, offset=0x44, pattern=parse_pattern_bytes("e6 43 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 00 e6 42"),
                         instruction_readable="- - -"),
             Instruction(identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 e6 44"),
                         instruction_readable="- - -"),
             Instruction(identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=22, offset=0x54, pattern=parse_pattern_bytes("8f 50 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=23, offset=0x58, pattern=parse_pattern_bytes("e6 45 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=24, offset=0x5c, pattern=parse_pattern_bytes("00 00 e6 46"),
                         instruction_readable="- - -"),
             Instruction(identifier=25, offset=0x60, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=26, offset=0x64, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=27, offset=0x68, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=28, offset=0x6c, pattern=parse_pattern_bytes("e6 47 90 bc"),
                         instruction_readable="- - -"),
             Instruction(identifier=29, offset=0x70, pattern=parse_pattern_bytes("00 00 97 76"),
                         instruction_readable="- - -"),
             Instruction(identifier=30, offset=0x74, pattern=parse_pattern_bytes("00 00 e6 48"),
                         instruction_readable="- - -"),
             Instruction(identifier=31, offset=0x78, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=32, offset=0x7c, pattern=parse_pattern_bytes("95 a2 94 65"),
                         instruction_readable="- - -"),
             Instruction(identifier=33, offset=0x80, pattern=parse_pattern_bytes("e6 49 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=34, offset=0x84, pattern=parse_pattern_bytes("e6 4a 8c a9"),
                         instruction_readable="- - -"),
             Instruction(identifier=35, offset=0x88, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=36, offset=0x8c, pattern=parse_pattern_bytes("00 00 8b 4b"),
                         instruction_readable="- - -"),
             Instruction(identifier=37, offset=0x90, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=38, offset=0x94, pattern=parse_pattern_bytes("00 00 e6 4b"),
                         instruction_readable="- - -"),
             Instruction(identifier=39, offset=0x98, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=40, offset=0x9c, pattern=parse_pattern_bytes("8e 8b 94 60"),
                         instruction_readable="- - -"),
             Instruction(identifier=41, offset=0xa0, pattern=parse_pattern_bytes("e6 4c 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=42, offset=0xa4, pattern=parse_pattern_bytes("8a 6f 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=43, offset=0xa8, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=44, offset=0xac, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=45, offset=0xb0, pattern=parse_pattern_bytes("00 00 e6 4d"),
                         instruction_readable="- - -"),
             Instruction(identifier=46, offset=0xb4, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=47, offset=0xb8, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=48, offset=0xbc, pattern=parse_pattern_bytes("e6 4f 97 97"),
                         instruction_readable="- - -"),
             Instruction(identifier=49, offset=0xc0, pattern=parse_pattern_bytes("00 00 e6 4e"),
                         instruction_readable="- - -"),
             Instruction(identifier=50, offset=0xc4, pattern=parse_pattern_bytes("90 65 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=51, offset=0xc8, pattern=parse_pattern_bytes("e6 50 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=52, offset=0xcc, pattern=parse_pattern_bytes("00 00 e6 51"),
                         instruction_readable="- - -"),
             Instruction(identifier=53, offset=0xd0, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=54, offset=0xd4, pattern=parse_pattern_bytes("e6 52 8a cf"),
                         instruction_readable="- - -"),
             Instruction(identifier=55, offset=0xd8, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=56, offset=0xdc, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=57, offset=0xe0, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=58, offset=0xe4, pattern=parse_pattern_bytes("e6 53 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=59, offset=0xe8, pattern=parse_pattern_bytes("00 00 e6 54"),
                         instruction_readable="- - -"),
             Instruction(identifier=60, offset=0xec, pattern=parse_pattern_bytes("00 00 e6 55"),
                         instruction_readable="- - -"),
             Instruction(identifier=61, offset=0xf0, pattern=parse_pattern_bytes("e6 56 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=62, offset=0xf4, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=63, offset=0xf8, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=64, offset=0xfc, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=65, offset=0x100, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=66, offset=0x104, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=67, offset=0x108, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=68, offset=0x10c, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=69, offset=0x110, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=70, offset=0x114, pattern=parse_pattern_bytes("8a 70 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=71, offset=0x118, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=72, offset=0x11c, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=73, offset=0x120, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=74, offset=0x124, pattern=parse_pattern_bytes("e6 57 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=75, offset=0x128, pattern=parse_pattern_bytes("e6 58 e6 59"),
                         instruction_readable="- - -"),
             Instruction(identifier=76, offset=0x12c, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=77, offset=0x130, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=78, offset=0x134, pattern=parse_pattern_bytes("00 00 89 f0"),
                         instruction_readable="- - -"),
             Instruction(identifier=79, offset=0x138, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=80, offset=0x13c, pattern=parse_pattern_bytes("90 47 e6 5a"),
                         instruction_readable="- - -"),
             Instruction(identifier=81, offset=0x140, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=82, offset=0x144, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=83, offset=0x148, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=84, offset=0x14c, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=85, offset=0x150, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=86, offset=0x154, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=87, offset=0x158, pattern=parse_pattern_bytes("e6 5b 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=88, offset=0x15c, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=89, offset=0x160, pattern=parse_pattern_bytes("e6 5c 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=90, offset=0x164, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=91, offset=0x168, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=92, offset=0x16c, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=93, offset=0x170, pattern=parse_pattern_bytes("8c be 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=94, offset=0x174, pattern=parse_pattern_bytes("92 f9 e6 5d"),
                         instruction_readable="- - -"),
             Instruction(identifier=95, offset=0x178, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=96, offset=0x17c, pattern=parse_pattern_bytes("00 00 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=97, offset=0x180, pattern=parse_pattern_bytes("8c 76 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=98, offset=0x184, pattern=parse_pattern_bytes("90 75 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=99, offset=0x188, pattern=parse_pattern_bytes("e6 60 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=100, offset=0x18c, pattern=parse_pattern_bytes("93 a2 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=101, offset=0x190, pattern=parse_pattern_bytes("e6 5f 00 00"),
                         instruction_readable="- - -"),
             Instruction(identifier=102, offset=0x194, pattern=parse_pattern_bytes("fb a3 8c 50"),
                         instruction_readable="- - -"),
             ],
    patchMap=[
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
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x93a10018).to_bytes(4, 'big'),
            new_instruction_readable="stw r29, 0x0018 (sp)"
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x3c608037).to_bytes(4, 'big'),
            new_instruction_readable="lis r3, 0x8037"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: setup_global_manager_r3_lower_address(data),
            new_instruction_readable="ori r3, r3, 0x4fe0 | 0x89e8"  # pal 89e8 jp 4fe0
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x3CC08000).to_bytes(4, 'big'),
            new_instruction_readable="lis r6, 0x8000"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x60C61800).to_bytes(4, 'big'),
            new_instruction_readable="ori r6, r6, 0x1800"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x90660000).to_bytes(4, 'big'),
            new_instruction_readable="stw r3, 0x0 (r6)"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x38C60004).to_bytes(4, 'big'),
            new_instruction_readable="addi r6, r6, 0x4"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x80e60000).to_bytes(4, 'big'),
            new_instruction_readable="lwz r7, 0 (r6)"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x2c07ffff).to_bytes(4, 'big'),
            new_instruction_readable="cmpwi r7, 0xffff"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x41820024).to_bytes(4, 'big'),
            new_instruction_readable="beq- identifier 22"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x7CC53378).to_bytes(4, 'big'),
            new_instruction_readable="mr r5, r6"
        ),

        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x80860004).to_bytes(4, 'big'),
            new_instruction_readable="lwz r4, 0x4 (r6)"  # lwz r4, 0x4 (r11)
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0x7cde3378).to_bytes(4, 'big'),
            new_instruction_readable="mr r30, r6"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(offset, data,
                                                                       global_manager_function_pattern, 1),
            new_instruction_readable="bl GlobalManager"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: (0x38e0ffff).to_bytes(4, 'big'),
            new_instruction_readable="li r7, 0xffff"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, matches: (0x7FC6f378).to_bytes(4, 'big'),
            new_instruction_readable="mr r6, r30"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, matches: (0x90E60000).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, 0 (r6)"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, matches: (0x90E60004).to_bytes(4, 'big'),
            new_instruction_readable="stw r7, 0x4 (r6)"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_with_target_offset(offset, data,
                                                                                                       offset + 0x1c),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x80610014).to_bytes(4, 'big'),
            new_instruction_readable="lwz r3, 0x0014 (sp)"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x83a10018).to_bytes(4, 'big'),
            new_instruction_readable="lwz r29, 0x0018 (sp)"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x8001001C).to_bytes(4, 'big'),
            new_instruction_readable="lwz r0, 0x001c (sp)"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0x7c0803a6).to_bytes(4, 'big'),
            new_instruction_readable="mtlr r0"
        ),
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0x38210020).to_bytes(4, 'big'),
            new_instruction_readable="addi sp, sp, 32"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0x4e800020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),

        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: (0x7C0802A6).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_with_target_offset(offset,data,offset+0x4),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, matches: (0x7C8802A6).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=33,
            patch_function=lambda offset, data, plando_dict, matches: (0x7C0803A6).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=34,
            patch_function=lambda offset, data, plando_dict, matches: (0x3884009c).to_bytes(4, 'big'), # hardcoded offset
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=35,
            patch_function=lambda offset, data, plando_dict, matches: (0x3C608000).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=36,
            patch_function=lambda offset, data, plando_dict, matches: (0x60631820).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, matches: (0x80A40000).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, matches: (0x80C40004).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, matches: (0x80E40008).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, matches: (0x8104000c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, matches: (0x81240010).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=42,
            patch_function=lambda offset, data, plando_dict, matches: (0x81440014).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=43,
            patch_function=lambda offset, data, plando_dict, matches: (0x81640018).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=44,
            patch_function=lambda offset, data, plando_dict, matches: (0x8184001c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=45,
            patch_function=lambda offset, data, plando_dict, matches: (0x90A30000).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=46,
            patch_function=lambda offset, data, plando_dict, matches: (0x90C30004).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=47,
            patch_function=lambda offset, data, plando_dict, matches: (0x90E30008).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=48,
            patch_function=lambda offset, data, plando_dict, matches: (0x9103000c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=49,
            patch_function=lambda offset, data, plando_dict, matches: (0x91230010).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=50,
            patch_function=lambda offset, data, plando_dict, matches: (0x91430014).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=51,
            patch_function=lambda offset, data, plando_dict, matches: (0x91630018).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=52,
            patch_function=lambda offset, data, plando_dict, matches: (0x9183001c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),


        Patch(
            identifier=53,
            patch_function=lambda offset, data, plando_dict, matches: (0x80A40020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=54,
            patch_function=lambda offset, data, plando_dict, matches: (0x80C40024).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=55,
            patch_function=lambda offset, data, plando_dict, matches: (0x80E40028).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=56,
            patch_function=lambda offset, data, plando_dict, matches: (0x8104002c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=57,
            patch_function=lambda offset, data, plando_dict, matches: (0x81240030).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=58,
            patch_function=lambda offset, data, plando_dict, matches: (0x81440034).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=59,
            patch_function=lambda offset, data, plando_dict, matches: (0x81640038).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=60,
            patch_function=lambda offset, data, plando_dict, matches: (0x8184003c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),

        Patch(
            identifier=61,
            patch_function=lambda offset, data, plando_dict, matches: (0x90A30020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=62,
            patch_function=lambda offset, data, plando_dict, matches: (0x90C30024).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=63,
            patch_function=lambda offset, data, plando_dict, matches: (0x90E30028).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=64,
            patch_function=lambda offset, data, plando_dict, matches: (0x9103002c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=65,
            patch_function=lambda offset, data, plando_dict, matches: (0x91230030).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=66,
            patch_function=lambda offset, data, plando_dict, matches: (0x91430034).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=67,
            patch_function=lambda offset, data, plando_dict, matches: (0x91630038).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=68,
            patch_function=lambda offset, data, plando_dict, matches: (0x9183003c).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=69,
            patch_function=lambda offset, data, plando_dict, matches: (0x4E800020).to_bytes(4, 'big'),
            new_instruction_readable="blr"
        ),

        Patch(
            identifier=71,
            patch_function=lambda offset, data, plando_dict, matches: get_player_name_from_dict(plando_dict),
            new_instruction_readable="blr"
        ),
    ],
)

custom_give_item_function_call_pattern = PatchPattern(
    name="Call for custom give item function",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("7f 83 e3 78"),
                    instruction_readable="mr r3, r30"),

        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("7f e5 fb 78"),
                    instruction_readable="bl FUN_??????"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("4b ff ?? ??"),
                    instruction_readable="mr r3, r30"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("7f 83 e3 78"),
                    instruction_readable="lwz r0, 0x0014 (sp)"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("7f a4 eb 78"),
                    instruction_readable="lwz r31, 0x000c (sp)"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("7f c5 f3 78"),
                    instruction_readable="lwz r30, 0x0008 (sp)"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("4b ff ?? ??"),
                    instruction_readable="mtlr r0"),
        Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("48 00 00 08"),
                    instruction_readable="addi sp, sp, 16"),
        Instruction(identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 60 00 00"),
                    instruction_readable="blr"),
        Instruction(identifier=10, offset=0x24, pattern=parse_pattern_bytes("80 01 00 24"),
                    instruction_readable="blr"),
        Instruction(identifier=11, offset=0x28, pattern=parse_pattern_bytes("83 e1 00 1c"),
                    instruction_readable="blr"),
        Instruction(identifier=12, offset=0x2c, pattern=parse_pattern_bytes("83 c1 00 18"),
                    instruction_readable="blr"),
        Instruction(identifier=13, offset=0x30, pattern=parse_pattern_bytes("83 a1 00 14"),
                    instruction_readable="blr"),
        Instruction(identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 81 00 10"),
                    instruction_readable="blr"),
        Instruction(identifier=15, offset=0x38, pattern=parse_pattern_bytes("7c 08 03 a6"),
                    instruction_readable="blr"),
        Instruction(identifier=16, offset=0x3c, pattern=parse_pattern_bytes("38 21 00 20"),
                    instruction_readable="blr"),
        Instruction(identifier=17, offset=0x40, pattern=parse_pattern_bytes("4e 80 00 20"),
                    instruction_readable="blr"),
        Instruction(identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
                    instruction_readable="blr"),
    ], patchMap=[
        Patch(identifier=10,
              patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function(offset, data,
                                                                         custom_give_item_function_pattern, 1),
              new_instruction_readable="bl custom_give_item_function"),
        Patch(identifier=11, patch_function=lambda offset, data, plando_dict, matches: (0x080010024).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="lwz r0, 0x0014 (sp)"),
        Patch(identifier=12, patch_function=lambda offset, data, plando_dict, matches: (0x83e1001c).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="lwz r31, 0x000C (sp)"),
        Patch(identifier=13, patch_function=lambda offset, data, plando_dict, matches: (0x83c10018).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="lwz r30, 0x0008 (sp)"),
        Patch(identifier=14, patch_function=lambda offset, data, plando_dict, matches: (0x83a10014).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="mtlr r0"),
        Patch(identifier=15, patch_function=lambda offset, data, plando_dict, matches: (0x83810010).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="addi sp, sp, 16"),
        Patch(identifier=16, patch_function=lambda offset, data, plando_dict, matches: (0x7c0803a6).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="blr"),
        Patch(identifier=17,
              patch_function=lambda offset, data, plando_dict, matches: (0x38210020).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="blr"),
        Patch(identifier=18,
              patch_function=lambda offset, data, plando_dict, matches: (0x4e800020).to_bytes(length=4, byteorder='big'),
              new_instruction_readable="blr"),
    ])
