from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

f0402FireWallB = PatchPattern(
    name="ds f0402FireWallB",
    description="replacing f0402FireWallB with f0402FireWallA to simplify item unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("66 30 34 30 32 46 69 72 65 57 61 6c 6c 42 00"),
            instruction_readable="ds f0402FireWallB"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x66303430324669726557616c6c4100).to_bytes(
                15,
                'big'
            ),
            new_instruction_readable="ds f0402FireWallA"
        ),

    ],
)

gkFireWall_pattern = [
    f0402FireWallB
]
