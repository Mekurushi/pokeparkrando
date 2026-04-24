from patcher.helper.entrance_exit_names import MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, \
    MEADOW_ZONE_MAIN_AREA_BULBASAUR_ATTRACTION, \
    MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, \
    MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, \
    MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, \
    MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, \
    MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL
from patcher.helper.patttern_handler import get_attraction_id_from_dict, get_exit_zone_area_position_data, \
    parse_pattern_bytes, \
    compute_call_instruction_fsb, \
    get_num_battle_count_from_dict_as_instruction, create_lstr_instruction_fsb, \
    compute_jmp_instruction_fsb
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import battle_counter_handling, get_friendship, get_module, globalManager, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 31 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr01Zn01_Npc_Main"
        ),

    ],
)

f0301BippaFlag = PatchPattern(
    name="ds f0301BippaFlag",
    description="using f0301BippaFlag string for custom-functions get_module calls",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 33 30 31 42 69 70 70 61 46 6c 61 67 00"),
            instruction_readable="ds f0301BippaFlag"
        ),

    ],
)

f0101TalkOnisuzume = PatchPattern(
    name="ds f0101TalkOnisuzume",
    description="using f0101TalkOnisuzume for lstr instructions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 31 30 31 54 61 6c 6b 4f 6e 69 73 75 7a 75 6d 65 00"),
            instruction_readable="ds f0101TalkOnisuzume"
        ),

    ]
)

overworld_pokemon_spawning_Ar01Zn01 = PatchPattern(
    name="Overworld Pokemon Spawn Logic",
    description="replacing chapter value call in Pokemon Overworld Spawn decision function, with hardcoded 0xf9f that every pokemon spawns befriendable",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 14 00 07"),
            instruction_readable="grow_stack 0x14"
        ),

        # check Magikarp unlock
        Instruction(
            identifier=2, offset=0x84, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=3, offset=0x88, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x8c, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=5, offset=0x90, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x94, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        # finished magikarp spawn logic
        Instruction(
            identifier=7, offset=0x130, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name,
                f0101TalkOnisuzume.name
            ),
            new_instruction_readable="lstr f0101TalkOnisuzume"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150006).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="ret -0x15"
        ),

    ],
)

set_magikarp_location_function = PatchPattern(
    name="set_magikarp_location",
    description="using unused code for set location function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_res"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="store_arg -0x2"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 39 00 10"),
            instruction_readable="push 0x39"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_res"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 14"),
            instruction_readable="---"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010007).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="grow_stack -0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, globalManager.name
            ),
            new_instruction_readable="lstr GlobalManager"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, f0101TalkOnisuzume.name
            ),
            new_instruction_readable="lstr f0101TalkOnisuzume"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150401).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC4 0x0:0x15"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x2"
        ),
    ]
)

set_bestfriend_function_pattern = PatchPattern(
    name="set bestfriend_function",
    description="pattern for finding the best_friend function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr GlobalManager"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_module(GlobalManager)"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="store_arg -0x1"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr DisposManager"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_module(DisposManager)"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="store_arg -0x2"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 0e 00 10"),
            instruction_readable="push 0xe"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="store_arg -0x3"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 4a 00 10"),
            instruction_readable="push 0x4a"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 04 00 06"),
            instruction_readable="ret -0x4"
        ),
    ],
)

turtwig_friendship_pattern = PatchPattern(
    name="Turtwig Friendship Logic",
    description="Winning against Turtwig sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=2, offset=0x04,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=3, offset=0x08,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x0c,
            pattern=parse_pattern_bytes("ff f4 00 0c"),
            instruction_readable="store_arg -0xc"
        ),
        Instruction(
            identifier=5, offset=0x10,
            pattern=parse_pattern_bytes("ff f4 00 0b"),
            instruction_readable="load_arg -0xc"
        ),
        Instruction(
            identifier=6, offset=0x14,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=7, offset=0x18,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=8, offset=0x1c,
            pattern=parse_pattern_bytes("00 0e 02 08"),
            instruction_readable="jz identifier 23"
        ),
        Instruction(
            identifier=9, offset=0x20,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10090"
        ),
        Instruction(
            identifier=10, offset=0x24,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=11, offset=0x28,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=12, offset=0x2c,
            pattern=parse_pattern_bytes("00 08 00 10"),
            instruction_readable="push 0x8"
        ),
        Instruction(
            identifier=13, offset=0x30,
            pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=14, offset=0x34,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=15, offset=0x38,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=16, offset=0x3c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00390"
        ),
        Instruction(
            identifier=17, offset=0x40,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=18, offset=0x44,
            pattern=parse_pattern_bytes("00 07 00 10"),
            instruction_readable="push 0x7"
        ),
        Instruction(
            identifier=19, offset=0x48,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x7)"
        ),
        Instruction(
            identifier=20, offset=0x4c,
            pattern=parse_pattern_bytes("00 12 00 10"),
            instruction_readable="push 0x12"
        ),
        Instruction(
            identifier=21, offset=0x50,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x12)"
        ),
        Instruction(
            identifier=22, offset=0x54,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=23, offset=0x58,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10080"
        ),
        Instruction(
            identifier=24, offset=0x5c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=25, offset=0x60,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=26, offset=0x64,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=27, offset=0x68,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x5)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x000e0008).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp identifier 23"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

turtwig_dialog_options_pattern = PatchPattern(
    name="Turtwig dialog options logic",
    description="Winning against Turtwig sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=2, offset=0x04,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=3, offset=0x08,
            pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="neq"
        ),
        Instruction(
            identifier=4, offset=0x0c,
            pattern=parse_pattern_bytes("00 62 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=5, offset=0x10,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10040"
        ),
        Instruction(
            identifier=6, offset=0x14,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=7, offset=0x18,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=8, offset=0x1c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=9, offset=0x20,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=10, offset=0x24,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=11, offset=0x28,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=12, offset=0x2c,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=13, offset=0x30,
            pattern=parse_pattern_bytes("00 56 02 08"),
            instruction_readable="jz"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

buneary_friendship_pattern = PatchPattern(
    name="Buneary Friendship Logic",
    description="Winning against Buneary sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=2, offset=0x04,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=3, offset=0x08,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x0c,
            pattern=parse_pattern_bytes("ff f5 00 0c"),
            instruction_readable="store_arg -0xb"
        ),
        Instruction(
            identifier=5, offset=0x10,
            pattern=parse_pattern_bytes("ff f5 00 0b"),
            instruction_readable="load_arg -0xb"
        ),
        Instruction(
            identifier=6, offset=0x14,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=7, offset=0x18,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=8, offset=0x1c,
            pattern=parse_pattern_bytes("00 18 02 08"),
            instruction_readable="jz identifier 33"
        ),
        Instruction(
            identifier=9, offset=0x20,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10190"
        ),
        Instruction(
            identifier=10, offset=0x24,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=11, offset=0x28,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=12, offset=0x2c,
            pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=13, offset=0x30,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x34,
            pattern=parse_pattern_bytes("00 09 00 10"),
            instruction_readable="push 0x9"
        ),
        Instruction(
            identifier=15, offset=0x38,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=16, offset=0x3c,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=17, offset=0x40,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=18, offset=0x44,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00400"
        ),
        Instruction(
            identifier=19, offset=0x48,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x4c,
            pattern=parse_pattern_bytes("00 0c 00 10"),
            instruction_readable="push 0xc"
        ),
        Instruction(
            identifier=21, offset=0x50,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0xc)"
        ),
        Instruction(
            identifier=22, offset=0x54,
            pattern=parse_pattern_bytes("00 2b 00 10"),
            instruction_readable="push 0x2b"
        ),
        Instruction(
            identifier=23, offset=0x58,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x2b)"
        ),
        Instruction(
            identifier=24, offset=0x5c,
            pattern=parse_pattern_bytes("00 2c 00 10"),
            instruction_readable="push 0x2c"
        ),
        Instruction(
            identifier=25, offset=0x60,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x2c)"
        ),
        Instruction(
            identifier=26, offset=0x64,
            pattern=parse_pattern_bytes("00 13 00 10"),
            instruction_readable="push 0x13"
        ),
        Instruction(
            identifier=27, offset=0x68,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x13)"
        ),
        Instruction(
            identifier=28, offset=0x6c,
            pattern=parse_pattern_bytes("00 2f 00 10"),
            instruction_readable="push 0x2f"
        ),
        Instruction(
            identifier=29, offset=0x70,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="unlock_pokemon(0x2f)"
        ),
        Instruction(
            identifier=30, offset=0x74,
            pattern=parse_pattern_bytes("00 30 00 10"),
            instruction_readable="push 0x30"
        ),
        Instruction(
            identifier=31, offset=0x78,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="unlock_pokemon(0x30)"
        ),
        Instruction(
            identifier=32, offset=0x7c,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=33, offset=0x80,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10180"
        ),
        Instruction(
            identifier=34, offset=0x84,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=35, offset=0x88,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=36, offset=0x8c,
            pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=37, offset=0x90,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=38, offset=0x94,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=39, offset=0x98,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x6)"
        ),
    ], patchMapJP=
    [
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00180008).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp identifier 33"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

buneary_dialog_options_pattern = PatchPattern(
    name="Buneary dialog options logic",
    description="always allowing power comp dialog, so it is always befriendable",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=2, offset=0x04,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=3, offset=0x08,
            pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="neq"
        ),
        Instruction(
            identifier=4, offset=0x0c,
            pattern=parse_pattern_bytes("00 71 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=5, offset=0x10,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10040"
        ),
        Instruction(
            identifier=6, offset=0x14,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=7, offset=0x18,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=8, offset=0x1c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=9, offset=0x20,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=10, offset=0x24,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=11, offset=0x28,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=12, offset=0x2c,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=13, offset=0x30,
            pattern=parse_pattern_bytes("00 65 02 08"),
            instruction_readable="jz"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

pachirisu1_friendship_pattern = PatchPattern(
    name="Pachirisu 1 Friendship Logic",
    description="Winning against Pachirisu sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0x00,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=2, offset=0x04,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=3, offset=0x08,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x0c,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=5, offset=0x10,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=6, offset=0x14,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=7, offset=0x18,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=8, offset=0x1c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz identifier 19"
        ),
        Instruction(
            identifier=9, offset=0x20,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10290"
        ),
        Instruction(
            identifier=10, offset=0x24,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=11, offset=0x28,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=12, offset=0x2c,
            pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),
        Instruction(
            identifier=13, offset=0x30,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=14, offset=0x34,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=15, offset=0x38,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=16, offset=0x3c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00410"
        ),
        Instruction(
            identifier=17, offset=0x40,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=18, offset=0x44,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=19, offset=0x48,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10280"
        ),
        Instruction(
            identifier=20, offset=0x4c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=21, offset=0x50,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x54,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=23, offset=0x58,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x7)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x000a0008).to_bytes(
                4,  # always jump to set best friend flag
                'big'
            ),
            new_instruction_readable="jmp identifier 19"
        ),
        Patch(
            identifier=15,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

pachirisu2_friendship_pattern = PatchPattern(
    name="Pachirisu 2 Friendship Logic",
    description="Winning against Pachirisu sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 34 00 10"),
            instruction_readable="push 0x34"
        ),

        Instruction(
            identifier=2, offset=0x228,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x22c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x230,
            pattern=parse_pattern_bytes("ff f9 00 0c"),
            instruction_readable="store_arg -0x7"
        ),
        Instruction(
            identifier=5, offset=0x234,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=6, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=7, offset=0x23c,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=8, offset=0x240,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x244,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=10, offset=0x248,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=11, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_14680"
        ),
        Instruction(
            identifier=12, offset=0x250,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=13, offset=0x254,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x258,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=15, offset=0x25c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x34)"
        ),
        Instruction(
            identifier=16, offset=0x260,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp identifier 23"
        ),
        Instruction(
            identifier=17, offset=0x264,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_14690"
        ),
        Instruction(
            identifier=18, offset=0x268,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=19, offset=0x26c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x270,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00410"
        ),
        Instruction(
            identifier=21, offset=0x274,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x278,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=23, offset=0x27c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x34)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # only enter set_bestfriend path
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

