from patcher.helper.patttern_handler import compute_call_to_function_script, create_jmp_instruction_script, \
    create_lstr_script, get_attraction_id_from_dict, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

set_attraction_record = PatchPattern(
    name="set_attraction_record",
    description="set attraction record for each zone option locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 98 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 36 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 15 03 01"),
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
            pattern=parse_pattern_bytes("65 76 41 72 30 36 5a 6e 30 32 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr06Zn02_Npc_Main"
        ),

    ],
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
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Flower Zone Main Area - Rayquaza's Balloon Panic Attraction"
            ),
            new_instruction_readable="update attraction id"
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
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
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
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
            identifier=4, offset=0x254, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x258, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0101HideAndSeek"
        ),
        Instruction(
            identifier=6, offset=0x25c, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=7, offset=0x260, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x264, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        Instruction(
            identifier=9, offset=0x278, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"  # request friendship opcode
        ),

        # each zone
        # each zone option
        Instruction(
            identifier=10, offset=0x288, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=11, offset=0x2a4, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=12, offset=0x2a8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=13, offset=0x2ac, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 62_00270"
        ),
        Instruction(
            identifier=14, offset=0x2b0, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call friendship_banner"
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
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # best friend opcode
        ),

        # each zone option
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x000d0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
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
            identifier=99, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr"
        ),
        Instruction(
            identifier=2, offset=0xec, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0xf0, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),

        Instruction(
            identifier=4, offset=0xf4, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x108, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x114, pattern=parse_pattern_bytes("00 04 00 06"),
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
        Patch(
            identifier=99,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x4"
        ),
    ]
)

special_spawn_conditions2 = PatchPattern(
    name="special_spawn_conditions2",
    description="removing drifblim despawn",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),
        Instruction(
            identifier=99, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr"
        ),
        Instruction(
            identifier=2, offset=0x118, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0x11c, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),

        Instruction(
            identifier=4, offset=0x120, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x134, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x140, pattern=parse_pattern_bytes("00 04 00 06"),
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
        Patch(
            identifier=99,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040006).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="ret -0x4"
        ),
    ]
)

bellosom_interaction = PatchPattern(
    name="bellosom interaction",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x3c, pattern=parse_pattern_bytes("01 d5 00 10"),
            instruction_readable="push 0x1d5"
        ),
        Instruction(
            identifier=3, offset=0x7c, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),

        Instruction(
            identifier=4, offset=0x280, pattern=parse_pattern_bytes("00 00 00 11 3f 80 00 00"),
            instruction_readable="push_imm 0x3f800000"
        ),
        Instruction(
            identifier=5, offset=0x2f4, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"  # request friendship opcode
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 4, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),

    ]
)

set_items = PatchPattern(
    name="set items flower zone",
    description="used for call in init",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),

        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("2a fd 00 10"),
            instruction_readable="push 0x2afd"
        ),
        Instruction(
            identifier=3, offset=0xb4, pattern=parse_pattern_bytes("00 06 00 06"),
            instruction_readable="ret -0x6"
        ),

    ],
    patchMapJP=[
    ]
)

ar06zn02_init_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
        instruction_readable="grow_stack 0x2"
    ),

    Instruction(
        identifier=2, offset=0x44, pattern=parse_pattern_bytes("4e 20 00 10"),
        instruction_readable="push 0x4e20"
    ),
    Instruction(
        identifier=3, offset=0x50, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=4, offset=0x54, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call fun_??????"
    ),
]

ar06zn02_init = PatchPattern(
    name="ar06zn02_init",
    description="adding set_items call",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x3c, pattern=parse_pattern_bytes("4e 20 00 10"),
            instruction_readable="push 0x4e20"
        ),
        Instruction(
            identifier=3, offset=0x48, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=4, offset=0x4c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call fun_??????"
        ),
    ],
    patternPAL=ar06zn02_init_patternPALNA,
    patternNA=ar06zn02_init_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_items
            ),
            new_instruction_readable="call set_items"
        ),
    ]
)

mareep_interaction = PatchPattern(
    name="mareep interaction",
    description="removing chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x18, pattern=parse_pattern_bytes("01 d6 00 10"),
            instruction_readable="push 0x1d6"
        ),
        Instruction(
            identifier=3, offset=0x64, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),

        Instruction(
            identifier=4, offset=0x104, pattern=parse_pattern_bytes("ff fb 00 0b"),  # jmp target
            instruction_readable="load_arg -0x5"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 4, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

teddiursa_interaction = PatchPattern(
    name="teddiursa interaction",
    description="adding each zone option support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x18, pattern=parse_pattern_bytes("01 da 00 10"),
            instruction_readable="push 0x1da"
        ),

        Instruction(
            identifier=3, offset=0x280, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
        # each zone option

        Instruction(
            identifier=4, offset=0x290, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=5, offset=0x2ac, pattern=parse_pattern_bytes("00 a2 00 10"),
            instruction_readable="push 0xa2"
        ),
        Instruction(
            identifier=6, offset=0x2b0, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=7, offset=0x2b4, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
        Instruction(
            identifier=8, offset=0x2b8, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x4b"  # get bestfriend opcode
        ),

        # each zone option
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x000d0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

meditite_quizPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
        instruction_readable="grow_stack 0xb"
    ),

    Instruction(
        identifier=2, offset=0x14, pattern=parse_pattern_bytes("01 e1 00 10"),
        instruction_readable="push 0x1e1"
    ),

    # each zone option

    Instruction(
        identifier=3, offset=0x760, pattern=parse_pattern_bytes("ff f5 00 0b"),
        instruction_readable="load_arg -0xb"
    ),
    Instruction(
        identifier=4, offset=0x788, pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr 62_00340"
    ),
    Instruction(
        identifier=5, offset=0x78c, pattern=parse_pattern_bytes("ff fe 00 0b"),
        instruction_readable="load_arg -0x2"
    ),
    Instruction(
        identifier=6, offset=0x790, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call set_friendship+dialog"
    ),

]

meditite_quiz = PatchPattern(
    name="meditite quiz",
    description="adding each zone option support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
            instruction_readable="grow_stack 0xc"
        ),

        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("01 e1 00 10"),
            instruction_readable="push 0x1e1"
        ),

        # each zone option

        Instruction(
            identifier=3, offset=0x760, pattern=parse_pattern_bytes("ff f5 00 0b"),
            instruction_readable="load_arg -0xb"
        ),
        Instruction(
            identifier=4, offset=0x788, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 62_00340"
        ),
        Instruction(
            identifier=5, offset=0x78c, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=6, offset=0x790, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship+dialog"
        ),

    ],
    patternNA=meditite_quizPALNA,
    patternPAL=meditite_quizPALNA,
    patchMapJP=[

        # each zone option
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x3"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x000d0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        )
    ]
)

evAr06Zn02_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    mareep_interaction,
    teddiursa_interaction,
    rayquaza_interaction,
    furret_interaction,
    meditite_quiz,

    return_at02,
    rayquaza_friendship_event,
    get_rayquaza_friendship_location_state,
    special_spawn_conditions,
    special_spawn_conditions2,
    bellosom_interaction,
    ar06zn02_init,
    set_attraction_record
]
