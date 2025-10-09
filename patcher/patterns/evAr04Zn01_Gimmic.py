from patcher.helper.patttern_handler import compute_call_to_function_script, create_lstr_script, parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 34 5a 6e 30 31 5f 47 69 6d 6d 69 63 00"),
            instruction_readable="ds evAr04Zn01_Gimmic"
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
                0x6630343031436c656172546f72696465707300).to_bytes(19, 'big'),
            new_instruction_readable="ds f0401ClearTorideps"
        ),

    ],
)

f0301FuwarideTaxiStop = PatchPattern(
    name="ds f0301FuwarideTaxiStop",
    description="replacing f0301FuwarideTaxiStop with flag for magnemite location",
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
                0x663032303154616c6b456c65626f6f00).to_bytes(16, 'big'),
            new_instruction_readable="ds f0201TalkEleboo"
        ),

    ],
)

slFindModule = PatchPattern(
    name="ds slFindModule:_module_not_found",
    description="replacing slFindModule string with string of other flag, breaking the next flag string",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes(
                "73 6c 46 69 6e 64 4d 6f 64 75 6c 65 3a 20 6d 6f 64 75 6c 65 20 6e 6f 74 20 66 6f 75 6e 64 20 25 73 0a 00"
            ),
            instruction_readable="slFindModule: module not found %s\n"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (
                0x663031303154616c6b4675736869676964616e654265666f726500).to_bytes(27, 'big'),
            new_instruction_readable="ds f0101TalkFushigidaneBefore"
        ),

    ],
)

f0402FuwarideTaxiStop = PatchPattern(
    name="ds f0402FuwarideTaxiStop",
    description="replacing f0402FuwarideTaxiStop with flag for magnemite location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 34 30 32 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
            instruction_readable="ds f0402FuwarideTaxiStop"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (
                0x6654616c6b467577617269646500).to_bytes(14, 'big'),
            new_instruction_readable="ds fTalkFuwaride"
        ),

    ],
)

box_digda = PatchPattern(
    name="box_digda",
    description="unlock digda location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 19 00 07"),
            instruction_readable="grow_stack 0x19"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("00 9a 00 10"),
            instruction_readable="push 0x9a"
        ),
        Instruction(
            identifier=3, offset=0x38, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x3c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=5, offset=0x40, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        # diglett dialog
        Instruction(
            identifier=6, offset=0x444, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0401DialogDigda"
        ),
        Instruction(
            identifier=7, offset=0x458, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0101FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0401ClearTorideps"
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
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0101FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0401ClearTorideps"
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
    ]
)

box_coil1 = PatchPattern(
    name="box_coil1",
    description="rewriting for ap location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 21 00 07"),
            instruction_readable="grow_stack 0x21"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("00 58 00 10"),
            instruction_readable="push 0x58"
        ),
        Instruction(
            identifier=3, offset=0x38, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x3c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=5, offset=0x40, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x64, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=7, offset=0x68, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call pokemon_unlock"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0301FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0201TalkEleboo"
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_magnemite_location_function
            ),
            new_instruction_readable="call set_magnemite_location"
        ),

    ]
)

box_coil2 = PatchPattern(
    name="box_coil2",
    description="rewriting for ap location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 21 00 07"),
            instruction_readable="grow_stack 0x21"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("00 a8 00 10"),
            instruction_readable="push 0xa8"
        ),
        Instruction(
            identifier=3, offset=0x38, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x3c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=5, offset=0x40, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x64, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=7, offset=0x68, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call pokemon_unlock"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, slFindModule
            ),
            new_instruction_readable="lstr f0101TalkFushigidaneBefore"
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_magnemite2_location_function
            ),
            new_instruction_readable="call set_magnemite2_location"
        ),

    ]
)

box_coil3 = PatchPattern(
    name="box_coil3",
    description="rewriting for ap location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 21 00 07"),
            instruction_readable="grow_stack 0x21"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("00 a9 00 10"),
            instruction_readable="push 0xa9"
        ),
        Instruction(
            identifier=3, offset=0x38, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x3c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=5, offset=0x40, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x64, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=7, offset=0x68, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call pokemon_unlock"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, f0402FuwarideTaxiStop
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_magnemite3_location_function
            ),
            new_instruction_readable="call set_magnemite3_location"
        ),

    ]
)

set_magnemite_location_function = PatchPattern(
    name="set_magnemite_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(  # 50184
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff f6 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 05 00 06"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 04 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 03 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 02 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 01 00 0b"),
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
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
            new_instruction_readable="lstr f0201TalkEleboo"
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

set_magnemite2_location_function = PatchPattern(
    name="set_magnemite2_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 c8 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 15 07 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 06 01 06"),
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
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
                data, string_section_start, slFindModule
            ),
            new_instruction_readable="lstr f0101TalkFushigidaneBefore"
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

set_magnemite3_location_function = PatchPattern(
    name="set_magnemite3_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 c9 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 15 02 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 03 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff f6 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 06 01 06"),
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
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
                data, string_section_start, f0402FuwarideTaxiStop
            ),
            new_instruction_readable="lstr fTalkFuwaride"
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

evAr04Zn01_Gimmic_patterns = [
    set_chapter,
    get_friendship,
    box_digda,
    box_coil1,
    box_coil2,
    box_coil3,

    set_magnemite_location_function,
    set_magnemite2_location_function,
    set_magnemite3_location_function,
    # strings
    f0101FuwarideTaxiStop,
    f0301FuwarideTaxiStop,
    f0402FuwarideTaxiStop,
    slFindModule
]
