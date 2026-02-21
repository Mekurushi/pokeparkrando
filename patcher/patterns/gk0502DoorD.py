from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

f0502DoorD = PatchPattern(
    name="ds f0502DoorCD",
    description="replacing f0502DoorCD with f0502DoorA to simplify item unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("66 30 35 30 32 44 6f 6f 72 43 44 00"),
            instruction_readable="ds f0502DoorCD"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x6630353032446f6f724100).to_bytes(
                11,
                'big'
            ),
            new_instruction_readable="ds f0502DoorA"
        ),

    ],
)

gk0502DoorD_pattern = [
    f0502DoorD
]
