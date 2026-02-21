from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

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

evAr06Zn01_DemoEvent_patterns = [
    special_spawn_conditions,
]
