from patcher.helper.patttern_handler import compute_call_to_function_script, create_lstr_instruction_fsb, \
    parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 35 5a 6e 30 32 5f 47 69 6d 6d 69 63 00"),
            instruction_readable="ds evAr05Zn02_Gimmic"
        ),

    ],
)

f0101FuwarideTaxiStop = PatchPattern(
    name="ds f0101FuwarideTaxiStop",
    description="replacing f0101FuwarideTaxiStop with flag for voltorb location",
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x663035303254616c6b596f6e6f697200).to_bytes(16, 'big'),
            new_instruction_readable="ds f0502TalkYonoir"
        ),

    ],
)

set_voltorb_location_function = PatchPattern(
    name="set_voltorb_location",
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010007).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="grow_stack -0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, globalManager.name
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data, get_module
            ),
            new_instruction_readable="call get_module"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, f0101FuwarideTaxiStop.name
            ),
            new_instruction_readable="lstr f0502TalkYonoir"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150401).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC4 0x0:0x15"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x2"
        ),
    ]
)

JAR_BIRIRI = PatchPattern(
    name="JAR_BIRIRI",
    description="rewriting for ap location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 21 00 07"),
            instruction_readable="grow_stack 0x21"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("00 b7 00 10"),
            instruction_readable="push 0xb7"
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
            identifier=6, offset=0x5c, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=7, offset=0x60, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call pokemon_unlock"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, f0101FuwarideTaxiStop.name
            ),
            new_instruction_readable="lstr fTalkFuwaride"
        ),

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"  # opcode flag request
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data, set_voltorb_location_function
            ),
            new_instruction_readable="call set_voltorb_location_function"
        ),

    ]
)

evAr05Zn02_Gimmic_patterns = [
    string_section_start,
    globalManager,
    set_chapter,
    get_friendship,
    JAR_BIRIRI,

    set_voltorb_location_function,

    # strings
    f0101FuwarideTaxiStop,
]
