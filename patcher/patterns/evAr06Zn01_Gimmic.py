from patcher.helper.patttern_handler import create_lstr_script, parse_pattern_bytes, patch_taxi_stop
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, set_chapter

f0602FuwarideTaxiStop = PatchPattern(
    name="f0602FuwarideTaxiStop",
    description="replace f0602FuwarideTaxiStop with f0601TalkKamex",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 36 30 32 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
            instruction_readable="ds f0602FuwarideTaxiStop"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x663036303154616c6b4b616d657800).to_bytes(
                15,
                'big'
            ),
            new_instruction_readable="ds f0601TalkKamex"
        ),
    ]
)

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 36 5a 6e 30 31 5f 47 69 6d 6d 69 63 00"),
            instruction_readable="ds evAr06Zn01_Gimmic"
        ),

    ],
)

special_spawn_conditions = PatchPattern(
    name="special_spawn_condtitions",
    description="remove despawns",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr GlobalManager"
        ),
        Instruction(
            identifier=3, offset=0x13c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=4, offset=0x384, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
        Instruction(
            identifier=5, offset=0x4c, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"  # blastoise condition
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x1f810010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1f81"
        ),
    ]
)

switchB = PatchPattern(
    name="granite zone switchB",
    description="replacing firewallb with f0601TalkKamex",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 17 00 07"),
            instruction_readable="grow_stack 0x17"
        ),
        Instruction(
            identifier=2, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0601FireWallB"
        ),
        Instruction(
            identifier=3, offset=0x4c, pattern=parse_pattern_bytes("4e 29 00 10"),
            instruction_readable="push 0x4e29"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_script(
                data, string_section_start, f0602FuwarideTaxiStop
            ),
            new_instruction_readable="lstr f0601TalkKamex"
        ),

    ],
)

taxi_stop = PatchPattern(
    name="granite zone taxi stop",
    description="removing zone drifblim unlock",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 1c 00 07"),
            instruction_readable="grow_stack 0x1c"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr GlobalManager"
        ),
        Instruction(
            identifier=3, offset=0x18, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x1c, pattern=parse_pattern_bytes("4e 23 00 10"),
            instruction_readable="push 0x4e23"
        ),
        Instruction(
            identifier=5, offset=0x40, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=6, offset=0x450, pattern=parse_pattern_bytes("00 1d 00 06"),
            instruction_readable="ret -0x1d"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: patch_taxi_stop(plando_dict),
            new_instruction_readable="push 0x1"
        ),

    ],
)

evAr06Zn01_Gimmic_patterns = [
    set_chapter,
    get_friendship,
    taxi_stop,
    special_spawn_conditions,
    switchB,

    f0602FuwarideTaxiStop
]