munchlax_friendship_pattern = PatchPattern(
    name="Munchlax Friendship Logic",
    description="Clearin Munchlax Errand calls the modified set_friend function that only sets best_friend flag also clearing unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 08 00 10"),
            instruction_readable="push 0x08"
        ),

        Instruction(
            identifier=2, offset=0x124,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x128,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x12c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x130,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=6, offset=0x134,
            pattern=parse_pattern_bytes("00 05 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=7, offset=0x138,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10360"
        ),
        Instruction(
            identifier=8, offset=0x13c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=9, offset=0x140,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=10, offset=0x144,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=11, offset=0x148,
            pattern=parse_pattern_bytes("00 0d 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=12, offset=0x14c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10360"
        ),
        Instruction(
            identifier=13, offset=0x150,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x154,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x158,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=16, offset=0x15c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10370"
        ),
        Instruction(
            identifier=17, offset=0x160,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=18, offset=0x164,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=19, offset=0x168,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00420"
        ),
        Instruction(
            identifier=20, offset=0x16c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x170,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=22, offset=0x174,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend"
        ),
        Instruction(
            identifier=23, offset=0x178,
            pattern=parse_pattern_bytes("00 1a 00 10"),
            instruction_readable="push 0x1a"
        ),
        Instruction(
            identifier=24, offset=0x17c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x1a)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00050008).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=22,  # removing the pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,  # removing the pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

munchlax2_friendship_pattern = PatchPattern(
    name="Munchlax 2 Friendship Logic",
    description="Clearin Munchlax Errand calls the modified set_friend function that only sets best_friend flag also clearing unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 32 00 10"),
            instruction_readable="push 0x32"
        ),

        Instruction(
            identifier=2, offset=0x124,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x128,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x12c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x130,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=6, offset=0x134,
            pattern=parse_pattern_bytes("00 05 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=7, offset=0x138,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10360"
        ),
        Instruction(
            identifier=8, offset=0x13c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=9, offset=0x140,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=10, offset=0x144,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=11, offset=0x148,
            pattern=parse_pattern_bytes("00 0d 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=12, offset=0x14c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10360"
        ),
        Instruction(
            identifier=13, offset=0x150,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x154,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x158,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=16, offset=0x15c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10370"
        ),
        Instruction(
            identifier=17, offset=0x160,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=18, offset=0x164,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=19, offset=0x168,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00420"
        ),
        Instruction(
            identifier=20, offset=0x16c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x170,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=22, offset=0x174,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend"
        ),
        Instruction(
            identifier=23, offset=0x178,
            pattern=parse_pattern_bytes("00 1a 00 10"),
            instruction_readable="push 0x1a"
        ),
        Instruction(
            identifier=24, offset=0x17c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x1a)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00050008).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=22,  # removing the pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,  # removing the pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

treecko_friendship_pattern = PatchPattern(
    name="Treecko Friendship Logic",
    description="Winning against Treecko sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 09 00 10"),
            instruction_readable="push 0x9"
        ),

        Instruction(
            identifier=2, offset=0x270,
            pattern=parse_pattern_bytes("00 38 00 10"),
            instruction_readable="push 0x38"
        ),
        Instruction(
            identifier=3, offset=0x274,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=4, offset=0x278,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x27c,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x280,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x284,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=8, offset=0x288,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=9, offset=0x28c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x290,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x294,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x298,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10490"
        ),
        Instruction(
            identifier=13, offset=0x29c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x2a0,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x2a4,
            pattern=parse_pattern_bytes("00 38 00 10"),
            instruction_readable="push 0x38"
        ),
        Instruction(
            identifier=16, offset=0x2a8,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=17, offset=0x2ac,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x2b0,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x2b4,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00420"
        ),
        Instruction(
            identifier=20, offset=0x2b8,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x2bc,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x2c0,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00480"
        ),
        Instruction(
            identifier=23, offset=0x2c4,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x2c8,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x2cc,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x2d0,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x9)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x9)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

chimchar_friendship_pattern = PatchPattern(
    name="Chimchar Friendship Logic",
    description="Winning against Chimchar sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 07 00 10"),
            instruction_readable="push 0x07"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10590"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 07 00 10"),
            instruction_readable="push 0x7"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00440"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00580"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x9)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xa)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

magikarp_friendship_pattern = PatchPattern(
    name="Magikarp Friendship Logic",
    description="Winning against Magikarp sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 0b 00 10"),
            instruction_readable="push 0xb"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 2b 00 10"),
            instruction_readable="push 0x2b"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10690"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 2b 00 10"),
            instruction_readable="push 0x2b"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00450"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00680"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0xb)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xb)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

lotad1_friendship_pattern = PatchPattern(
    name="Lotad 1 Friendship Logic",
    description="Winning against Lotad sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 0c 00 10"),
            instruction_readable="push 0xc"
        ),

        Instruction(
            identifier=2, offset=0x260,
            pattern=parse_pattern_bytes("00 19 00 10"),
            instruction_readable="push 0x19"
        ),
        Instruction(
            identifier=3, offset=0x264,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=4, offset=0x268,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x26c,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x270,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x274,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=8, offset=0x278,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=9, offset=0x27c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x280,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x284,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x288,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10790"
        ),
        Instruction(
            identifier=13, offset=0x28c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x290,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x294,
            pattern=parse_pattern_bytes("00 19 00 10"),
            instruction_readable="push 0x19"
        ),
        Instruction(
            identifier=16, offset=0x298,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=17, offset=0x29c,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x2a0,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x2a4,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00460"
        ),
        Instruction(
            identifier=20, offset=0x2a8,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x2ac,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x2b0,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00780"
        ),
        Instruction(
            identifier=23, offset=0x2b4,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x2b8,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x2bc,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x2c0,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0xc)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xc)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

caterpie_friendship_pattern = PatchPattern(
    name="Caterpie Friendship Logic",
    description="Winning against Caterpie sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 0d 00 10"),
            instruction_readable="push 0xd"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 27 00 10"),
            instruction_readable="push 0x27"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 19 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10890"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 27 00 10"),
            instruction_readable="push 0x27"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00470"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 19 00 10"),
            instruction_readable="push 0x19"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x19)"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 31 00 10"),
            instruction_readable="push 0x31"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x31)"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("00 19 00 10"),
            instruction_readable="push 0x19"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????(0x19)"
        ),
        Instruction(
            identifier=27, offset=0x26c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=28, offset=0x270,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=29, offset=0x274,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=30, offset=0x278,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=31, offset=0x27c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=32, offset=0x280,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=33, offset=0x284,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=34, offset=0x288,
            pattern=parse_pattern_bytes("00 01 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=35, offset=0x28c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=36, offset=0x290,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=37, offset=0x294,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10880"
        ),
        Instruction(
            identifier=38, offset=0x298,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=39, offset=0x29c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=40, offset=0x2a0,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=41, offset=0x2a4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0xd)"
        ),
        Instruction(
            identifier=42, offset=0x2a8,
            pattern=parse_pattern_bytes("00 03 00 08"),
            instruction_readable="jmp"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xc)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=22,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=40,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=41,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

weedle_friendship_pattern = PatchPattern(
    name="Weedle Friendship Logic",
    description="Winning against Weedle sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 0e 00 10"),
            instruction_readable="push 0xe"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 28 00 10"),
            instruction_readable="push 0x28"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_10990"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 28 00 10"),
            instruction_readable="push 0x28"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00480"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00980"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0xe)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xe)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

event_bidoof_friendship_pattern = PatchPattern(
    name="Event Bidoof Friendship Logic",
    description="Event Bidoof sets",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 18 00 07"),
            instruction_readable="grow_stack 0x18"
        ),

        # Chapter 802 dialog
        #
        Instruction(
            identifier=2, offset=0x68,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter()"
        ),
        Instruction(
            identifier=3, offset=0x6c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x70,
            pattern=parse_pattern_bytes("08 02 00 10"),
            instruction_readable="push 0x802"
        ),
        Instruction(
            identifier=5, offset=0x74,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=6, offset=0x78,
            pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=7, offset=0x7c,
            pattern=parse_pattern_bytes("00 04 00 10"),
            instruction_readable="push 0x4"
        ),
        Instruction(
            identifier=8, offset=0x80,
            pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0xf"
        ),
        Instruction(
            identifier=9, offset=0x84,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),

        # Chapter 802 dialog
        #

        Instruction(
            identifier=10, offset=0x2c4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter()"
        ),
        Instruction(
            identifier=11, offset=0x2c8,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=12, offset=0x2cc,
            pattern=parse_pattern_bytes("08 02 00 10"),
            instruction_readable="push 0x802"
        ),
        Instruction(
            identifier=13, offset=0x2d0,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=14, offset=0x2d4,
            pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=15, offset=0x2d8,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=16, offset=0x2dc,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),

        # removin Pokemon Unlocks
        #

        Instruction(
            identifier=17, offset=0x4fc,
            pattern=parse_pattern_bytes("00 23 00 10"),
            instruction_readable="push 0x23"
        ),
        Instruction(
            identifier=18, offset=0x500,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x23)"
        ),
        Instruction(
            identifier=19, offset=0x504,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=20, offset=0x508,
            pattern=parse_pattern_bytes("00 24 00 10"),
            instruction_readable="push 0x24"
        ),
        Instruction(
            identifier=21, offset=0x50c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x24)"
        ),
        Instruction(
            identifier=22, offset=0x510,
            pattern=parse_pattern_bytes("00 02 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=23, offset=0x514,
            pattern=parse_pattern_bytes("00 25 00 10"),
            instruction_readable="push 0x25"
        ),
        Instruction(
            identifier=24, offset=0x518,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x25)"
        ),
        Instruction(
            identifier=25, offset=0x610,
            pattern=parse_pattern_bytes("00 1b 00 10"),
            instruction_readable="push 0x1b"
        ),
        Instruction(
            identifier=26, offset=0x614,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x1b)"
        ),

        Instruction(
            identifier=27, offset=0x654,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0c3d"
        ),
        Instruction(
            identifier=28, offset=0x658,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=29, offset=0x65c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=30, offset=0x660,
            pattern=parse_pattern_bytes("ff e8 00 0c"),
            instruction_readable="store_arg -0x18"
        ),
        Instruction(
            identifier=31, offset=0x664,
            pattern=parse_pattern_bytes("ff e8 00 0b"),
            instruction_readable="load_arg -0x18"
        ),
        Instruction(
            identifier=32, offset=0x668,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=33, offset=0x66c,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=34, offset=0x670,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=35, offset=0x674,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=36, offset=0x678,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship(uVar4)"
        ),
        Instruction(
            identifier=37, offset=0x67c,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 11_00490"
        ),
        Instruction(
            identifier=38, offset=0x680,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),

        Instruction(  # replacing with separeate friendship function
            identifier=99, offset=0xbc,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_friendship"
        ),
    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=12,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=13,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=14,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=15,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=16,  # removing world state content
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        Patch(
            identifier=17,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=20,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        Patch(
            identifier=23,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # always entering path
        #
        Patch(
            identifier=27,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=28,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=29,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=30,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=31,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=32,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=33,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=34,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=36,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xe)"
        ),

        # replacing getfriendship function
        Patch(
            identifier=99,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                get_mankey_friendship_function.name
            ),
            new_instruction_readable="call getMankeyFriendship"
        ),
    ]
)

