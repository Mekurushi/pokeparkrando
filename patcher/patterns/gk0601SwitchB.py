from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

f0601FireWallB = PatchPattern(
    name="ds f0601FireWallB",
    description="f0601FireWallB replacing with f0601TalkKamex",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("66 30 36 30 31 46 69 72 65 57 61 6c 6c 42 00"),
            instruction_readable="ds f0601FireWallB"
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

gk0601SwitchB_pattern = [
    f0601FireWallB
]
