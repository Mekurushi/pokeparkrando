from patcher.helper.patttern_handler import compute_bl_to_function_script, create_jmp_instruction_script, \
    create_lstr_script, \
    get_attraction_id_from_dict, get_num_battle_count_from_dict_as_instruction, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 36 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr06Zn01_Npc_Main"
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

absol_interaction = PatchPattern(
    name="absol interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
            instruction_readable="grow_stack 0xc"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 b7 00 10"),
            instruction_readable="push 0x1b7"
        ),

        Instruction(
            identifier=3, offset=0x3bc, pattern=parse_pattern_bytes("00 00 00 10"),  # attraction id
            instruction_readable="push 0x0"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Granite Zone Main Area - Absol's Hurdle Bounce Attraction"
            ),
            new_instruction_readable="update attraction id"
        ),
    ]
)

get_salamence_friendship_location_state = PatchPattern(
    name="salamence friendship location state",
    description="get bestfriend for salamence",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff f2 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 03 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("ff ce 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 13 00 06"),
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
            patch_function=lambda offset, data, plando_dict, matches: (0x009d0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x9d"  # salamence friendship id
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

get_absol_friendship_location_state = PatchPattern(
    name="absol friendship location state",
    description="get bestfriend for absol",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff f1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 03 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("ff ce 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 12 00 06"),
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00460010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x46"  # absol friendship id
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

return_at01_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
        instruction_readable="grow_stack 0xa"
    ),
    Instruction(
        identifier=2, offset=0x74, pattern=parse_pattern_bytes("01 b7 00 10"),
        instruction_readable="push 0x1b7"
    ),

    Instruction(
        identifier=3, offset=0x7c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter"
    ),
    Instruction(
        identifier=4, offset=0x178, pattern=parse_pattern_bytes("1f 5e 00 10"),
        instruction_readable="push 0x1f5e"
    ),

]

return_at01 = PatchPattern(
    name="return_at01",
    description="return attraction 01",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),
        Instruction(
            identifier=2, offset=0x6c, pattern=parse_pattern_bytes("01 b7 00 10"),
            instruction_readable="push 0x1b7"
        ),

        Instruction(
            identifier=3, offset=0x74, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x170, pattern=parse_pattern_bytes("1f 5e 00 10"),
            instruction_readable="push 0x1f5e"
        ),

    ],
    patternPAL=return_at01_patternPALNA,
    patternNA=return_at01_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, get_absol_friendship_location_state
            ),
            new_instruction_readable="call get_absol_friendship_location_state"
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

salamence_interaction_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
        instruction_readable="grow_stack 0xc"
    ),

    Instruction(
        identifier=2, offset=0x3c, pattern=parse_pattern_bytes("01 b6 00 10"),
        instruction_readable="push 0x1b6"
    ),

    Instruction(
        identifier=3, offset=0x4f8, pattern=parse_pattern_bytes("00 0e 00 10"),  # attraction id
        instruction_readable="push 0xe"
    ),

]

salamence_interaction = PatchPattern(
    name="salamence interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
            instruction_readable="grow_stack 0xc"
        ),

        Instruction(
            identifier=2, offset=0x3c, pattern=parse_pattern_bytes("01 b6 00 10"),
            instruction_readable="push 0x1b6"
        ),

        Instruction(
            identifier=3, offset=0x4fc, pattern=parse_pattern_bytes("00 0e 00 10"),  # attraction id
            instruction_readable="push 0xe"
        ),

    ],
    patternPAL=salamence_interaction_patternPALNA,
    patternNA=salamence_interaction_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Granite Zone Salamence Area - Salamence's Sky Race Attraction"
            ),
            new_instruction_readable="update attraction id"
        ),
    ]
)

return_at15_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
        instruction_readable="grow_stack 0xa"
    ),
    Instruction(
        identifier=2, offset=0x74, pattern=parse_pattern_bytes("01 b6 00 10"),
        instruction_readable="push 0x1b6"
    ),

    Instruction(
        identifier=3, offset=0x7c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter"
    ),
    Instruction(
        identifier=4, offset=0x178, pattern=parse_pattern_bytes("1f c2 00 10"),
        instruction_readable="push 0x1fc2"
    ),

]

return_at15 = PatchPattern(
    name="return_at15",
    description="return attraction 15",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),
        Instruction(
            identifier=2, offset=0x6c, pattern=parse_pattern_bytes("01 b6 00 10"),
            instruction_readable="push 0x1b6"
        ),

        Instruction(
            identifier=3, offset=0x74, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x170, pattern=parse_pattern_bytes("1f c2 00 10"),
            instruction_readable="push 0x1fc2"
        ),

    ],
    patternPAL=return_at15_patternPALNA,
    patternNA=return_at15_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, get_salamence_friendship_location_state
            ),
            new_instruction_readable="call get_salamence_friendship_location_state"
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

furret_interaction = PatchPattern(
    name="furret interaction",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 b9 00 10"),
            instruction_readable="push 0x1b9"
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
            identifier=5, offset=0x220, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=6, offset=0x224, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=7, offset=0x228, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x22c, pattern=parse_pattern_bytes("00 15 04 01"),
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

arcanine_interaction = PatchPattern(
    name="arcanine interaction",
    description="updating wincounter with options",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 b0 00 10"),
            instruction_readable="push 0x1b0"
        ),

        Instruction(
            identifier=3, offset=0xc8, pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
        ),
        Instruction(
            identifier=4, offset=0x1b8, pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_num_battle_count_from_dict_as_instruction(
                plando_dict
            ),
            new_instruction_readable="push battlecounter"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: get_num_battle_count_from_dict_as_instruction(
                plando_dict
            ),
            new_instruction_readable="push battlecounter"
        ),

    ]
)

special_spawn_conditions = PatchPattern(
    name="special_spawn_conditions",
    description="removing drifblim despawn",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),

        Instruction(
            identifier=2, offset=0x1a0, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0x1a4, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),

        Instruction(
            identifier=4, offset=0x1a8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x1bc, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x1c8, pattern=parse_pattern_bytes("00 04 00 06"),
            instruction_readable="ret -0x4"
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

evAr06Zn01_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    absol_interaction,
    salamence_interaction,
    furret_interaction,
    arcanine_interaction,

    return_at01,
    return_at15,
    get_absol_friendship_location_state,
    get_salamence_friendship_location_state,
    special_spawn_conditions
]

# TODO:
# Bellosom
# Mareep
