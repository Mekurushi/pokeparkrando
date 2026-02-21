from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

wait = PatchPattern(
    name="0402Bridge Wait",
    description="replacing f0402Bridge call with rhyperior prisma",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),
        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0402Bridge"
        ),
        Instruction(
            identifier=3, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x000a0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0xa"  # rhyperior prisma
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00510010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x51"  # check prisma request opcode
        ),
    ],
)

gk0402Bridge_pattern = [
    wait
]
