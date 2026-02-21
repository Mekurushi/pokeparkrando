from patcher.helper.entrance_exit_names import BEACH_ZONE_LAPRAS_AREA_BEACH_ZONE_LAPRAS, \
    BEACH_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, BEACH_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, \
    BEACH_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, \
    BEACH_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, \
    BEACH_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, \
    BEACH_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, BEACH_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, \
    BEACH_ZONE_MAIN_AREA_PELIPPER_ATTRACTION, \
    BEACH_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, BEACH_ZONE_RECYCLE_AREA_GYARADOS_ATTRACTION
from patcher.helper.patttern_handler import get_attraction_id_from_dict, get_exit_zone_area_position_data, \
    parse_pattern_bytes, \
    create_jmp_instruction_script, create_lstr_script, \
    compute_call_to_function_script
from patcher.models.models import Instruction, PatchPattern, Patch
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 33 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr03Zn01_Npc_Main"
        ),

    ],
)

fBippasWoodLevel = PatchPattern(
    name="ds fBippasWoodLevel",
    description="using fBippasWoodLevel for lstr instructions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 42 69 70 70 61 73 57 6f 6f 64 4c 65 76 65 6c 00"),
            instruction_readable="ds fBippasWoodLevel"
        ),

    ]
)

set_bestfriend = PatchPattern(
    name="set_bestfriend functopm",
    description="using set_bestfriends to replace friendship flags",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),
        Instruction(
            identifier=2, offset=0x44,
            pattern=parse_pattern_bytes("00 4a 00 10"),
            instruction_readable="push 0x4a"
        ),
        Instruction(
            identifier=3, offset=0x4c,
            pattern=parse_pattern_bytes("00 04 00 06"),
            instruction_readable="ret -0x4"
        ),
    ]
)

custom_prisma_check_function = PatchPattern(
    name="unused code space",
    description="Modifing gate Logic",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 02 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 10"),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_script(
                data, string_section_start,
                globalManager
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data,
                get_module
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x0000000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg 0x0"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00510010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x51"
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

eEvent02090 = PatchPattern(
    name="eEvent02090",
    description="eEvent02090",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 1b 00 07"),
            instruction_readable="grow_stack 0xe"
        ),

        Instruction(
            identifier=2, offset=0x870, pattern=parse_pattern_bytes("08 34 00 10"),
            instruction_readable="push 0x834"
        ),
        Instruction(
            identifier=3, offset=0x874, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
        ),

        Instruction(
            identifier=4, offset=0x460, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay 0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay 0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay 0"
        ),
    ]
)

bidoof_quest_condition = PatchPattern(
    name="bidoof_bridge_quest_condition",
    description="Init of Bidoof bridge quest condition to be Pelipper Prisma not chapter",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
            instruction_readable="grow_stack 0xe"
        ),

        # condition
        Instruction(
            identifier=2, offset=0x3a4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301BippaFlag"
        ),
        Instruction(
            identifier=3, offset=0x3a8, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=4, offset=0x3ac, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x3b0, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        Instruction(
            identifier=6, offset=0x33c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301BippaFlag"
        ),
        Instruction(
            identifier=7, offset=0x340, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=8, offset=0x344, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=9, offset=0x348, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),

        Instruction(
            identifier=10, offset=0x35c, pattern=parse_pattern_bytes("00 00 00 11"),
            instruction_readable="push imm part1"
        ),
        Instruction(
            identifier=11, offset=0x360, pattern=parse_pattern_bytes("3f 80 00 00"),
            instruction_readable="push imm part2"
        ),
        Instruction(
            identifier=12, offset=0x364, pattern=parse_pattern_bytes("00 00 00 11"),
            instruction_readable="push imm part1"
        ),
        Instruction(
            identifier=13, offset=0x368, pattern=parse_pattern_bytes("3f 80 00 00"),
            instruction_readable="push imm part2"
        ),
        Instruction(
            identifier=14, offset=0x36c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=15, offset=0x370, pattern=parse_pattern_bytes("0a 40 00 10"),
            instruction_readable="push 0xa40"
        ),
        Instruction(
            identifier=16, offset=0x374, pattern=parse_pattern_bytes("ff f3 00 0b"),
            instruction_readable="load_arg -0xd"
        ),
        Instruction(
            identifier=17, offset=0x378, pattern=parse_pattern_bytes("00 28 00 10"),
            instruction_readable="push 0x28"
        ),
        Instruction(
            identifier=18, offset=0x37c, pattern=parse_pattern_bytes("00 15 06 01"),
            instruction_readable="SC6 0x0:0x15"
        ),
        Instruction(
            identifier=19, offset=0x380, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        # end of specific interaction
        Instruction(
            identifier=20, offset=0x414, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call"
        ),

        # end of complete bidoof
        Instruction(
            identifier=21, offset=0xacc, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="ret"
        ),

        Instruction(
            identifier=22, offset=0x580, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_script(
                data, string_section_start, fBippasWoodLevel
            ),
            new_instruction_readable="lstr fBippasWoodLevel"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffd000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg -0x3"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x1"
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
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 20,
                patch_patterns, pattern_name, "jnz"
            ),
            new_instruction_readable="jnz"
        ),

        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x0000000b).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data, eEvent02090
            ),
            new_instruction_readable="call event"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 21, patch_patterns, pattern_name
            ),
            new_instruction_readable="call event"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00060010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x6"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00510010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x51"
        ),

        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x1"
        ),
    ]
)

