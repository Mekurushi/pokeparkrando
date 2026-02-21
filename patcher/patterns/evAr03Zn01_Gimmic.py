from patcher.helper.patttern_handler import parse_pattern_bytes, patch_taxi_stop
from patcher.models.models import Instruction, Patch, PatchPattern

taxi_stop = PatchPattern(
    name="beach taxi stop",
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
            identifier=4, offset=0x1c, pattern=parse_pattern_bytes("4e 2b 00 10"),
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

recycle = PatchPattern(
    name="Recycle",
    description="increeasing after errand berry gain",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),
        Instruction(
            identifier=2, offset=0xa8, pattern=parse_pattern_bytes("00 06 00 10"),
            instruction_readable="push 0x6"
        ),
        Instruction(
            identifier=3, offset=0x52c, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
                ) if
            plando_dict["Options"]["remove_errand_power_comp_locations"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00640010).to_bytes(
                4, 'big'
                ),
            new_instruction_readable="push 0x64"
        ),

    ],
)

evAr03Zn01_Gimmic_patch_pattern = [
    taxi_stop,
    recycle
]
