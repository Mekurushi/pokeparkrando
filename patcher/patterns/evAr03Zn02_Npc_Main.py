from patcher.helper.patttern_handler import parse_pattern_bytes, create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch

lift_top = PatchPattern(
    name="Lift Top",
    description="removing Prinplup friendship condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0x48, pattern=parse_pattern_bytes("00 b8 00 10"),
            instruction_readable="push 0xb8"
        ),

        Instruction(
            identifier=3, offset=0x4c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=4, offset=0x50, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),

    ]
)

evAr03Zn02_Npc_Main_patterns = [
    lift_top,
]
