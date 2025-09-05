from patcher.helper.patttern_handler import get_num_battle_count_from_dict_as_instruction, parse_pattern_bytes, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch

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
            instruction_readable="push 0xa0"
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

evAr04Zn02_Npc_Main_patterns = [
    trap_events,
    rhyperior_interaction,
    return_at11,
    rhyperior_friendship_event,
    infernape_interaction,
    bonsly_interaction,
    geodude_interaction,
]
