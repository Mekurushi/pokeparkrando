from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, set_chapter

rotBridgeSwitch = PatchPattern(
    name="rotBridgeSwitch",
    description="fixing catch ai",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x44, pattern=parse_pattern_bytes("4e 24 00 10"),
            instruction_readable="push 0x4e24"
        ),
        Instruction(
            identifier=3, offset=0x374, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x378, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x394, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=6, offset=0x398, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),

        Instruction(
            identifier=7, offset=0x408, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=8, offset=0x40c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x428, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=10, offset=0x42c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
    ]
)

switchB = PatchPattern(
    name="switchB",
    description="fixing catch ai",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 17 00 07"),
            instruction_readable="grow_stack 0x17"
        ),

        Instruction(
            identifier=2, offset=0x4c, pattern=parse_pattern_bytes("4e 29 00 10"),
            instruction_readable="push 0x4e29"
        ),
        Instruction(
            identifier=3, offset=0x3ec, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x3f0, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x480, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=6, offset=0x484, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),

    ]
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
            identifier=3, offset=0x24, pattern=parse_pattern_bytes("1f 72 00 10"),
            instruction_readable="push 0x1f72"
        ),

        Instruction(
            identifier=4, offset=0x384, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),

    ]
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),

    ],
)

evAr06Zn01_Gimmic_patterns = [
    set_chapter,
    get_friendship,
    rotBridgeSwitch,
    taxi_stop,
    switchB,
    special_spawn_conditions
]