bidoof1 = PatchPattern(
    name="meadow_bidoof1",
    description="remove beach zone bidoof unlock",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),
        Instruction(
            identifier=2, offset=0x10,
            pattern=parse_pattern_bytes("00 23 00 10"),
            instruction_readable="push 0x23"
        ),
        # condition
        Instruction(
            identifier=3, offset=0x54,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=4, offset=0x58,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=5, offset=0x5c,
            pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="neq"
        ),
    ],
    patchMapJP=[
        # making it always unequal so it skips the beach zone bidoof location trigger
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
    ]
)

bidoof2 = PatchPattern(
    name="meadow_bidoof2",
    description="remove beach zone bidoof unlock",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),
        Instruction(
            identifier=2, offset=0x10,
            pattern=parse_pattern_bytes("00 24 00 10"),
            instruction_readable="push 0x24"
        ),
        # condition
        Instruction(
            identifier=3, offset=0x54,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=4, offset=0x58,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=5, offset=0x5c,
            pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="neq"
        ),
    ],
    patchMapJP=[
        # making it always unequal so it skips the beach zone bidoof location trigger
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
    ]
)

bidoof3 = PatchPattern(
    name="meadow_bidoof3",
    description="remove beach zone bidoof unlock",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),
        Instruction(
            identifier=2, offset=0x10,
            pattern=parse_pattern_bytes("00 25 00 10"),
            instruction_readable="push 0x25"
        ),
        # condition
        Instruction(
            identifier=3, offset=0x54,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=4, offset=0x58,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=5, offset=0x5c,
            pattern=parse_pattern_bytes("00 0c 00 16"),
            instruction_readable="neq"
        ),
    ],
    patchMapJP=[
        # making it always unequal so it skips the beach zone bidoof location trigger
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
    ]
)

oddish_friendship_pattern = PatchPattern(
    name="Oddish Friendship Logic",
    description="Winning against Oddish sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 10 00 10"),
            instruction_readable="push 0x10"
        ),

        # remove hide and seek tutorial popup
        #
        Instruction(
            identifier=2, offset=0x118,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0101HideAndSeek"
        ),
        Instruction(
            identifier=3, offset=0x11c,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x120,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x01"
        ),
        Instruction(
            identifier=5, offset=0x124,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x128,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x12c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x130,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=9, offset=0x134,
            pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=10, offset=0x138,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 02_60100"
        ),
        Instruction(
            identifier=11, offset=0x13c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=12, offset=0x140,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),

        # setting hide and seek popup flag
        #
        Instruction(
            identifier=13, offset=0x1F8,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0101HideAndSeek"
        ),
        Instruction(
            identifier=14, offset=0x1fc,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=15, offset=0x200,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=16, offset=0x204,
            pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # replacing friendship flag with best friend
        #
        Instruction(
            identifier=17, offset=0x218,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=18, offset=0x21c,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x220,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=20, offset=0x224,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=21, offset=0x228,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=22, offset=0x22c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=23, offset=0x230,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=24, offset=0x234,
            pattern=parse_pattern_bytes("00 08 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=25, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 11_11090"
        ),
        Instruction(
            identifier=26, offset=0x23c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=27, offset=0x240,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=28, offset=0x244,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=29, offset=0x248,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x10)"
        ),
        Instruction(
            identifier=30, offset=0x24c,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 11_00500"
        ),
        Instruction(
            identifier=31, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=12,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=13,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=14,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=15,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=16,  # removing tutorial popup
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # replacing friendship flag with best friend
        #
        Patch(
            identifier=17,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=19,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=20,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=22,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        Patch(
            identifier=29,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x10)"
        ),
    ]
)

shroomish_friendship_pattern = PatchPattern(
    name="Shroomish Friendship Logic",
    description="Winning against Shroomish sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 11 00 10"),
            instruction_readable="push 0x11"
        ),

        Instruction(
            identifier=2, offset=0x1f8,
            pattern=parse_pattern_bytes("00 26 00 10"),
            instruction_readable="push 0x28"
        ),
        Instruction(
            identifier=3, offset=0x1fc,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x200,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x204,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x208,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x20c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x210,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x214,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x218,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x21c,
            pattern=parse_pattern_bytes("00 08 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x220,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11990"
        ),
        Instruction(
            identifier=13, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x228,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x22c,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=16, offset=0x230,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x11)"
        ),
        Instruction(
            identifier=17, offset=0x234,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00510"
        ),
        Instruction(
            identifier=18, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=19, offset=0x23c,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=20, offset=0x240,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 11_11180"
        ),
        Instruction(
            identifier=21, offset=0x244,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=22, offset=0x248,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="cal FUN_??????"
        ),
        Instruction(
            identifier=23, offset=0x24c,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=24, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x11)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x11)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=23,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

bonsly_friendship_pattern = PatchPattern(
    name="Bonsly Friendship Logic",
    description="Winning against Bonsly sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 0c 00 07"),
            instruction_readable="grow_stack 0xc"
        ),
        # model id
        Instruction(
            identifier=2, offset=0x20,
            pattern=parse_pattern_bytes("00 12 00 10"),
            instruction_readable="push 0x12"
        ),
        # hide and seek flag result
        Instruction(
            identifier=3, offset=0x174,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        # set hide and seek flag
        Instruction(
            identifier=4, offset=0x1c4,
            pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
        # set hide and seek flag
        Instruction(
            identifier=5, offset=0x274,
            pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
        # get friendship opcode
        Instruction(
            identifier=6, offset=0x288,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=3,  # skip hide and seek logic
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=4,  # skip hide and seek logic
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay 0x0"
        ),
        Patch(
            identifier=5,  # skip hide and seek logic
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay 0x0"
        ),
        Patch(  # replacing is friend check with location flag check
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"
        ),
        # set friendship is automatically transformed to archipelago flag
    ]
)

shinx_friendship_pattern = PatchPattern(
    name="Shinx Friendship Logic",
    description="Winning against Shinx sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 13 00 10"),
            instruction_readable="push 0xa"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 ae 00 10"),
            instruction_readable="push 0xae"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11390"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 ae 00 10"),
            instruction_readable="push 0xae"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00530"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11380"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x13)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xa)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

aipom_tree_friendship_pattern = PatchPattern(
    name="Aipom Tree Friendship Logic",
    description="Winning against Aipom sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 15 00 10"),
            instruction_readable="push 0x15"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0x0f"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 17 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11590"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0xf"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00550"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 1c 00 10"),
            instruction_readable="push 0x1c"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x1c)"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 1c 00 10"),
            instruction_readable="push 0x1c"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????(0x1c)"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=27, offset=0x26c,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=28, offset=0x270,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=29, offset=0x274,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=30, offset=0x278,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=31, offset=0x27c,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=32, offset=0x280,
            pattern=parse_pattern_bytes("00 01 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=33, offset=0x284,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=34, offset=0x288,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=35, offset=0x28c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11580"
        ),
        Instruction(
            identifier=36, offset=0x290,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=37, offset=0x294,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=38, offset=0x298,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=39, offset=0x29c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x15)"
        ),
        Instruction(
            identifier=40, offset=0x2a0,
            pattern=parse_pattern_bytes("00 03 00 08"),
            instruction_readable="jmp"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xc)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=22,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=38,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=39,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

spearow_overworld_friendship_pattern = PatchPattern(
    name="Spearow Overworld Friendship Logic",
    description="Winning against Spearow sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 16 00 10"),
            instruction_readable="push 0x16"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 8f 00 10"),
            instruction_readable="push 0x8f"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11690"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 8f 00 10"),
            instruction_readable="push 0x8f"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00560"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11380"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x13)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xa)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

torterra_friendship_pattern = PatchPattern(
    name="Torterra Overworld Friendship Logic",
    description="Winning against Torterra sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 17 00 10"),
            instruction_readable="push 0x17"
        ),

        Instruction(
            identifier=2, offset=0x244,
            pattern=parse_pattern_bytes("00 2d 00 10"),
            instruction_readable="push 0x2d"
        ),
        Instruction(
            identifier=3, offset=0x248,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=4, offset=0x24c,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x250,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x254,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x258,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=8, offset=0x25c,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=9, offset=0x260,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x264,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x268,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x26c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11790"
        ),
        Instruction(
            identifier=13, offset=0x270,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x274,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x278,
            pattern=parse_pattern_bytes("00 2d 00 10"),
            instruction_readable="push 0x2d"
        ),
        Instruction(
            identifier=16, offset=0x27c,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=17, offset=0x280,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x284,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x288,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00570"
        ),
        Instruction(
            identifier=20, offset=0x28c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x290,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x294,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11780"
        ),
        Instruction(
            identifier=23, offset=0x298,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x29c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x2a0,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x2a4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x17)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xa)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

starly_friendship_pattern = PatchPattern(
    name="Starly Overworld Friendship Logic",
    description="Winning against Starly sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 18 00 10"),
            instruction_readable="push 0x18"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11890"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00580"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11880"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x18)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xa)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

butterfree_friendship_pattern = PatchPattern(
    name="Butterfree Overworld Friendship Logic",
    description="Winning against Butterfree sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 19 00 10"),
            instruction_readable="push 0x19"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 8e 00 10"),
            instruction_readable="push 0x8e"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11990"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 8e 00 10"),
            instruction_readable="push 0x8e"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00590"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_11980"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x19)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xa)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

tropius_friendship_pattern = PatchPattern(
    name="Tropius Friendship Logic",
    description="Clearin Tropius Errand calls the modified set_friend function that only sets best_friend flag also clearing unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 1a 00 10"),
            instruction_readable="push 0x1a"
        ),

        Instruction(
            identifier=2, offset=0xb4,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=3, offset=0xb8,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=4, offset=0xbc,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=5, offset=0xc0,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=6, offset=0xc4,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=7, offset=0xc8,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz identifier 12"
        ),
        Instruction(
            identifier=8, offset=0xcc,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12060"
        ),
        Instruction(
            identifier=9, offset=0xd0,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=10, offset=0xd4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=11, offset=0xd8,
            pattern=parse_pattern_bytes("00 0b 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=12, offset=0xdc,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12070"
        ),
        Instruction(
            identifier=13, offset=0xe0,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0xe4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0xe8,
            pattern=parse_pattern_bytes("00 4c 00 10"),
            instruction_readable="push 0x4c"
        ),
        Instruction(
            identifier=16, offset=0xec,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=17, offset=0xf0,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=18, offset=0xf4,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0xf8,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00600"
        ),
        Instruction(
            identifier=20, offset=0xfc,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x100,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=22, offset=0x104,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,  # removing is friend calls
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # removing is friend calls
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # removing is friend calls
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # removing is friend calls
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # removing is friend calls
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        #
        # always enter path after winning
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00040008).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=22,  # set bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

bibarel_friendship_pattern = PatchPattern(
    name="Bibarel Friendship Logic",
    description="Winning against Bibarel sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 1b 00 10"),
            instruction_readable="push 0x1b"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 2f 00 10"),
            instruction_readable="push 0x2f"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12190"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 2f 00 10"),
            instruction_readable="push 0x2f"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00610"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12180"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x1b)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x1b)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

