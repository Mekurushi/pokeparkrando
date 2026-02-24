from patcher.helper.entrance_exit_names import HAUNTED_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, \
    HAUNTED_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, HAUNTED_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, \
    HAUNTED_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, \
    HAUNTED_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, \
    HAUNTED_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, HAUNTED_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, \
    HAUNTED_ZONE_MAIN_AREA_TANGROWTH_ATTRACTION, HAUNTED_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL
from patcher.helper.patttern_handler import compute_call_instruction_fsb, create_lstr_instruction_fsb, \
    get_attraction_id_from_dict, get_exit_zone_area_position_data, parse_pattern_bytes, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

set_attraction_record = PatchPattern(
    name="set_attraction_record",
    description="set attraction record for each zone option locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 3e 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 02 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 63 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 0a 00 06"),
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

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 35 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr05Zn01_Npc_Main"
        ),

    ],
)

f0101FuwarideTaxiStop = PatchPattern(
    name="ds f0101FuwarideTaxiStop",
    description="replacing f0101FuwarideTaxiStop with flag for kakuna location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 31 30 31 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
            instruction_readable="ds f0101FuwarideTaxiStop"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x663035303154616c6b4d6f7a79616e626f00).to_bytes(18, 'big'),
            new_instruction_readable="ds f0501TalkMozyanbo"
        ),

    ],
)

trap_gate = PatchPattern(
    name="Trap Event Mansion Gate",
    description="removing Trap Event",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr EventScript"
        ),

        Instruction(
            identifier=3, offset=0xb8, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 3, patch_patterns, pattern_name
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

tangrowth_interaction = PatchPattern(
    name="tangrowth interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0f 00 07"),
            instruction_readable="grow_stack 0xf"
        ),
        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 4e 00 10"),
            instruction_readable="push 0x14e"
        ),

        Instruction(
            identifier=3, offset=0x128, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_prisma_init"
        ),
        Instruction(
            identifier=4, offset=0x27c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0501TalkMozyanbo"
        ),
        Instruction(
            identifier=5, offset=0x2f0, pattern=parse_pattern_bytes("00 0a 00 10"),  # jump target
            instruction_readable="push 0xa"
        ),
        Instruction(
            identifier=6, offset=0x41c, pattern=parse_pattern_bytes("00 03 00 10"),  # attraction id
            instruction_readable="push 0x3"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 5,
                patch_patterns, pattern_name, "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, HAUNTED_ZONE_MAIN_AREA_TANGROWTH_ATTRACTION
            ),
            new_instruction_readable="update attraction id"
        ),
    ]
)

get_tangrowth_friendship_location_state = PatchPattern(
    name="tangrowth friendship location state",
    description="get bestfriend for tangrowth",
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
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff ff 00 0b"),
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
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 02 00 06"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=99, offset=-0x4, pattern=parse_pattern_bytes("00 02 01 06"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020007).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="grow_stack 0x2"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, globalManager.name
            ),
            new_instruction_readable="lstr globalmanager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_module.name
            ),
            new_instruction_readable="call get_module"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00b90010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0xb9"  # tangrowth friendship id
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # best friend opcode
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150301).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x2"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020106).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="retv -0x2"
        ),
    ]
)

return_at04_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
        instruction_readable="grow_stack 0x7"
    ),
    Instruction(
        identifier=2, offset=0x48, pattern=parse_pattern_bytes("01 4e 00 10"),
        instruction_readable="push 0x14e"
    ),

    Instruction(
        identifier=3, offset=0x50, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter"
    ),
    Instruction(
        identifier=4, offset=0xec, pattern=parse_pattern_bytes("17 84 00 10"),
        instruction_readable="push 0x1784"
    ),

]

