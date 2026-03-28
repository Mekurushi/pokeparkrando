from patcher.helper.entrance_exit_names import GRANITE_ZONE_MAIN_AREA_ABSOL_ATTRACTION, \
    GRANITE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, GRANITE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, \
    GRANITE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, GRANITE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, \
    GRANITE_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, \
    GRANITE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, GRANITE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, \
    GRANITE_ZONE_MAIN_AREA_SALAMENCE_ATTRACTION, \
    GRANITE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL
from patcher.helper.patttern_handler import compute_call_instruction_fsb, \
    create_lstr_instruction_fsb, \
    get_attraction_id_from_dict, get_exit_zone_area_position_data, get_num_battle_count_from_dict_as_instruction, \
    parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import battle_counter_handling, get_friendship, get_module, globalManager, set_chapter

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
            pattern=parse_pattern_bytes("65 76 41 72 30 36 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr06Zn01_Npc_Main"
        ),

    ],
)
f0601FireWallB = PatchPattern(
    name="f0601FireWallB",
    description="f0601FireWallB for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 36 30 31 46 69 72 65 57 61 6c 6c 42 00"),
            instruction_readable="ds f0601FireWallB"
        ),

    ],
)

f0601TalkKamex = PatchPattern(
    name="f0601TalkKamex",
    description="f0601TalkKamex for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 36 30 31 54 61 6c 6b 4b 61 6d 65 78 00"),
            instruction_readable="ds f0601TalkKamex"
        ),

    ],
)

fRuinsGateKey = PatchPattern(
    name="fRuinsGateKey",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 52 75 69 6e 73 47 61 74 65 4b 65 79 00"),
            instruction_readable="ds fRuinsGateKey"
        ),

    ],
)

init_gate_function = PatchPattern(
    name="init gate and firewall function",
    description="setup flags for granite zone so npc ai works correct",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 1a 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 15 00 10"),
            instruction_readable="push 0x15"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 17 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 0b 00 10"),
            instruction_readable="push 0xb"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 14 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 1f 00 10"),
            instruction_readable="push 0x1f"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 11 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 20 00 10"),
            instruction_readable="push 0x20"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 0e 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="push 0x29"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("00 0b 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 2a 00 10"),
            instruction_readable="push 0x2a"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 08 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 33 00 10"),
            instruction_readable="push 0x33"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="store_arg -0x9"
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
                patch_patterns, string_section_start.name, f0601FireWallB.name
            ),
            new_instruction_readable="lstr f0601FireWallB"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name, fRuinsGateKey.name
            ),
            new_instruction_readable="lstr fRuinsGateKey"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150401).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC4 0x0:0x15"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00050010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x5"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00060010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x6"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x002d0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x2d"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150501).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="SC5 0x0:0x15"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x2"
        ),
    ]
)
A06_Z01_INIT_PATTERNPAL = [

    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
        instruction_readable="grow_stack 0x2"
    ),

    Instruction(
        identifier=2, offset=0x44, pattern=parse_pattern_bytes("4e 21 00 10"),
        instruction_readable="push 0x4e21"
    ),

    Instruction(
        identifier=3, offset=0x4c, pattern=parse_pattern_bytes("4e 22 00 10"),
        instruction_readable="push 0x4e22"
    ),
    Instruction(
        identifier=4, offset=0x58, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=5, offset=0x5c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call unlock_garchomp_tyranitar"
    ),

]