ambipom_friendship_pattern = PatchPattern(
    name="Ambipom Friendship Logic",
    description="Winning against Ambipom sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 1c 00 10"),
            instruction_readable="push 0x1c"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 0e 00 10"),
            instruction_readable="push 0xe"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12290"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 0e 00 10"),
            instruction_readable="push 0xe"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00620"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12280"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x1c)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x1b)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

sudowoodo_interaction_patternJP = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 1d 00 10"),
        instruction_readable="push 0x1d"
    ),

    # remove hide and seek tutorial popup
    #
    Instruction(
        identifier=2, offset=0x118,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr f0101HideAndSeek"
    ),
    Instruction(
        identifier=3, offset=0x11c,
        pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1"
    ),
    Instruction(
        identifier=4, offset=0x120,
        pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x01"
    ),
    Instruction(
        identifier=5, offset=0x124,
        pattern=parse_pattern_bytes("00 15 03 01"),
        instruction_readable="SC3 0x0:0x15"
    ),
    Instruction(
        identifier=6, offset=0x128,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=7, offset=0x12c,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=8, offset=0x130,
        pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=9, offset=0x134,
        pattern=parse_pattern_bytes("00 03 02 08"),
        instruction_readable="jz"
    ),
    Instruction(
        identifier=10, offset=0x138,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 02_60100"
    ),
    Instruction(
        identifier=11, offset=0x13c,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=12, offset=0x140,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),

    # setting hide and seek popup flag
    #
    Instruction(
        identifier=13, offset=0x1F8,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr f0101HideAndSeek"
    ),
    Instruction(
        identifier=14, offset=0x1fc,
        pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1"
    ),
    Instruction(
        identifier=15, offset=0x200,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=16, offset=0x204,
        pattern=parse_pattern_bytes("00 15 04 01"),
        instruction_readable="SC4 0x0:0x15"
    ),

    # replacing friendship flag with best friend
    #
    Instruction(
        identifier=17, offset=0x210,
        pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=18, offset=0x214,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=19, offset=0x218,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=20, offset=0x21c,
        pattern=parse_pattern_bytes("ff f8 00 0c"),
        instruction_readable="store_arg -0x8"
    ),
    Instruction(
        identifier=21, offset=0x220,
        pattern=parse_pattern_bytes("ff f8 00 0b"),
        instruction_readable="load_arg -0x8"
    ),
    Instruction(
        identifier=22, offset=0x224,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=23, offset=0x228,
        pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=24, offset=0x22c,
        pattern=parse_pattern_bytes("00 ?? 02 08"),  # jump is unknown becuase of the version difference
        instruction_readable="jz"
    ),
    Instruction(
        identifier=25, offset=0x230,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 11_12390"
    ),
    Instruction(
        identifier=26, offset=0x234,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=27, offset=0x238,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=28, offset=0x23c,
        pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=29, offset=0x240,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_friend(0x1d)"
    ),
    Instruction(
        identifier=30, offset=0x244,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 11_00630"
    ),
    Instruction(
        identifier=31, offset=0x248,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=32, offset=0x24c,
        pattern=parse_pattern_bytes("00 ?? 00 08"),  # jump is unknown becuase of the version difference
        instruction_readable="jmp"
    ),
    Instruction(
        identifier=33, offset=0x250,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 11_12380"
    ),
    Instruction(
        identifier=34, offset=0x254,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=35, offset=0x258,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=36, offset=0x25c,
        pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=37, offset=0x260,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_bestfriend(0x1d)"
    ),
]

sudowoodo_interaction_patternPAL = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 1d 00 10"),
        instruction_readable="push 0x1d"
    ),

    # remove hide and seek tutorial popup
    #
    Instruction(
        identifier=2, offset=0x118,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr f0101HideAndSeek"
    ),
    Instruction(
        identifier=3, offset=0x11c,
        pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1"
    ),
    Instruction(
        identifier=4, offset=0x120,
        pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x01"
    ),
    Instruction(
        identifier=5, offset=0x124,
        pattern=parse_pattern_bytes("00 15 03 01"),
        instruction_readable="SC3 0x0:0x15"
    ),
    Instruction(
        identifier=6, offset=0x128,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=7, offset=0x12c,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=8, offset=0x130,
        pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=9, offset=0x134,
        pattern=parse_pattern_bytes("00 03 02 08"),
        instruction_readable="jz"
    ),
    Instruction(
        identifier=10, offset=0x138,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 02_60100"
    ),
    Instruction(
        identifier=11, offset=0x13c,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=12, offset=0x140,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),

    # setting hide and seek popup flag
    #
    Instruction(
        identifier=13, offset=0x1F8,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr f0101HideAndSeek"
    ),
    Instruction(
        identifier=14, offset=0x1fc,
        pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1"
    ),
    Instruction(
        identifier=15, offset=0x200,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=16, offset=0x204,
        pattern=parse_pattern_bytes("00 15 04 01"),
        instruction_readable="SC4 0x0:0x15"
    ),

    # replacing friendship flag with best friend
    #
    Instruction(
        identifier=17, offset=0x210,
        pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=18, offset=0x214,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=19, offset=0x218,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=20, offset=0x21c,
        pattern=parse_pattern_bytes("ff f8 00 0c"),
        instruction_readable="store_arg -0x8"
    ),
    Instruction(
        identifier=21, offset=0x220,
        pattern=parse_pattern_bytes("ff f8 00 0b"),
        instruction_readable="load_arg -0x8"
    ),
    Instruction(
        identifier=22, offset=0x224,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=23, offset=0x228,
        pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=24, offset=0x22c,
        pattern=parse_pattern_bytes("00 ?? 02 08"),  # jump is unknown becuase of the version difference
        instruction_readable="jz"
    ),
    Instruction(
        identifier=25, offset=0x230,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 11_12390"
    ),
    Instruction(
        identifier=26, offset=0x234,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=27, offset=0x238,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=28, offset=0x23c,
        pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=29, offset=0x240,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_friend(0x1d)"
    ),
    Instruction(
        identifier=30, offset=0x24c,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 11_00630"
    ),
    Instruction(
        identifier=31, offset=0x250,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=32, offset=0x254,
        pattern=parse_pattern_bytes("00 ?? 00 08"),  # jump is unknown becuase of the version difference
        instruction_readable="jmp"
    ),
    Instruction(
        identifier=33, offset=0x258,
        pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 11_12380"
    ),
    Instruction(
        identifier=34, offset=0x25c,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=35, offset=0x260,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=36, offset=0x244,
        pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=37, offset=0x248,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_bestfriend(0x1d)"
    ),
]

