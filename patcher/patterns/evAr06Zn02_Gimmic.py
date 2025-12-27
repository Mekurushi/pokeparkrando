from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

taxi_stop = PatchPattern(
    name="flower zone taxi stop",
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
            identifier=4, offset=0x1c, pattern=parse_pattern_bytes("4e 21 00 10"),
            instruction_readable="push 0x4e21"
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big') if
            plando_dict["Options"][
                "unlock_fast_travel_with_taxi_stop"] else None,
            new_instruction_readable="push 0x1"
        ),

    ],
)

evAr06Zn02_Gimmic_patch_pattern = [
    taxi_stop
]
