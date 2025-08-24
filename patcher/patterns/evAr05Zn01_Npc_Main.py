from patcher.helper.patttern_handler import parse_pattern_bytes, create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch

trap_gate = PatchPattern(
    name="Trap Event Mansion Gate",
    description="removing Trap Event",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr EventScript"
        ),

        Instruction(
            identifier=3, offset=0xb8, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 3, matches),
            new_instruction_readable="jmp"
        ),

    ]
)

evAr05Zn01_Npc_Main_patterns = [
    trap_gate
]
