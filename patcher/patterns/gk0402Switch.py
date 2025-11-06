from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

break_switch = PatchPattern(
    name="0402 bridge switch",
    description="deactivating bridge switch functionality",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),
        Instruction(
            identifier=2, offset=0x70, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0402BridgeSwitch"
        ),
        Instruction(
            identifier=3, offset=0x80, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0xb8, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x2"
        ),
    ],
)

gk0402Switch_pattern = [
    break_switch
]
