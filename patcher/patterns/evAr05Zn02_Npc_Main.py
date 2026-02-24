from patcher.helper.entrance_exit_names import HAUNTED_ZONE_MANSION_AREA_DUSKNOIR_ATTRACTION
from patcher.helper.patttern_handler import compute_call_instruction_fsb, compute_jmp_instruction_fsb, \
    create_lstr_instruction_fsb, \
    get_attraction_id_from_dict, get_num_battle_count_from_dict_as_instruction, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

set_attraction_record = PatchPattern(
    name="set_attraction_record",
    description="set attraction record for each zone option locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 0e 00 08"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 2a 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 0b 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 33 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 08 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("ff f7 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 05 00 08"),
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
            pattern=parse_pattern_bytes("65 76 41 72 30 35 5a 6e 30 32 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr05Zn02_Npc_Main"
        ),

    ],
)

f0502DoorA = PatchPattern(
    name="ds f0502DoorA",
    description="using f0502DoorA for lstr instructions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("66 30 35 30 32 44 6f 6f 72 41 00"),
            instruction_readable="ds f0502DoorA"
        ),

    ]
)

dusknoir_interaction = PatchPattern(
    name="dusknoir interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 16 00 07"),
            instruction_readable="grow_stack 0x16"
        ),
        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("01 81 00 10"),
            instruction_readable="push 0x181"
        ),

        Instruction(
            identifier=3, offset=0x50, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=4, offset=0x498, pattern=parse_pattern_bytes("00 04 00 10"),  # attraction id
            instruction_readable="push 0x4"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"  # always skipping init phase
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, HAUNTED_ZONE_MANSION_AREA_DUSKNOIR_ATTRACTION
            ),
            new_instruction_readable="update attraction id"
        ),

    ]
)

get_dusknoir_friendship_location_state = PatchPattern(
    name="dusknoir friendship location state",
    description="get bestfriend for dusknoir",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
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
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 28 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 15 03 01"),
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
            new_instruction_readable="grow_stack 0x1"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00ba0010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0xba"  # dusknoir friendship id
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

return_at05_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
        instruction_readable="grow_stack 0x7"
    ),
    Instruction(
        identifier=2, offset=0x84, pattern=parse_pattern_bytes("01 81 00 10"),
        instruction_readable="push 0x181"
    ),
    Instruction(
        identifier=3, offset=0xe4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call FUN_??????"
    ),
    Instruction(
        identifier=4, offset=0xe8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call get_chapter"
    ),
    Instruction(
        identifier=5, offset=0x13c, pattern=parse_pattern_bytes("1b b2 00 10"),
        instruction_readable="push 0x1bb2"
    ),

]

return_at05 = PatchPattern(
    name="return_at05",
    description="return attraction 05",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0x7c, pattern=parse_pattern_bytes("01 81 00 10"),
            instruction_readable="push 0x181"
        ),

        Instruction(
            identifier=3, offset=0xdc, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=4, offset=0xe0, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),

        Instruction(
            identifier=5, offset=0x134, pattern=parse_pattern_bytes("1b b2 00 10"),
            instruction_readable="push 0x1bb2"
        ),

    ],
    patternPAL=return_at05_patternPALNA,
    patternNA=return_at05_patternPALNA,
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"  # this somehow fixes the dusknoir crash
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, get_dusknoir_friendship_location_state.name
            ),
            new_instruction_readable="call get_dusknoir_friendship"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
    ]
)

dusknoir_friendship_event = PatchPattern(
    name="dusknoir_friendship_event",
    description="remove unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
            instruction_readable="grow_stack 0xe"
        ),
        Instruction(
            identifier=2, offset=0x20c, pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),

        Instruction(
            identifier=3, offset=0x210, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0502TalkYonoir"
        ),
        Instruction(
            identifier=4, offset=0x214, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=5, offset=0x218, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=6, offset=0x21c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
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
    ]
)

spinarak_interaction = PatchPattern(
    name="spinarak interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0f 00 07"),
            instruction_readable="grow_stack 0xf"
        ),
        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 77 00 10"),
            instruction_readable="push 0x177"
        ),

        Instruction(
            identifier=3, offset=0x110, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),

        Instruction(
            identifier=4, offset=0x114, pattern=parse_pattern_bytes("1b f8 00 10"),
            instruction_readable="push 0x1bf8"
        ),
        Instruction(
            identifier=5, offset=0x98, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
    ]
)

elekid_interaction = PatchPattern(
    name="elekid interaction",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 72 00 10"),
            instruction_readable="push 0x172"
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
    ]
)

