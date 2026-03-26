from patcher.helper.entrance_exit_names import SKYGARDEN_PIPLUP_SKYBALLOON
from patcher.helper.patttern_handler import compute_call_instruction_fsb, compute_jmp_instruction_fsb, \
    create_lstr_instruction_fsb, get_exit_zone_area_position_data, \
    parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, get_module, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 37 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr07Zn01_Npc_Main"
        ),

    ],
)

ending_string = PatchPattern(
    name="ending string",
    description="ending string for lstr usage",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("45 6e 64 69 6e 67 00"),
            instruction_readable="Ending"
        ),

    ],
)

sceneManager_string = PatchPattern(
    name="SceneManager string",
    description="SceneManager string for lstr usage",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("53 63 65 6e 65 4d 61 6e 61 67 65 72 00"),
            instruction_readable="SceneManager"
        ),

    ],
)

mew_interaction = PatchPattern(
    name="mew interaction",
    description="modify mew Interaction for Locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 18 00 07"),
            instruction_readable="grow_stack 0x18"
        ),
        Instruction(
            identifier=2, offset=0x60, pattern=parse_pattern_bytes("02 06 00 10"),
            instruction_readable="push 0x206"
        ),

        Instruction(
            identifier=3, offset=0xb8, pattern=parse_pattern_bytes("00 14 02 08"),
            instruction_readable="jz"
        ),

        Instruction(
            identifier=4, offset=0x10c, pattern=parse_pattern_bytes("00 00 00 10"),  # jmp target
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x16c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=6, offset=0x294, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="load_arg -0xe"
        ),
    ],

    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 4, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00040010).to_bytes(
                4,
                'big'
            ) if plando_dict["Options"]["goal"] != 1 else None,
            new_instruction_readable="push 0x4"
            # make postgame location only accessible when postgame goal option is used
        ),
    ]
)
mew_power_competition_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 22 00 07"),
        instruction_readable="grow_stack 0x22"
    ),
    Instruction(
        identifier=2, offset=0xcc, pattern=parse_pattern_bytes("00 00 00 12"),  # first postgame check
        instruction_readable="push_result"
    ),

    Instruction(
        identifier=3, offset=0x1fc8, pattern=parse_pattern_bytes("00 00 00 12"),  # second postgame check
        instruction_readable="push_result"
    ),

    Instruction(
        identifier=4, offset=0x2034, pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=5, offset=0x2084, pattern=parse_pattern_bytes("?? ?? ?? 19"),  # jmp target
        instruction_readable="lea"
    ),

    Instruction(
        identifier=6, offset=0x2118, pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=7, offset=0x2168, pattern=parse_pattern_bytes("00 0a 00 10"),
        instruction_readable="push 0xa"
    ),
    Instruction(
        identifier=8, offset=0x235c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="bl set_chapter"
    ),
]

mew_power_competition = PatchPattern(
    name="mew power competition",
    description="modify mew Power Competition logic to suit ap implementation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 22 00 07"),
            instruction_readable="grow_stack 0x22"
        ),
        Instruction(
            identifier=2, offset=0xcc, pattern=parse_pattern_bytes("00 00 00 12"),  # first postgame check
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=3, offset=0x1f98, pattern=parse_pattern_bytes("00 00 00 12"),  # second postgame check
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=4, offset=0x2004, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x2054, pattern=parse_pattern_bytes("?? ?? ?? 19"),  # jmp target
            instruction_readable="lea"
        ),

        Instruction(
            identifier=6, offset=0x20e8, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=7, offset=0x2138, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        Instruction(
            identifier=8, offset=0x232c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="bl set_chapter"
        ),
    ],
    patternNA=mew_power_competition_patternPALNA,
    patternPAL=mew_power_competition_patternPALNA,

    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 5, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 7, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, custom_ending_start_function.name
            ) if
            plando_dict["Options"]["goal"] == 0 else None,
            new_instruction_readable="call start_ending"
        ),
    ]
)

custom_ending_start_function = PatchPattern(
    name="custom ending starter",
    description="starts the ending scene when Mew is beat",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("01 34 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 00 10"),
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
                sceneManager_string.name
            ),
            new_instruction_readable="lstr SceneManager"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name:
            create_lstr_instruction_fsb(patch_patterns, string_section_start.name, ending_string.name),
            new_instruction_readable="lstr Ending"
        ),
        Patch(
            identifier=8,  # load_arg SceneManager
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: (0x00060010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x6"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: (0x00150401).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC4 0x0:0x15"
        ),
        Patch(
            identifier=11,  # load_arg SceneManager
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: (0x00030010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x3"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: (0x00150201).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC2 0x0:0x15"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: (0x00010006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x1"
        ),

    ]
)

start_ending_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
        instruction_readable="grow_stack 0xe"
    ),
    Instruction(
        identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr mnFieldInfo"
    ),
    Instruction(
        identifier=3, offset=0x148, pattern=parse_pattern_bytes("27 4c 00 10"),
        instruction_readable="push 0x274c"
    ),
]

start_ending = PatchPattern(
    name="start ending",
    description="original function that runs ending scene",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
            instruction_readable="grow_stack 0xe"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr mnFieldInfo"
        ),
        Instruction(
            identifier=3, offset=0x130, pattern=parse_pattern_bytes("27 4c 00 10"),
            instruction_readable="push 0x274c"
        ),
    ],
    patternNA=start_ending_patternPALNA,
    patternPAL=start_ending_patternPALNA
)

spawn_conditions = PatchPattern(
    name="setup_npcs_and_player",
    description="modify spawn conditions for npcs and player",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x22"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr GlobalManager"
        ),

        Instruction(
            identifier=3, offset=0x3bc, pattern=parse_pattern_bytes("02 06 00 10"),
            instruction_readable="push 0x206"
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

piplup_interaction = PatchPattern(
    name="piplup interaction",
    description="allowing leaving skygarden",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 11 00 07"),
            instruction_readable="grow_stack 0x11"
        ),
        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("02 07 00 10"),
            instruction_readable="push 0x207"
        ),

        Instruction(
            identifier=3, offset=0x68, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

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
    ]
)

EBALLOONAREA = PatchPattern(
    name="EBALLOONAREA",
    description="Skygarden -> Treehouse",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),
        Instruction(
            identifier=2, offset=0x8c,
            pattern=parse_pattern_bytes("00 06 00 10"),  # position
            instruction_readable="push 0x6"
        ),
        Instruction(
            identifier=3, offset=0x90,
            pattern=parse_pattern_bytes("00 01 00 10"),  # area
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x94,
            pattern=parse_pattern_bytes("00 02 00 10"),  # zone
            instruction_readable="push 0x2"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                SKYGARDEN_PIPLUP_SKYBALLOON, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                SKYGARDEN_PIPLUP_SKYBALLOON, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                SKYGARDEN_PIPLUP_SKYBALLOON, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr07Zn01_Npc_Main_patterns = [
    get_module,
    string_section_start,
    ending_string,
    sceneManager_string,
    custom_ending_start_function,
    set_chapter,
    get_friendship,
    mew_interaction,
    mew_power_competition,
    spawn_conditions,
    piplup_interaction,
    start_ending
]
