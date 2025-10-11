from patcher.helper.patttern_handler import compute_call_to_function_script, create_lstr_script, \
    get_attraction_id_from_dict, \
    get_num_battle_count_from_dict_as_instruction, \
    parse_pattern_bytes, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 34 5a 6e 30 32 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr04Zn02_Npc_Main"
        ),

    ],
)

set_attraction_record = PatchPattern(
    name="set_attraction_record",
    description="set attraction record for each zone option locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 6a 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 14"),
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
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 03 01 06"),
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

trapEventsPatternJP = [
    # TRAPEVENT1
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),

    Instruction(
        identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call camerupt_trap_event"
    ),
    Instruction(
        identifier=3, offset=0x10, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT2
    Instruction(
        identifier=4, offset=0x14, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=5, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call drill_trap_event"
    ),
    Instruction(
        identifier=6, offset=0x24, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT3
    Instruction(
        identifier=7, offset=0x28, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=8, offset=0x2c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call charmander_trap_event"
    ),
    Instruction(
        identifier=9, offset=0x38, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT4
    Instruction(
        identifier=10, offset=0x3c, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=11, offset=0x40, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call meditite_trap_event"
    ),
    Instruction(
        identifier=12, offset=0x4c, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT5
    Instruction(
        identifier=13, offset=0x50, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=14, offset=0x54, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call farfetchd_trap_event"
    ),
    Instruction(
        identifier=15, offset=0x60, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT6
    Instruction(
        identifier=16, offset=0x64, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=17, offset=0x68, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call ???_trap_event"
    ),
    Instruction(
        identifier=18, offset=0x74, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT7
    Instruction(
        identifier=19, offset=0x78, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=20, offset=0x7c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call ???_trap_event"
    ),
    Instruction(
        identifier=21, offset=0x88, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),
]

trapEventsPatchMapJP = [
    Patch(
        identifier=2,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=5,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=8,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=11,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=14,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=17,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=20,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
]

trapEventsPatternPALNA = [
    # TRAPEVENT1
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),

    Instruction(
        identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call camerupt_trap_event"
    ),
    Instruction(
        identifier=3, offset=0x10, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT2
    Instruction(
        identifier=4, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=5, offset=0x20, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call drill_trap_event"
    ),
    Instruction(
        identifier=6, offset=0x2c, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT3
    Instruction(
        identifier=7, offset=0x38, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=8, offset=0x3c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call charmander_trap_event"
    ),
    Instruction(
        identifier=9, offset=0x48, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT4
    Instruction(
        identifier=10, offset=0x54, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=11, offset=0x58, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call meditite_trap_event"
    ),
    Instruction(
        identifier=12, offset=0x64, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT5
    Instruction(
        identifier=13, offset=0x70, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=14, offset=0x74, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call farfetchd_trap_event"
    ),
    Instruction(
        identifier=15, offset=0x80, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT6
    Instruction(
        identifier=16, offset=0x8c, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=17, offset=0x90, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call ???_trap_event"
    ),
    Instruction(
        identifier=18, offset=0x9c, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),

    # TRAPEVENT7
    Instruction(
        identifier=19, offset=0xa8, pattern=parse_pattern_bytes("00 00 00 0b"),
        instruction_readable="load_arg 0x0"
    ),
    Instruction(
        identifier=20, offset=0xac, pattern=parse_pattern_bytes("?? ?? ?? 03"),
        instruction_readable="call ???_trap_event"
    ),
    Instruction(
        identifier=21, offset=0xb8, pattern=parse_pattern_bytes("00 01 00 06"),
        instruction_readable="ret -0x1"
    ),
]

trapEventsPatchMapPALNA = [
    Patch(
        identifier=2,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=5,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=8,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=11,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=14,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=17,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
    Patch(
        identifier=20,
        patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
            4,
            'big'
        ),
        new_instruction_readable="delay(0)"
    ),
]

trap_events = PatchPattern(
    name="Trap Events",
    description="removing Trap Events",
    patternJP=trapEventsPatternJP,
    patternPAL=trapEventsPatternPALNA,
    patternNA=trapEventsPatternPALNA,
    patchMapJP=trapEventsPatchMapJP,
    patchMapPAL=trapEventsPatchMapPALNA,
    patchMapNA=trapEventsPatchMapPALNA
)

rhyperior_interaction = PatchPattern(
    name="rhyperior interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 0b 00 07"),
            instruction_readable="grow_stack 0xb"
        ),
        Instruction(
            identifier=2, offset=0x258,
            pattern=parse_pattern_bytes("00 0c 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=3, offset=0x280,
            pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),
        Instruction(
            identifier=4, offset=0x284,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_prisma_init"
        ),

        Instruction(
            identifier=5, offset=0x324,  # jz target
            pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),
        Instruction(
            identifier=6, offset=0x48C,  # attraction id
            pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 5, matches,
                "jz"
            ),
            new_instruction_readable="jz"
        ),
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
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Magma Zone Circle Area - Rhyperior's Bumper Burn Attraction"
            ),
            new_instruction_readable="update attraction id"
        ),
    ],
)

return_at11_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
        instruction_readable="grow_stack 0x07"
    ),

    Instruction(
        identifier=2, offset=0xd4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
        instruction_readable="lstr f0401ClearDosidon"
    ),
    Instruction(
        identifier=3, offset=0xdc, pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1"
    ),

]

return_at11 = PatchPattern(
    name="return at 11",
    description="bastiodon friendship location",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x07"
        ),

        Instruction(
            identifier=2, offset=0xcc, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0401ClearDosidon"
        ),
        Instruction(
            identifier=3, offset=0xd4, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

    ],
    patternNA=return_at11_patternPALNA,
    patternPAL=return_at11_patternPALNA,
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00750010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x75"  # rhyperior friendship id
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x4b"  # best_friend request opcode
        ),
    ]
)

