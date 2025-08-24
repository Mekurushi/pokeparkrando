from patcher.helper.patttern_handler import parse_pattern_bytes, compute_bl_to_function_script, create_lstr_script, \
    create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("65 76 41 72 30 32 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
            instruction_readable="ds evAr02Zn01_Npc_Main"
        ),

    ],
)
string_21_60160 = PatchPattern(
    name="ds 21_60160",
    description="string for lstr 21_60160",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("32 31 5f 36 30 31 36 30 00"),
            instruction_readable="ds 21_60160"
        ),

    ],
)

string_21_60170 = PatchPattern(
    name="ds 21_60170",
    description="string for lstr 21_60170",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("32 31 5f 36 30 31 37 30 00"),
            instruction_readable="ds 21_60170"
        ),

    ],
)

globalManager = PatchPattern(
    name="ds GlobalManager",
    description="using GlobalManager for lstr instructions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("47 6c 6f 62 61 6c 4d 61 6e 61 67 65 72 00"),
            instruction_readable="ds GlobalManager"
        ),

    ]
)

get_module = PatchPattern(
    name="get module",
    description="using get module for calls",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="grow_stack 0x1"
        ),
        Instruction(
            identifier=2, offset=0x4,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=3, offset=0x8,
            pattern=parse_pattern_bytes("00 10 01 01"),
            instruction_readable="SC1 0x0:0x10"
        ),
    ]
)

run_interaction_dialog = PatchPattern(
    name="run interaction dialog",
    description="using for calls",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),
        Instruction(
            identifier=2, offset=0x68,
            pattern=parse_pattern_bytes("00 06 00 06"),
            instruction_readable="ret -0x6"
        ),

    ]
)

is_friend_function = PatchPattern(
    name="is_friend_function",
    description="patching is_friend function checks for location (bestfriend flag)",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 04 00 07"),
            instruction_readable="grow_stack 0x4"
        ),
        Instruction(
            identifier=2, offset=0x4c,
            pattern=parse_pattern_bytes("00 3d 00 10"),
            instruction_readable="push 0x3d"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x4b"
        ),
    ]
)

set_best_friend_function = PatchPattern(
    name="set_best_friend function",
    description="set best friend function used for calls",
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
    ]
)

gate_open_logic = PatchPattern(
    name="Close ar02Zn01 Gates depending on",
    description="Modifing gate Logic",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="grow_stack 0x1"
        ),

        Instruction(
            identifier=99, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),

        Instruction(
            identifier=98, offset=0x8, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=97, offset=0xc, pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="store_arg -0x1"
        ),

        # open meadow gate
        Instruction(
            identifier=2, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call open_gate(Meadow)"
        ),

        # beach gate condition
        #
        Instruction(
            identifier=3, offset=0x1c, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=4, offset=0x20, pattern=parse_pattern_bytes("07 d0 00 10"),
            instruction_readable="push 0x7d0"
        ),
        Instruction(
            identifier=5, offset=0x24, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        Instruction(
            identifier=6, offset=0x28, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),

        # open beach gate
        #
        Instruction(
            identifier=7, offset=0x2c, pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=8, offset=0x30, pattern=parse_pattern_bytes("4e 29 00 10"),
            instruction_readable="push 0x4e29"
        ),
        Instruction(
            identifier=9, offset=0x34, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call open_gate(Beach)"
        ),

        # cavern gate condition
        #
        Instruction(
            identifier=10, offset=0x38, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=11, offset=0x3c, pattern=parse_pattern_bytes("0f a0 00 10"),
            instruction_readable="push 0xfa0"
        ),
        Instruction(
            identifier=12, offset=0x40, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        Instruction(
            identifier=13, offset=0x44, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),

        # open cavern gate
        #
        Instruction(
            identifier=14, offset=0x48, pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=15, offset=0x4c, pattern=parse_pattern_bytes("4e 2a 00 10"),
            instruction_readable="push 0x4e2a"
        ),
        Instruction(
            identifier=16, offset=0x50, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call open_gate(Cavern)"
        ),

        # haunted gate condition
        #
        Instruction(
            identifier=17, offset=0x54, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=18, offset=0x58, pattern=parse_pattern_bytes("17 70 00 10"),
            instruction_readable="push 0x1770"
        ),
        Instruction(
            identifier=19, offset=0x5c, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        Instruction(
            identifier=20, offset=0x60, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),

        # open haunted gate
        #
        Instruction(
            identifier=21, offset=0x64, pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=22, offset=0x68, pattern=parse_pattern_bytes("4e 2b 00 10"),
            instruction_readable="push 0x4e2b"
        ),
        Instruction(
            identifier=23, offset=0x6c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call open_gate(Haunted)"
        ),

        # granite gate condition
        #
        Instruction(
            identifier=24, offset=0x70, pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="load_arg -0x1"
        ),
        Instruction(
            identifier=25, offset=0x74, pattern=parse_pattern_bytes("1f 40 00 10"),
            instruction_readable="push 0x1f40"
        ),
        Instruction(
            identifier=26, offset=0x78, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        Instruction(
            identifier=27, offset=0x7c, pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),

        # open granite gate
        #
        Instruction(
            identifier=28, offset=0x80, pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=29, offset=0x84, pattern=parse_pattern_bytes("4e 2c 00 10"),
            instruction_readable="push 0x4e2c"
        ),
        Instruction(
            identifier=30, offset=0x88, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call open_gate(Granite)"
        ),
    ],
    patchMapJP=[
        # Modifying Beach Gate Condition
        #
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x2"  # prisma id Venusaur
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data,
                custom_prisma_check_function
            ),
            new_instruction_readable="call custom_have_prisma_fun"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),

        # Modifying Cavern Gate Condition

        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00080010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x8"  # prisma id Empoleon
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data,
                custom_prisma_check_function
            ),
            new_instruction_readable="call custom_have_prisma_fun"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        # Modifying Haunted Gate Condition

        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0x000b0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xb"  # prisma id Blaziken
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data,
                custom_prisma_check_function
            ),
            new_instruction_readable="call custom_have_prisma_fun"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),

        # Modifying Granite Gate Condition

        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x000c0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xc"  # prisma id Rotom
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data,
                custom_prisma_check_function
            ),
            new_instruction_readable="call custom_have_prisma_fun"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=99,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=98,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=97,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ],
)

