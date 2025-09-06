from patcher.helper.patttern_handler import compute_bl_to_function_script, create_lstr_script, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 36 5a 6e 30 32 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr06Zn02_Npc_Main"
        ),

    ],
)

globalManager = PatchPattern(
    name="ds GlobalManager",
    description="using GlobalManager for lstr instructions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("47 6c 6f 62 61 6c 4d 61 6e 61 67 65 72 00"),
            instruction_readable="ds GlobalManager"
        ),

    ]
)
get_module = PatchPattern(
    name="get module",
    description="using get module for calls",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="grow_stack 0x1"
        ),
        Instruction(
            identifier=2, offset=0x4,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=3, offset=0x8,
            pattern=parse_pattern_bytes("00 10 01 01"),
            instruction_readable="SC1 0x0:0x10"
        ),
    ]
)

set_chapter = PatchPattern(
    name="set_chapter",
    description="removing set_chapter",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

        Instruction(
            identifier=3, offset=0x20, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=4, offset=0x48, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x4c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x50, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030006).to_bytes(4, 'big'),
            new_instruction_readable="ret -0x3"
        ),
    ]
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

rayquaza_interaction = PatchPattern(
    name="rayquaza interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
            instruction_readable="grow_stack 0xb"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 e8 00 10"),
            instruction_readable="push 0x1e8"
        ),

        Instruction(
            identifier=3, offset=0x18c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x190, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_prisma_init"
        ),
        Instruction(
            identifier=5, offset=0x394, pattern=parse_pattern_bytes("00 01 00 10"),  # attraction id
            instruction_readable="push 0x1"
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
    ]
)

get_rayquaza_friendship_location_state = PatchPattern(
    name="rayquaza friendship location state",
    description="get bestfriend for rayquaza",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 63 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 03 01 06"),
            instruction_readable="---"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020007).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="grow_stack 0x2"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, globalManager
            ),
            new_instruction_readable="lstr globalmanager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, get_module
            ),
            new_instruction_readable="call get_module"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00950010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x95"  # rayquaza friendship id
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # best friend opcode
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffe000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x2"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020106).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="retv -0x2"
        ),
    ]
)

return_at02_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
        instruction_readable="grow_stack 0x9"
    ),
    Instruction(
        identifier=2, offset=0x50, pattern=parse_pattern_bytes("01 e8 00 10"),
        instruction_readable="push 0x1e8"
    ),

    Instruction(
        identifier=3, offset=0x58, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter"
    ),
    Instruction(
        identifier=4, offset=0x11c, pattern=parse_pattern_bytes("23 46 00 10"),
        instruction_readable="push 0x2346"
    ),

]

return_at02 = PatchPattern(
    name="return_at02",
    description="return attraction 02",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x50, pattern=parse_pattern_bytes("01 e8 00 10"),
            instruction_readable="push 0x1e8"
        ),

        Instruction(
            identifier=3, offset=0x58, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x114, pattern=parse_pattern_bytes("23 46 00 10"),
            instruction_readable="push 0x2346"
        ),

    ],
    patternPAL=return_at02_patternPALNA,
    patternNA=return_at02_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, get_rayquaza_friendship_location_state
            ),
            new_instruction_readable="call get_rayquaza_friendship_location_state"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
    ]
)

rayquaza_friendship_event = PatchPattern(
    name="rayquaza_friendship_event",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("01 e8 00 10"),
            instruction_readable="push 0x1e8"
        ),

        Instruction(
            identifier=3, offset=0x1d0, pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=4, offset=0x1d4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0602TalkRekkuuza"
        ),
        Instruction(
            identifier=5, offset=0x1d8, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=6, offset=0x1dc, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=7, offset=0x1e0, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
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
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
    ]
)

furret_interaction = PatchPattern(
    name="furret interaction",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 d8 00 10"),
            instruction_readable="push 0x1d8"
        ),

        Instruction(
            identifier=3, offset=0x150, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x21c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x254, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=6, offset=0x258, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=7, offset=0x25c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x260, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
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
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
    ]
)

evAr06Zn02_Npc_Main_patterns = [
    set_chapter,
    get_friendship,

    rayquaza_interaction,
    furret_interaction,
    return_at02,
    rayquaza_friendship_event,
    get_rayquaza_friendship_location_state,

]
