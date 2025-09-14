from patcher.helper.patttern_handler import compute_bl_to_function_script, create_lstr_script, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 34 5a 6e 30 32 5f 47 69 6d 6d 69 63 00"),
            instruction_readable="ds evAr04Zn02_Gimmic"
        ),

    ],
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

f0402TrapKamonegi = PatchPattern(
    name="ds f0402TrapKamonegi",
    description="replacing f0402TrapKamonegi with flag for golem unlock location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 34 30 32 54 72 61 70 4b 61 6d 6f 6e 65 67 69 00"),
            instruction_readable="ds f0402TrapKamonegi"
        ),

    ],
)

f0101FuwarideTaxiStop = PatchPattern(
    name="ds f0101FuwarideTaxiStop",
    description="replacing f0101FuwarideTaxiStop with flag for digda location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 31 30 31 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
            instruction_readable="ds f0101FuwarideTaxiStop"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (
                0x6630343032436c656172446f7369646f6e00).to_bytes(18, 'big'),
            new_instruction_readable="ds f0402ClearDosidon"
        ),

    ],
)

drill_switch = PatchPattern(
    name="drill_switch",
    description="removing condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 12 00 07"),
            instruction_readable="grow_stack 0x12"
        ),

        Instruction(
            identifier=2, offset=0x100, pattern=parse_pattern_bytes("13 b0 00 10"),
            instruction_readable="push 0x13b0"
        ),
        Instruction(
            identifier=3, offset=0x18c, pattern=parse_pattern_bytes("13 b0 00 10"),
            instruction_readable="push 0x13b0"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
    ]
)

set_golem_location_function = PatchPattern(
    name="set_golem_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(  # 50184
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 3e 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff f1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 02 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 63 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff f1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff f1 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 12 00 06"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010007).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="grow_stack -0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, globalManager
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, get_module
            ),
            new_instruction_readable="call get_module"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0402TrapKamonegi
            ),
            new_instruction_readable="lstr f0402TrapKamonegi"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150401).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC4 0x0:0x15"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x2"
        ),
    ]
)

set_baltoy_location_function = PatchPattern(
    name="set_baltoy_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(  # 50184
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff f4 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff f1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 09 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff f3 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010007).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="grow_stack -0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, globalManager
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, get_module
            ),
            new_instruction_readable="call get_module"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0101FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0402ClearDosidon"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150401).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC4 0x0:0x15"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x2"
        ),
    ]
)

yokoro = PatchPattern(
    name="yokoro",
    description="yokoro (smithing furnace) patch for golem location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 10 00 07"),
            instruction_readable="grow_stack 0x10"
        ),
        Instruction(
            identifier=2, offset=0x5e0, pattern=parse_pattern_bytes("00 6c 00 10"),
            instruction_readable="push 0x6c"
        ),
        Instruction(
            identifier=3, offset=0x5e8, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),

        Instruction(
            identifier=4, offset=0x600, pattern=parse_pattern_bytes("01 17 00 10"),
            instruction_readable="push 0x117"
        ),

        Instruction(
            identifier=5, offset=0x604, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="cal pokemon_unlock"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0402TrapKamonegi
            ),
            new_instruction_readable="lstr f0402TrapKamonegi"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"  # flag request opcode
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay 0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, set_golem_location_function
            ),
            new_instruction_readable="call set_golem_location"
        ),
    ]
)

box_yajilon_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 22 00 07"),
        instruction_readable="grow_stack 0x22"
    ),
    Instruction(
        identifier=2, offset=0x34, pattern=parse_pattern_bytes("00 9d 00 10"),
        instruction_readable="push 0x9d"
    ),
    Instruction(
        identifier=3, offset=0x3c, pattern=parse_pattern_bytes("00 29 00 10"),
        instruction_readable="push 0x29"
    ),

    Instruction(
        identifier=4, offset=0x6c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="cal pokemon_unlock"
    ),

]

box_yajilon = PatchPattern(
    name="BOX_YAJILON",
    description="yokoro (smithing furnace) patch for golem location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 18 00 07"),
            instruction_readable="grow_stack 0x18"
        ),
        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("00 9d 00 10"),
            instruction_readable="push 0x9d"
        ),
        Instruction(
            identifier=3, offset=0x3c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),

        Instruction(
            identifier=4, offset=0x6c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call pokemon_unlock"
        ),

    ],
    patternPAL=box_yajilon_patternPALNA,
    patternNA=box_yajilon_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0101FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0402ClearDosidon"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"  # flag request opcode
        ),

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, set_baltoy_location_function
            ),
            new_instruction_readable="call set_baltoy_location_function"
        ),
    ]
)

evAr04Zn02_Gimmic_patterns = [
    set_chapter,
    get_friendship,
    drill_switch,
    yokoro,
    box_yajilon,
    set_golem_location_function,
    set_baltoy_location_function,
    f0101FuwarideTaxiStop
]
