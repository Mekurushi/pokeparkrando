from patcher.helper.patttern_handler import compute_bl_to_function_script, create_lstr_script, \
    get_attraction_id_from_dict, parse_pattern_bytes, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch
from patcher.patterns.general import get_friendship, get_module, globalManager, set_chapter

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
            patch_function=lambda offset, data, plando_dict, matches: (
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
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 3, matches),
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 5,
                matches, "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: get_attraction_id_from_dict(
                plando_dict, "Haunted Zone Main Area - Tangrowth's Swing-Along Attraction"
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
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00b90010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0xb9"  # tangrowth friendship id
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
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, get_tangrowth_friendship_location_state
            ),
            new_instruction_readable="call get_tangrowth_friendship_location"
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
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 6, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

evAr05Zn01_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    trap_gate,
    tangrowth_interaction,
    return_at04,
    get_tangrowth_friendship_location_state,
    special_spawn_conditions
]