custom_prisma_check_function = PatchPattern(
    name="unused code space",
    description="Modifing gate Logic",
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
            identifier=99, offset=-0x4, pattern=parse_pattern_bytes("00 02 01 06"),
            instruction_readable="retv -0x2"
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
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
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
            patch_function=lambda offset, data, plando_dict, matches: (0x0000000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(4, 'big'),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020106).to_bytes(4, 'big'),
            new_instruction_readable="retv -0x2"
        ),

    ],
)

treehouse_additional_pokemon_spawn_conditions = PatchPattern(
    name="Treehouse Pokemon Spawns",
    description="Modifying Treehouse pokemon spawn conditions to allow full state start",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),
        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        # primeape spawn condition
        Instruction(
            identifier=3, offset=0xcc, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0xd0, pattern=parse_pattern_bytes("0b b8 00 10"),
            instruction_readable="push 0xbb8"
        ),
        Instruction(
            identifier=5, offset=0xd4, pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
        Instruction(
            identifier=6, offset=0xd8, pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz"
        ),
        # end of primeape spawn condition
        Instruction(
            identifier=7, offset=0xec, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        # end of state baased checks
        Instruction(
            identifier=8, offset=0x1b4, pattern=parse_pattern_bytes("00 06 00 10"),
            instruction_readable="push 0x6"
        ),

        # end of function
        Instruction(
            identifier=9, offset=0x204, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),

        # for differenting the two identically functions
        Instruction(
            identifier=99, offset=0x208, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 3, matches),
            new_instruction_readable="jmp"
        ),

        # primeape spawn condition -> empoleon prisma
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00080010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x8"  # prisma id Empoleon
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data,
                custom_prisma_check_function
            ),
            new_instruction_readable="call custom_have_prisma_fun"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040108).to_bytes(4, 'big'),
            new_instruction_readable="jnz"  # so it only jumps when the prisma is not zero
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 8, matches),
            new_instruction_readable="jmp"  # skip all chapter based logic
        ),

    ],
)

treehouse_additional_pokemon_spawn_conditions2 = PatchPattern(
    name="Treehouse Pokemon Spawns 2",
    description="Modifying Treehouse pokemon spawn conditions to remove chapter based conditions",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),
        Instruction(
            identifier=2, offset=0x14, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        # primeape spawn condition
        Instruction(
            identifier=3, offset=0xcc, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        Instruction(
            identifier=4, offset=0xd0, pattern=parse_pattern_bytes("0b b8 00 10"),
            instruction_readable="push 0xbb8"
        ),
        Instruction(
            identifier=5, offset=0xd4, pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
        Instruction(
            identifier=6, offset=0xd8, pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz"
        ),
        # end of primeape spawn condition
        Instruction(
            identifier=7, offset=0xec, pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="load_arg -0x2"
        ),
        # end of state baased checks
        Instruction(
            identifier=8, offset=0x1b4, pattern=parse_pattern_bytes("00 06 00 10"),
            instruction_readable="push 0x6"
        ),

        # end of function
        Instruction(
            identifier=9, offset=0x204, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),

        # for differenting the two identically functions
        Instruction(
            identifier=99, offset=0x208, pattern=parse_pattern_bytes("00 01 00 07"),
            instruction_readable="grow_stack 0x1"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 3, matches),
            new_instruction_readable="jmp"
        ),

        # primeape spawn condition -> empoleon prisma
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00080010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x8"  # prisma id Empoleon
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data,
                custom_prisma_check_function
            ),
            new_instruction_readable="call custom_have_prisma_fun"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040108).to_bytes(4, 'big'),
            new_instruction_readable="jnz"  # so it only jumps when the prisma is not zero
        ),

        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 8, matches),
            new_instruction_readable="jmp"  # skip all chapter based logic
        ),

    ],
)