luxray_interaction = PatchPattern(
    name="luxray interaction",
    description="updating wincounter with options",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 7d 00 10"),
            instruction_readable="push 0x17d"
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

are_doors_unlocked = PatchPattern(
    name="unused code space",
    description="ap logic are doors unlocked state",
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
                patch_patterns, string_section_start.name, f0502DoorA.name
            ),
            new_instruction_readable="lstr f0502DoorA"
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

prepare_chase_ai = PatchPattern(
    name="fix_chase_ai_haunted_zone",
    description="updating wincounter with options",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr Globalmanager"
        ),

        Instruction(
            identifier=3, offset=0x14, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=4, offset=0x18, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="store_arg -0x2"
        ),
        Instruction(
            identifier=5, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=6, offset=0x20, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="store_arg -0x3"
        ),
        Instruction(
            identifier=7, offset=0x24, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x28, pattern=parse_pattern_bytes("ff fc 00 0c"),
            instruction_readable="store_arg -0x4"
        ),
        Instruction(
            identifier=9, offset=0x2c, pattern=parse_pattern_bytes("?? ?? ?? 19"),
            instruction_readable="lea"
        ),
        Instruction(
            identifier=10, offset=0x30, pattern=parse_pattern_bytes("?? ?? ?? 1a"),
            instruction_readable="lw"
        ),
        Instruction(
            identifier=11, offset=0x34, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=12, offset=0x38, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=13, offset=0x3c, pattern=parse_pattern_bytes("00 00 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=14, offset=0x40, pattern=parse_pattern_bytes("00 06 00 06"),
            instruction_readable="ret -0x6"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_call_instruction_fsb(
                offset, patch_patterns, are_doors_unlocked.name
            ),
            new_instruction_readable="call are_doors_unlocked"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: compute_jmp_instruction_fsb(
                offset, 12, patch_patterns, pattern_name,
                "jz"
            ),
            new_instruction_readable="jz"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00050010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x5"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00020010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00050010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x5"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x002d0010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x2d"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00060006).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="ret -0x6"
        ),
    ]
)

abra_interaction = PatchPattern(
    name="abra interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 73 00 10"),
            instruction_readable="push 0x173"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x7c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0xc0, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 52_00310"
        ),
        Instruction(
            identifier=5, offset=0xc4, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=6, offset=0xc8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship+"
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00160010).to_bytes(
                4, 'big'
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x16"
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

    ]
)

misdreavus_interaction = PatchPattern(
    name="misdreavus interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 23 00 07"),
            instruction_readable="grow_stack 0x23"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 6f 00 10"),
            instruction_readable="push 0x16f"
        ),

        Instruction(
            identifier=3, offset=0xac, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x1bf80010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1bf8"
        ),

    ]
)

sable_quiz_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
        instruction_readable="grow_stack 0xb"
    ),

    Instruction(
        identifier=2, offset=0x4, pattern=parse_pattern_bytes("01 80 00 10"),
        instruction_readable="push 0x180"
    ),

    Instruction(
        identifier=3, offset=0x970, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call give_book"
    ),
]

sableye_quiz = PatchPattern(
    name="sableye quiz",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
            instruction_readable="grow_stack 0xc"
        ),

        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("01 80 00 10"),
            instruction_readable="push 0x180"
        ),

        Instruction(
            identifier=3, offset=0x970, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call give_book"
        ),
    ],
    patternPAL=sable_quiz_patternPALNA,
    patternNA=sable_quiz_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        )
    ]
)

sableye_interaction = PatchPattern(
    name="sableye interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0f 00 07"),
            instruction_readable="grow_stack 0xf"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 80 00 10"),
            instruction_readable="push 0x180"
        ),

        Instruction(
            identifier=3, offset=0x168, pattern=parse_pattern_bytes("00 00 00 12"),
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

darkrai_interaction = PatchPattern(
    name="darkrai interaction",
    description="modified behavior for darkrai location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 82 00 10"),
            instruction_readable="push 0x182"
        ),

        Instruction(
            identifier=3, offset=0x90, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x1d4, pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=5, offset=0x1f0, pattern=parse_pattern_bytes("?? ?? ?? 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=6, offset=0x1f4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 52_12380"
        ),
        Instruction(
            identifier=7, offset=0x1f8, pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=8, offset=0x1fc, pattern=parse_pattern_bytes("?? ?? ?? 03"),
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
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00060010).to_bytes(
                4, 'big'
            ),
            new_instruction_readable="push 0x6"
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
mismagius_interaction = PatchPattern(
    name="mismagius interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 7c 00 10"),
            instruction_readable="push 0x17c"
        ),

        Instruction(
            identifier=3, offset=0x58, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x1c340010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1c34"
        ),

    ]
)

evAr05Zn02_Npc_Main_patterns = [
    get_module,
    string_section_start,
    f0502DoorA,
    globalManager,
    set_chapter,
    get_friendship,
    dusknoir_interaction,
    abra_interaction,
    misdreavus_interaction,
    mismagius_interaction,
    return_at05,
    dusknoir_friendship_event,
    get_dusknoir_friendship_location_state,
    spinarak_interaction,
    elekid_interaction,
    luxray_interaction,
    sableye_interaction,
    sableye_quiz,
    darkrai_interaction,
    prepare_chase_ai,
    are_doors_unlocked,
    set_attraction_record
]