rhyperior_friendship_event = PatchPattern(
    name="rhyperior friendship event",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),
        Instruction(
            identifier=2, offset=0x38,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=3, offset=0x3c,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0402ClearDosidon"
        ),
        Instruction(
            identifier=4, offset=0x40,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),

        Instruction(
            identifier=5, offset=0x44,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=6, offset=0x48,
            pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay0"
        ),
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
    ],
)

infernape_interaction = PatchPattern(
    name="infernape interaction",
    description="battlecount options",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 0b 00 07"),
            instruction_readable="grow_stack 0xb"
        ),
        Instruction(
            identifier=2, offset=0x30,
            pattern=parse_pattern_bytes("01 16 00 10"),
            instruction_readable="push 0x116"
        ),
        Instruction(
            identifier=3, offset=0xc0,
            pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
        ),
        Instruction(
            identifier=4, offset=0x1b0,
            pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_num_battle_count_from_dict_as_instruction(
                plando_dict
            ),
            new_instruction_readable="set battle count"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: get_num_battle_count_from_dict_as_instruction(
                plando_dict
            ),
            new_instruction_readable="set battle count"
        ),
    ],
)

bonsly_interaction = PatchPattern(
    name="bonsly interaction",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 07 00 10"),
            instruction_readable="push 0x107"
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
            instruction_readable="lstr f0101HideAndSeek"
        ),
        Instruction(
            identifier=6, offset=0x23c, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
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
            identifier=10, offset=0x268, pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=11, offset=0x284, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=12, offset=0x288, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=13, offset=0x28c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 42_00290"
        ),
        Instruction(
            identifier=14, offset=0x290, pattern=parse_pattern_bytes("?? ?? ?? 03"),
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

        # each zone option
        Patch(
            identifier=10,  # not only for each zone option necessary
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x000c0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xc"
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
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

geodude_interaction = PatchPattern(
    name="geodude interaction",
    description="removing hide and seek flag",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("01 0c 00 10"),
            instruction_readable="push 0x10c"
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
            instruction_readable="lstr f0101HideAndSeek"
        ),
        Instruction(
            identifier=6, offset=0x23c, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=7, offset=0x240, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=8, offset=0x244, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # each zone
        Instruction(
            identifier=10, offset=0x268, pattern=parse_pattern_bytes("ff f6 00 0b"),
            instruction_readable="load_arg -0xa"
        ),
        Instruction(
            identifier=11, offset=0x284, pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=12, offset=0x288, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=13, offset=0x28c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 42_00290"
        ),
        Instruction(
            identifier=14, offset=0x290, pattern=parse_pattern_bytes("?? ?? ?? 03"),
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

        # each zone
        Patch(
            identifier=10,  # not only for each zone option necessary
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00100010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x10"
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
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

hitmontop_interaction = PatchPattern(
    name="hitmontop interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 16 00 07"),
            instruction_readable="grow_stack 0x16"
        ),

        Instruction(
            identifier=2, offset=0x50, pattern=parse_pattern_bytes("01 1a 00 10"),
            instruction_readable="push 0x11a"
        ),

        Instruction(
            identifier=3, offset=0x64, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=4, offset=0x4ec, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
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

camerupt_interaction = PatchPattern(
    name="camerupt interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 18 00 10"),
            instruction_readable="push 0x118"
        ),

        Instruction(
            identifier=3, offset=0x50, pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0x94, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
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

special_spawn_conditions = PatchPattern(
    name="special_spawn_conditions",
    description="removing drifblim despawn",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
            instruction_readable="grow_stack 0x3"
        ),

        Instruction(
            identifier=2, offset=0x104, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0301FuwarideTaxiStop"
        ),
        Instruction(
            identifier=3, offset=0x108, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),

        Instruction(
            identifier=4, offset=0x10c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x120, pattern=parse_pattern_bytes("00 02 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=6, offset=0x12c, pattern=parse_pattern_bytes("00 04 00 06"),
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

    ]
)

farfetchd_interaction = PatchPattern(
    name="farfetch'd interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 07"),
            instruction_readable="grow_stack 0xa"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 19 00 10"),
            instruction_readable="push 0x119"
        ),

        Instruction(
            identifier=3, offset=0x50, pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=4, offset=0x94, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
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

chimchar_interaction = PatchPattern(
    name="chimchar interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 0e 00 10"),
            instruction_readable="push 0x10e"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=4, offset=0x25c, pattern=parse_pattern_bytes("00 07 00 10"),
            instruction_readable="push 0x7"
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x000d0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xd"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00070010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

aron_interaction = PatchPattern(
    name="aron interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 0f 00 10"),
            instruction_readable="push 0x10f"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x108, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=4, offset=0x11c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=5, offset=0x120, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x124, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend"
        ),

        Instruction(
            identifier=7, offset=0x190, pattern=parse_pattern_bytes("ff f8 00 0b"),
            instruction_readable="load_arg -0x8"
        ),
        Instruction(
            identifier=8, offset=0x1a4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=9, offset=0x1a8, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=10, offset=0x1ac, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend"
        ),

        Instruction(
            identifier=11, offset=0x218, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=12, offset=0x22c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
        Instruction(
            identifier=13, offset=0x230, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=14, offset=0x234, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_bestfriend"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x000e0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xe"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00070010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x000e0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xe"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00070010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),

        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x000e0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xe"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x00070010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),

    ]
)

torchic_interaction = PatchPattern(
    name="torchic interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 0d 00 10"),
            instruction_readable="push 0x10d"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=4, offset=0x25c, pattern=parse_pattern_bytes("00 3f 00 10"),
            instruction_readable="push 0x3f"
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x000f0010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0xf"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00070010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

baltoy_interaction = PatchPattern(
    name="baltoy interaction",
    description="adding each zone support",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),

        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 08 00 10"),
            instruction_readable="push 0x108"
        ),

        # each zone option
        Instruction(
            identifier=3, offset=0x240, pattern=parse_pattern_bytes("ff f7 00 0b"),
            instruction_readable="load_arg -0x9"
        ),
        Instruction(
            identifier=4, offset=0x25c, pattern=parse_pattern_bytes("00 a3 00 10"),
            instruction_readable="push 0xa3"
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00110010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x11"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00070010).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="push 0x7"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: compute_call_to_function_script(
                offset, data, set_attraction_record
            ) if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="call set_attraction_record"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big') if
            plando_dict["Options"]["each_zone"] else None,
            new_instruction_readable="delay0"
        ),
    ]
)

evAr04Zn02_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    trap_events,
    rhyperior_interaction,
    return_at11,
    rhyperior_friendship_event,
    infernape_interaction,
    bonsly_interaction,
    geodude_interaction,
    hitmontop_interaction,
    farfetchd_interaction,
    chimchar_interaction,
    aron_interaction,
    torchic_interaction,
    baltoy_interaction,

    special_spawn_conditions,
    set_attraction_record
]
