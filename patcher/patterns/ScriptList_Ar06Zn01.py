from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

f0601FireWallB = PatchPattern(
    name="f0601FireWallB",
    description="replace f0601FireWallB with f0601TalkKamex",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 36 30 31 46 69 72 65 57 61 6c 6c 42 00"),
            instruction_readable="ds f0601FireWallB"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x663036303154616c6b4b616d657800).to_bytes(
                15,
                'big'
            ),
            new_instruction_readable="ds f0601TalkKamex"
        ),
    ]
)
ScriptList_Ar06Zn01_patterns = [
    f0601FireWallB
]