A06_Z01_INIT = PatchPattern(
    name="A06_Z01_INIT",
    description="call init_gates_function",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x3c, pattern=parse_pattern_bytes("4e 21 00 10"),
            instruction_readable="push 0x4e21"
        ),

        Instruction(
            identifier=3, offset=0x44, pattern=parse_pattern_bytes("4e 22 00 10"),
            instruction_readable="push 0x4e22"
        ),
        Instruction(
            identifier=4, offset=0x50, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=5, offset=0x54, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call unlock_garchomp_tyranitar"
        ),
    ],
    patternPAL=A06_Z01_INIT_PATTERNPAL,
    patternNA=A06_Z01_INIT_PATTERNPAL,
    patchMapJP=[
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, init_gate_function.name
            ),
            new_instruction_readable="call init_gate_function"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, GRANITE_ZONE_MAIN_AREA_ABSOL_ATTRACTION
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x009d0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x9d"  # salamence friendship id
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00460010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x46"  # absol friendship id
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
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_absol_friendship_location_state.name
            ),
            new_instruction_readable="call get_absol_friendship_location_state"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, GRANITE_ZONE_MAIN_AREA_SALAMENCE_ATTRACTION
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
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_salamence_friendship_location_state.name
            ),
            new_instruction_readable="call get_salamence_friendship_location_state"
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

        Instruction(
            identifier=9, offset=0x240, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
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

        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # get bestfriend opcode
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
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="push 0x1b1"
        ),
        Instruction(
            identifier=3, offset=0x38, pattern=parse_pattern_bytes("1f 4a 00 10"),
            instruction_readable="call fun_??????"
        ),

        Instruction(
            identifier=4, offset=0x3c, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="push 0x1b1"
        ),
        Instruction(
            identifier=5, offset=0x40, pattern=parse_pattern_bytes("00 14 02 08"),
            instruction_readable="call fun_??????"
        ),
        Instruction(
            identifier=6, offset=0x44, pattern=parse_pattern_bytes("01 b1 00 10"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="store_arg -0x3"
        ),
        Instruction(
            identifier=8, offset=0x4c, pattern=parse_pattern_bytes("01 b1 00 10"),
            instruction_readable="push 0xfe4a"
        ),
        Instruction(
            identifier=9, offset=0xc0, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"  # blastoise condition
        ),
        Instruction(
            identifier=10, offset=0x1a0, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0601FuwarideTaxiStop"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x1f810010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1f81"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00040006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x4"
        ),

    ]
)

drifloon_interaction = PatchPattern(
    name="drifloon interaction",
    description="adding each zone option support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 ae 00 10"),
            instruction_readable="push 0x1ae"
        ),

        Instruction(
            identifier=3, offset=0x64, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        # each zone option

        Instruction(
            identifier=4, offset=0x74, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=5, offset=0xb8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=6, offset=0xbc, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 61_00380"
        ),
        Instruction(
            identifier=7, offset=0xc0, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # get bestfriend opcode
        ),

        # each zone option
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00170010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x17"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

skorupi_interaction = PatchPattern(
    name="skorupi interaction",
    description="adding absol prisma condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 a0 00 10"),
            instruction_readable="push 0x1a0"
        ),

        Instruction(
            identifier=3, offset=0xa8, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0601FireWallB"
        ),

        Instruction(
            identifier=4, offset=0xb0, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name,
                f0601TalkKamex.name
            ),
            new_instruction_readable="lstr f0601TalkKamex"
        ),

    ]
)

taillow_interaction = PatchPattern(
    name="taillow interaction",
    description="adding each zone option support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 a8 00 10"),
            instruction_readable="push 0x1a8"
        ),

        Instruction(
            identifier=3, offset=0x228, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        # each zone option

        Instruction(
            identifier=4, offset=0x238, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=5, offset=0x254, pattern=parse_pattern_bytes("00 ad 00 10"),
            instruction_readable="push 0xad"
        ),
        Instruction(
            identifier=6, offset=0x258, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=7, offset=0x25c, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=8, offset=0x260, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # get bestfriend opcode
        ),

        # each zone option
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00180010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x18"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

marowak_interaction = PatchPattern(
    name="marowak interaction",
    description="adding each zone option support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 a3 00 10"),
            instruction_readable="push 0x1a3"
        ),

        Instruction(
            identifier=3, offset=0x228, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        # each zone option

        Instruction(
            identifier=4, offset=0x238, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=5, offset=0x254, pattern=parse_pattern_bytes("00 70 00 10"),
            instruction_readable="push 0x70"
        ),
        Instruction(
            identifier=6, offset=0x258, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=7, offset=0x25c, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=8, offset=0x260, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # get bestfriend opcode
        ),

        # each zone option
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00190010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x19"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

baltoy_interaction = PatchPattern(
    name="baltoy interaction",
    description="adding each zone option support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 a7 00 10"),
            instruction_readable="push 0x1a7"
        ),

        Instruction(
            identifier=3, offset=0x254, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        # each zone option

        Instruction(
            identifier=4, offset=0x264, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=5, offset=0x280, pattern=parse_pattern_bytes("00 a3 00 10"),
            instruction_readable="push 0xa3"
        ),
        Instruction(
            identifier=6, offset=0x284, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=7, offset=0x288, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=8, offset=0x28c, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # get bestfriend opcode
        ),

        # each zone option
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x000d0010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

claydol_interaction = PatchPattern(
    name="claydol interaction",
    description="adding each zone option support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 a4 00 10"),
            instruction_readable="push 0x1a4"
        ),

        Instruction(
            identifier=3, offset=0x228, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        # each zone option

        Instruction(
            identifier=4, offset=0x238, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=5, offset=0x254, pattern=parse_pattern_bytes("00 a4 00 10"),
            instruction_readable="push 0xa4"
        ),
        Instruction(
            identifier=6, offset=0x258, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=7, offset=0x25c, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=8, offset=0x260, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # get bestfriend opcode
        ),

        # each zone option
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00040010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x4"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x000d0010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

togekiss_interaction = PatchPattern(
    name="togekiss interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 15 00 07"),
            instruction_readable="grow_stack 0x15"
        ),

        Instruction(
            identifier=2, offset=0x34, pattern=parse_pattern_bytes("01 ab 00 10"),
            instruction_readable="push 0x1a4"
        ),

        Instruction(
            identifier=3, offset=0x210, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x1f9a0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1f9a"
        ),

    ]
)

