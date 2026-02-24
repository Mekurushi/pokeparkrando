from patcher.helper.entrance_exit_names import ICE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, \
    ICE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, ICE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, \
    ICE_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, \
    ICE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, \
    ICE_ZONE_MAIN_AREA_ICE_ZONE_LAPRAS, \
    ICE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, ICE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, \
    ICE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL
from patcher.helper.patttern_handler import compute_call_instruction_fsb, create_lstr_instruction_fsb, \
    get_exit_zone_area_position_data, get_num_battle_count_from_dict_as_instruction, \
    parse_pattern_bytes, compute_jmp_instruction_fsb
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import disposManager, get_friendship, get_module, globalManager, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 33 5a 6e 30 32 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="evAr03Zn02_Npc_Main"
        ),

    ],
)

f0302TalkTree = PatchPattern(
    name="ds f0302TalkTree",
    description="replacing EventManager string with string of other flag, breaking the next flag string",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 33 30 32 54 61 6c 6b 54 72 65 65 00"),
            instruction_readable="ds f0302TalkTree"
        ),

    ]
)

lift_top = PatchPattern(
    name="Lift Top",
    description="removing Prinplup friendship condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0x48, pattern=parse_pattern_bytes("00 b8 00 10"),
            instruction_readable="push 0xb8"
        ),

        Instruction(
            identifier=3, offset=0x4c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=4, offset=0x50, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),

    ]
)

tree_talk_trap_event = PatchPattern(
    name="Kirlia Tree Talk",
    description="removing Trap Event Complete",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0f 00 07"),
            instruction_readable="grow_stack 0xf"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr EventScript"
        ),

        Instruction(
            identifier=3, offset=0x2d8, pattern=parse_pattern_bytes("00 10 00 06"),
            instruction_readable="ret -0x10"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00100006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x10"
        ),

    ]
)
mamoswine_unlock_event_entry_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
        instruction_readable="grow_stack 0x1"
    ),

    Instruction(
        identifier=2, offset=0x24, pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1"
    ),

    Instruction(
        identifier=3, offset=0x28, pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr f0302GateOpen"
    ),
    Instruction(
        identifier=4, offset=0x2c, pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1"
    ),
    Instruction(
        identifier=5, offset=0x30, pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=6, offset=0x34, pattern=parse_pattern_bytes("00 15 04 01"),
        instruction_readable="SC4 0x0:0x15"
    ),
]
mamoswine_unlock_event_entry = PatchPattern(
    name="C03070_03080",
    description="replace f0302GateOpen flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="grow_stack 0x1"
        ),

        Instruction(
            identifier=2, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

        Instruction(
            identifier=3, offset=0x20, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0302GateOpen"
        ),
        Instruction(
            identifier=4, offset=0x24, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=5, offset=0x28, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=6, offset=0x2c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patternPAL=mamoswine_unlock_event_entry_patternPALNA,
    patternNA=mamoswine_unlock_event_entry_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, f0302TalkTree.name
            ),
            new_instruction_readable="lstr f0302TalkTree"
        ),

    ]
)
mamoswine_unlock_event_function_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 15 00 07"),
        instruction_readable="grow_stack 0x15"
    ),

    Instruction(
        identifier=2, offset=0x3e8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call GATEOPEN"
    ),

    Instruction(
        identifier=3, offset=0x6b8, pattern=parse_pattern_bytes("0c 08 00 10"),
        instruction_readable="push 0xc08"
    ),
    Instruction(
        identifier=4, offset=0x6bc, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_chapter"
    ),
    Instruction(
        identifier=5, offset=0x6c0, pattern=parse_pattern_bytes("00 16 00 06"),
        instruction_readable="ret -0x16"
    ),
]
mamoswine_unlock_event_function = PatchPattern(
    name="piloswine_unlock",
    description="remove setChapter and other unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 15 00 07"),
            instruction_readable="grow_stack 0x15"
        ),

        Instruction(
            identifier=2, offset=0x3d4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call GATEOPEN"
        ),

        Instruction(
            identifier=3, offset=0x6a4, pattern=parse_pattern_bytes("0c 08 00 10"),
            instruction_readable="push 0xc08"
        ),
        Instruction(
            identifier=4, offset=0x6a8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
        ),
        Instruction(
            identifier=5, offset=0x6ac, pattern=parse_pattern_bytes("00 16 00 06"),
            instruction_readable="ret -0x16"
        ),
    ],
    patternPAL=mamoswine_unlock_event_function_patternPALNA,
    patternNA=mamoswine_unlock_event_function_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
    ]
)