piplup_interaction = PatchPattern(
    name="piplup interaction",
    description="replacing piplup friendship flag with bestfriend",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 6b 00 10"),
            instruction_readable="push 0x6b"
        ),

        # opcode of friendship request
        Instruction(
            identifier=3, offset=0x2c4, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),

        # set_friendship
        Instruction(
            identifier=4, offset=0x2f4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
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
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data, set_bestfriend
            ),
            new_instruction_readable="call set_bestfriend"
        ),

    ]
)

# hide and seek using flag interactions

psyduck_interaction = PatchPattern(
    name="psyduck interaction",
    description="removing psyduck hide and seek flag usage",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        # hide and seek request branch
        Instruction(
            identifier=2, offset=0x190, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=3, offset=0x1a0, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 31_10240"
        ),

        # set hide and seek
        Instruction(
            identifier=4, offset=0x250, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x254, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0101HideAndSeek"
        ),
        Instruction(
            identifier=6, offset=0x258, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=7, offset=0x25c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x260, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        Instruction(
            identifier=9, offset=0x274, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 3, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay0"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
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

mudkip_interaction = PatchPattern(
    name="mudkip interaction",
    description="removing mudkip hide and seek flag usage",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        # hide and seek request branch
        Instruction(
            identifier=2, offset=0x164, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=3, offset=0x174, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 31_11240"
        ),

        # set hide and seek
        Instruction(
            identifier=4, offset=0x224, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x228, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0101HideAndSeek"
        ),
        Instruction(
            identifier=6, offset=0x22c, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=7, offset=0x230, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x234, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        Instruction(
            identifier=9, offset=0x248, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 3, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay0"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
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

feraligatr_interaction = PatchPattern(
    name="feraligatr interaction",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
            instruction_readable="grow_stack 0xe"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 85 00 10"),
            instruction_readable="push 0x85"
        ),
        Instruction(
            identifier=3, offset=0x38, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0x3c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
        Patch(
            identifier=4,  # pushing 0x900 so only wanted chapter logic triggers
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x09000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
    ]
)

# attraction pokemon
pelipper_interaction = PatchPattern(
    name="pelipper interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
            instruction_readable="grow_stack 0xe"
        ),

        Instruction(
            identifier=2, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get chapter"
        ),
        Instruction(
            identifier=3, offset=0x1d0, pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=4, offset=0x1e0, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=5, offset=0x3e4, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        Instruction(
            identifier=6, offset=0x470, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call getattractionpokemonfriendships"
        ),
        Instruction(
            identifier=7, offset=0x474, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=8, offset=0x538, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),

        Instruction(
            identifier=9, offset=0x5c4, pattern=parse_pattern_bytes("00 06 00 10"),  # attraction id
            instruction_readable="push 0x6"
        ),

        Instruction(
            identifier=10, offset=0x668, pattern=parse_pattern_bytes("00 06 00 10"),
            instruction_readable="push 0x6"
        ),
        Instruction(
            identifier=11, offset=0x744, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 3, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 5, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                # allows always
                # entering attraction
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                # allows always
                # entering attraction
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),

        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, BEACH_ZONE_MAIN_AREA_PELIPPER_ATTRACTION
            ),
            new_instruction_readable="update attraction id"
        ),

        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 11, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
    ]
)

returnAt07_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
        instruction_readable="grow_stack 0x8"
    ),

    Instruction(
        identifier=2, offset=0xcc, pattern=parse_pattern_bytes("ff fa 00 0b"),
        instruction_readable="load_arg -0x6"
    ),
    Instruction(
        identifier=3, offset=0xd0, pattern=parse_pattern_bytes("07 da 00 10"),
        instruction_readable="load_arg -0x6"
    ),
    Instruction(
        identifier=4, offset=0xd4, pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=5, offset=0xd8, pattern=parse_pattern_bytes("00 09 06 08"),
        instruction_readable="jzSet"
    ),
    Instruction(
        identifier=6, offset=0xdc, pattern=parse_pattern_bytes("4e 3b 00 10"),
        instruction_readable="push 0x4e3b"
    ),

    Instruction(
        identifier=7, offset=0xe0, pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=8, offset=0xe4, pattern=parse_pattern_bytes("00 0a 00 10"),
        instruction_readable="push 0xa"
    ),

    Instruction(  # jump target
        identifier=9, offset=0x294, pattern=parse_pattern_bytes("00 04 00 10"),
        instruction_readable="push 0x4"
    ),
    Instruction(  # chapter condition
        identifier=10, offset=0x2c4, pattern=parse_pattern_bytes("08 20 00 10"),
        instruction_readable="push 0x820"
    ),

]

return_at7 = PatchPattern(
    name="pelipper return attraction event",
    description="prep for pelipper friendship location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0xc4, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=3, offset=0xc8, pattern=parse_pattern_bytes("07 da 00 10"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=4, offset=0xcc, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=5, offset=0xd0, pattern=parse_pattern_bytes("00 09 06 08"),
            instruction_readable="jzSet"
        ),
        Instruction(
            identifier=6, offset=0xd4, pattern=parse_pattern_bytes("4e 3b 00 10"),
            instruction_readable="push 0x4e3b"
        ),

        Instruction(
            identifier=7, offset=0xd8, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=8, offset=0xdc, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        Instruction(  # jump target
            identifier=9, offset=0x28c, pattern=parse_pattern_bytes("00 04 00 10"),
            instruction_readable="push 0x4"
        ),
        Instruction(  # chapter condition
            identifier=10, offset=0x2bc, pattern=parse_pattern_bytes("08 20 00 10"),
            instruction_readable="push 0x820"
        ),
    ],
    patternPAL=returnAt07_patternPALNA,
    patternNA=returnAt07_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x005a0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x5a"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"  # Global Manager
        ),

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # request best friend pelipper (location flag)
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150301).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffa000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x6"
        ),

        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 9, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"  # only enter when best friend is 0
        ),
    ]
)