sudowoodo_interaction_patchMapJP = [
    # removing unneeded code
    #
    Patch(
        identifier=2,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=3,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=4,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=5,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=6,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=7,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=8,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=9,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=10,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=11,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=12,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=13,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=14,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=15,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=16,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # replacing friendship flag with best friend
    #
    Patch(
        identifier=17,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=18,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=19,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=20,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=21,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=22,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=23,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=24,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    Patch(
        identifier=29,  # replace friendship flag with bestfriend flag
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_call_instruction_fsb(
            offset, patch_patterns,
            set_bestfriend_function_pattern.name
        ),
        new_instruction_readable="call set_bestfriend(0x10)"
    ),
    Patch(
        identifier=36,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=37,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
]
sudowoodo_interaction_patchMapPAL = [
    # removing unneeded code
    #
    Patch(
        identifier=2,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=3,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=4,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=5,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=6,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=7,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=8,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=9,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=10,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=11,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=12,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=13,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=14,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=15,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=16,  # removing tutorial popup
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # replacing friendship flag with best friend
    #
    Patch(
        identifier=17,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=18,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=19,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=20,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=21,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=22,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=23,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=24,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    Patch(
        identifier=29,  # replace friendship flag with bestfriend flag
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_call_instruction_fsb(
            offset, patch_patterns,
            set_bestfriend_function_pattern.name
        ),
        new_instruction_readable="call set_bestfriend(0x10)"
    ),
    Patch(
        identifier=36,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=37,  # removing friendship flag request
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
]
sudowoodo_friendship_pattern = PatchPattern(
    name="Sudowoodo Friendship Logic",
    description="Winning against Sudowoodo sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=sudowoodo_interaction_patternJP,
    patternPAL=sudowoodo_interaction_patternPAL,
    patternNA=sudowoodo_interaction_patternPAL,
    patchMapJP=sudowoodo_interaction_patchMapJP,
    patchMapPAL=sudowoodo_interaction_patchMapPAL,
    patchMapNA=sudowoodo_interaction_patchMapPAL
)

scyther_friendship_pattern = PatchPattern(
    name="Scyther Friendship Logic",
    description="Winning against Scyther sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship."
                "Also sets required battle_count from options",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 1e 00 10"),
            instruction_readable="push 0x1e"
        ),

        # first battle count validation
        Instruction(
            identifier=2, offset=0xa0,
            pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
        ),
        Instruction(
            identifier=3, offset=0xa4,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
        # second battle count validation
        Instruction(
            identifier=4, offset=0x198,
            pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
        ),
        Instruction(
            identifier=5, offset=0x19c,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),

        # after winning path
        Instruction(
            identifier=6, offset=0x314,
            pattern=parse_pattern_bytes("00 45 00 10"),
            instruction_readable="push 0x45"
        ),
        Instruction(
            identifier=7, offset=0x318,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x31c,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=9, offset=0x320,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=10, offset=0x324,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=11, offset=0x328,
            pattern=parse_pattern_bytes("ff f6 00 0c"),
            instruction_readable="store_arg -0xa"
        ),
        Instruction(
            identifier=12, offset=0x32c,
            pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=13, offset=0x330,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=14, offset=0x334,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=15, offset=0x338,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=16, offset=0x33c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12490"
        ),
        Instruction(
            identifier=17, offset=0x340,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=18, offset=0x344,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=19, offset=0x348,
            pattern=parse_pattern_bytes("00 45 00 10"),
            instruction_readable="push 0x45"
        ),
        Instruction(
            identifier=20, offset=0x34c,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=21, offset=0x350,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=22, offset=0x354,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=23, offset=0x358,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00640"
        ),
        Instruction(
            identifier=24, offset=0x35c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x360,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=26, offset=0x364,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12480"
        ),
        Instruction(
            identifier=27, offset=0x368,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=28, offset=0x36c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=29, offset=0x370,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=30, offset=0x374,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x1e)"
        ),
    ],
    patchMapJP=[
        # setting battle count to option value
        Patch(
            identifier=2,  # setting battle count with option value
            patch_function=lambda offset, data, plando_dict,
                                  patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
                plando_dict
            ),
            new_instruction_readable="push $battlecount"
        ),
        Patch(
            identifier=4,  # setting battle count with option value
            patch_function=lambda offset, data, plando_dict,
                                  patch_patterns, pattern_name: get_num_battle_count_from_dict_as_instruction(
                plando_dict
            ),
            new_instruction_readable="push $battlecount"
        ),

        # removing friendship flag request
        #
        Patch(
            identifier=6,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=12,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=13,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=14,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=15,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # replacing friendship flag with bestfriend
        #
        Patch(
            identifier=19,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=20,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x1b)"
        ),

        # removing unnnecessary friendship/bestfriend flag instruction
        Patch(
            identifier=21,  # removing friendship flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=22,  # removing friendship flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=29,  # removing bestfriend flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=30,  # removing bestfriend flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

leafeon_friendship_pattern = PatchPattern(
    name="Leafeon Friendship Logic",
    description="Winning against Leafeon sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship.",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 1f 00 10"),
            instruction_readable="push 0x1f"
        ),

        # first friendship count validation
        Instruction(
            identifier=2, offset=0x84,
            pattern=parse_pattern_bytes("00 14 00 10"),
            instruction_readable="push 0x14"
        ),
        Instruction(
            identifier=3, offset=0x88,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
        # second friendship count validation
        Instruction(
            identifier=4, offset=0x144,
            pattern=parse_pattern_bytes("00 14 00 10"),
            instruction_readable="push 0x14"
        ),
        Instruction(
            identifier=5, offset=0x148,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),

        # friendship count validation for additional dialog
        Instruction(
            identifier=6, offset=0x178,
            pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0x0a"
        ),
        Instruction(
            identifier=7, offset=0x17c,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),

        # after winning path
        Instruction(
            identifier=8, offset=0x26c,
            pattern=parse_pattern_bytes("00 50 00 10"),
            instruction_readable="push 0x50"
        ),
        Instruction(
            identifier=9, offset=0x270,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=10, offset=0x274,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=11, offset=0x278,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=12, offset=0x27c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=13, offset=0x280,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=14, offset=0x284,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=15, offset=0x288,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=16, offset=0x28c,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=17, offset=0x290,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=18, offset=0x294,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12590"
        ),
        Instruction(
            identifier=19, offset=0x298,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=20, offset=0x29c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x2a0,
            pattern=parse_pattern_bytes("00 50 00 10"),
            instruction_readable="push 0x50"
        ),
        Instruction(
            identifier=22, offset=0x2a4,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=23, offset=0x2a8,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=24, offset=0x2ac,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=25, offset=0x2b0,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00650"
        ),
        Instruction(
            identifier=26, offset=0x2b4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=27, offset=0x2b8,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=28, offset=0x2bc,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_12580"
        ),
        Instruction(
            identifier=29, offset=0x2c0,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=30, offset=0x2c4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=31, offset=0x2c8,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=32, offset=0x2cc,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x1f)"
        ),
    ],
    patchMapJP=[
        # removing friendship flag request
        #
        Patch(
            identifier=8,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=12,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=13,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=14,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=15,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=16,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=17,  # removing friendship flag request
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # replacing friendship flag with bestfriend
        #
        Patch(
            identifier=21,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffd000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x3"
        ),
        Patch(
            identifier=22,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x1f)"
        ),

        # removing unnnecessary friendship/bestfriend flag instruction
        Patch(
            identifier=23,  # removing friendship flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,  # removing friendship flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=31,  # removing bestfriend flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=32,  # removing bestfriend flag set
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

croagunk_interaction_patternJP = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 20 00 10"),
        instruction_readable="push 0x20"
    ),

    # get chapter call
    Instruction(
        identifier=2, offset=0x28,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter()"
    ),
    Instruction(
        identifier=3, offset=0x2c,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=4, offset=0x30,
        pattern=parse_pattern_bytes("ff fb 00 0c"),
        instruction_readable="store_arg -0x5"
    ),
    # get friendship call
    Instruction(
        identifier=5, offset=0x34,
        pattern=parse_pattern_bytes("ff fe 00 0b"),
        instruction_readable="load_arg -0x2"
    ),
    Instruction(
        identifier=6, offset=0x38,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_friendship()"
    ),
    Instruction(
        identifier=7, offset=0x3c,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=8, offset=0x40,
        pattern=parse_pattern_bytes("ff fa 00 0c"),
        instruction_readable="store_arg -0x6"
    ),

    # start of event code
    Instruction(
        identifier=9, offset=0x84,
        pattern=parse_pattern_bytes("ff fb 00 0b"),
        instruction_readable="load_arg -0x5"
    ),
    # end of event code
    Instruction(
        identifier=10, offset=0x430,
        pattern=parse_pattern_bytes("ff f0 00 0c"),
        instruction_readable="store_arg -0x10"
    ),

    # enter path after winning
    Instruction(
        identifier=11, offset=0xa68,
        pattern=parse_pattern_bytes("ff fa 00 0b"),
        instruction_readable="load_arg -0x6"
    ),
    Instruction(
        identifier=12, offset=0xa6c,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=13, offset=0xa70,
        pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=14, offset=0xa74,
        pattern=parse_pattern_bytes("00 0c 02 08"),
        instruction_readable="jz"
    ),
    Instruction(
        identifier=15, offset=0xa78,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr 11_12690"
    ),
    Instruction(
        identifier=16, offset=0xa7c,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=17, offset=0xa80,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=18, offset=0xa84,
        pattern=parse_pattern_bytes("00 0b 00 10"),
        instruction_readable="push 0xb"
    ),
    Instruction(
        identifier=19, offset=0xa88,
        pattern=parse_pattern_bytes("ff ed 00 0b"),
        instruction_readable="load_arg -0x13"
    ),
    Instruction(
        identifier=20, offset=0xa8c,
        pattern=parse_pattern_bytes("00 3c 00 10"),
        instruction_readable="push 0x3c"
    ),
    Instruction(
        identifier=21, offset=0xa90,
        pattern=parse_pattern_bytes("00 15 03 01"),
        instruction_readable="SC 0x0:0x15"
    ),
    Instruction(
        identifier=22, offset=0xa94,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr 11_00660"
    ),
    Instruction(
        identifier=23, offset=0xa98,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=24, offset=0xa9c,
        pattern=parse_pattern_bytes("00 1e 00 10"),
        instruction_readable="push 0x1e"
    ),
    Instruction(
        identifier=25, offset=0xaa0,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call unlock_pokemon(0x1e)"
    ),
    Instruction(
        identifier=26, offset=0xaa4,
        pattern=parse_pattern_bytes("00 05 00 08"),
        instruction_readable="jmp"
    ),
    Instruction(
        identifier=27, offset=0xaa8,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr 11_12680"
    ),
    Instruction(
        identifier=28, offset=0xaac,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=29, offset=0xab0,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=30, offset=0xab4,
        pattern=parse_pattern_bytes("ff fe 00 0b"),
        instruction_readable="load_arg -0x2"
    ),
    Instruction(
        identifier=31, offset=0xab8,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_bestfriend(0x20)"
    ),

    # skip event
    Instruction(
        identifier=32, offset=0xae0,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter"
    ),
    Instruction(
        identifier=33, offset=0xae4,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
]

croagunk_interaction_patternPAL = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 20 00 10"),
        instruction_readable="push 0x20"
    ),

    # get chapter call
    Instruction(
        identifier=2, offset=0x28,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter()"
    ),
    Instruction(
        identifier=3, offset=0x2c,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=4, offset=0x30,
        pattern=parse_pattern_bytes("ff fb 00 0c"),
        instruction_readable="store_arg -0x5"
    ),
    # get friendship call
    Instruction(
        identifier=5, offset=0x34,
        pattern=parse_pattern_bytes("ff fe 00 0b"),
        instruction_readable="load_arg -0x2"
    ),
    Instruction(
        identifier=6, offset=0x38,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_friendship()"
    ),
    Instruction(
        identifier=7, offset=0x3c,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
    Instruction(
        identifier=8, offset=0x40,
        pattern=parse_pattern_bytes("ff fa 00 0c"),
        instruction_readable="store_arg -0x6"
    ),

    # start of event code
    Instruction(
        identifier=9, offset=0x84,
        pattern=parse_pattern_bytes("ff fb 00 0b"),
        instruction_readable="load_arg -0x5"
    ),
    # end of event code
    Instruction(
        identifier=10, offset=0x474,
        pattern=parse_pattern_bytes("ff f0 00 0c"),
        instruction_readable="store_arg -0x10"
    ),

    # enter path after winning
    Instruction(
        identifier=11, offset=0xa6c,
        pattern=parse_pattern_bytes("ff fa 00 0b"),
        instruction_readable="load_arg -0x6"
    ),
    Instruction(
        identifier=12, offset=0xa70,
        pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=13, offset=0xa74,
        pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=14, offset=0xa78,
        pattern=parse_pattern_bytes("00 0c 02 08"),
        instruction_readable="jz"
    ),
    Instruction(
        identifier=15, offset=0xa7c,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr 11_12690"
    ),
    Instruction(
        identifier=16, offset=0xa80,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=17, offset=0xa84,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=18, offset=0xa88,
        pattern=parse_pattern_bytes("00 0b 00 10"),
        instruction_readable="push 0xb"
    ),
    Instruction(
        identifier=19, offset=0xa8c,
        pattern=parse_pattern_bytes("ff ed 00 0b"),
        instruction_readable="load_arg -0x13"
    ),
    Instruction(
        identifier=20, offset=0xa90,
        pattern=parse_pattern_bytes("00 3c 00 10"),
        instruction_readable="push 0x3c"
    ),
    Instruction(
        identifier=21, offset=0xa94,
        pattern=parse_pattern_bytes("00 15 03 01"),
        instruction_readable="SC 0x0:0x15"
    ),
    Instruction(
        identifier=22, offset=0xa98,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr 11_00660"
    ),
    Instruction(
        identifier=23, offset=0xa9c,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=24, offset=0xaa0,
        pattern=parse_pattern_bytes("00 1e 00 10"),
        instruction_readable="push 0x1e"
    ),
    Instruction(
        identifier=25, offset=0xaa4,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call unlock_pokemon(0x1e)"
    ),
    Instruction(
        identifier=26, offset=0xaa8,
        pattern=parse_pattern_bytes("00 05 00 08"),
        instruction_readable="jmp"
    ),
    Instruction(
        identifier=27, offset=0xaac,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr 11_12680"
    ),
    Instruction(
        identifier=28, offset=0xab0,
        pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=29, offset=0xab4,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=30, offset=0xab8,
        pattern=parse_pattern_bytes("ff fe 00 0b"),
        instruction_readable="load_arg -0x2"
    ),
    Instruction(
        identifier=31, offset=0xabc,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_bestfriend(0x20)"
    ),

    # skip event
    Instruction(
        identifier=32, offset=0xae4,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter"
    ),
    Instruction(
        identifier=33, offset=0xae8,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result"
    ),
]

croagunk_interaction_patchMapJP = [
    # set chapter value so it skips all events
    #
    Patch(
        identifier=2,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=3,  # pushing instead of chapter 0x2af8 so no event is triggerable
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2af80010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x2af8"
    ),

    # removing friend flag request
    #
    Patch(
        identifier=11,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=12,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=13,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=14,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # set best friend flag
    #
    Patch(
        identifier=18,  # replace friendship flag with bestfriend flag
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="load_arg -0x2"
    ),
    Patch(
        identifier=19,  # replace friendship flag with bestfriend flag
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_call_instruction_fsb(
            offset, patch_patterns,
            set_bestfriend_function_pattern.name
        ),
        new_instruction_readable="call set_bestfriend(0x1b)"
    ),

    # remove set friend flag
    #
    Patch(
        identifier=20,  # removing set_bestfriend call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=21,  # removing set_bestfriend call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # remove unlock
    #
    Patch(
        identifier=24,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=25,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # remove original set bestfriend flag
    #
    Patch(
        identifier=30,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=31,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # remove event interaction
    #
    Patch(
        identifier=32,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=33,  # pushing instead of chapter 0x2af8 so no event is triggerable
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2af80010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x2af8"
    ),
]
croagunk_interaction_patchMapPAL = [
    # set chapter value so it skips all events
    #
    Patch(
        identifier=2,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=3,  # pushing instead of chapter 0x2af8 so no event is triggerable
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2af80010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x2af8"
    ),

    # removing friend flag request
    #
    Patch(
        identifier=11,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=12,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=13,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=14,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # set best friend flag
    #
    Patch(
        identifier=18,  # replace friendship flag with bestfriend flag
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="load_arg -0x2"
    ),
    Patch(
        identifier=19,  # replace friendship flag with bestfriend flag
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_call_instruction_fsb(
            offset, patch_patterns,
            set_bestfriend_function_pattern.name
        ),
        new_instruction_readable="call set_bestfriend(0x1b)"
    ),

    # remove set friend flag
    #
    Patch(
        identifier=20,  # removing set_bestfriend call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=21,  # removing set_bestfriend call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # remove unlock
    #
    Patch(
        identifier=24,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=25,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # remove original set bestfriend flag
    #
    Patch(
        identifier=30,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=31,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),

    # remove event interaction
    #
    Patch(
        identifier=32,  # removing get_chapter call
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=33,  # pushing instead of chapter 0x2af8 so no event is triggerable
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2af80010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x2af8"
    ),
]
croagunk_friendship_pattern = PatchPattern(
    name="Croagunk Friendship Logic",
    description="Winning against Croagunk sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship also events.",
    patternJP=croagunk_interaction_patternJP,
    patternPAL=croagunk_interaction_patternPAL,
    patternNA=croagunk_interaction_patternPAL,
    patchMapJP=croagunk_interaction_patchMapJP,
    patchMapPAL=croagunk_interaction_patchMapPAL,
    patchMapNA=croagunk_interaction_patchMapPAL,
)

bulbasaur_friendship_pattern = PatchPattern(
    name="Bulbasaur Friendship Logic",
    description="Winning against Bulbasaur sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship also events.",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 21 00 10"),
            instruction_readable="push 0x21"
        ),

        # get chapter call
        Instruction(
            identifier=2, offset=0x388,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr talk_fushigidaneBefore"
        ),
        Instruction(
            identifier=3, offset=0x38c,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x390,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x394,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x398,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x39c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x3a0,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="store_arg -0x6"
        ),

        Instruction(
            identifier=9, offset=0x3a4,
            pattern=parse_pattern_bytes("00 46 02 08"),
            instruction_readable="jz"
        ),

        Instruction(
            identifier=10, offset=0x18,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=11, offset=0x1c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        # prisma check skip
        Instruction(
            identifier=12, offset=0x4f8,
            pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0xf"
        ),
        Instruction(
            identifier=13, offset=0x4fc,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=14, offset=0x500,
            pattern=parse_pattern_bytes("00 51 00 10"),
            instruction_readable="push 0x51"
        ),
        Instruction(
            identifier=15, offset=0x504,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=16, offset=0x508,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=17, offset=0x50c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=18, offset=0x510,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=19, offset=0x514,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz"
        ),

        # skipping berry costs
        Instruction(
            identifier=20, offset=0x71c,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=21, offset=0x720,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=22, offset=0x724,
            pattern=parse_pattern_bytes("00 51 00 10"),
            instruction_readable="push 0x51"
        ),
        Instruction(
            identifier=23, offset=0x728,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=24, offset=0x72c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=25, offset=0x730,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=26, offset=0x734,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=27, offset=0x738,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz"
        ),

        # skipping beat venusaur dialog
        Instruction(
            identifier=28, offset=0x668,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=29, offset=0x66c,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=30, offset=0x670,
            pattern=parse_pattern_bytes("00 51 00 10"),
            instruction_readable="push 0x51"
        ),
        Instruction(
            identifier=31, offset=0x674,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=32, offset=0x678,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=33, offset=0x67c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=34, offset=0x680,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=35, offset=0x684,
            pattern=parse_pattern_bytes("00 08 02 08"),
            instruction_readable="jz"
        ),

        Instruction(  # Attraction Id
            identifier=36, offset=0x7dc,
            pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0xf"
        ),
    ],
    patchMapJP=[
        # set chapter value so it skips all events
        #
        Patch(
            identifier=9,  # removing get_chapter call
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00460208).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=10,  # removing get_chapter call
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # removing get_chapter call
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # removing get_chapter call
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2af80010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x2af8"
        ),

        # skipping having not cleared minigame pre-dialog
        Patch(
            identifier=19,  # removing get_chapter call
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00040008).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp"
        ),

        # skipping beat venusaur dialog and berry costs
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00060008).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=35,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay"
        ),
        Patch(
            identifier=36,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, MEADOW_ZONE_MAIN_AREA_BULBASAUR_ATTRACTION
            ),
            new_instruction_readable="delay"
        ),
    ]
)

drifblim_friendship_pattern = PatchPattern(
    name="Drifblim Friendship Logic",
    description="Traveling enough with drifblim sets only the bestfriend flag in Meadow Zone",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 62 00 10"),
            instruction_readable="push 0x62"
        ),

        # get chapter call
        Instruction(
            identifier=2, offset=0x4,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=3, offset=0x8,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=4, offset=0xc,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
    ],
    patchMapJP=[
        # replace friendship with bestfriend flag
        #
        Patch(
            identifier=3,  # removing get_chapter call
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004a0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4a"
        ),
    ]
)

starly2_friendship_pattern = PatchPattern(
    name="Starly 2 Friendship Logic",
    description="Winning against Starly 2 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship also events.",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 26 00 10"),
            instruction_readable="push 0x26"
        ),

        # minigame win logic
        Instruction(
            identifier=2, offset=0x22c,
            pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=3, offset=0x230,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x234,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x238,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x23c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x240,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x244,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x248,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x24c,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x250,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x254,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13290"
        ),
        Instruction(
            identifier=13, offset=0x258,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x25c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x260,
            pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=16, offset=0x264,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x268,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x26c,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x270,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00580"
        ),
        Instruction(
            identifier=20, offset=0x274,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x278,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x27c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13280"
        ),
        Instruction(
            identifier=23, offset=0x280,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x284,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x288,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x28c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x26)"
        ),
    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xa)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

starly3_friendship_pattern = PatchPattern(
    name="Starly 3 Friendship Logic",
    description="Winning against Starly 3 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 27 00 10"),
            instruction_readable="push 0x27"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13390"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00580"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13380"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x27)"
        ),

    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0x1b)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=25,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

aipom_friendship_pattern = PatchPattern(
    name="Aipom Friendship Logic",
    description="Winning against Aipom sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 28 00 10"),
            instruction_readable="push 0x28"
        ),

        Instruction(
            identifier=2, offset=0x208,
            pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0x0f"
        ),
        Instruction(
            identifier=3, offset=0x20c,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0x210,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=5, offset=0x214,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x218,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x21c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x220,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=9, offset=0x224,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x228,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x22c,
            pattern=parse_pattern_bytes("00 17 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=12, offset=0x230,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13490"
        ),
        Instruction(
            identifier=13, offset=0x234,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=14, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=15, offset=0x23c,
            pattern=parse_pattern_bytes("00 0f 00 10"),
            instruction_readable="push 0xf"
        ),
        Instruction(
            identifier=16, offset=0x240,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=17, offset=0x244,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=18, offset=0x248,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00550"
        ),
        Instruction(
            identifier=20, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=21, offset=0x254,
            pattern=parse_pattern_bytes("00 1c 00 10"),
            instruction_readable="push 0x1c"
        ),
        Instruction(
            identifier=22, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_pokemon(0x1c)"
        ),
        Instruction(
            identifier=23, offset=0x25c,
            pattern=parse_pattern_bytes("00 1c 00 10"),
            instruction_readable="push 0x1c"
        ),
        Instruction(
            identifier=24, offset=0x260,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????(0x1c)"
        ),
        Instruction(
            identifier=25, offset=0x264,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=26, offset=0x268,
            pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=27, offset=0x26c,
            pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=28, offset=0x270,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=29, offset=0x274,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=30, offset=0x278,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=31, offset=0x27c,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=32, offset=0x280,
            pattern=parse_pattern_bytes("00 01 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=33, offset=0x284,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=34, offset=0x288,
            pattern=parse_pattern_bytes("00 05 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=35, offset=0x28c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13480"
        ),
        Instruction(
            identifier=36, offset=0x290,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=37, offset=0x294,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=38, offset=0x298,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=39, offset=0x29c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x28)"
        ),
        Instruction(
            identifier=40, offset=0x2a0,
            pattern=parse_pattern_bytes("00 03 00 08"),
            instruction_readable="jmp"
        ),
    ],
    patchMapJP=[
        # removing unneeded code
        #
        Patch(
            identifier=2,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,  # not requesting friendship
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # only entering one path
        #
        Patch(
            identifier=9,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=11,  # enter only one path after winning
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # setting bestfriend flag instead of regular friendship
        #
        Patch(
            identifier=15,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffe000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=16,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="call set_bestfriend(0xc)"
        ),

        # removing unneeded code
        #
        Patch(
            identifier=17,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=18,  # removing unnecessary prep for setting friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=22,  # removing pokemon unlock
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing original set best friend flag call
        Patch(
            identifier=38,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=39,  # removing setting original best friend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

starly4_friendship_pattern = PatchPattern(
    name="Starly 4 Friendship Logic",
    description="Winning against Starly 4 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),

        Instruction(
            identifier=2, offset=0x204,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x208,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x20c,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=5, offset=0x210,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=6, offset=0x214,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=7, offset=0x218,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x21c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x220,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=10, offset=0x224,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=11, offset=0x228,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13580"
        ),
        Instruction(
            identifier=12, offset=0x22c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=13, offset=0x230,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x234,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=15, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x34)"
        ),
        Instruction(
            identifier=16, offset=0x23c,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp identifier 23"
        ),
        Instruction(
            identifier=17, offset=0x240,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13590"
        ),
        Instruction(
            identifier=18, offset=0x244,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=19, offset=0x248,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00580"
        ),
        Instruction(
            identifier=21, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x254,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=23, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x29)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # only enter set_bestfriend path
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

spearow_attraction_friendship_pattern = PatchPattern(
    name="Spearow Attraction Friendship Logic",
    description="Winning against Spearow Attraction sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship also events.",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 2a 00 10"),
            instruction_readable="push 0x2a"
        ),

        # get chapter call
        Instruction(
            identifier=2, offset=0x18,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter()"
        ),
        Instruction(
            identifier=3, offset=0x1c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x20,
            pattern=parse_pattern_bytes("ff fa 00 0c"),
            instruction_readable="store_arg -0x6"
        ),
        # get friendship call
        Instruction(
            identifier=5, offset=0x2f0,
            pattern=parse_pattern_bytes("00 8f 00 10"),
            instruction_readable="push 0x8f"
        ),
        Instruction(
            identifier=6, offset=0x2f4,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=7, offset=0x2f8,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        Instruction(
            identifier=8, offset=0x2fc,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=9, offset=0x300,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=10, offset=0x304,
            pattern=parse_pattern_bytes("ff f5 00 0c"),
            instruction_readable="store_arg -0xb"
        ),

        # enter path after winning
        #
        Instruction(
            identifier=11, offset=0x308,
            pattern=parse_pattern_bytes("ff f5 00 0b"),
            instruction_readable="load_arg -0xb"
        ),
        Instruction(
            identifier=12, offset=0x30c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=13, offset=0x310,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=14, offset=0x314,
            pattern=parse_pattern_bytes("00 0a 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=15, offset=0x318,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13690"
        ),
        Instruction(
            identifier=16, offset=0x31c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=17, offset=0x320,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=18, offset=0x324,
            pattern=parse_pattern_bytes("00 8f 00 10"),
            instruction_readable="push 0x8f"
        ),
        Instruction(
            identifier=19, offset=0x328,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=20, offset=0x32c,
            pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=21, offset=0x330,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=22, offset=0x334,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00560"
        ),
        Instruction(
            identifier=23, offset=0x338,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=24, offset=0x33c,
            pattern=parse_pattern_bytes("00 03 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=25, offset=0x340,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13680"
        ),
        Instruction(
            identifier=26, offset=0x344,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=27, offset=0x348,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),

        # attraction tutorial popup
        Instruction(
            identifier=28, offset=0x1F8,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f010Athletic"
        ),
        Instruction(
            identifier=29, offset=0x1Fc,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=30, offset=0x200,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=31, offset=0x204,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=32, offset=0x208,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=33, offset=0x20c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=34, offset=0x210,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=35, offset=0x214,
            pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=36, offset=0x218,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 11_00130"
        ),
        Instruction(
            identifier=37, offset=0x21c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=38, offset=0x220,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
    ],

    patchMapJP=[
        # set chapter value so it skips all events
        #
        Patch(
            identifier=2,  # removing get_chapter call
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,  # pushing instead of chapter 0x2af8 so no event is triggerable
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x2af80010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x2af8"
        ),

        # removing friend flag request
        #
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        # set best friend flag
        #
        Patch(
            identifier=20,  # replace friendship flag with bestfriend flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004a0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4a"
        ),
    ]
)

lotad2_friendship_pattern = PatchPattern(
    name="Lotad 2 Friendship Logic",
    description="Winning against Lotad 2 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 2b 00 10"),
            instruction_readable="push 0x2b"
        ),

        Instruction(
            identifier=2, offset=0x24c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x250,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x254,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=5, offset=0x258,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=6, offset=0x25c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=7, offset=0x260,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x264,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x268,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=10, offset=0x26c,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=11, offset=0x270,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13780"
        ),
        Instruction(
            identifier=12, offset=0x274,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=13, offset=0x278,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x27c,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=15, offset=0x280,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x2b)"
        ),
        Instruction(
            identifier=16, offset=0x284,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp identifier 23"
        ),
        Instruction(
            identifier=17, offset=0x288,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13790"
        ),
        Instruction(
            identifier=18, offset=0x28c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=19, offset=0x290,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x294,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00460"
        ),
        Instruction(
            identifier=21, offset=0x298,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x29c,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=23, offset=0x2a0,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x2b)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # only enter set_bestfriend path
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

lotad3_friendship_pattern = PatchPattern(
    name="Lotad 3 Friendship Logic",
    description="Winning against Lotad 3 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 2c 00 10"),
            instruction_readable="push 0x2c"
        ),

        Instruction(
            identifier=2, offset=0x248,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x24c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x250,
            pattern=parse_pattern_bytes("ff f8 00 0c"),
            instruction_readable="store_arg -0x8"
        ),
        Instruction(
            identifier=5, offset=0x254,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=6, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=7, offset=0x25c,
            pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x260,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x264,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=10, offset=0x268,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=11, offset=0x26c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13880"
        ),
        Instruction(
            identifier=12, offset=0x270,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=13, offset=0x274,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x278,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=15, offset=0x27c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x2c)"
        ),
        Instruction(
            identifier=16, offset=0x280,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp identifier 23"
        ),
        Instruction(
            identifier=17, offset=0x284,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13890"
        ),
        Instruction(
            identifier=18, offset=0x288,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=19, offset=0x28c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x290,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00460"
        ),
        Instruction(
            identifier=21, offset=0x294,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x298,
            pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=23, offset=0x29c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x2c)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # only enter set_bestfriend path
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

starly5_friendship_pattern = PatchPattern(
    name="Starly 5 Friendship Logic",
    description="Winning against Starly 5 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 2d 00 10"),
            instruction_readable="push 0x2d"
        ),

        Instruction(
            identifier=2, offset=0x204,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x208,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x20c,
            pattern=parse_pattern_bytes("ff f9 00 0c"),
            instruction_readable="store_arg -0x7"
        ),
        Instruction(
            identifier=5, offset=0x210,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=6, offset=0x214,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=7, offset=0x218,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=8, offset=0x21c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x220,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=10, offset=0x224,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=11, offset=0x228,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13980"
        ),
        Instruction(
            identifier=12, offset=0x22c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=13, offset=0x230,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x234,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=15, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x2d)"
        ),
        Instruction(
            identifier=16, offset=0x23c,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp identifier 23"
        ),
        Instruction(
            identifier=17, offset=0x240,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_13990"
        ),
        Instruction(
            identifier=18, offset=0x244,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=19, offset=0x248,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00580"
        ),
        Instruction(
            identifier=21, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x254,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=23, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x2d)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # only enter set_bestfriend path
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

shinx2_friendship_pattern = PatchPattern(
    name="Shinx 2 Friendship Logic",
    description="Winning against Shinx 2 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 2f 00 10"),
            instruction_readable="push 0x2f"
        ),

        Instruction(
            identifier=2, offset=0x204,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x208,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x20c,
            pattern=parse_pattern_bytes("ff f9 00 0c"),
            instruction_readable="store_arg -0x7"
        ),
        Instruction(
            identifier=5, offset=0x210,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=6, offset=0x214,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=7, offset=0x218,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=8, offset=0x21c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x220,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=10, offset=0x224,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=11, offset=0x228,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_14180"
        ),
        Instruction(
            identifier=12, offset=0x22c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=13, offset=0x230,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x234,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=15, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x2f)"
        ),
        Instruction(
            identifier=16, offset=0x23c,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp identifier 23"
        ),
        Instruction(
            identifier=17, offset=0x240,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_14190"
        ),
        Instruction(
            identifier=18, offset=0x244,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=19, offset=0x248,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00530"
        ),
        Instruction(
            identifier=21, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x254,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=23, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x2f)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # only enter set_bestfriend path
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