piloswine_talk_event = PatchPattern(
    name="einomu_talk",
    description="removing event",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0f 00 07"),
            instruction_readable="grow_stack 0xf"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr EventScript"
        ),
        Instruction(
            identifier=3, offset=0x284, pattern=parse_pattern_bytes("?? ?? ?? 19"),
            instruction_readable="lea"
        ),
        Instruction(
            identifier=4, offset=0x2a0, pattern=parse_pattern_bytes("00 10 00 06"),
            instruction_readable="ret -0x10"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 3, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

froslass_interaction = PatchPattern(
    name="froslass interaction",
    description="removing story chapter based logic",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 33 00 07"),
            instruction_readable="grow_stack 0x33"
        ),

        Instruction(
            identifier=2, offset=0x50, pattern=parse_pattern_bytes("00 b5 00 10"),
            instruction_readable="push 0xb5"
        ),

        Instruction(
            identifier=3, offset=0x68, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x6c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x0bf60010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0xbf6"
        ),

    ]
)

piloswine_interaction = PatchPattern(
    name="piloswine interaction",
    description="removing story chapter based logic",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 13 00 07"),
            instruction_readable="grow_stack 0x13"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 b7 00 10"),
            instruction_readable="push 0xb7"
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
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x0c090010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0xc09"
        ),

    ]
)

mudkip_interaction = PatchPattern(
    name="mudkip interaction",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 a0 00 10"),
            instruction_readable="push 0xa0"
        ),

        Instruction(
            identifier=3, offset=0x17c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x2ac, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x2b0, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=6, offset=0x2b4, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=7, offset=0x2b8, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x2bc, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # each zone option
        Instruction(
            identifier=10, offset=0x270, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=11, offset=0x2a0, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=12, offset=0x2a4, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=13, offset=0x2a8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),

        # each zone option
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00040010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x4"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

primeape_interaction = PatchPattern(
    name="primeape interaction",
    description="updating wincounter with options",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 af 00 10"),
            instruction_readable="push 0xaf"
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
            patch_function=lambda offset, data, plando_dict,
                                  patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
                plando_dict
            ),
            new_instruction_readable="push battlecounter"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict,
                                  patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
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
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x108, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0x10c, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x110, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x124, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x130, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 6, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

special_spawn_conditions2 = PatchPattern(
    name="special_spawn_conditions2",
    description="removing drifblim despawn",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x124, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0x128, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x12c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x140, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x14c, pattern=parse_pattern_bytes("01 c2 00 10"),
            instruction_readable="push 0x1c2"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 6, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

set_attraction_record = PatchPattern(
    name="set_attraction_record",
    description="set attraction record for each zone option locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 02 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 03 01 06"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010007).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="grow_stack 0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name,
                globalManager.name
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                get_module.name
            ),
            new_instruction_readable="call get_module()"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000c).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x0001000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg 0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x0000000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x006d0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x6d"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150501).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="SC5 0x0:0x15"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020006).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="ret -0x2"
        ),
    ]
)

