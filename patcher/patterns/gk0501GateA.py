from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

wait = PatchPattern(
    name="0501GateA Wait",
    description="always showing gate as open",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),
        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("?? ?? 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=3, offset=0x88, pattern=parse_pattern_bytes("00 04 00 06"),
            instruction_readable="ret -0x4"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

    ],
)

gk0501Gate_pattern = [
    wait
]
