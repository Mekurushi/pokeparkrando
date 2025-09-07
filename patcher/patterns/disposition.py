from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

disposition_pattern = PatchPattern(
    name="Disposition",
    description="always spawning Drifblim",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 1f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff ff ff ff"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0xffffffff).to_bytes(4, 'big'),
            new_instruction_readable="---"
        ),

    ],
)

disposition_patterns = [
    disposition_pattern
]
