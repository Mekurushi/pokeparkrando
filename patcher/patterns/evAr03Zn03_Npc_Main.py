from patcher.helper.patttern_handler import get_attraction_id_from_dict, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, set_chapter

get_chapter = PatchPattern(
    name="get Chapter function in empoleon area",
    description="replacing chapter function to check for empoleon friendship location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr Chapter"
        ),
        Instruction(
            identifier=3, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x20, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=5, offset=0x30, pattern=parse_pattern_bytes("00 02 01 06"),
            instruction_readable="retv -0x2"
        ),
        Instruction(
            identifier=99, offset=-0x4, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),

    ],

    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x003b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x3b"  # Empoleon Friendship Id
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # best friend opcode
        ),

    ]
)

return_at9_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
        instruction_readable="grow_stack 0x7"
    ),

    Instruction(
        identifier=2, offset=0xdc, pattern=parse_pattern_bytes("0c 0d 00 10"),
        instruction_readable="push 0xc0d"
    ),

]

return_at9 = PatchPattern(
    name="Empoleon return attraction event",
    description="prep for Empoleon friendship location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0xd4, pattern=parse_pattern_bytes("0c 0d 00 10"),
            instruction_readable="push 0xc0d"
        ),

    ],
    patternPAL=return_at9_patternPALNA,
    patternNA=return_at9_patternPALNA,

    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),

    ]
)

emopleon_friendship_event = PatchPattern(
    name="Empoleon friendship event",
    description="remove unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 10 00 07"),
            instruction_readable="grow_stack 0x10"
        ),

        Instruction(
            identifier=2, offset=0x370, pattern=parse_pattern_bytes("0c 12 00 10"),
            instruction_readable="push 0xc12"
        ),
        Instruction(
            identifier=3, offset=0x374, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
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
    ]
)

emopleon_friendship_check = PatchPattern(
    name="Empoleon friendship check",
    description="always trigger betfriend",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="grow_stack 0x1"
        ),

        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=3, offset=0x40, pattern=parse_pattern_bytes("00 03 01 06"),
            instruction_readable="retv -0x3"
        ),
    ],

    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),

    ]
)

empoleon_interaction = PatchPattern(
    name="Empoleon Interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 d1 00 10"),
            instruction_readable="push 0xd1"
        ),
        Instruction(
            identifier=3, offset=0x84, pattern=parse_pattern_bytes("00 08 00 10"),  # attraction id
            instruction_readable="push 0x8"
        ),
        Instruction(
            identifier=4, offset=0x88, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_prisma_menu"
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Ice Zone Empoleon Area - Empoleon's Snow Slide Attraction"
            ),
            new_instruction_readable="update attraction id"
        ),

    ]
)

evAr03Zn03_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    get_chapter,
    return_at9,
    emopleon_friendship_event,
    emopleon_friendship_check,
    empoleon_interaction
]
