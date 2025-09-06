from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

set_chapter = PatchPattern(
    name="set_chapter",
    description="removing set_chapter",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

        Instruction(
            identifier=3, offset=0x20, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=4, offset=0x48, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x4c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x50, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030006).to_bytes(4, 'big'),
            new_instruction_readable="ret -0x3"
        ),
    ]
)

evAr06Zn01_Gimmic_patterns = [
    set_chapter,

]
