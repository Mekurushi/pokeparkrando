from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.dol.pattern_helper import compute_b_instruction_from_identifier, compute_bl_to_function, \
    compute_conditional_branch_instruction_from_identifier, get_enemy_ai_option, \
    get_player_name_from_dict, li_upper_address_from_pattern, ori_lower_address_from_pattern, \
    write_address_of_target_patch

custom_functions_cgu0_memcpy = PatchPattern(
    name=f"custom_functions_cgu0_memcpy",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("28 85 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("4d 86 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("7c 84 18 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("41 84 01 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("4d 86 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("38 c0 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("41 94 00 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("54 89 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("54 6a 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7d 0a 18 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("7c 00 22 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("40 82 01 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("71 4a 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("41 a2 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("38 c0 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("7d 29 30 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("39 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7d 29 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c a9 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("89 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("38 84 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("99 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("39 08 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("42 00 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("54 a6 d9 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c8 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("c8 44 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("c8 64 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("c8 84 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 84 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("d8 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("d8 48 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("d8 68 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("d8 88 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("39 08 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("42 00 ff d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("70 a6 00 1f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("38 84 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("39 08 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("8d 24 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("9d 28 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("38 c0 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("40 95 00 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("54 89 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("54 6a 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("40 82 00 84"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("38 c0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("7d 29 30 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("39 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("7c a9 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("7d 29 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("89 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 84 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("99 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("39 08 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("42 00 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("54 a6 e1 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("81 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("81 44 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("81 64 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("81 84 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("38 84 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("91 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("91 48 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("91 68 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("91 88 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("39 08 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("42 00 ff d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("70 a6 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("38 84 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("39 08 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("8d 24 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("9d 28 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("38 e4 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("39 03 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("7c a9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("8d 27 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("9d 28 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("7c 84 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("7d 83 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("38 c0 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("41 94 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("54 89 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("55 8a 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("40 82 00 f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("71 4a 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("41 a2 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("7d 49 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("7c aa 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("54 a6 d9 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("c8 24 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("c8 44 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("c8 64 ff e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("c8 84 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("38 84 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("d8 2c ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("d8 4c ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("d8 6c ff e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("dc 8c ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("42 00 ff dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("70 a6 00 1f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=129, offset=0x200, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=130, offset=0x204, pattern=parse_pattern_bytes("38 c0 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=131, offset=0x208, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=132, offset=0x20c, pattern=parse_pattern_bytes("40 95 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=133, offset=0x210, pattern=parse_pattern_bytes("54 89 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=134, offset=0x214, pattern=parse_pattern_bytes("55 8a 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=135, offset=0x218, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=136, offset=0x21c, pattern=parse_pattern_bytes("40 82 00 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=137, offset=0x220, pattern=parse_pattern_bytes("71 4a 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=138, offset=0x224, pattern=parse_pattern_bytes("41 a2 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=139, offset=0x228, pattern=parse_pattern_bytes("7d 49 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=140, offset=0x22c, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=141, offset=0x230, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=142, offset=0x234, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=143, offset=0x238, pattern=parse_pattern_bytes("7c aa 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=144, offset=0x23c, pattern=parse_pattern_bytes("54 a6 e1 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=145, offset=0x240, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=146, offset=0x244, pattern=parse_pattern_bytes("81 24 ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=147, offset=0x248, pattern=parse_pattern_bytes("81 44 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=148, offset=0x24c, pattern=parse_pattern_bytes("81 64 ff f4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=149, offset=0x250, pattern=parse_pattern_bytes("81 04 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=150, offset=0x254, pattern=parse_pattern_bytes("38 84 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=151, offset=0x258, pattern=parse_pattern_bytes("91 2c ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=152, offset=0x25c, pattern=parse_pattern_bytes("91 4c ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=153, offset=0x260, pattern=parse_pattern_bytes("91 6c ff f4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=154, offset=0x264, pattern=parse_pattern_bytes("95 0c ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=155, offset=0x268, pattern=parse_pattern_bytes("42 00 ff dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=156, offset=0x26c, pattern=parse_pattern_bytes("70 a6 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=157, offset=0x270, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=158, offset=0x274, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=159, offset=0x278, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=160, offset=0x27c, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=161, offset=0x280, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=162, offset=0x284, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=163, offset=0x288, pattern=parse_pattern_bytes("7c a9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=164, offset=0x28c, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=165, offset=0x290, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=166, offset=0x294, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=167, offset=0x298, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_memset = PatchPattern(
    name=f"custom_functions_cgu0_memset",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff ff 39"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0___ct__TextWriterBase_WChar = PatchPattern(
    name=f"custom_functions_cgu0___ct__TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff e9 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c0 02 a1 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("c0 22 a1 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 0d b1 f4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d0 3f 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d0 1f 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d0 1f 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 bf 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 9f 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 1f 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternNA=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff e9 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c0 02 a1 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("c0 22 a1 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 0d b1 ec"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d0 3f 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d0 1f 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d0 1f 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 bf 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 9f 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 1f 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff bf cd"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c0 02 a1 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("c0 22 a1 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 0d b2 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d0 3f 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d0 1f 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d0 1f 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 bf 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 9f 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 1f 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)

custom_functions_cgu0_CharWriter__UpdateVertexColor = PatchPattern(
    name=f"custom_functions_cgu0_CharWriter__UpdateVertexColor",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("88 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("88 a3 00 19"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("2c 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("88 83 00 1a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("88 03 00 1b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("98 c3 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("98 a3 00 09"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("98 83 00 0a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("98 03 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("41 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 a3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("38 a3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("88 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("98 03 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("88 85 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("98 83 00 0d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("2c 00 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("88 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("98 03 00 0e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("88 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("98 03 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("41 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("38 a3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("38 a3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("88 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("98 03 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("88 85 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("98 83 00 11"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("88 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("98 03 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("88 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("98 03 00 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("40 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("38 a3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("38 a3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("88 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("3c 80 80 81"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("98 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("39 44 80 81"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("88 03 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("88 85 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("98 83 00 15"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("88 e3 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("88 85 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("98 83 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("7c c0 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("88 83 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("88 03 00 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("89 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("7c a0 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("7c 08 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("7c 84 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("7d 0a 30 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("7c ea 20 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("7c c8 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("7c c8 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("7c ca 28 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("55 09 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("7c 87 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("7c e8 4a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("98 e3 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("7c 87 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("7c a6 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("54 e6 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("7c 8a 00 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("7c c7 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("98 c3 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("7c a5 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("54 a6 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("7c 04 02 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("7c 00 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("7c a5 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("54 04 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("98 a3 00 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("7c 00 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("98 03 00 17"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_CalcStringRect_TextWriterBase_WChar = PatchPattern(
    name=f"custom_functions_cgu0_CalcStringRect_TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("48 0f 40 c5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("82 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("82 23 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("82 43 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("82 63 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("82 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("82 a3 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("82 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("82 e3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("83 23 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("83 43 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 63 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 83 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 a3 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("83 c3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("83 e3 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("a1 83 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("89 63 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("89 43 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("c0 63 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("81 23 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("c0 43 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("c0 23 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("81 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("92 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("92 21 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("92 41 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("92 61 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("92 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("92 a1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("92 c1 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("92 e1 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("93 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("93 21 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("93 41 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("93 61 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("93 81 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("93 a1 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 c1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("93 e1 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("b1 81 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("99 61 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("99 41 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("d0 61 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("91 21 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("d0 41 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 21 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("90 e1 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 0e 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("4b ff b6 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("48 0f 40 1d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("80 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 21 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternNA=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("48 0f 42 f5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("82 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("82 23 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("82 43 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("82 63 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("82 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("82 a3 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("82 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("82 e3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("83 23 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("83 43 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 63 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 83 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 a3 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("83 c3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("83 e3 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("a1 83 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("89 63 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("89 43 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("c0 63 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("81 23 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("c0 43 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("c0 23 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("81 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("92 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("92 21 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("92 41 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("92 61 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("92 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("92 a1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("92 c1 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("92 e1 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("93 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("93 21 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("93 41 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("93 61 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("93 81 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("93 a1 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 c1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("93 e1 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("b1 81 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("99 61 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("99 41 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("d0 61 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("91 21 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("d0 41 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 21 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("90 e1 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 0e 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("4b ff b6 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("48 0f 42 4d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("80 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 21 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("48 0f 42 f5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("82 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("82 23 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("82 43 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("82 63 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("82 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("82 a3 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("82 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("82 e3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("83 23 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("83 43 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 63 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 83 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 a3 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("83 c3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("83 e3 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("a1 83 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("89 63 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("89 43 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("c0 63 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("81 23 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("c0 43 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("c0 23 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("81 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("92 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("92 21 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("92 41 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("92 61 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("92 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("92 a1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("92 c1 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("92 e1 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("93 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("93 21 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("93 41 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("93 61 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("93 81 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("93 a1 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 c1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("93 e1 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("b1 81 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("99 61 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("99 41 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("d0 61 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("91 21 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("d0 41 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 21 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("90 e1 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 0e 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("4b ff b6 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("48 0f 42 4d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("80 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 21 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)

custom_functions_cgu0_GXSetProjection = PatchPattern(
    name=f"custom_functions_cgu0_GXSetProjection",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("2c 04 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("c0 23 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 85 05 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("c0 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("d0 25 05 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("c0 23 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("d0 05 05 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("c0 03 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("d0 25 05 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("d0 05 05 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("40 82 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("c0 03 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x38, pattern=parse_pattern_bytes("d0 05 05 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x3c, pattern=parse_pattern_bytes("c0 03 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x40, pattern=parse_pattern_bytes("d0 05 05 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x44, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x48, pattern=parse_pattern_bytes("c0 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x4c, pattern=parse_pattern_bytes("d0 05 05 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x50, pattern=parse_pattern_bytes("c0 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x54, pattern=parse_pattern_bytes("d0 05 05 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x58, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x5c, pattern=parse_pattern_bytes("64 00 08 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x60, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x64, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_C_MTXOrtho = PatchPattern(
    name=f"custom_functions_cgu0_C_MTXOrtho",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("ed 64 18 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("c1 02 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("c1 42 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ec e1 10 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ec 06 28 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("c1 22 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ed 8a 58 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("c0 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("d1 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("d1 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("d1 03 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d1 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("ed 6a 38 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d1 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d1 03 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("d1 03 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("d1 03 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("d1 03 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("ec ea 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("d1 43 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("fc 00 30 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("ec 21 10 2a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("ec 64 18 2a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("ec c9 03 32"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("ec 00 01 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("fc 40 18 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("d0 c3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("ec 69 02 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("fc 20 08 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("d0 03 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("ec 8c 00 b2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("d0 63 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("ec 4b 00 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("ec 25 01 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("d0 83 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("d0 43 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("d0 23 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetViewport = PatchPattern(
    name=f"custom_functions_cgu0_GXSetViewport",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("d0 23 05 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("d0 43 05 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("d0 63 05 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("d0 83 05 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("d0 a3 05 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("d0 c3 05 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("80 03 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("64 00 10 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("90 03 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)
custom_functions_cgu0_float_to_unsigned = PatchPattern(
    name=f"custom_functions_cgu0_float_to_unsigned",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("3c 80 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 84 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("c8 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("c8 64 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c8 84 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("fc 01 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff 01 18 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("41 80 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 63 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("40 98 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("ff 81 20 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("fc 40 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("41 9c 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("fc 41 20 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("fc 40 10 1e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("d8 41 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 61 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("41 9c 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("3c 63 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetScissor = PatchPattern(
    name=f"custom_functions_cgu0_GXSetScissor",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("81 02 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 84 01 56"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("39 23 01 56"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("3c e0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 08 01 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 80 05 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("51 20 62 66"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 08 01 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("7c c4 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("7c 69 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("38 06 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("80 a8 01 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("50 05 05 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x38, pattern=parse_pattern_bytes("38 63 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x3c, pattern=parse_pattern_bytes("50 65 62 66"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x40, pattern=parse_pattern_bytes("90 a8 01 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x44, pattern=parse_pattern_bytes("38 80 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x48, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x4c, pattern=parse_pattern_bytes("98 87 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x50, pattern=parse_pattern_bytes("80 68 01 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x54, pattern=parse_pattern_bytes("90 67 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x58, pattern=parse_pattern_bytes("98 87 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x5c, pattern=parse_pattern_bytes("80 68 01 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x60, pattern=parse_pattern_bytes("90 67 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x64, pattern=parse_pattern_bytes("b0 08 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x68, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXLoadPosMtxImm = PatchPattern(
    name=f"custom_functions_cgu0_GXLoadPosMtxImm",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("3c a0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("98 05 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 80 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("64 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("38 85 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("90 05 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("e0 a3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("e0 83 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("e0 63 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("e0 43 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("e0 23 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("e0 03 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("f0 a4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("f0 84 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("f0 64 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("f0 44 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("f0 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("f0 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetCurrentMtx = PatchPattern(
    name=f"custom_functions_cgu0_GXSetCurrentMtx",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 06 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("64 00 04 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXClearVtxDesc = PatchPattern(
    name=f"custom_functions_cgu0_GXClearVtxDesc",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("50 03 4d 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("90 65 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 85 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("98 85 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("98 85 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("60 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetVtxAttrFmt = PatchPattern(
    name=f"custom_functions_cgu0_GXSetVtxAttrFmt",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("38 04 ff f7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("81 02 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("28 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 64 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7d 08 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("41 81 01 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("3c 80 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("54 00 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 84 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("7c 84 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7c 89 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("4e 80 04 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("50 a0 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("50 c0 0f 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("50 e0 25 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("48 00 01 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("2c 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("50 c0 54 ea"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("40 82 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("60 00 02 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("64 00 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("48 00 01 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("50 a0 4d ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("54 00 00 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("48 00 00 f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("50 a0 6c a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("50 c0 73 e2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("48 00 00 dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("50 a0 8b 9c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("50 c0 92 da"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 00 c8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("50 a0 aa 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("50 c0 b1 d2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("50 e0 c8 8c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("48 00 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("50 a0 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("50 c0 0f 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("50 e0 25 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("48 00 00 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("50 a0 4d ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("50 c0 54 ea"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("50 e0 6b a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("50 a0 93 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("50 c0 9a 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("50 e0 b1 52"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("48 00 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("50 a0 d9 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("50 c0 e0 46"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("50 e0 06 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("48 00 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("50 a0 2e b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("50 c0 35 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("50 e0 4c ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("48 00 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("50 a0 74 62"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("50 c0 7b a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("50 e0 92 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("48 00 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("50 a0 ba 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("50 c0 c1 4e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("50 e0 d8 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("54 60 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("80 85 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("7c 60 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("54 00 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("60 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("90 65 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("88 65 05 fb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("7c 60 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("98 05 05 fb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)
custom_functions_cgu0_GXInvalidateVtxCache = PatchPattern(
    name=f"custom_functions_cgu0_GXInvalidateVtxCache",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 00 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("98 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetVtxDesc = PatchPattern(
    name=f"custom_functions_cgu0_GXSetVtxDesc",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("28 03 00 19"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("41 81 02 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("3c a0 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 60 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("38 a5 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c a5 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7c a9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("4e 80 04 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("50 80 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("48 00 01 e4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("50 80 0f bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("48 00 01 d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("50 80 17 7a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("48 00 01 bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("50 80 1f 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("48 00 01 a8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("50 80 26 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("48 00 01 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("50 80 2e b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("48 00 01 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("50 80 36 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 01 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("50 80 3e 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("48 00 01 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("50 80 45 ee"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("48 00 01 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("50 80 4d 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("48 00 01 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("2c 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("41 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("98 65 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("98 05 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("90 85 05 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("48 00 01 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("98 03 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("48 00 00 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("2c 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("41 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("98 65 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("98 05 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("90 85 05 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("48 00 00 d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("98 03 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("48 00 00 c8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("50 80 6c 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("48 00 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("50 80 7b e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("48 00 00 a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("50 80 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("48 00 00 8c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("50 80 17 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("48 00 00 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("50 80 26 b6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("48 00 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("50 80 36 32"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("48 00 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("50 80 45 ae"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("48 00 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("50 80 55 2a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("48 00 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("50 80 64 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=129, offset=0x200, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=130, offset=0x204, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=131, offset=0x208, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=132, offset=0x20c, pattern=parse_pattern_bytes("50 80 74 22"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=133, offset=0x210, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=134, offset=0x214, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=135, offset=0x218, pattern=parse_pattern_bytes("88 04 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=136, offset=0x21c, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=137, offset=0x220, pattern=parse_pattern_bytes("40 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=138, offset=0x224, pattern=parse_pattern_bytes("88 04 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=139, offset=0x228, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=140, offset=0x22c, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=141, offset=0x230, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=142, offset=0x234, pattern=parse_pattern_bytes("80 05 05 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=143, offset=0x238, pattern=parse_pattern_bytes("80 65 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=144, offset=0x23c, pattern=parse_pattern_bytes("50 03 5c e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=145, offset=0x240, pattern=parse_pattern_bytes("90 65 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=146, offset=0x244, pattern=parse_pattern_bytes("48 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=147, offset=0x248, pattern=parse_pattern_bytes("80 04 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=148, offset=0x24c, pattern=parse_pattern_bytes("54 00 05 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=149, offset=0x250, pattern=parse_pattern_bytes("90 04 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=150, offset=0x254, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=151, offset=0x258, pattern=parse_pattern_bytes("60 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=152, offset=0x25c, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=153, offset=0x260, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetNumChans = PatchPattern(
    name=f"custom_functions_cgu0_GXSetNumChans",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 26 76"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("64 00 01 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)

custom_functions_cgu0_GXSetChanCtrl = PatchPattern(
    name=f"custom_functions_cgu0_GXSetChanCtrl",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("2c 09 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("39 40 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("50 8a 0f bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 6b 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("50 ca 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("50 aa 36 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("40 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("20 a9 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 89 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7c a4 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7c 09 00 d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("51 0a 3d f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("50 8a 55 ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("55 64 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("7c 00 4b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("2c 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("50 0a 5d 6a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 85 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("50 ea 16 ba"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 00 10 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("50 ea 3c 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("91 44 00 b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("7c 00 58 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("80 85 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("7c 80 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("40 82 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("91 45 00 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("60 00 50 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("2c 03 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("4c 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("91 45 00 c4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("60 00 a0 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetNumTexGens = PatchPattern(
    name=f"custom_functions_cgu0_GXSetNumTexGens",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 07 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("64 00 02 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetNumIndStages = PatchPattern(
    name=f"custom_functions_cgu0_GXSetNumIndStages",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 83 5e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("60 00 00 06"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetChanMatColor = PatchPattern(
    name=f"custom_functions_cgu0_GXSetChanMatColor",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("41 82 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("41 82 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("2c 03 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("41 82 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("2c 03 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("41 82 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("2c 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("41 82 00 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("2c 03 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("41 82 00 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("80 e3 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("50 07 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("48 00 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("39 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("80 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("80 e3 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("50 07 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("48 00 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("88 04 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("80 e3 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("50 07 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("48 00 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("39 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("88 04 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("80 e3 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("50 07 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("48 00 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("80 e4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("80 e4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("39 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("80 c2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("38 60 04 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("55 00 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("80 a6 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("7c 64 40 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("7c 66 02 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("7c a0 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("90 06 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("90 e3 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0___GXSetIndirectMask = PatchPattern(
    name=f"custom_functions_cgu0___GXSetIndirectMask",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 c7 01 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 66 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 c7 01 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("80 67 01 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("90 64 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetNumTevStages = PatchPattern(
    name=f"custom_functions_cgu0_GXSetNumTevStages",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 03 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("80 64 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("50 03 54 aa"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("90 64 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetTevOp = PatchPattern(
    name=f"custom_functions_cgu0_GXSetTevOp",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("3c a0 80 35"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 a5 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("40 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("54 86 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("38 85 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 05 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7d 04 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7d 20 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("48 00 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("54 86 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 85 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("38 05 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7d 04 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("7d 20 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("54 60 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("80 68 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c c7 02 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("81 06 01 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("55 08 00 0e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("50 68 02 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("91 04 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("91 06 01 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("81 06 01 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("80 69 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("55 08 07 0e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("50 68 02 36"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("91 04 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("91 06 01 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetTevOrder = PatchPattern(
    name=f"custom_functions_cgu0_GXSetTevOrder",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("54 ab 06 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 e0 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("54 69 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("81 42 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 07 58 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("54 68 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7c 07 01 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7d 29 1a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7c ea 42 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("2c 04 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("55 28 08 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("20 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("90 a7 05 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7c ea 42 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("7d 69 00 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("41 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("81 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("7c 00 18 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7d 00 00 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("48 00 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("81 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("7c 00 18 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("7d 00 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("90 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("54 60 07 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("41 82 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("81 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("2c 06 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("51 28 64 66"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("50 88 7b a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("40 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("38 00 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("3c 60 80 35"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("54 c0 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("38 63 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("7c 03 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("2c 05 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("50 08 9a 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("41 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("54 a0 05 ef"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("40 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("50 68 93 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("48 00 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("81 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("2c 06 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("51 28 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("50 88 1e b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("40 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("38 00 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("3c 60 80 35"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("54 c0 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("38 63 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("7c 03 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("2c 05 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("50 08 3d b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("41 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("54 a0 05 ef"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("40 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("50 68 36 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("38 00 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("98 04 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("80 67 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("90 64 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("b0 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("60 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetBlendMode = PatchPattern(
    name=f"custom_functions_cgu0_GXSetBlendMode",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("81 42 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 03 ff fd"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("39 03 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("3c e0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("81 2a 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("7c 00 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("50 09 35 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("7d 08 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("38 00 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("98 07 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("50 69 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("51 09 e7 bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x38, pattern=parse_pattern_bytes("50 c9 64 26"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x3c, pattern=parse_pattern_bytes("50 89 45 6e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x40, pattern=parse_pattern_bytes("50 a9 2e 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x44, pattern=parse_pattern_bytes("91 27 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x48, pattern=parse_pattern_bytes("91 2a 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x4c, pattern=parse_pattern_bytes("b0 0a 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x50, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetColorUpdate = PatchPattern(
    name=f"custom_functions_cgu0_GXSetColorUpdate",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 66 1f 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 c4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("90 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)

custom_functions_cgu0_GXSetAlphaUpdate = PatchPattern(
    name=f"custom_functions_cgu0_GXSetAlphaUpdate",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 66 26 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 c4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("90 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetZMode = PatchPattern(
    name=f"custom_functions_cgu0_GXSetZMode",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("81 22 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c c0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 e0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("81 09 02 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 68 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("50 88 0f 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("98 e6 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("50 a8 26 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("91 06 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("91 09 02 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("b0 09 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetCullMode = PatchPattern(
    name=f"custom_functions_cgu0_GXSetCullMode",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("54 65 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 65 0f bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("50 a0 74 22"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)
custom_functions_cgu0_GXBegin = PatchPattern(
    name=f"custom_functions_cgu0_GXBegin",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("83 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("93 c1 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7c be 2b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("93 a1 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7c 9d 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("93 81 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7c 7c 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("80 1f 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("41 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b ff fd 49"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("40 82 00 d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 00 00 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("a0 a7 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("a0 87 00 06"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("7c a5 21 d7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("98 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("a0 07 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("b0 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("41 82 00 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("38 65 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("38 e5 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("54 60 f0 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("28 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("40 81 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("28 03 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("41 80 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("7c 05 18 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("41 81 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("41 82 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("38 07 00 1f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("54 00 d9 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("7c 09 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("28 07 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("40 81 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("38 c6 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("42 00 ff dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("38 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("7c 06 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("54 00 f0 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("7c 09 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("7c 06 28 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("40 80 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("42 00 ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("b0 1f 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("7f a0 e3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("98 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("b3 c3 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("80 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("83 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("83 c1 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("83 a1 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("83 81 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("38 21 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_CharWriter__GetFontWidth = PatchPattern(
    name=f"custom_functions_cgu0_CharWriter__GetFontWidth",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("80 63 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("81 83 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("81 8c 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7d 89 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("4e 80 04 21"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("6c 63 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("3c 00 43 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("3c 80 80 31"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("90 61 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("c8 44 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("c0 1f 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("c8 21 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("ec 21 10 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("80 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("ec 20 00 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("38 21 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_GXSetAlphaCompare = PatchPattern(
    name=f"custom_functions_cgu0_GXSetAlphaCompare",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("3d 00 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 00 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("98 08 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("3d 20 f3 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("50 89 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("50 e9 44 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("50 69 83 5e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("50 c9 9a 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("50 a9 b2 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("91 28 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("b0 04 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_CharWriter__SetupGX = PatchPattern(
    name=f"custom_functions_cgu0_CharWriter__SetupGX",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("38 00 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("3b e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("3f c0 80 ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("3b de ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 9e 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("90 1e 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("93 e4 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("80 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("40 82 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 83 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("3c 04 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("28 00 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("41 82 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 81 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 01 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("80 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("38 61 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("90 01 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("48 00 12 ad"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("48 00 08 d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("80 63 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("41 82 07 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("81 83 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("81 8c 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("7d 89 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("4e 80 04 21"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("38 03 ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("28 00 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("40 81 03 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("28 03 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("40 81 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("38 03 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("28 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("40 81 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 05 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("88 1e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("40 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 fe 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("98 1e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("3c 60 80 31"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("80 1e 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("c0 23 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("38 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("90 01 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("fc 40 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("fc 60 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("fc 80 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 c0 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("38 e0 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("38 80 00 11"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("38 60 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("38 c0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("39 20 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("38 60 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("39 20 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("38 c0 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("39 00 00 7d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("38 80 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("38 a0 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("38 c0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("38 c0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("38 80 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("38 a0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("38 c0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("38 e0 00 0a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("38 80 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("38 c0 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("38 e0 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=129, offset=0x200, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=130, offset=0x204, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=131, offset=0x208, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=132, offset=0x20c, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=133, offset=0x210, pattern=parse_pattern_bytes("38 e0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=134, offset=0x214, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=135, offset=0x218, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=136, offset=0x21c, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=137, offset=0x220, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=138, offset=0x224, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=139, offset=0x228, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=140, offset=0x22c, pattern=parse_pattern_bytes("38 e0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=141, offset=0x230, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=142, offset=0x234, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=143, offset=0x238, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=144, offset=0x23c, pattern=parse_pattern_bytes("38 80 00 09"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=145, offset=0x240, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=146, offset=0x244, pattern=parse_pattern_bytes("38 c0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=147, offset=0x248, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=148, offset=0x24c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=149, offset=0x250, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=150, offset=0x254, pattern=parse_pattern_bytes("38 80 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=151, offset=0x258, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=152, offset=0x25c, pattern=parse_pattern_bytes("38 c0 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=153, offset=0x260, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=154, offset=0x264, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=155, offset=0x268, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=156, offset=0x26c, pattern=parse_pattern_bytes("38 80 00 0d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=157, offset=0x270, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=158, offset=0x274, pattern=parse_pattern_bytes("38 c0 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=159, offset=0x278, pattern=parse_pattern_bytes("38 e0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=160, offset=0x27c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=161, offset=0x280, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=162, offset=0x284, pattern=parse_pattern_bytes("38 60 00 09"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=163, offset=0x288, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=164, offset=0x28c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=165, offset=0x290, pattern=parse_pattern_bytes("38 60 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=166, offset=0x294, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=167, offset=0x298, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=168, offset=0x29c, pattern=parse_pattern_bytes("38 60 00 0d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=169, offset=0x2a0, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=170, offset=0x2a4, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=171, offset=0x2a8, pattern=parse_pattern_bytes("48 00 06 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=172, offset=0x2ac, pattern=parse_pattern_bytes("88 1e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=173, offset=0x2b0, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=174, offset=0x2b4, pattern=parse_pattern_bytes("40 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=175, offset=0x2b8, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        # uncomplete pattern
    ]
)

custom_functions_cgu0_Print_TextWriterBase_WChar = PatchPattern(
    name=f"custom_functions_cgu0_Print_TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("db e1 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("f3 e1 00 88"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 e1 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("80 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("90 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("80 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("90 01 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("80 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("90 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("80 03 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("80 03 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 01 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("90 01 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 01 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("80 03 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("90 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("90 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("80 e3 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("80 03 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("90 01 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("90 e1 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("90 01 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("90 e1 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("80 03 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("90 01 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("80 e3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("80 03 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("90 01 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("90 e1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("a0 03 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("b0 01 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("88 03 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("98 01 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("88 03 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("98 01 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("c0 03 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("d0 01 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("80 03 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("90 01 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("c0 03 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("d0 01 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("c0 03 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("d0 01 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("80 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("90 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("80 03 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("48 00 0a 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("c0 01 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("ff e0 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("c0 41 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("d0 5f 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("d0 1f 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("4b ff b1 55"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("fc 20 f8 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("e3 e1 00 88"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("cb e1 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("83 e1 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("80 01 00 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("38 21 00 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0___dt__TextWriterBase_WChar = PatchPattern(
    name=f"custom_functions_cgu0___dt__TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("4b ff d1 c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("2c 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b d5 41 39"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternNA=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("4b ff d1 c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("2c 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b d5 1d b9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("4b ff d1 c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("2c 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b d5 1a d9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)

custom_functions_cgu0_get_font_data = PatchPattern(
    name=f"custom_functions_cgu0_get_font_data",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("88 0d af b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("40 82 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 6d af bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("48 00 13 b5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("98 0d af b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 6d af bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("88 0d b0 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("40 82 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 6d b0 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("48 00 14 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("98 0d b0 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 6d b0 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)

custom_functions_cgu0_lookup_module = PatchPattern(
    name="custom_functions_cgu0_lookup_module",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("7c 64 1b 78"),
            instruction_readable="or r4,r4,r4"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("80 6d ?? ??"),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x38a00002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x38000005).to_bytes(
                4, 'big'
            ),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xA01F5F02).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="lhz r0, 0x5F02 (r31)"
        ),

    ],
)

custom_functions_cgu0_scene_manager_syscall_handler = PatchPattern(
    name="custom_functions_cgu0_scene_manager_syscall_handler",
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
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: write_address_of_target_patch(
                data, patch_patterns, custom_global_manager_syscall_handler_wrapper.name, 1
            ),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_enemy_ai_option(
                plando_dict
            ),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2c1e00ff).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="cmpwi r30,0xff"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2c1e00ff).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="cmpwi r30,0xff"
        )

    ],
)

original_message_id_to_index = PatchPattern(
    name="messageId to index function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00, pattern=parse_pattern_bytes("80 a3 00 10"),
            instruction_readable="lwz r5,0x10(r3)"
        ),
        Instruction(
            identifier=2, offset=0x04, pattern=parse_pattern_bytes("2c 05 00 00"),
            instruction_readable="cmpwi r5, 0x0"
        ),
        Instruction(
            identifier=3, offset=0x08, pattern=parse_pattern_bytes("40 82 00 10"),
            instruction_readable="bne"
        ),
        Instruction(
            identifier=4, offset=0x0c, pattern=parse_pattern_bytes("3c 60 00 01"),
            instruction_readable="li r3, 0x1"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("38 63 ff ff"),
            instruction_readable="subi r3, r3, 0x1"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="blr"
        ),

    ],
)

original_resident_text_lookup = PatchPattern(
    name="original_resident_text_lookup",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="stwu r1,local_10(r1)"
        ),
        Instruction(
            identifier=2, offset=0x04, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="mfspr r0"
        ),
        Instruction(
            identifier=3, offset=0x08, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="stw r0,local_res4(r1)"
        ),
        Instruction(
            identifier=4, offset=0x0c, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="stw r31,local_4(r1)"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="r31,message_idx,message_idx"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("93 c1 00 08"),
            instruction_readable="stw r30,local_8(r1)"
        ),
        Instruction(
            identifier=7, offset=0x30, pattern=parse_pattern_bytes("7c 1f 00 40"),
            instruction_readable="cmplw r31, r0"
        ),
    ],
)

main_game_loop_iteration_restore = PatchPattern(
    name="main game loop iteration restore",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("83 6b ff ec"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("83 8b ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("83 ab ff f4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("83 cb ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("83 eb ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[]
)

main_game_loop_iteration = PatchPattern(
    name="main game loop iteration",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff e0"),
            instruction_readable="stwu r1,local_20(r1)"
        ),
        Instruction(
            identifier=2, offset=0x334, pattern=parse_pattern_bytes("39 61 00 20"),
            instruction_readable="addi r11,r1,0x20"
        ),
        Instruction(
            identifier=3, offset=0x338, pattern=parse_pattern_bytes("48 2c ?? ??"),
            instruction_readable="bl restore_main_game_loop_iteration"
        ),
        Instruction(
            identifier=4, offset=0x33c, pattern=parse_pattern_bytes("80 01 00 24"),
            instruction_readable="lwz r0,local_res4(r1)"
        ),
        Instruction(
            identifier=5, offset=0x340, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="mtspr LR,r0"
        ),
        Instruction(
            identifier=6, offset=0x344, pattern=parse_pattern_bytes("38 21 00 20"),
            instruction_readable="addi r1,r1,0x20"
        ),
        Instruction(
            identifier=7, offset=0x348, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="blr"
        ),
        Instruction(
            identifier=8, offset=0x34c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns,
                "custom_functions_cgu0_main_routine", 1
            ),
            new_instruction_readable="bl main_routine"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x39610020).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="addi r11,r1,0x20"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns,
                main_game_loop_iteration_restore.name, 1
            ),
            new_instruction_readable="bl main_game_loop_iteration_restore"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x80010024).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="lwz r0,local_res4(r1)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x7c0803a6).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="mtspr LR,r0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x38210020).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="addi r1,r1,0x60"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x4e800020).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="blr"
        ),
    ]
)

custom_functions_cgu0_read_bits = PatchPattern(
    name=f"custom_functions_cgu0_read_bits",
    patchMapJP=[

    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("80 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c c4 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("39 40 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("7c 06 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("41 81 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("2c 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("41 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("28 05 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("54 8b 06 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("54 89 e8 fa"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("38 c0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("48 00 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("60 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("20 0b 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("7c a8 2b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("7c 05 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("40 81 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c 08 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("28 08 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("7d 4a 40 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("38 e0 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("40 80 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("7c c4 40 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("38 e4 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("80 83 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("7c 0b 42 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("20 00 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("7c a8 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("7c 84 48 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("39 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("39 29 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("7c 80 04 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("7c e0 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("7d 4a 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("2c 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("40 82 ff a8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("7d 43 53 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_write_bits = PatchPattern(
    name=f"custom_functions_cgu0_write_bits",
    patchMapJP=[

    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c e4 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("80 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 07 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("41 81 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("2c 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("41 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("28 05 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("48 00 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("38 00 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("40 80 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("7c 07 28 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("38 07 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("7c 06 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("41 80 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 06 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("54 8c 06 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("54 8b e8 fa"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("39 20 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("48 00 00 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("20 0c 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("7c a7 2b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("7c 05 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("40 81 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("7c 07 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("28 07 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("39 40 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("40 80 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("7d 24 38 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("39 44 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("81 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("7c 8c 3a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("7c 07 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("7c a7 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("23 e4 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("7c e8 58 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("7d 44 f8 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("7c c0 04 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("7c e4 20 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("7c 88 59 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("7d 40 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("39 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("80 e3 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("7c 00 f8 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("7c 87 58 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("7c 80 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("7c 07 59 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("39 6b 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("2c 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("40 82 ff 8c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

original_dol_pattern = [
    custom_functions_cgu0_memcpy,
    custom_functions_cgu0_memset,
    custom_functions_cgu0___ct__TextWriterBase_WChar,
    custom_functions_cgu0_CharWriter__UpdateVertexColor,
    custom_functions_cgu0_CalcStringRect_TextWriterBase_WChar,
    custom_functions_cgu0_GXSetProjection,
    custom_functions_cgu0_C_MTXOrtho,
    custom_functions_cgu0_GXSetViewport,
    custom_functions_cgu0_float_to_unsigned,
    custom_functions_cgu0_GXSetScissor,
    custom_functions_cgu0_GXLoadPosMtxImm,
    custom_functions_cgu0_GXSetCurrentMtx,
    custom_functions_cgu0_GXClearVtxDesc,
    custom_functions_cgu0_GXSetVtxAttrFmt,
    custom_functions_cgu0_GXInvalidateVtxCache,
    custom_functions_cgu0_GXSetVtxDesc,
    custom_functions_cgu0_GXSetNumChans,
    custom_functions_cgu0_GXSetChanCtrl,
    custom_functions_cgu0_GXSetNumTexGens,
    custom_functions_cgu0_GXSetNumIndStages,
    custom_functions_cgu0_GXSetChanMatColor,
    custom_functions_cgu0___GXSetIndirectMask,
    custom_functions_cgu0_GXSetNumTevStages,
    custom_functions_cgu0_GXSetTevOp,
    custom_functions_cgu0_GXSetTevOrder,
    custom_functions_cgu0_GXSetBlendMode,
    custom_functions_cgu0_GXSetColorUpdate,
    custom_functions_cgu0_GXSetAlphaUpdate,
    custom_functions_cgu0_GXSetZMode,
    custom_functions_cgu0_GXSetCullMode,
    custom_functions_cgu0_GXBegin,
    custom_functions_cgu0_CharWriter__GetFontWidth,
    custom_functions_cgu0_GXSetAlphaCompare,
    custom_functions_cgu0_CharWriter__SetupGX,
    custom_functions_cgu0_Print_TextWriterBase_WChar,
    custom_functions_cgu0___dt__TextWriterBase_WChar,
    custom_functions_cgu0_get_font_data,
    custom_functions_cgu0_lookup_module,

    main_game_loop_iteration_restore,
    main_game_loop_iteration,
    stage_setup_new_file_pattern,
    load_file_spawn_position,
    ai_difficulty_logic,
    attraction_record_unlock,

    global_manager_v_table,
    custom_functions_cgu0_scene_manager_syscall_handler,

    global_manager_syscall_handler,
    custom_functions_cgu0_read_bits,
    custom_functions_cgu0_write_bits
]