powerup_electabuzz_interaction = PatchPattern(
    name="Electabuzz Powerup Interaction",
    description="Modifying Electabuzz Interaction to remove f0201TalkEleboo flag and remove actual unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 10 00 07"),
            instruction_readable="grow_stack 0x10"
        ),

        # request f0201TalkEleboo flag
        Instruction(
            identifier=2, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0201TalkEleboo"
        ),
        Instruction(
            identifier=3, offset=0x4c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=4, offset=0x50, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x54, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x58, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x5c, pattern=parse_pattern_bytes("ff fa 00 0c"),
            instruction_readable="store_arg -0x6"
        ),

        # f0201TalkEleboo Condition
        Instruction(
            identifier=8, offset=0x80, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=9, offset=0x84, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x88, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x8c, pattern=parse_pattern_bytes("00 41 02 08"),
            instruction_readable="jz"
        ),

        # end of f0201TalkEleboo logic
        Instruction(
            identifier=12, offset=0x194, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),

        # unlocking Thunderbolt 1
        Instruction(
            identifier=23, offset=0x2d8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=24, offset=0x2dc, pattern=parse_pattern_bytes("00 20 00 10"),
            instruction_readable="push 0x20"
        ),
        Instruction(
            identifier=25, offset=0x2e0, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=26, offset=0x2e4, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=27, offset=0x2e8, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Thunderbolt 2
        Instruction(
            identifier=28, offset=0x37c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=29, offset=0x380, pattern=parse_pattern_bytes("00 40 00 10"),
            instruction_readable="push 0x40"
        ),
        Instruction(
            identifier=30, offset=0x384, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=31, offset=0x388, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=32, offset=0x38c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Thunderbolt 3
        Instruction(
            identifier=37, offset=0x420, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=38, offset=0x424, pattern=parse_pattern_bytes("00 80 00 10"),
            instruction_readable="push 0x80"
        ),
        Instruction(
            identifier=39, offset=0x428, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=40, offset=0x42c, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=41, offset=0x430, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patchMapJP=[
        # removing f0201TalkEleboo flag request
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # skipping f0201TalkEleboo interaction
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 12,
                matches
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing Thunderbolt powerup unlock
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing Thunderbolt 2 powerup unlock
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing Thunderbolt 3 powerup unlock
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ],
)

powerup_bibarel_interaction = PatchPattern(
    name="Bibarel Powerup Interaction",
    description="Modifying Bibarel Interaction to remove f0201TalkBeadaru flag and remove actual unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x08"
        ),

        # request f0201TalkBeadaru flag
        Instruction(
            identifier=2, offset=0x54, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0201TalkBeadaru"
        ),
        Instruction(
            identifier=3, offset=0x58, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=4, offset=0x5c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x60, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x64, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x68, pattern=parse_pattern_bytes("ff fa 00 0c"),
            instruction_readable="store_arg -0x6"
        ),

        # f0201TalkBeadaru Condition
        Instruction(
            identifier=8, offset=0x8c, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=9, offset=0x90, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x94, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x98, pattern=parse_pattern_bytes("00 16 02 08"),
            instruction_readable="jz"
        ),

        # end of f0201TalkBeadaru logic
        Instruction(
            identifier=12, offset=0xf4, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        # unlocking Health 1
        Instruction(
            identifier=23, offset=0x1b8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=24, offset=0x1bc, pattern=parse_pattern_bytes("01 00 00 10"),
            instruction_readable="push 0x100"
        ),
        Instruction(
            identifier=25, offset=0x1c0, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=26, offset=0x1c4, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=27, offset=0x1c8, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Health 2
        Instruction(
            identifier=28, offset=0x25c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=29, offset=0x260, pattern=parse_pattern_bytes("02 00 00 10"),
            instruction_readable="push 0x200"
        ),
        Instruction(
            identifier=30, offset=0x264, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=31, offset=0x268, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=32, offset=0x26c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Health 3
        Instruction(
            identifier=37, offset=0x300, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=38, offset=0x304, pattern=parse_pattern_bytes("04 00 00 10"),
            instruction_readable="push 0x400"
        ),
        Instruction(
            identifier=39, offset=0x308, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=40, offset=0x30c, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=41, offset=0x310, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patchMapJP=[
        # removing f0201TalkBeadaru flag request
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # skipping f0201TalkBeadaru interaction
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 12,
                matches
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing Health 1 powerup unlock
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing Health 2 powerup unlock
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing Health 3 powerup unlock
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ],
)

powerup_ponyta_interaction = PatchPattern(
    name="Ponyta Powerup Interaction",
    description="Modifying Ponyta Interaction to remove f0201TalkPonyta flag and remove actual unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x8"
        ),

        # request f0201TalkPonyta flag
        Instruction(
            identifier=2, offset=0x54, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0201TalkPonyta"
        ),
        Instruction(
            identifier=3, offset=0x58, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=4, offset=0x5c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x60, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x64, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x68, pattern=parse_pattern_bytes("ff fa 00 0c"),
            instruction_readable="store_arg -0x6"
        ),

        # f0201TalkPonyta Condition
        Instruction(
            identifier=8, offset=0x8c, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=9, offset=0x90, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x94, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x98, pattern=parse_pattern_bytes("00 16 02 08"),
            instruction_readable="jz"
        ),

        # end of f0201TalkPonyta logic
        Instruction(
            identifier=12, offset=0xf4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0201PowerUpDash"
        ),

        # f0201PowerUpDash powerup chapter condition
        Instruction(
            identifier=13, offset=0x114, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=14, offset=0x118, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=15, offset=0x11c, pattern=parse_pattern_bytes("13 88 00 10"),
            instruction_readable="push 0x1388"
        ),
        Instruction(
            identifier=16, offset=0x120, pattern=parse_pattern_bytes("00 0d 00 16"),
            instruction_readable="lt"
        ),
        Instruction(
            identifier=17, offset=0x124, pattern=parse_pattern_bytes("00 01 06 08"),
            instruction_readable="jzSet"
        ),

        # unlocking PowerUpDash
        Instruction(
            identifier=18, offset=0x174, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=19, offset=0x178, pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=20, offset=0x17c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=21, offset=0x180, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=22, offset=0x184, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Dash 1
        Instruction(
            identifier=23, offset=0x224, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=24, offset=0x228, pattern=parse_pattern_bytes("00 04 00 10"),
            instruction_readable="push 0x4"
        ),
        Instruction(
            identifier=25, offset=0x22c, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=26, offset=0x230, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=27, offset=0x234, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Dash 2
        Instruction(
            identifier=28, offset=0x2c8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=29, offset=0x2cc, pattern=parse_pattern_bytes("00 08 00 10"),
            instruction_readable="push 0x8"
        ),
        Instruction(
            identifier=30, offset=0x2d0, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=31, offset=0x2d4, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=32, offset=0x2d8, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # ponyta unlock
        Instruction(
            identifier=33, offset=0x2dc, pattern=parse_pattern_bytes("00 1a 00 10"),
            instruction_readable="push 0x1a"
        ),
        Instruction(
            identifier=34, offset=0x2e0, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=35, offset=0x2e4, pattern=parse_pattern_bytes("00 28 00 10"),
            instruction_readable="push 0x28"
        ),
        Instruction(
            identifier=36, offset=0x2e8, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),

        # unlocking Dash 3
        Instruction(
            identifier=37, offset=0x37c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=38, offset=0x380, pattern=parse_pattern_bytes("40 00 00 10"),
            instruction_readable="push 0x4000"
        ),
        Instruction(
            identifier=39, offset=0x384, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=40, offset=0x388, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=41, offset=0x38c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patchMapJP=[
        # removing f0201TalkPonyta flag request
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # skipping f0201TalkPonyta interaction
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 12,
                matches
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing chapter condition
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing powerupdash unlock

        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing dash1 powerup unlock
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing dash2 powerup unlock
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing ponyta unlock
        Patch(
            identifier=33,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=34,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=35,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=36,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing dash3 powerup unlock
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ],
)

powerup_primeape_interaction = PatchPattern(
    name="Primeape Powerup Interaction",
    description="Modifying Primeape Interaction to remove f0201TalkOkorizaru flag and remove actual unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
            instruction_readable="grow_stack 0x08"
        ),

        # request f0201TalkOkorizaru flag
        Instruction(
            identifier=2, offset=0x54, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0201TalkOkorizaru"
        ),
        Instruction(
            identifier=3, offset=0x58, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=4, offset=0x5c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x60, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x64, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x68, pattern=parse_pattern_bytes("ff fa 00 0c"),
            instruction_readable="store_arg -0x6"
        ),

        # f0201TalkOkorizaru Condition
        Instruction(
            identifier=8, offset=0x8c, pattern=parse_pattern_bytes("ff fa 00 0b"),
            instruction_readable="load_arg -0x6"
        ),
        Instruction(
            identifier=9, offset=0x90, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x94, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x98, pattern=parse_pattern_bytes("00 16 02 08"),
            instruction_readable="jz"
        ),

        # end of f0201TalkOkorizaru logic
        Instruction(
            identifier=12, offset=0xf4, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),

        # unlocking Iron Tail 1
        Instruction(
            identifier=23, offset=0x1b8, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=24, offset=0x1bc, pattern=parse_pattern_bytes("08 00 00 10"),
            instruction_readable="push 0x800"
        ),
        Instruction(
            identifier=25, offset=0x1c0, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=26, offset=0x1c4, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=27, offset=0x1c8, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Iron Tail 2
        Instruction(
            identifier=28, offset=0x268, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=29, offset=0x26c, pattern=parse_pattern_bytes("10 00 00 10"),
            instruction_readable="push 0x1000"
        ),
        Instruction(
            identifier=30, offset=0x270, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=31, offset=0x274, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=32, offset=0x278, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),

        # unlocking Iron Tail 3
        Instruction(
            identifier=37, offset=0x30c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=38, offset=0x310, pattern=parse_pattern_bytes("20 00 00 10"),
            instruction_readable="push 0x2000"
        ),
        Instruction(
            identifier=39, offset=0x314, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=40, offset=0x318, pattern=parse_pattern_bytes("00 b9 00 10"),
            instruction_readable="push 0xb9"
        ),
        Instruction(
            identifier=41, offset=0x31c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
    ],
    patchMapJP=[
        # removing f0201TalkOkorizaru flag request
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # skipping f0201TalkOkorizaru interaction
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 12,
                matches
            ),
            new_instruction_readable="delay(0)"
        ),

        # removing Iron Tail 1 powerup unlock
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing Iron Tail 2 powerup unlock
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing Iron Tail 3 powerup unlock
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ],
)

drifblim_interaction = PatchPattern(
    name="Drifblim Interaction",
    description="Modifying Drifblim Interaction to remove fTalkFuwaride flag and remove actual unlocks",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 12 00 07"),
            instruction_readable="grow_stack 0x12"
        ),

        # request fTalkFuwaride flag
        Instruction(
            identifier=2, offset=0x70, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr fTalkFuwaride"
        ),
        Instruction(
            identifier=3, offset=0x74, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=4, offset=0x78, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=5, offset=0x7c, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x80, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=7, offset=0x84, pattern=parse_pattern_bytes("ff f9 00 0c"),
            instruction_readable="store_arg -0x7"
        ),

        # fTalkFuwaride Condition
        Instruction(
            identifier=8, offset=0x88, pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="load_arg -0x7"
        ),
        Instruction(
            identifier=9, offset=0x8c, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=10, offset=0x90, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
        Instruction(
            identifier=11, offset=0x94, pattern=parse_pattern_bytes("00 60 02 08"),
            instruction_readable="jz"
        ),

        # end of fTalkFuwaride logic
        Instruction(
            identifier=12, offset=0x218, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),

        # opcode friendship
        Instruction(
            identifier=13, offset=0x314, pattern=parse_pattern_bytes("00 3c 00 10"),
            instruction_readable="push 0x3c"
        ),
    ],
    patchMapJP=[
        # removing fTalkFuwaride flag request
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # skipping fTalkFuwaride interaction
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 12,
                matches
            ),
            new_instruction_readable="delay(0)"
        ),

        # replacing friendship syscall with best friend
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x004a0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x4a"
        ),
    ],
)

mime_jr_interaction = PatchPattern(
    name="mime_jr interaction",
    description="patching mime_jr to check location (best friend flag) instead of friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),
        Instruction(
            identifier=2, offset=0xc0,
            pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=3, offset=0xc4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ]
)

abra_interaction = PatchPattern(
    name="abra interaction",
    description="patching abra to check location (best friend flag) instead of friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0xe4,
            pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=3, offset=0xe8,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, set_best_friend_function
            ),
            new_instruction_readable="call set_best_friend"
        ),
    ]
)