return_at04 = PatchPattern(
    name="return_at04",
    description="return attraction 04",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),
        Instruction(
            identifier=2, offset=0x40, pattern=parse_pattern_bytes("01 4e 00 10"),
            instruction_readable="push 0x14e"
        ),

        Instruction(
            identifier=3, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0xe4, pattern=parse_pattern_bytes("17 84 00 10"),
            instruction_readable="push 0x1784"
        ),

    ],
    patternPAL=return_at04_patternPALNA,
    patternNA=return_at04_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_tangrowth_friendship_location_state.name
            ),
            new_instruction_readable="call get_tangrowth_friendship_location"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
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
            identifier=2, offset=0xe4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0xe8, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),

        Instruction(
            identifier=4, offset=0xec, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x100, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x10c, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 6, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

raichu_interaction = PatchPattern(
    name="raichu interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 41 00 10"),
            instruction_readable="push 0x141"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x280, pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=4, offset=0x29c, pattern=parse_pattern_bytes("00 a7 00 10"),
            instruction_readable="push 0xa3"
        ),
        Instruction(
            identifier=5, offset=0x2a0, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=6, offset=0x2a4, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=7, offset=0x2a8, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),

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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00120010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x12"
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
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

meowth_quizPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
        instruction_readable="grow_stack 0xc"
    ),

    Instruction(
        identifier=2, offset=0x75c, pattern=parse_pattern_bytes("00 7d 00 10"),
        instruction_readable="push 0x7d"
    ),
    Instruction(
        identifier=3, offset=0x760, pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1"
    ),
    Instruction(
        identifier=4, offset=0x764, pattern=parse_pattern_bytes("00 3d 00 10"),
        instruction_readable="push 0x3d"
    ),
    Instruction(
        identifier=5, offset=0x768, pattern=parse_pattern_bytes("00 15 03 01"),
        instruction_readable="SC3 0x0:0x15"
    ),
    Instruction(
        identifier=6, offset=0x76c, pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),

]

meowth_quiz = PatchPattern(
    name="meowth quiz",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x75c, pattern=parse_pattern_bytes("00 7d 00 10"),
            instruction_readable="push 0x7d"
        ),
        Instruction(
            identifier=3, offset=0x760, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x764, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x768, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x76c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patternPAL=meowth_quizPALNA,
    patternNA=meowth_quizPALNA,
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00130010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x13"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1 | push 0x0"
        ),

    ]
)

aipom_interaction = PatchPattern(
    name="aipom interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 3b 00 10"),
            instruction_readable="push 0x13b"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x280, pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=4, offset=0x29c, pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0xf"
        ),
        Instruction(
            identifier=5, offset=0x2a0, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=6, offset=0x2a4, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=7, offset=0x2a8, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),

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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00140010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x14"
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
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

ambipom_interaction = PatchPattern(
    name="ambipom interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 3c 00 10"),
            instruction_readable="push 0x13c"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=4, offset=0x25c, pattern=parse_pattern_bytes("00 0e 00 10"),
            instruction_readable="push 0xe"
        ),
        Instruction(
            identifier=5, offset=0x260, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=6, offset=0x264, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=7, offset=0x268, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),

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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x15"
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
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

kakuna_interaction = PatchPattern(
    name="kakuna interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 45 00 10"),
            instruction_readable="push 0x145"
        ),
        Instruction(
            identifier=3, offset=0xdc, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x4b"
        ),
    ]
)

metapod_interaction = PatchPattern(
    name="metapod interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 46 00 10"),
            instruction_readable="push 0x146"
        ),
        Instruction(
            identifier=3, offset=0xdc, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x4b"
        ),
    ]
)

STAXIAREA = PatchPattern(
    name="STAXIAREA",
    description="Haunted Fast Travels",
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
                HAUNTED_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # treehouse
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # beach
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # ice
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # cavern
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # magma
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # haunted
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update position target based on exit"
        ),

        # granite
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # flower
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr05Zn01_Npc_Main_patterns = [
    get_module,
    string_section_start,
    globalManager,
    set_chapter,
    get_friendship,
    trap_gate,
    tangrowth_interaction,
    raichu_interaction,
    meowth_quiz,
    aipom_interaction,
    ambipom_interaction,
    kakuna_interaction,
    metapod_interaction,

    return_at04,
    get_tangrowth_friendship_location_state,

    special_spawn_conditions,
    set_attraction_record,

    STAXIAREA
]