butterfree2_friendship_pattern = PatchPattern(
    name="Butterfree 2 Friendship Logic",
    description="Winning against Butterfree 2 sets the Best Friend Flag instead of the friend flag, also removes the original unlocks and friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 31 00 10"),
            instruction_readable="push 0x31"
        ),

        Instruction(
            identifier=2, offset=0x204,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call is_friend"
        ),
        Instruction(
            identifier=3, offset=0x208,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x20c,
            pattern=parse_pattern_bytes("ff f9 00 0c"),
            instruction_readable="store_arg -0x7"
        ),
        Instruction(
            identifier=5, offset=0x210,
            pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=6, offset=0x214,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=7, offset=0x218,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=8, offset=0x21c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x220,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=10, offset=0x224,
            pattern=parse_pattern_bytes("00 06 02 08"),
            instruction_readable="jz identifier 16"
        ),
        Instruction(
            identifier=11, offset=0x228,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_14380"
        ),
        Instruction(
            identifier=12, offset=0x22c,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=13, offset=0x230,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=14, offset=0x234,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=15, offset=0x238,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend(0x31)"
        ),
        Instruction(
            identifier=16, offset=0x23c,
            pattern=parse_pattern_bytes("00 07 00 08"),
            instruction_readable="jmp identifier 23"
        ),
        Instruction(
            identifier=17, offset=0x240,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_14390"
        ),
        Instruction(
            identifier=18, offset=0x244,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=19, offset=0x248,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=20, offset=0x24c,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr 11_00590"
        ),
        Instruction(
            identifier=21, offset=0x250,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call FUN_??????"
        ),
        Instruction(
            identifier=22, offset=0x254,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=23, offset=0x258,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x31)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't request friendship flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # only enter set_bestfriend path
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=23,  # removing the original set friendship flag
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