burmy_interaction = PatchPattern(
    name="burmy interaction",
    description="patching burmy to check location (best friend flag) instead of friendship",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0xf0,
            pattern=parse_pattern_bytes("ff fc 00 0b"),
            instruction_readable="load_arg -0x4"
        ),
        Instruction(
            identifier=3, offset=0xf4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call set_friendship"
        ),
    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ]
)

piplup_interaction = PatchPattern(
    name="Treehouse Piplup interaction",
    description="patching piplu to allow skygarden travel only with all prismas",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 07 00 07"),
            instruction_readable="grow_stack 0x7"
        ),

        Instruction(
            identifier=2, offset=0xa4,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=3, offset=0xa8,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=4, offset=0xac,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        Instruction(
            identifier=5, offset=0xb0,
            pattern=parse_pattern_bytes("00 05 06 08"),
            instruction_readable="jzSet"
        ),
        Instruction(
            identifier=6, offset=0xb4,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=7, offset=0xb8,
            pattern=parse_pattern_bytes("13 ec 00 10"),
            instruction_readable="push 0x13ec"
        ),
        Instruction(
            identifier=8, offset=0xbc,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ),
        Instruction(
            identifier=9, offset=0xc0,
            pattern=parse_pattern_bytes("00 01 06 08"),
            instruction_readable="jzSet"
        ),
        Instruction(
            identifier=10, offset=0xc4,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=11, offset=0xc8,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz"
        ), Instruction(
            identifier=12, offset=0xcc,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 21_60160"
        ),
        Instruction(
            identifier=13, offset=0xd0,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ), Instruction(
            identifier=14, offset=0xd4,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call start_dialog"
        ), Instruction(
            identifier=15, offset=0xd8,
            pattern=parse_pattern_bytes("00 29 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=16, offset=0xdc,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=17, offset=0xe0,
            pattern=parse_pattern_bytes("13 ec 00 10"),
            instruction_readable="push 0x13ec"
        ), Instruction(
            identifier=18, offset=0xe4,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ), Instruction(
            identifier=19, offset=0xe8,
            pattern=parse_pattern_bytes("00 05 06 08"),
            instruction_readable="jzSet"
        ), Instruction(
            identifier=20, offset=0xec,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ), Instruction(
            identifier=21, offset=0xf0,
            pattern=parse_pattern_bytes("1c 34 00 10"),
            instruction_readable="push 0x1c34"
        ), Instruction(
            identifier=22, offset=0xf4,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ), Instruction(
            identifier=23, offset=0xf8,
            pattern=parse_pattern_bytes("00 01 06 08"),
            instruction_readable="jzSet"
        ), Instruction(
            identifier=24, offset=0xfc,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=25, offset=0x100,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=26, offset=0x104,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 21_60170"
        ),
        Instruction(
            identifier=27, offset=0x108,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ), Instruction(
            identifier=28, offset=0x10c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call start_dialog"
        ), Instruction(
            identifier=29, offset=0x110,
            pattern=parse_pattern_bytes("00 1b 00 08"),
            instruction_readable="jmp"
        ), Instruction(
            identifier=30, offset=0x114,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ), Instruction(
            identifier=31, offset=0x118,
            pattern=parse_pattern_bytes("1c 34 00 10"),
            instruction_readable="push 0x1c34"
        ),
        Instruction(
            identifier=32, offset=0x11c,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        Instruction(
            identifier=33, offset=0x120,
            pattern=parse_pattern_bytes("00 05 06 08"),
            instruction_readable="jzSet"
        ), Instruction(
            identifier=34, offset=0x124,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ), Instruction(
            identifier=35, offset=0x128,
            pattern=parse_pattern_bytes("27 10 00 10"),
            instruction_readable="push 0x2710"
        ), Instruction(
            identifier=36, offset=0x12c,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ), Instruction(
            identifier=37, offset=0x130,
            pattern=parse_pattern_bytes("00 01 06 08"),
            instruction_readable="jzSet"
        ),
        Instruction(
            identifier=38, offset=0x134,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ), Instruction(
            identifier=39, offset=0x138,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="jz"
        ), Instruction(
            identifier=40, offset=0x13c,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 21_60171"
        ), Instruction(
            identifier=41, offset=0x140,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg -0x0"
        ), Instruction(
            identifier=42, offset=0x144,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call start_dialog"
        ), Instruction(
            identifier=43, offset=0x148,
            pattern=parse_pattern_bytes("00 0d 00 08"),
            instruction_readable="jmp"
        ),
        Instruction(
            identifier=44, offset=0x14c,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=45, offset=0x150,
            pattern=parse_pattern_bytes("27 10 00 10"),
            instruction_readable="push 0x2710"
        ),
        Instruction(
            identifier=46, offset=0x154,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        Instruction(
            identifier=47, offset=0x158,
            pattern=parse_pattern_bytes("00 05 06 08"),
            instruction_readable="jzSet"
        ), Instruction(
            identifier=48, offset=0x15c,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ), Instruction(
            identifier=49, offset=0x160,
            pattern=parse_pattern_bytes("27 4c 00 10"),
            instruction_readable="push 0x274c"
        ), Instruction(
            identifier=50, offset=0x164,
            pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
        ), Instruction(
            identifier=51, offset=0x168,
            pattern=parse_pattern_bytes("00 01 06 08"),
            instruction_readable="jzSet"
        ), Instruction(
            identifier=52, offset=0x16c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ), Instruction(
            identifier=53, offset=0x170,
            pattern=parse_pattern_bytes("00 03 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=54, offset=0x174,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr 21_60180"
        ),
        Instruction(
            identifier=55, offset=0x178,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="load_arg 0x0"
        ),
        Instruction(
            identifier=56, offset=0x17c,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call start_dialog"
        ),
        Instruction(
            identifier=57, offset=0x180,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="load_arg -0x5"
        ),
        Instruction(
            identifier=58, offset=0x184,
            pattern=parse_pattern_bytes("27 10 00 10"),
            instruction_readable="push 0x2710"
        ),
        Instruction(
            identifier=59, offset=0x188,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_amount_function
            ),
            new_instruction_readable="call get_prisma_amount"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x000e0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xe"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x000f0016).to_bytes(4, 'big'),
            new_instruction_readable="le"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 11,
                matches, "jz"
            ),
            new_instruction_readable="jz"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, string_21_60170
            ),
            new_instruction_readable="lstr 21_60170"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x0000000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, run_interaction_dialog
            ),
            new_instruction_readable="call run_interaction_dialog"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 56,
                matches, "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(
                data, string_section_start, string_21_60160
            ),
            new_instruction_readable="lstr 21_60160"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x0000000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, run_interaction_dialog
            ),
            new_instruction_readable="call run_interaction_dialog"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 56,
                matches, "jmp"
            ),
            new_instruction_readable="jmp"
        ),

        Patch(
            identifier=56,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_amount_function
            ),
            new_instruction_readable="call get_prisma_amount"
        ),
        Patch(
            identifier=57,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=58,
            patch_function=lambda offset, data, plando_dict, matches: (0x000e0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xe"
        ),
        Patch(
            identifier=59,
            patch_function=lambda offset, data, plando_dict, matches: (0x000f0016).to_bytes(4, 'big'),
            new_instruction_readable="le"
        ),
    ]
)

