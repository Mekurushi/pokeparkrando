from patcher.helper.patttern_handler import create_jmp_instruction_script, parse_pattern_bytes, patch_taxi_stop
from patcher.models.models import Instruction, Patch, PatchPattern

taxi_stop = PatchPattern(
    name="ice zone taxi stop",
    description="removing zone drifblim unlock",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 1c 00 07"),
            instruction_readable="grow_stack 0x1c"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr GlobalManager"
        ),
        Instruction(
            identifier=3, offset=0x18, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x1c, pattern=parse_pattern_bytes("4e 29 00 10"),
            instruction_readable="push 0x4e2b"
        ),
        Instruction(
            identifier=5, offset=0x40, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=6, offset=0x458, pattern=parse_pattern_bytes("00 1d 00 06"),
            instruction_readable="ret -0x1d"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: patch_taxi_stop(plando_dict),
            new_instruction_readable="push 0x1"
        ),

    ],
)

special_spawn_conditions = PatchPattern(
    name="special_spawn_conditions",
    description="removing drifblim despawn",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x108, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0x10c, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x110, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x124, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x130, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 6, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

evAr03Zn02_Gimmic_patch_pattern = [
    taxi_stop,
    special_spawn_conditions
]