return_attraction_patternJP = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 10 00 07"),
        instruction_readable="grow_stack 0x10"
    ),

    # get chapter value for events
    Instruction(
        identifier=2, offset=0x5c,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter",
    ),
    Instruction(
        identifier=3, offset=0x60,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result",
    ),

    Instruction(
        identifier=4, offset=0x300,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr f0101EventTE03",
    ),
    Instruction(
        identifier=5, offset=0x304,
        pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1",
    ),
    Instruction(
        identifier=6, offset=0x308,
        pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1",
    ),
    Instruction(
        identifier=7, offset=0x30c,
        pattern=parse_pattern_bytes("00 15 03 01"),
        instruction_readable="SC3 0x0:0x15",
    ),

]

return_attraction_patternPAL = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 10 00 07"),
        instruction_readable="grow_stack 0x10"
    ),

    # get chapter value for events
    Instruction(
        identifier=2, offset=0x64,
        pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter",
    ),
    Instruction(
        identifier=3, offset=0x68,
        pattern=parse_pattern_bytes("00 00 00 12"),
        instruction_readable="push_result",
    ),

    Instruction(
        identifier=4, offset=0x308,
        pattern=parse_pattern_bytes("00 ?? ?? 13"),
        instruction_readable="lstr f0101EventTE03",
    ),
    Instruction(
        identifier=5, offset=0x30c,
        pattern=parse_pattern_bytes("ff ff 00 0b"),
        instruction_readable="load_arg -0x1",
    ),
    Instruction(
        identifier=6, offset=0x310,
        pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1",
    ),
    Instruction(
        identifier=7, offset=0x314,
        pattern=parse_pattern_bytes("00 15 03 01"),
        instruction_readable="SC3 0x0:0x15",
    ),

]

