from patcher.helper.patttern_handler import get_attraction_id_from_dict, get_num_battle_count_from_dict_as_instruction, \
    parse_pattern_bytes, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch

special_spawn_conditions = PatchPattern(
    name="special spawn conditions",
    description="replacing special spawn conditions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0x24, pattern=parse_pattern_bytes("00 c6 02 08"),
            instruction_readable="jz"
        ),

        Instruction(
            identifier=3, offset=0x340, pattern=parse_pattern_bytes("00 08 00 06"),
            instruction_readable="ret -0x8"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 3, matches),
            new_instruction_readable="jmp"
        ),

    ]
)

gimmic_spawn_conditions = PatchPattern(
    name="gimmic spawn conditions",
    description="replacing gimmic spawn conditions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),

        Instruction(
            identifier=2, offset=0x24, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=3, offset=0x28, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x2c, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="store_arg -0x3"
        ),
        Instruction(
            identifier=5, offset=0x30, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x34, pattern=parse_pattern_bytes("10 04 00 10"),
            instruction_readable="push 0x1004"
        ),
        Instruction(
            identifier=7, offset=0x38, pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
        Instruction(
            identifier=8, offset=0x3c, pattern=parse_pattern_bytes("00 18 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=9, offset=0xa0, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0401RailA"
        ),
        Instruction(
            identifier=10, offset=0x160, pattern=parse_pattern_bytes("00 06 00 06"),
            instruction_readable="ret -0x6"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00090010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x9"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffe000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(4, 'big'),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00180108).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 10,
                matches
            ),
            new_instruction_readable="jmp"
        ),
    ]
)

bastiodon_interaction = PatchPattern(
    name="bastiodon interaction",
    description="removing unnecessary dialog and unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 19 00 07"),
            instruction_readable="grow_stack 0x19"
        ),

        Instruction(
            identifier=2, offset=0x8c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr fRockTalkTorideps"
        ),
        Instruction(
            identifier=3, offset=0x3bc, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),
        Instruction(
            identifier=4, offset=0x550, pattern=parse_pattern_bytes("00 09 00 10"),
            instruction_readable="push 0x9"  # attraction id
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 3, matches,
                "jmp"
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Cavern Zone Main Area - Bastiodon's Panel Crush Attraction"
            ),
            new_instruction_readable="update attraction id"
        ),

    ]
)

return_at_10_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 11 00 07"),
        instruction_readable="grow_stack 0x11"
    ),

    Instruction(
        identifier=2, offset=0x21c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr f0401ClearTorideps"
    ),
    Instruction(
        identifier=3, offset=0x224, pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1"
    ), ]

return_at10 = PatchPattern(
    name="return at 10",
    description="bastiodon friendship location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 11 00 07"),
            instruction_readable="grow_stack 0x11"
        ),

        Instruction(
            identifier=2, offset=0x214, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0401ClearTorideps"
        ),
        Instruction(
            identifier=3, offset=0x21c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

    ],
    patternPAL=return_at_10_patternPALNA,
    patternNA=return_at_10_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00850010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x85"  # bastiodon friendship id
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x4b"  # best_friend request opcode
        ),
    ]
)

bastiodon_friendship_event = PatchPattern(
    name="bastiodon friendship event",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x1f8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=3, offset=0x1fc, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0401ClearTorideps"
        ),
        Instruction(
            identifier=4, offset=0x200, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=5, offset=0x204, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=6, offset=0x208, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
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

gible_interaction = PatchPattern(
    name="gible_interaction",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
            instruction_readable="grow_stack 0xb"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 01 00 10"),
            instruction_readable="push 0x101"
        ),

        Instruction(
            identifier=3, offset=0x64, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x68, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x0ffb0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xffb"  # always entering power comp
        ),
    ]
)

gible_interaction_2 = PatchPattern(
    name="gible_interaction_2",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
            instruction_readable="grow_stack 0xb"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 d2 00 10"),
            instruction_readable="push 0xd2"
        ),

        Instruction(
            identifier=3, offset=0x64, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x68, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x0ffb0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xffb"  # always entering power comp
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

mawile_interaction = PatchPattern(
    name="mawile_interaction",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 d9 00 10"),
            instruction_readable="push 0xd9"
        ),

        Instruction(
            identifier=3, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x4c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x0ffb0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xffb"  # always entering power comp
        ),
    ]
)

scizor_interaction = PatchPattern(
    name="scizor_interaction",
    description="set battle counter by options",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 ed 00 10"),
            instruction_readable="push 0xed"
        ),

        Instruction(
            identifier=3, offset=0xc0, pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
        ),
        Instruction(
            identifier=4, offset=0x1b0, pattern=parse_pattern_bytes("00 05 00 10"),
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

marowak_interaction = PatchPattern(
    name="marowak_interaction",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 dd 00 10"),
            instruction_readable="push 0xdd"
        ),

        Instruction(
            identifier=3, offset=0x64, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x68, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x0ffb0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xffb"  # always entering power comp
        ),
    ]
)
# TODO Dugtrio

evAr04Zn01_Npc_Main_patterns = [
    special_spawn_conditions,
    gimmic_spawn_conditions,
    bastiodon_interaction,
    return_at10,
    bastiodon_friendship_event,
    get_friendship,
    gible_interaction,
    gible_interaction_2,
    mawile_interaction,
    set_chapter,
    scizor_interaction,
    marowak_interaction
]