custom_prisma_amount_function = PatchPattern(
    name="custom get_prisma_amount function",
    description="using unused space to get prisma amount",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=2, offset=0x4,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=4, offset=0xc,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10,
            pattern=parse_pattern_bytes("ff ff 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=6, offset=0x14,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=8, offset=0x1c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20,
            pattern=parse_pattern_bytes("ff fe 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=10, offset=0x24,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=12, offset=0x2c,
            pattern=parse_pattern_bytes("00 28 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=14, offset=0x34,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=16, offset=0x3c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40,
            pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=18, offset=0x44,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48,
            pattern=parse_pattern_bytes("ff fe 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=20, offset=0x4c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=22, offset=0x54,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58,
            pattern=parse_pattern_bytes("ff fc 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=24, offset=0x5c,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=26, offset=0x64,
            pattern=parse_pattern_bytes("00 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=28, offset=0x6c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70,
            pattern=parse_pattern_bytes("ff fb 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=30, offset=0x74,
            pattern=parse_pattern_bytes("ff fb 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78,
            pattern=parse_pattern_bytes("00 19 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=32, offset=0x7c,
            pattern=parse_pattern_bytes("00 15 02 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=34, offset=0x84,
            pattern=parse_pattern_bytes("ff fa 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88,
            pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=36, offset=0x8c,
            pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90,
            pattern=parse_pattern_bytes("ff f9 00 0c"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=38, offset=0x94,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=40, offset=0x9c,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=42, offset=0xa4,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8,
            pattern=parse_pattern_bytes("07 da 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=44, offset=0xac,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=46, offset=0xb4,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=48, offset=0xbc,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=50, offset=0xc4,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8,
            pattern=parse_pattern_bytes("0b c2 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=52, offset=0xcc,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=54, offset=0xd4,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=56, offset=0xdc,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=58, offset=0xe4,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8,
            pattern=parse_pattern_bytes("0f aa 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=60, offset=0xec,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=62, offset=0xf4,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=64, offset=0xfc,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=66, offset=0x104,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108,
            pattern=parse_pattern_bytes("13 92 00 10"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=68, offset=0x10c,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=70, offset=0x114,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),

        Instruction(
            identifier=72, offset=0x11c,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128,
            pattern=parse_pattern_bytes("17 7a 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ), Instruction(
            identifier=77, offset=0x130,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ), Instruction(
            identifier=78, offset=0x134,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ), Instruction(
            identifier=79, offset=0x138,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ), Instruction(
            identifier=80, offset=0x13c,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ), Instruction(
            identifier=81, offset=0x140,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ), Instruction(
            identifier=82, offset=0x144,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="---"
        ), Instruction(
            identifier=83, offset=0x148,
            pattern=parse_pattern_bytes("1f 4a 00 10"),
            instruction_readable="---"
        ), Instruction(
            identifier=84, offset=0x14c,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ), Instruction(
            identifier=85, offset=0x150,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ), Instruction(
            identifier=86, offset=0x154,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ), Instruction(
            identifier=87, offset=0x158,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ), Instruction(
            identifier=88, offset=0x15c,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ), Instruction(
            identifier=89, offset=0x160,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ), Instruction(
            identifier=90, offset=0x164,
            pattern=parse_pattern_bytes("ff f9 00 0b"),
            instruction_readable="---"
        ), Instruction(
            identifier=91, offset=0x168,
            pattern=parse_pattern_bytes("23 32 00 10"),
            instruction_readable="---"
        ), Instruction(
            identifier=92, offset=0x16c,
            pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170,
            pattern=parse_pattern_bytes("00 04 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ), Instruction(
            identifier=95, offset=0x178,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c,
            pattern=parse_pattern_bytes("00 29 00 10"),
            instruction_readable="---"
        ), Instruction(
            identifier=97, offset=0x180,
            pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184,
            pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188,
            pattern=parse_pattern_bytes("ff ff 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c,
            pattern=parse_pattern_bytes("00 29 00 10"),
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # absol prisma
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"  # prisma id
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),

        # rayquaza prisma
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"  # prisma id
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),

        # venusaur prisma
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x2"  # prisma id
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # tangrowth prisma
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x3"  # prisma id
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # dusknoir prisma
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x4"  # prisma id
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=33,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=34,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # gyarados prisma
        Patch(
            identifier=35,
            patch_function=lambda offset, data, plando_dict, matches: (0x00050010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x5"  # prisma id
        ),
        Patch(
            identifier=36,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # pelipper prisma
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, matches: (0x00060010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x6"  # prisma id
        ),
        Patch(
            identifier=42,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=43,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=44,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=45,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=46,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # empoleon prisma
        Patch(
            identifier=47,
            patch_function=lambda offset, data, plando_dict, matches: (0x00080010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x8"  # prisma id
        ),
        Patch(
            identifier=48,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=49,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=50,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=51,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=52,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # bastiodon prisma
        Patch(
            identifier=53,
            patch_function=lambda offset, data, plando_dict, matches: (0x00090010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x9"  # prisma id
        ),
        Patch(
            identifier=54,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=55,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=56,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=57,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=58,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # rhyperior prisma
        Patch(
            identifier=59,
            patch_function=lambda offset, data, plando_dict, matches: (0x000a0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xa"  # prisma id
        ),
        Patch(
            identifier=60,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=61,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=62,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=63,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=64,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # blaziken prisma
        Patch(
            identifier=65,
            patch_function=lambda offset, data, plando_dict, matches: (0x000b0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xb"  # prisma id
        ),
        Patch(
            identifier=66,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=67,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=68,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=69,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=70,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # rotom prisma
        Patch(
            identifier=71,
            patch_function=lambda offset, data, plando_dict, matches: (0x000c0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xc"  # prisma id
        ),
        Patch(
            identifier=72,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=73,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=74,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=75,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=76,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # salamence prisma
        Patch(
            identifier=77,
            patch_function=lambda offset, data, plando_dict, matches: (0x000e0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xe"  # prisma id
        ),
        Patch(
            identifier=78,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=78,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=80,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=81,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=82,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        # bulbasaur prisma
        Patch(
            identifier=83,
            patch_function=lambda offset, data, plando_dict, matches: (0x000f0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xf"  # prisma id
        ),
        Patch(
            identifier=84,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(
                offset, data, custom_prisma_check_function
            ),
            new_instruction_readable="call prisma_check"  # prisma check function
        ),
        Patch(
            identifier=85,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"  # push result
        ),
        Patch(
            identifier=86,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000014).to_bytes(4, 'big'),
            new_instruction_readable="add"  # add
        ),
        Patch(
            identifier=87,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=88,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),

        # return
        Patch(
            identifier=89,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020106).to_bytes(4, 'big'),
            new_instruction_readable="retv -0x2"  # amount of prismas + result of syscall at the beginning (1 success)
        ),

    ]
)

evAr02Zn01_Npc_Main_pattern = [
    gate_open_logic,
    treehouse_additional_pokemon_spawn_conditions,
    treehouse_additional_pokemon_spawn_conditions2,
    powerup_ponyta_interaction,
    powerup_electabuzz_interaction,
    powerup_bibarel_interaction,
    powerup_primeape_interaction,
    drifblim_interaction,
    is_friend_function,
    mime_jr_interaction,
    abra_interaction,
    burmy_interaction,
    piplup_interaction,

    custom_prisma_amount_function,
    custom_prisma_check_function,

]
