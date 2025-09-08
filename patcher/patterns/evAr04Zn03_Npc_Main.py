from patcher.helper.patttern_handler import get_attraction_id_from_dict, parse_pattern_bytes
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
        Instruction(
            identifier=5, offset=0x404,
            pattern=parse_pattern_bytes("00 0b 00 10"),  # attraction id
            instruction_readable="push 0xb"
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
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Magma Zone Blaziken Area - Blaziken's Boulder Bash Attraction"
            ),
            new_instruction_readable="update attraction id"
        ),
    ],
)

get_friendship = PatchPattern(
    name="get_friendship function",
    description="replacing with best friend request",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),

        Instruction(
            identifier=2, offset=0x4c, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=3, offset=0x60, pattern=parse_pattern_bytes("00 05 01 06"),
            instruction_readable="retv -0x5"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x4b"  # best friend opcode
        ),

    ]
)

evAr04Zn03_Npc_Main_patterns = [
    blaziken_interaction,
    get_friendship
]