starly2_interaction = PatchPattern(
    name="starly 2 interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 aa 00 10"),
            instruction_readable="push 0xaa"
        ),

        Instruction(
            identifier=3, offset=0x238, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x270, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x274, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x278, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

starly_interaction = PatchPattern(
    name="starly interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 bc 00 10"),
            instruction_readable="push 0xbc"
        ),

        Instruction(
            identifier=3, offset=0x290, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),

        Instruction(
            identifier=4, offset=0x2c8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x2cc, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x2d0, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

krabby_interaction = PatchPattern(
    name="krabby interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 a1 00 10"),
            instruction_readable="push 0xa1"
        ),

        Instruction(
            identifier=3, offset=0x264, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),

        Instruction(
            identifier=4, offset=0x29c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x2a0, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x2a4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

krabby2_interaction = PatchPattern(
    name="krabby2 interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 c9 00 10"),
            instruction_readable="push 0xc9"
        ),

        Instruction(
            identifier=3, offset=0x254, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x28c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x290, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x294, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

krabby3_interaction = PatchPattern(
    name="krabby3 interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 ca 00 10"),
            instruction_readable="push 0xca"
        ),

        Instruction(
            identifier=3, offset=0x230, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x268, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x26c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x270, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

corphish_interaction = PatchPattern(
    name="corphish interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 a2 00 10"),
            instruction_readable="push 0xa2"
        ),

        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),

        Instruction(
            identifier=4, offset=0x278, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x27c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x280, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00030010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x3"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

corphish2_interaction = PatchPattern(
    name="corphish2 interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 bf 00 10"),
            instruction_readable="push 0xbf"
        ),

        Instruction(
            identifier=3, offset=0x230, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x268, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x26c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x270, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00030010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x3"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

corphish3_interaction = PatchPattern(
    name="corphish3 interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 c0 00 10"),
            instruction_readable="push 0xc0"
        ),

        Instruction(
            identifier=3, offset=0x230, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x268, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x26c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x270, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00030010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x3"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

taillow_interaction = PatchPattern(
    name="taillow interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 ac 00 10"),
            instruction_readable="push 0xac"
        ),

        Instruction(
            identifier=3, offset=0x230, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x268, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x26c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x270, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00050010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x5"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

staravia_interaction = PatchPattern(
    name="staravia interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 ab 00 10"),
            instruction_readable="push 0xab"
        ),

        Instruction(
            identifier=3, offset=0x278, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x2b0, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x2b4, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x2b8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00060010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x6"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

wingull_interaction = PatchPattern(
    name="wingull interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 cb 00 10"),
            instruction_readable="push 0xcb"
        ),

        Instruction(
            identifier=3, offset=0x230, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x268, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x26c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x270, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

wingull2_interaction = PatchPattern(
    name="wingull2 interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 ad 00 10"),
            instruction_readable="push 0xad"
        ),

        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),

        Instruction(
            identifier=4, offset=0x278, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x27c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x280, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

wingull3_interaction = PatchPattern(
    name="wingull3 interaction ice zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 cc 00 10"),
            instruction_readable="push 0xcc"
        ),

        Instruction(
            identifier=3, offset=0x230, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),

        Instruction(
            identifier=4, offset=0x268, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
        Instruction(
            identifier=5, offset=0x26c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x270, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        )
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

prinplup_interactionPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 22 00 07"),
        instruction_readable="grow_stack 0x22"
    ),

    Instruction(
        identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 b8 00 10"),
        instruction_readable="push 0xb8"
    ),

    Instruction(
        identifier=3, offset=0x1f4, pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),

]
prinplup_interaction = PatchPattern(
    name="prinplup2 interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 23 00 07"),
            instruction_readable="grow_stack 0x23"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 b8 00 10"),
            instruction_readable="push 0xb8"
        ),

        Instruction(
            identifier=3, offset=0x1f4, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patternPAL=prinplup_interactionPALNA,
    patternNA=prinplup_interactionPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00030010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x3"  # removed quest condition
        ),
    ]
)

glalie_interaction = PatchPattern(
    name="glalie interaction ice zone",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 1e 00 07"),
            instruction_readable="grow_stack 0x1e"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x50, pattern=parse_pattern_bytes("00 b2 00 10"),
            instruction_readable="push 0xb2"
        ),

        Instruction(
            identifier=3, offset=0x1c8, pattern=parse_pattern_bytes("00 03 00 10"),
            instruction_readable="push 0x3"
        ),

        Instruction(
            identifier=4, offset=0x598, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=5, offset=0x628, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["remove_errand_power_comp_locations"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 5, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
    ]
)

