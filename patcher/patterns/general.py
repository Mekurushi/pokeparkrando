from patcher.helper.patttern_handler import get_num_battle_count_from_dict_as_instruction, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

set_chapter = PatchPattern(
    name="set_chapter",
    description="removing set_chapter",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

        Instruction(
            identifier=3, offset=0x20, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=4, offset=0x48, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x4c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x50, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00030006).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="ret -0x3"
        ),
    ]
)

get_friendship = PatchPattern(
    name="get_friendship function",
    description="replacing with best friend request",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),

        Instruction(
            identifier=2, offset=0x4c, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=3, offset=0x60, pattern=parse_pattern_bytes("00 05 01 06"),
            instruction_readable="retv -0x5"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x4b"  # best friend opcode
        ),

    ]
)

globalManager = PatchPattern(
    name="ds GlobalManager",
    description="using GlobalManager for lstr instructions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("47 6c 6f 62 61 6c 4d 61 6e 61 67 65 72 00"),
            instruction_readable="ds GlobalManager"
        ),

    ]
)

disposManager = PatchPattern(
    name="ds disposManager",
    description="using disposManager for lstr instructions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("44 69 73 70 6f 73 4d 61 6e 61 67 65 72 00"),
            instruction_readable="ds disposManager"
        ),

    ]
)

get_module = PatchPattern(
    name="get module",
    description="using get module for calls",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="grow_stack 0x1"
        ),
        Instruction(
            identifier=2, offset=0x4,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=3, offset=0x8,
            pattern=parse_pattern_bytes("00 10 01 01"),
            instruction_readable="SC1 0x0:0x10"
        ),
    ]
)

set_friendship = PatchPattern(
    name="set_friendship",
    description="set_friendship function for custom-functions calls",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),
        Instruction(
            identifier=2, offset=0x2c, pattern=parse_pattern_bytes("00 0e 00 10"),
            instruction_readable="push 0xe"
        ),
        Instruction(
            identifier=3, offset=0x44, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=4, offset=0x48, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=5, offset=0x64, pattern=parse_pattern_bytes("00 4a 00 10"),
            instruction_readable="push 0x4a"
        ),
        Instruction(
            identifier=6, offset=0x68, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=7, offset=0x6c, pattern=parse_pattern_bytes("00 04 00 06"),
            instruction_readable="ret -0x4"
        ),
    ]
)

battle_counter_handling_patternPalNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
        instruction_readable="grow_stack 0x2"
    ),
    Instruction(
        identifier=2, offset=0x64, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0101BatlleCounterNum < 5
    ),
    Instruction(
        identifier=3, offset=0xa0, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0101BatlleCounterNum == 5
    ),

    Instruction(
        identifier=4, offset=0xe0, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0302BatlleCounterNum < 5
    ),
    Instruction(
        identifier=5, offset=0x11c, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0302BatlleCounterNum == 5
    ),

    Instruction(
        identifier=6, offset=0x15c, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0401BatlleCounterNum < 5
    ),
    Instruction(
        identifier=7, offset=0x198, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0401BatlleCounterNum == 5
    ),

    Instruction(
        identifier=8, offset=0x1d8, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0402BatlleCounterNum < 5
    ),
    Instruction(
        identifier=9, offset=0x214, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0402BatlleCounterNum == 5
    ),

    Instruction(
        identifier=10, offset=0x254, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0502BatlleCounterNum < 5
    ),
    Instruction(
        identifier=11, offset=0x290, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0502BatlleCounterNum == 5
    ),

    Instruction(
        identifier=12, offset=0x2d0, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0601BatlleCounterNum < 5
    ),
    Instruction(
        identifier=13, offset=0x30c, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0601BatlleCounterNum == 5
    ),

    Instruction(
        identifier=14, offset=0x34c, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0602BatlleCounterNum < 5
    ),
    Instruction(
        identifier=15, offset=0x388, pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"  # f0602BatlleCounterNum == 5
    ),
]

battle_counter_handling_patchPalNA = [
    Patch(
        identifier=2,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=3,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=4,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=5,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ), Patch(
        identifier=6,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=7,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ), Patch(
        identifier=8,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=9,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ), Patch(
        identifier=10,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=11,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ), Patch(
        identifier=12,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=13,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ), Patch(
        identifier=14,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
    Patch(
        identifier=15,
        patch_function=lambda offset, data, plando_dict,
                              patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
            plando_dict
        ),
        new_instruction_readable="push battlecounter"
    ),
]

battle_counter_handling = PatchPattern(
    name="battle_counter_handler",
    description="handles additional battle counter in PAL and NA",
    patternJP=[
    ],
    patternPAL=battle_counter_handling_patternPalNA,
    patternNA=battle_counter_handling_patternPalNA,
    patchMapJP=[],
    patchMapNA=battle_counter_handling_patchPalNA,
    patchMapPAL=battle_counter_handling_patchPalNA
)