return_attraction_patchMapJP = [
    Patch(
        identifier=2,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x00000002).to_bytes(
            4,  # don't request chapter
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=3,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x2af80010).to_bytes(
            4,  # push 0x2af8 chapter so all events are skipped
            'big'
        ),
        new_instruction_readable="push 0x2af8"
    ),
    Patch(
        identifier=4,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x00390010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x39"
    ),
    Patch(
        identifier=6,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x004b0010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x39"
    ),
]

return_attraction_patchMapPAL = [
    Patch(
        identifier=2,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x00000002).to_bytes(
            4,  # don't request chapter
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=3,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x2af80010).to_bytes(
            4,  # push 0x2af8 chapter so all events are skipped
            'big'
        ),
        new_instruction_readable="push 0x2af8"
    ),
    Patch(
        identifier=4,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x00390010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x39"
    ),
    Patch(
        identifier=6,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
            0x004b0010).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="push 0x39"
    ),
]

return_attraction_pattern = PatchPattern(
    name="Return Attraction",
    description="Returning from Attraction triggers bulbasaur friendship only when the location is not checked, also removing event code",
    patternJP=return_attraction_patternJP,
    patternPAL=return_attraction_patternPAL,
    patternNA=return_attraction_patternPAL,
    patchMapJP=return_attraction_patchMapJP,
    patchMapPAL=return_attraction_patchMapPAL,
    patchMapNA=return_attraction_patchMapPAL
)

eventTE03_logic = PatchPattern(
    name="f0101EventTE03 Logic",  # bulbasaur friendship after winning prisma
    description="Returning from Attraction triggers bulbasaur friendship location and doesn't set regular friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x04"
        ),

        # get chapter value for events
        Instruction(
            identifier=2, offset=0x154,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=3, offset=0x158,
            pattern=parse_pattern_bytes("00 ?? ?? 13"),
            instruction_readable="lstr f0101EventTE03"
        ),
        Instruction(
            identifier=4, offset=0x15c,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=5, offset=0x160,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=6, offset=0x164,
            pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # set friendship
        Instruction(
            identifier=7, offset=0x174,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friend(0x21)"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't set event flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't set event flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't set event flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't set event flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x00000002).to_bytes(
                4,  # don't set event flag
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns,
                set_bestfriend_function_pattern.name
            ),
            new_instruction_readable="set_bestfriend(0x21)"
        ),

    ]
)

torterra_starly_unlock_patternJP = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 01 00 07"),
        instruction_readable="grow_stack 0x01"
    ),

    # get chapter value for events
    Instruction(
        identifier=2, offset=0x44,
        pattern=parse_pattern_bytes("00 04 02 08"),
        instruction_readable="jz"
    ),
    Instruction(
        identifier=3, offset=0x58,
        pattern=parse_pattern_bytes("00 02 00 06"),
        instruction_readable="ret -0x2"
    ),

]
torterra_starly_unlock_patternPAL = [
    Instruction(
        identifier=1, offset=0,
        pattern=parse_pattern_bytes("00 01 00 07"),
        instruction_readable="grow_stack 0x01"
    ),

    # get chapter value for events
    Instruction(
        identifier=2, offset=0x64,
        pattern=parse_pattern_bytes("00 04 02 08"),
        instruction_readable="jz"
    ),
    Instruction(
        identifier=3, offset=0x78,
        pattern=parse_pattern_bytes("00 02 00 06"),
        instruction_readable="ret -0x2"
    ),

]

torterra_starly_unlock_patchmapJP = [
    Patch(
        identifier=1,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_jmp_instruction_fsb(
            offset, 3,
            patch_patterns, pattern_name
        ),
        new_instruction_readable="jmp"
    ),  # skipping whole function

]
torterra_starly_unlock_patchmapPAL = [
    Patch(
        identifier=1,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_jmp_instruction_fsb(
            offset, 3,
            patch_patterns, pattern_name
        ),
        new_instruction_readable="jmp"
    ),  # skipping whole function

]

torterra_starly_unlock = PatchPattern(
    name="Torterra Starly Unlock after Venusaur Prisma Logic",
    description="Removing automatic Unlocks for Torterra and Starly after Venusaur Prisma",
    patternJP=torterra_starly_unlock_patternJP,
    patternPAL=torterra_starly_unlock_patternPAL,
    patternNA=torterra_starly_unlock_patternPAL,
    patchMapJP=torterra_starly_unlock_patchmapJP,
    patchMapPAL=torterra_starly_unlock_patchmapPAL,
    patchMapNA=torterra_starly_unlock_patchmapPAL, )

unlock_beach_bidoof_interaction = PatchPattern(
    name="Unlock Beach Bidoof Unlock",
    description="Removing actual unlocks and set flag also trigger only when location is not checked",
    patternJP=[
        Instruction(
            identifier=1, offset=0,
            pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x05"
        ),

        # get chapter value for events
        Instruction(
            identifier=2, offset=0x4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=3, offset=0x8,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0xc,
            pattern=parse_pattern_bytes("08 02 00 10"),
            instruction_readable="push 0x802"
        ),
        Instruction(
            identifier=5, offset=0x10,
            pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=6, offset=0x14,
            pattern=parse_pattern_bytes("00 51 02 08"),
            instruction_readable="jz"
        ),

        Instruction(
            identifier=7, offset=0x124,
            pattern=parse_pattern_bytes("08 0c 00 10"),
            instruction_readable="push 0x80c"
        ),
        Instruction(
            identifier=8, offset=0x128,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, custom_check_f0301BippaFlag_funtion.name
            ),
            new_instruction_readable="call get f0301BippaFlag"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay(0)"
        ),
    ]
)

custom_check_f0301BippaFlag_funtion = PatchPattern(
    name="f0301BippaFlag check",
    description="using unused code space for f0301BippaFlag check",
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
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 b6 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 02 01 06"),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, f0301BippaFlag.name
            ),
            new_instruction_readable="lstr f0301BippaFlag"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150301).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020106).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="retv -0x2"
        ),

    ],
)

thunderbolt_hit_magikarp_event_patternJP = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 18 00 07"),
        instruction_readable="grow_stack 0x18"
    ),
    Instruction(
        identifier=2, offset=0x348, pattern=parse_pattern_bytes("00 19 00 06"),
        instruction_readable="ret -0x19"
    ),
    Instruction(
        identifier=5, offset=0x11c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call unlock_pokemon"
    ),
]

thunderbolt_hit_magikarp_event_patchMapJP = [
    Patch(
        identifier=5,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_call_instruction_fsb(
            offset, patch_patterns, set_magikarp_location_function.name
        ),
        new_instruction_readable="call set_magikarp_function"
    ),
]

thunderbolt_hit_magikarp_event_patternPAL = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 18 00 07"),
        instruction_readable="grow_stack 0x18"
    ),
    # start of setting object Magikarp logic
    Instruction(
        identifier=2, offset=0x31c, pattern=parse_pattern_bytes("ff f2 00 0b"),
        instruction_readable="load_arg -0xe"
    ),
    # end of magikarp object logic
    Instruction(
        identifier=3, offset=0x3b8, pattern=parse_pattern_bytes("00 1e 00 10"),
        instruction_readable="push 0x1e"
    ),
    Instruction(
        identifier=5, offset=0x11c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call unlock_pokemon"
    ),
]
thunderbolt_hit_magikarp_event_patchMapPAL = [
    Patch(
        identifier=2,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_jmp_instruction_fsb(
            offset, 3, patch_patterns, pattern_name
        ),
        new_instruction_readable="jmp"
    ),
    Patch(
        identifier=5,
        patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_call_instruction_fsb(
            offset, patch_patterns, set_magikarp_location_function.name
        ),
        new_instruction_readable="call set_magikarp_function"
    ),
]

thunderbolt_hit_magikarp_event = PatchPattern(
    name="hitting Magikarp with Thunderbolt event Logic",
    description="skipping additional magikarp object placement in pal and NA version",
    patternJP=thunderbolt_hit_magikarp_event_patternJP,
    patternPAL=thunderbolt_hit_magikarp_event_patternPAL,
    patternNA=thunderbolt_hit_magikarp_event_patternPAL,
    patchMapJP=thunderbolt_hit_magikarp_event_patchMapJP,
    patchMapPAL=thunderbolt_hit_magikarp_event_patchMapPAL,
    patchMapNA=thunderbolt_hit_magikarp_event_patchMapPAL,
)

get_mankey_friendship_function = PatchPattern(
    name="get_mankey_friendship_function",
    description="get mankey friendship function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff f2 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 03 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("ff ce 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 13 00 06"),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00210010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x21"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x003d0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x3d"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150301).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020106).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="retv -0x2"
        ),

    ],
)

STAXIAREA = PatchPattern(
    name="STAXIAREA",
    description="Meadow Fast Travels",
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update position target based on exit"
        ),

        # treehouse
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # beach
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # ice
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # cavern
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # magma
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # haunted
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # granite
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # flower
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr01Zn01_Npc_Main_patch_pattern = [
    string_section_start,
    f0101TalkOnisuzume,
    globalManager,
    f0301BippaFlag,

    set_chapter,
    get_friendship,
    get_module,
    overworld_pokemon_spawning_Ar01Zn01,
    turtwig_friendship_pattern,
    turtwig_dialog_options_pattern,
    buneary_friendship_pattern,
    buneary_dialog_options_pattern,
    pachirisu1_friendship_pattern,
    pachirisu2_friendship_pattern,
    munchlax_friendship_pattern,
    munchlax2_friendship_pattern,
    treecko_friendship_pattern,
    chimchar_friendship_pattern,
    magikarp_friendship_pattern,
    lotad1_friendship_pattern,
    caterpie_friendship_pattern,
    weedle_friendship_pattern,
    event_bidoof_friendship_pattern,
    bidoof1,
    bidoof2,
    bidoof3,
    oddish_friendship_pattern,
    shroomish_friendship_pattern,
    bonsly_friendship_pattern,
    shinx_friendship_pattern,
    # overworld Mankey does not need a patch, it originally only sets the bestfriend flag and sets no other flags
    aipom_tree_friendship_pattern,
    aipom_friendship_pattern,
    spearow_overworld_friendship_pattern,
    torterra_friendship_pattern,
    starly_friendship_pattern,
    butterfree_friendship_pattern,
    tropius_friendship_pattern,
    bibarel_friendship_pattern,
    ambipom_friendship_pattern,
    sudowoodo_friendship_pattern,
    scyther_friendship_pattern,
    leafeon_friendship_pattern,
    croagunk_friendship_pattern,
    bulbasaur_friendship_pattern,
    drifblim_friendship_pattern,
    starly2_friendship_pattern,
    starly3_friendship_pattern,
    starly4_friendship_pattern,
    spearow_attraction_friendship_pattern,
    lotad2_friendship_pattern,
    lotad3_friendship_pattern,
    starly5_friendship_pattern,
    shinx2_friendship_pattern,
    butterfree2_friendship_pattern,
    set_bestfriend_function_pattern,

    return_attraction_pattern,
    eventTE03_logic,
    torterra_starly_unlock,

    # custom-functions beach bidoof
    unlock_beach_bidoof_interaction,
    custom_check_f0301BippaFlag_funtion,

    # magikarp logic
    thunderbolt_hit_magikarp_event,
    set_magikarp_location_function,
    get_mankey_friendship_function,

    STAXIAREA,
    battle_counter_handling
]
