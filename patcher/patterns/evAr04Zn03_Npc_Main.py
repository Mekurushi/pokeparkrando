from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

blaziken_interaction = PatchPattern(
    name="blaziken interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 0c 00 07"),
            instruction_readable="grow_stack 0xc"
        ),
        Instruction(
            identifier=2, offset=0x30,
            pattern=parse_pattern_bytes("01 38 00 10"),
            instruction_readable="push 0x138"
        ),
        Instruction(
            identifier=3, offset=0x1b4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_prisma_init"
        ),

        Instruction(
            identifier=4, offset=0x218,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),

    ],
    patchMapJP=[
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
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(  # get bestfriend opcode
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"
        ),

    ],
)

evAr04Zn03_Npc_Main_patterns = [
    blaziken_interaction
]