delibird_interaction = PatchPattern(
    name="delibird interaction ice zone",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
            instruction_readable="grow_stack 0xe"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x40, pattern=parse_pattern_bytes("00 a5 00 10"),
            instruction_readable="push 0xa5"
        ),

        Instruction(
            identifier=3, offset=0xf8, pattern=parse_pattern_bytes("00 a3 00 10"),
            instruction_readable="push 0xa3"
        ),
        Instruction(
            identifier=4, offset=0xfc, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=5, offset=0x110, pattern=parse_pattern_bytes("00 be 00 10"),
            instruction_readable="push 0xbe"
        ),
        Instruction(
            identifier=6, offset=0x114, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=7, offset=0x128, pattern=parse_pattern_bytes("00 a9 00 10"),
            instruction_readable="push 0xa9"
        ),
        Instruction(
            identifier=8, offset=0x12c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=9, offset=0x140, pattern=parse_pattern_bytes("00 a8 00 10"),
            instruction_readable="push 0xa8"
        ),
        Instruction(
            identifier=10, offset=0x144, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=11, offset=0x430, pattern=parse_pattern_bytes("ff f5 00 0b"),  # quiz condition
            instruction_readable="load_arg -0xb"
        ),
        Instruction(
            identifier=12, offset=0x744, pattern=parse_pattern_bytes("00 a3 00 10"),
            instruction_readable="push 0xa3"
        ),
        Instruction(
            identifier=13, offset=0x748, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=14, offset=0x7f4, pattern=parse_pattern_bytes("00 be 00 10"),
            instruction_readable="push 0xbe"
        ),
        Instruction(
            identifier=15, offset=0x7f8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=16, offset=0x8a4, pattern=parse_pattern_bytes("00 a9 00 10"),
            instruction_readable="push 0xa9"
        ),
        Instruction(
            identifier=17, offset=0x8a8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=18, offset=0x954, pattern=parse_pattern_bytes("00 a8 00 10"),
            instruction_readable="push 0xa8"
        ),
        Instruction(
            identifier=19, offset=0x958, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),

        Instruction(
            identifier=20, offset=0xad0, pattern=parse_pattern_bytes("00 a3 00 10"),
            instruction_readable="push 0xa3"
        ),
        Instruction(
            identifier=21, offset=0xad4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=22, offset=0xb20, pattern=parse_pattern_bytes("00 be 00 10"),
            instruction_readable="push 0xbe"
        ),
        Instruction(
            identifier=23, offset=0xb24, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=24, offset=0xb70, pattern=parse_pattern_bytes("00 a9 00 10"),
            instruction_readable="push 0xa9"
        ),
        Instruction(
            identifier=25, offset=0xb74, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
        Instruction(
            identifier=26, offset=0xbc0, pattern=parse_pattern_bytes("00 a8 00 10"),
            instruction_readable="push 0xa8"
        ),
        Instruction(
            identifier=27, offset=0xbc4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00040010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["remove_errand_power_comp_locations"] else None,
            new_instruction_readable="push 0x4"  # allow direct entering quiz when errand locations are removed
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_friendship_function.name
            ),
            new_instruction_readable="call get_friendship"
        ),
    ]
)

get_friendship_function = PatchPattern(
    name="unused code space",
    description="get friendship function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ff f1 00 0c"),
            instruction_readable="store_arg -0xf"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="load_arg -0xe"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 0d 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 30 00 10"),
            instruction_readable="push 0x30"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 15 02 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_res"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("ff f1 00 0c"),
            instruction_readable="store_arg -0xf"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("00 00 03 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("ff ce 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("00 12 00 06"),
            instruction_readable="retv -0x12"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00040007).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="grow_stack 0x4"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name,
                globalManager.name
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                get_module.name
            ),
            new_instruction_readable="call get_module()"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push_res"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000c).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name,
                disposManager.name
            ),
            new_instruction_readable="lstr DisposManager"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                get_module.name
            ),
            new_instruction_readable="call get_module()"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push_res"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000c).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="store_arg -0x2"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x0000000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x000e0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0xe"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150301).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push_res"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffd000c).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="store_arg -0x3"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffc000c).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="store_arg -0x4"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffd000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x3"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x003d0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x3d"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150301).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push_res"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffc000c).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="store_arg -0x4"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffc000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x4"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00050106).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="retv -0x5"
        ),

    ],
)