jirachi_interaction = PatchPattern(
    name="jirachi interaction",
    description="modified behavior for jirachi location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 bb 00 10"),
            instruction_readable="push 0x1bb"
        ),

        Instruction(
            identifier=3, offset=0x88, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x1dc, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=5, offset=0x200, pattern=parse_pattern_bytes("?? ?? ?? 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=6, offset=0x204, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 61_12590"
        ),
        Instruction(
            identifier=7, offset=0x208, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=8, offset=0x20c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call dialog"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x1"  # skip postgame check
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay0"
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00070010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x000d0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0xd"
        ),

        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, set_attraction_record.name
            ),
            new_instruction_readable="call set_attraction_record"
        ),
    ]
)
porygon_z_quiz_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
        instruction_readable="grow_stack 0xb"
    ),

    Instruction(
        identifier=2, offset=0x2c, pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1"
    ),

    Instruction(
        identifier=3, offset=0x74c, pattern=parse_pattern_bytes("00 c8 00 10"),
        instruction_readable="push 0xc8"
    ),
    Instruction(
        identifier=4, offset=0x754, pattern=parse_pattern_bytes("00 3d 00 10"),
        instruction_readable="push 0x3d"
    )
]
porygon_z_quiz = PatchPattern(
    name="PorygonZ quiz",
    description="sending always location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
            instruction_readable="grow_stack 0xc"
        ),

        Instruction(
            identifier=2, offset=0x2c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

        Instruction(
            identifier=3, offset=0x74c, pattern=parse_pattern_bytes("00 c8 00 10"),
            instruction_readable="push 0xc8"
        ),
        Instruction(
            identifier=4, offset=0x754, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        )

    ],
    patternNA=porygon_z_quiz_patternPALNA,
    patternPAL=porygon_z_quiz_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x4b"  # best friend opcode
        )
    ]
)

STAXIAREA = PatchPattern(
    name="STAXIAREA",
    description="Granite Fast Travels",
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
                GRANITE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # treehouse
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # beach
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # ice
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # cavern
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # magma
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # haunted
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # granite
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update position target based on exit"
        ),

        # flower
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                GRANITE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr06Zn01_Npc_Main_patterns = [
    get_module,
    string_section_start,
    f0601TalkKamex,
    globalManager,
    f0601FireWallB,
    fRuinsGateKey,
    set_chapter,
    get_friendship,
    absol_interaction,
    salamence_interaction,
    furret_interaction,
    arcanine_interaction,
    drifloon_interaction,
    taillow_interaction,
    marowak_interaction,
    baltoy_interaction,
    claydol_interaction,
    togekiss_interaction,
    jirachi_interaction,
    skorupi_interaction,
    porygon_z_quiz,
    A06_Z01_INIT,

    return_at01,
    return_at15,
    get_absol_friendship_location_state,
    get_salamence_friendship_location_state,
    special_spawn_conditions,
    set_attraction_record,
    init_gate_function,

    STAXIAREA,
    battle_counter_handling
]
