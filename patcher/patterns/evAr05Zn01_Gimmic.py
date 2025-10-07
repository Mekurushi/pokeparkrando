from patcher.helper.patttern_handler import compute_bl_to_function_script, create_lstr_script, parse_pattern_bytes, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 35 5a 6e 30 31 5f 47 69 6d 6d 69 63 00"),
            instruction_readable="ds evAr05Zn01_Gimmic"
        ),

    ],
)

f0101FuwarideTaxiStop = PatchPattern(
    name="ds f0101FuwarideTaxiStop",
    description="replacing f0101FuwarideTaxiStop with flag for kakuna location",
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
                0x663035303154616c6b4d6f7a79616e626f00).to_bytes(18, 'big'),
            new_instruction_readable="ds f0501TalkMozyanbo"
        ),

    ],
)

f0301FuwarideTaxiStop = PatchPattern(
    name="ds f0101FuwarideTaxiStop",
    description="replacing f0301FuwarideTaxiStop with flag for metapod location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 33 30 31 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
            instruction_readable="ds f0301FuwarideTaxiStop"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (
                0x663035303153656b69686900).to_bytes(12, 'big'),
            new_instruction_readable="ds f0501Sekihi"
        ),

    ],
)

mansion_door = PatchPattern(
    name="mansion door condition",
    description="replacing chapter condition with tangrowth prisma",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=3, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x30, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="store_arg -0x3"
        ),
        Instruction(
            identifier=5, offset=0x34, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x38, pattern=parse_pattern_bytes("1b 58 00 10"),
            instruction_readable="push 0x1b58"
        ),
        Instruction(
            identifier=7, offset=0x3c, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        # no prisma path
        Instruction(
            identifier=8, offset=0x74, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=9, offset=0x78, pattern=parse_pattern_bytes("17 98 00 10"),
            instruction_readable="push 0x1798"
        ),
        Instruction(
            identifier=10, offset=0x7c, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x3"  # tangrowth prisma id
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"  # global manager
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x51"  # prisma request opcode
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffd000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x3"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffd000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x3"
        ),
    ]
)

set_kakuna_location_function = PatchPattern(
    name="set_kakuna_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 12 00 06"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("ff ff 00 0b"),
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
            new_instruction_readable="lstr f0501TalkMozyanbo"
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

set_metapod_location_function = PatchPattern(
    name="set_metapod_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 14 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 10 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 02 00 06"),
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
                data, string_section_start, f0301FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0501Sekihi"
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

TREECOCOON = PatchPattern(
    name="TREECOCOON",
    description="rewriting for ap location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 20 00 07"),
            instruction_readable="grow_stack 0x20"
        ),

        Instruction(
            identifier=2, offset=0x44, pattern=parse_pattern_bytes("00 71 00 10"),
            instruction_readable="push 0x71"
        ),
        Instruction(
            identifier=3, offset=0x48, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x4c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=5, offset=0x50, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x80, pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=7, offset=0x84, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call pokemon_unlock"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0101FuwarideTaxiStop
            ),
            new_instruction_readable="lstr fTalkFuwaride"
        ),

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"  # opcode flag request
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, set_kakuna_location_function
            ),
            new_instruction_readable="call set_kakuna_location_function"
        ),

    ]
)

TREETRANSEL = PatchPattern(
    name="TREETRANSEL",
    description="rewriting for ap location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 20 00 07"),
            instruction_readable="grow_stack 0x20"
        ),

        Instruction(
            identifier=2, offset=0x44, pattern=parse_pattern_bytes("00 72 00 10"),
            instruction_readable="push 0x72"
        ),
        Instruction(
            identifier=3, offset=0x48, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x4c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=5, offset=0x50, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x6c, pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=7, offset=0x70, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call pokemon_unlock"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0301FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0501Sekihi"
        ),

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"  # opcode flag request
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, set_metapod_location_function
            ),
            new_instruction_readable="call set_metapod_location_function"
        ),

    ]
)

evAr05Zn01_Gimmic_patterns = [
    set_chapter,
    get_friendship,
    mansion_door,
    TREECOCOON,
    TREETRANSEL,

    set_kakuna_location_function,
    set_metapod_location_function,

    # strings
    f0101FuwarideTaxiStop,
    f0301FuwarideTaxiStop
]