ELAPLACEAREA = PatchPattern(
    name="ELAPLACEAREA",
    description="Ice Zone -> Beach Zone Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),
        Instruction(
            identifier=2, offset=0x40,  # position
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=3, offset=0x44,  # area
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x48,  # zone
            pattern=parse_pattern_bytes("00 03 00 10"),
            instruction_readable="push 0x3"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_ICE_ZONE_LAPRAS, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_ICE_ZONE_LAPRAS, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_ICE_ZONE_LAPRAS, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

STAXIAREA = PatchPattern(
    name="STAXIAREA",
    description="Ice Fast Travels",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),
        # meadow
        Instruction(
            identifier=2, offset=0x100,
            pattern=parse_pattern_bytes("00 03 00 10"),  # position
            instruction_readable="push 0x3"
        ),
        Instruction(
            identifier=3, offset=0x104,
            pattern=parse_pattern_bytes("00 01 00 10"),  # area
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x108,
            pattern=parse_pattern_bytes("00 01 00 10"),  # zone
            instruction_readable="push 0x1"
        ),

        # treehouse
        Instruction(
            identifier=5, offset=0x114,
            pattern=parse_pattern_bytes("00 05 00 10"),  # position
            instruction_readable="push 0x5"
        ),
        Instruction(
            identifier=6, offset=0x118,
            pattern=parse_pattern_bytes("00 01 00 10"),  # area
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=7, offset=0x11c,
            pattern=parse_pattern_bytes("00 02 00 10"),  # zone
            instruction_readable="push 0x2"
        ),

        # beach
        Instruction(
            identifier=8, offset=0x128,
            pattern=parse_pattern_bytes("00 02 00 10"),  # position
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=9, offset=0x12c,
            pattern=parse_pattern_bytes("00 01 00 10"),  # area
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=10, offset=0x130,
            pattern=parse_pattern_bytes("00 03 00 10"),  # zone
            instruction_readable="push 0x3"
        ),

        # ice
        Instruction(
            identifier=11, offset=0x13c,
            pattern=parse_pattern_bytes("00 02 00 10"),  # position
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=12, offset=0x140,
            pattern=parse_pattern_bytes("00 02 00 10"),  # area
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=13, offset=0x144,
            pattern=parse_pattern_bytes("00 03 00 10"),  # zone
            instruction_readable="push 0x3"
        ),

        # Cavern
        Instruction(
            identifier=14, offset=0x150,
            pattern=parse_pattern_bytes("00 02 00 10"),  # position
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=15, offset=0x154,
            pattern=parse_pattern_bytes("00 01 00 10"),  # area
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=16, offset=0x158,
            pattern=parse_pattern_bytes("00 04 00 10"),  # zone
            instruction_readable="push 0x4"
        ),

        # Magma
        Instruction(
            identifier=17, offset=0x164,
            pattern=parse_pattern_bytes("00 02 00 10"),  # position
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=18, offset=0x168,
            pattern=parse_pattern_bytes("00 02 00 10"),  # area
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=19, offset=0x16c,
            pattern=parse_pattern_bytes("00 04 00 10"),  # zone
            instruction_readable="push 0x4"
        ),

        # Haunted
        Instruction(
            identifier=20, offset=0x178,
            pattern=parse_pattern_bytes("00 02 00 10"),  # position
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=21, offset=0x17c,
            pattern=parse_pattern_bytes("00 01 00 10"),  # area
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=22, offset=0x180,
            pattern=parse_pattern_bytes("00 05 00 10"),  # zone
            instruction_readable="push 0x5"
        ),

        # Granite
        Instruction(
            identifier=23, offset=0x1a0,
            pattern=parse_pattern_bytes("00 02 00 10"),  # position
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=24, offset=0x1a4,
            pattern=parse_pattern_bytes("00 01 00 10"),  # area
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=25, offset=0x1a8,
            pattern=parse_pattern_bytes("00 06 00 10"),  # zone
            instruction_readable="push 0x6"
        ),

        # Flower
        Instruction(
            identifier=26, offset=0x1b4,
            pattern=parse_pattern_bytes("00 01 00 10"),  # position
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=27, offset=0x1b8,
            pattern=parse_pattern_bytes("00 02 00 10"),  # area
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=28, offset=0x1bc,
            pattern=parse_pattern_bytes("00 06 00 10"),  # zone
            instruction_readable="push 0x6"
        ),
    ],
    patchMapJP=[

        # meadow
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # treehouse
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # beach
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # ice
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update position target based on exit"
        ),

        # cavern
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # magma
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # haunted
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # granite
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # flower
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr03Zn02_Npc_Main_patterns = [
    get_module,
    string_section_start,
    globalManager,
    disposManager,
    f0302TalkTree,
    set_chapter,
    get_friendship,
    lift_top,
    tree_talk_trap_event,
    mamoswine_unlock_event_entry,
    mamoswine_unlock_event_function,
    piloswine_talk_event,
    froslass_interaction,
    piloswine_interaction,
    mudkip_interaction,
    primeape_interaction,
    starly_interaction,
    starly2_interaction,
    krabby_interaction,
    krabby2_interaction,
    krabby3_interaction,
    corphish_interaction,
    corphish2_interaction,
    corphish3_interaction,
    taillow_interaction,
    staravia_interaction,
    wingull_interaction,
    wingull2_interaction,
    wingull3_interaction,
    prinplup_interaction,
    glalie_interaction,
    delibird_interaction,

    special_spawn_conditions,
    special_spawn_conditions2,
    set_attraction_record,
    get_friendship_function,

    ELAPLACEAREA,
    STAXIAREA
]
