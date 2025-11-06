from patcher.helper.patttern_handler import parse_pattern_bytes, create_lstr_script
from patcher.models.models import PatchPattern, Instruction, Patch


wait = PatchPattern(
    name="wait for RockB",
    description="replacing fOrdileStone flag with gyarados prisma condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
            ),
        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr fOrdileStone"
        ),
        Instruction(
            identifier=3, offset=0x18, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00050010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x5"
        ),

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),
    ],
)

gkRockB = [
    wait,
]