pelipper_friendship_event = PatchPattern(
    name="pelipper friendship event",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
            instruction_readable="grow_stack 0xb"
        ),

        Instruction(
            identifier=2, offset=0x24, pattern=parse_pattern_bytes("00 87 00 10"),
            instruction_readable="push 0x87"
        ),
        Instruction(
            identifier=3, offset=0x2b4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),

    ]
)

gyarados_interaction = PatchPattern(
    name="gyarados interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x38, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get chapter"
        ),
        Instruction(
            identifier=3, offset=0x194, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=4, offset=0x1ec, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr fSeaTalkGyarados"
        ),
        Instruction(
            identifier=5, offset=0x420, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        Instruction(
            identifier=6, offset=0x4ac, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call getattractionpokemonfriendships"
        ),
        Instruction(
            identifier=7, offset=0x4b0, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=9, offset=0x5b0, pattern=parse_pattern_bytes("00 05 00 10"),  # attraction id
            instruction_readable="push 0x5"
        ),

        Instruction(
            identifier=10, offset=0x64c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=11, offset=0x718, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 3, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 5, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                # allows always
                # entering attraction
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),

        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, BEACH_ZONE_RECYCLE_AREA_GYARADOS_ATTRACTION
            ),
            new_instruction_readable="update attraction id"
        ),

        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 11, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
    ]
)

