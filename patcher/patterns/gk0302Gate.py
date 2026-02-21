from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

close = PatchPattern(
    name="0302Gate Close",
    description="replacing f0302GateOpen call with gyarados prisma",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),
        Instruction(
            identifier=2, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0302GateOpen"
        ),
        Instruction(
            identifier=3, offset=0x50, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00050010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x5"  # gyarados prisma
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

gk0302Gate_pattern = [
    close
]
