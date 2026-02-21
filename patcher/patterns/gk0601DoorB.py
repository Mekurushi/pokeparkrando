from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

wait = PatchPattern(
    name="gk0601DoorB Close",
    description="always open flygon door",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),
        Instruction(
            identifier=2, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0601DoorBOpen"
        ),
        Instruction(
            identifier=3, offset=0x50, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x58, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
    ],
)

gk0601DoorB_pattern = [
    wait
]