returnAt06_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
        instruction_readable="grow_stack 0x8"
    ),

    Instruction(
        identifier=2, offset=0xcc, pattern=parse_pattern_bytes("ff fa 00 0b"),
        instruction_readable="load_arg -0x6"
    ),
    Instruction(
        identifier=3, offset=0xd0, pattern=parse_pattern_bytes("07 da 00 10"),
        instruction_readable="load_arg -0x6"
    ),
    Instruction(
        identifier=4, offset=0xd4, pattern=parse_pattern_bytes("00 0b 00 16"),
        instruction_readable="eq"
    ),
    Instruction(
        identifier=5, offset=0xd8, pattern=parse_pattern_bytes("00 09 06 08"),
        instruction_readable="jzSet"
    ),
    Instruction(
        identifier=6, offset=0xdc, pattern=parse_pattern_bytes("4e 3b 00 10"),
        instruction_readable="push 0x4e3b"
    ),

    Instruction(
        identifier=7, offset=0xe0, pattern=parse_pattern_bytes("ff fd 00 0b"),
        instruction_readable="load_arg -0x3"
    ),
    Instruction(
        identifier=8, offset=0xe4, pattern=parse_pattern_bytes("00 0a 00 10"),
        instruction_readable="push 0xa"
    ),

    Instruction(  # jump target
        identifier=9, offset=0x294, pattern=parse_pattern_bytes("00 04 00 10"),
        instruction_readable="push 0x4"
    ),
    Instruction(  # chapter condition
        identifier=10, offset=0x2c4, pattern=parse_pattern_bytes("08 48 00 10"),
        instruction_readable="push 0x848"
    ),

]

return_at6 = PatchPattern(
    name="gyarados return attraction event",
    description="prep for gyarados friendship location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0xc4, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=3, offset=0xc8, pattern=parse_pattern_bytes("07 da 00 10"),
            instruction_readable="push 0x7da"
        ),
        Instruction(
            identifier=4, offset=0xcc, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=5, offset=0xd0, pattern=parse_pattern_bytes("00 09 06 08"),
            instruction_readable="jzSet"
        ),
        Instruction(
            identifier=6, offset=0xd4, pattern=parse_pattern_bytes("4e 3b 00 10"),
            instruction_readable="push 0x4e3b"
        ),

        Instruction(
            identifier=7, offset=0xd8, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=8, offset=0xdc, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        Instruction(  # jump target
            identifier=9, offset=0x28c, pattern=parse_pattern_bytes("00 04 00 10"),
            instruction_readable="push 0x4"
        ),
        Instruction(  # chapter condition
            identifier=10, offset=0x2bc, pattern=parse_pattern_bytes("08 48 00 10"),
            instruction_readable="push 0x848"
        ),
    ],
    patternPAL=returnAt06_patternPALNA,
    patternNA=returnAt06_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00350010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x35"  # gyarados friendship id
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"  # Global Manager
        ),

        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # request best friend pelipper (location flag)
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00150301).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0xfffa000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x6"
        ),

        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 9, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"  # only enter when best friend is 0
        ),
    ]
)

gyarados_friendship_event = PatchPattern(
    name="gyarados friendship event",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x24, pattern=parse_pattern_bytes("00 88 00 10"),
            instruction_readable="push 0x88"
        ),
        Instruction(
            identifier=3, offset=0x288, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_chapter"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),

    ]
)

special_spawn_conditions = PatchPattern(
    name="special_spawn_conditions",
    description="removing drifblim despawn",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),

        Instruction(
            identifier=2, offset=0x210, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0x214, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),

        Instruction(
            identifier=4, offset=0x218, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x22c, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x238, pattern=parse_pattern_bytes("00 07 00 06"),
            instruction_readable="ret -0x7"
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

wailord_interaction = PatchPattern(
    name="wailord interaction",
    description="making wailord quest doable",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 7d 00 10"),
            instruction_readable="push 0x7d"
        ),

        Instruction(
            identifier=3, offset=0x104, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=4, offset=0x108, pattern=parse_pattern_bytes("00 03 00 10"),
            instruction_readable="push 0x3"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00030010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x3"
        ),

    ]
)

set_attraction_record = PatchPattern(
    name="set_attraction_record",
    description="set attraction record for each zone option locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 05 00 10"),
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
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff fe 00 0c"),
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
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 02 01 06"),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_script(
                data, string_section_start,
                globalManager
            ),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data,
                get_module
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

