from patcher.helper.entrance_exit_names import MAGMA_ZONE_BLAZIKEN_AREA_BLAZIKEN_ATTRACTION
from patcher.helper.patttern_handler import get_attraction_id_from_dict, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, set_chapter

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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                # get bestfriend opcode
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, MAGMA_ZONE_BLAZIKEN_AREA_BLAZIKEN_ATTRACTION
            ),
            new_instruction_readable="update attraction id"
        ),
    ],
)

blaziken2_interactionPALNA = [
    Instruction(
        identifier=1, offset=0x0,
        pattern=parse_pattern_bytes("00 23 00 07"),
        instruction_readable="grow_stack 0x23"
    ),
    Instruction(
        identifier=2, offset=0x24,
        pattern=parse_pattern_bytes("01 38 00 10"),
        instruction_readable="push 0x138"
    ),
    Instruction(
        identifier=3, offset=0x8cc,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_prisma_init"
    ),
    Instruction(
        identifier=4, offset=0x9cc,
        pattern=parse_pattern_bytes("00 0b 00 10"),  # attraction id
        instruction_readable="push 0xb"
    ),
]

blaziken2_interaction = PatchPattern(
    name="blaziken 2 interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 17 00 07"),
            instruction_readable="grow_stack 0x17"
        ),
        Instruction(
            identifier=2, offset=0x24,
            pattern=parse_pattern_bytes("01 38 00 10"),
            instruction_readable="push 0x138"
        ),
        Instruction(
            identifier=3, offset=0x658,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_prisma_init"
        ),
        Instruction(
            identifier=4, offset=0x758,
            pattern=parse_pattern_bytes("00 0b 00 10"),  # attraction id
            instruction_readable="push 0xb"
        ),
    ],
    patternNA=blaziken2_interactionPALNA,
    patternPAL=blaziken2_interactionPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, MAGMA_ZONE_BLAZIKEN_AREA_BLAZIKEN_ATTRACTION
            ),
            new_instruction_readable="update attraction id"
        ),
    ],
)

evAr04Zn03_Npc_Main_patterns = [
    set_chapter,
    blaziken_interaction,
    blaziken2_interaction,
    get_friendship
]
