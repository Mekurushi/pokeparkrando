from patcher.helper.patttern_handler import compute_call_to_function_script, create_lstr_script, \
    get_attraction_id_from_dict, \
    get_num_battle_count_from_dict_as_instruction, \
    parse_pattern_bytes, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

set_attraction_record = PatchPattern(
    name="set_attraction_record",
    description="set attraction record for each zone option locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 0b 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 15 05 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010007).to_bytes(4, 'big'),
            new_instruction_readable="grow_stack 0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start,
                globalManager
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data,
                get_module
            ),
            new_instruction_readable="call get_module()"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x0001000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg 0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x0000000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x006d0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x6d"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150501).to_bytes(4, 'big'),
            new_instruction_readable="SC5 0x0:0x15"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020006).to_bytes(4, 'big'),
            new_instruction_readable="ret -0x2"
        ),
    ]
)

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 34 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr04Zn01_Npc_Main"
        ),

    ],
)

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
        Instruction(
            identifier=5, offset=0x57c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
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
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"  # friendship cmp
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

bastiodon_prisma_check_function = PatchPattern(
    name="unused code space",
    description="get bastiodon prisma state",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 3e 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 02 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 63 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 0a 00 06"),
            instruction_readable="---"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010007).to_bytes(4, 'big'),
            new_instruction_readable="grow_stack 0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start,
                globalManager
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data,
                get_module
            ),
            new_instruction_readable="call get_module()"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00090010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x9"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(4, 'big'),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020106).to_bytes(4, 'big'),
            new_instruction_readable="retv -0x2"
        ),

    ],
)

dugtrio_interaction = PatchPattern(
    name="dugtrio_interaction",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0f 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 e5 00 10"),
            instruction_readable="push 0xe5"
        ),

        Instruction(
            identifier=3, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x68, pattern=parse_pattern_bytes("0f fa 00 10"),
            instruction_readable="push 0xffa"
        ),
        Instruction(
            identifier=5, offset=0x6c, pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, bastiodon_prisma_check_function
            ),
            new_instruction_readable="call get_bastiodon_prisma"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x000b0016).to_bytes(4, 'big'),
            new_instruction_readable="eq"
        ),
    ]
)

diglett_interaction = PatchPattern(
    name="diglett_interaction",
    description="replacing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 e4 00 10"),
            instruction_readable="push 0xe4"
        ),

        Instruction(
            identifier=3, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x90, pattern=parse_pattern_bytes("0f f0 00 10"),
            instruction_readable="push 0xff0"
        ),
        Instruction(
            identifier=5, offset=0x94, pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
        Instruction(
            identifier=6, offset=0x284, pattern=parse_pattern_bytes("00 08 02 08"),
            instruction_readable="jz"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, bastiodon_prisma_check_function
            ),
            new_instruction_readable="call get_bastiodon_prisma"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x000b0016).to_bytes(4, 'big'),
            new_instruction_readable="eq"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay0"
        ),
    ]
)

bonsly_interaction = PatchPattern(
    name="bonsly interaction",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 d6 00 10"),
            instruction_readable="push 0xd6"
        ),

        Instruction(
            identifier=3, offset=0x158, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x234, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x238, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=6, offset=0x23c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=7, offset=0x240, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x244, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # each zone option
        Instruction(
            identifier=10, offset=0x258, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=11, offset=0x290, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=12, offset=0x294, pattern=parse_pattern_bytes("00 eb 00 10"),
            instruction_readable="push 0xeb"
        ),
        Instruction(
            identifier=13, offset=0x298, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon"
        )

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

        # each zone
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00080010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x8"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x00070010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

unknown_interaction2 = PatchPattern(  # TODO: find pokemon
    name="unkown interaction2",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 d8 00 10"),
            instruction_readable="push 0xd8"
        ),

        Instruction(
            identifier=3, offset=0x158, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x234, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x238, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=6, offset=0x23c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=7, offset=0x240, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x244, pattern=parse_pattern_bytes("00 15 04 01"),
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

unknown_interaction3 = PatchPattern(  # TODO: find pokemon
    name="unkown interaction3",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 eb 00 10"),
            instruction_readable="push 0xeb"
        ),

        Instruction(
            identifier=3, offset=0x158, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x264, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x268, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=6, offset=0x26c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=7, offset=0x270, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x274, pattern=parse_pattern_bytes("00 15 04 01"),
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

evAr04Zn01_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    special_spawn_conditions,
    gimmic_spawn_conditions,
    bastiodon_interaction,
    return_at10,
    bastiodon_friendship_event,
    gible_interaction,
    gible_interaction_2,
    mawile_interaction,
    scizor_interaction,
    marowak_interaction,
    dugtrio_interaction,
    diglett_interaction,
    bonsly_interaction,
    unknown_interaction2,
    unknown_interaction3,

    bastiodon_prisma_check_function,
    set_attraction_record
]