starly_interaction = PatchPattern(
    name="starly interaction beach zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 72 00 10"),
            instruction_readable="push 0x72"
        ),

        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),

        Instruction(
            identifier=4, offset=0x25c, pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=5, offset=0x260, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
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
                                  pattern_name: compute_call_to_function_script(
                offset, data, set_attraction_record
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

starly2_interaction = PatchPattern(
    name="starly2 interaction beach zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 8f 00 10"),
            instruction_readable="push 0x8f"
        ),

        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),

        Instruction(
            identifier=4, offset=0x25c, pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=5, offset=0x260, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
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
                                  pattern_name: compute_call_to_function_script(
                offset, data, set_attraction_record
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

starly3_interaction = PatchPattern(
    name="starly3 interaction beach zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 90 00 10"),
            instruction_readable="push 0x90"
        ),

        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),

        Instruction(
            identifier=4, offset=0x25c, pattern=parse_pattern_bytes("00 2e 00 10"),
            instruction_readable="push 0x2e"
        ),
        Instruction(
            identifier=5, offset=0x260, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
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
                                  pattern_name: compute_call_to_function_script(
                offset, data, set_attraction_record
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

spearow_interaction = PatchPattern(
    name="spearow interaction beach zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 94 00 10"),
            instruction_readable="push 0x94"
        ),

        Instruction(
            identifier=3, offset=0x174, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=4, offset=0x184, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 31_13760"
        ),
        Instruction(
            identifier=5, offset=0x188, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=6, offset=0x18c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call dialog"
        ),
        Instruction(
            identifier=7, offset=0x190, pattern=parse_pattern_bytes("?? ?? ?? 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=8, offset=0x23c, pattern=parse_pattern_bytes("?? ?? ?? 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=9, offset=0x24c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="cal FUN_??????"
        ),
        Instruction(
            identifier=10, offset=0x238, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="cal set_bestfriend"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x1"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x000d0010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 9, patch_patterns, pattern_name,
                "jmp"
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 4, patch_patterns, pattern_name,
                "jmp"
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

spearow2_interaction = PatchPattern(
    name="spearow2 interaction beach zone",
    description="added support for each zone option",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # model id
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("00 73 00 10"),
            instruction_readable="push 0x73"
        ),

        Instruction(
            identifier=3, offset=0x174, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=4, offset=0x184, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 31_13760"
        ),
        Instruction(
            identifier=5, offset=0x188, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=6, offset=0x18c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call dialog"
        ),
        Instruction(
            identifier=7, offset=0x190, pattern=parse_pattern_bytes("?? ?? ?? 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=8, offset=0x23c, pattern=parse_pattern_bytes("?? ?? ?? 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=9, offset=0x24c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="cal FUN_??????"
        ),
        Instruction(
            identifier=10, offset=0x238, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="cal set_bestfriend"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x1"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x000d0010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 9, patch_patterns, pattern_name,
                "jmp"
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 4, patch_patterns, pattern_name,
                "jmp"
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

ELAPLACEAREA = PatchPattern(
    name="ELAPLACEAREA",
    description="Beach Zone -> Ice Zone Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),
        Instruction(
            identifier=2, offset=0x40,  # position
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=3, offset=0x44,  # area
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
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
                BEACH_ZONE_LAPRAS_AREA_BEACH_ZONE_LAPRAS, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_LAPRAS_AREA_BEACH_ZONE_LAPRAS, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_LAPRAS_AREA_BEACH_ZONE_LAPRAS, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

STAXIAREA = PatchPattern(
    name="STAXIAREA",
    description="Beach Fast Travels",
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
                BEACH_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # treehouse
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # beach
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: None,
            new_instruction_readable="update position target based on exit"
        ),

        # ice
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # cavern
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # magma
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # haunted
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # granite
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),

        # flower
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                BEACH_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr03Zn01_Npc_Main_pattern = [
    set_chapter,
    get_friendship,
    # bidoof_quest_condition,
    # eEvent02090,
    # custom_prisma_check_function
    piplup_interaction,
    psyduck_interaction,
    mudkip_interaction,
    feraligatr_interaction,
    wailord_interaction,
    starly_interaction,
    starly2_interaction,
    starly3_interaction,
    spearow_interaction,
    spearow2_interaction,

    return_at7,
    return_at6,
    pelipper_interaction,
    pelipper_friendship_event,

    gyarados_interaction,
    gyarados_friendship_event,
    special_spawn_conditions,
    set_attraction_record,

    ELAPLACEAREA,
    STAXIAREA
]
