from patcher.helper.patttern_handler import parse_pattern_bytes, create_jmp_instruction_script, create_lstr_script
from patcher.models.models import Instruction, PatchPattern, Patch

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    pattern=[
        Instruction(identifier=1, offset=0x0,
                    pattern=parse_pattern_bytes("65 76 41 72 39 39 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
                    instruction_readable="ds evAr99Zn01_Npc_Main"),

    ],
)

f9901TalkCelebi = PatchPattern(
    name="f9901TalkCelebi",
    description="f9901TalkCelebi for lstr instruction computation",
    pattern=[
        Instruction(identifier=1, offset=0x0,
                    pattern=parse_pattern_bytes("66 39 39 30 31 54 61 6c 6b 43 65 6c 65 62 69 00"),
                    instruction_readable="ds f9901TalkCelebi"),

    ],
)

a99_z01_init = PatchPattern(
    name="a99_z01_init remove spawn conditions",
    description="remove event stuff",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
                    instruction_readable="grow_stack 0x5"),
        # checks if snorlax invisible wall should be removed
        Instruction(identifier=2, offset=0x40, pattern=parse_pattern_bytes("00 01 02 08"),
                    instruction_readable="jz",
                    alternate_offset=0x48),
        Instruction(identifier=3, offset=0x48, pattern=parse_pattern_bytes("ff fd 00 0b"),#jump target
                    instruction_readable="load_arg -0x3",
                    alternate_offset=0x50),
        # checks if snorlax should spawn
        Instruction(identifier=4, offset=0x54, pattern=parse_pattern_bytes("00 05 02 08"),
                    instruction_readable="jz",
                    alternate_offset=0x5c),
        Instruction(identifier=5, offset=0x6c, pattern=parse_pattern_bytes("00 01 00 10"),# jump target
                    instruction_readable="push 0x1",
                    alternate_offset=0x74),
        # checks if event chatot should spawn
        Instruction(identifier=6, offset=0xb4, pattern=parse_pattern_bytes("00 16 02 08"),
                    instruction_readable="jz",
                    alternate_offset=0xbc),
        Instruction(identifier=7, offset=0x110, pattern=parse_pattern_bytes("00 00 00 0b"), # jump target
                    instruction_readable="load_arg 0x0",
                    alternate_offset=0x118),

    ],
    patchMap=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"  # always removing invisible snorlax wall
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset,5,matches),
            new_instruction_readable="jmp"  # always spawning snorlax
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset,7,matches),
            new_instruction_readable="jmp"  # never spawning event chatot
        ),
    ]
)

C00000_00010 = PatchPattern(
    name="C00000_00010",
    description="C00000_00010 skip mew park entry intro",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
                    instruction_readable="grow_stack 0xe"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("ff ff 00 0c"),
                    instruction_readable="store_arg -0x1"),
        Instruction(identifier=5, offset=0x180, pattern=parse_pattern_bytes("00 00 00 0b"),  # jump target
                    instruction_readable="load_arg 0x0",
                    alternate_offset=0x188),
        Instruction(identifier=6, offset=0x184, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????",
                    alternate_offset=0x18c),

    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset,5,matches),
            new_instruction_readable="jmp"
        ),

    ],
)

C00020_00030 = PatchPattern(
    name="skip event c00020_00030",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
                    instruction_readable="grow_stack 0x1"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr GlobalManager"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call get_module"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=5, offset=0x64, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0",
                    alternate_offset=0x6c),
        Instruction(identifier=6, offset=0x24, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15",
                    alternate_offset=0x2c),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 5, matches),
            new_instruction_readable="jmp"  # skipping all event logic
        ),

    ],
)

C00060_01000 = PatchPattern(
    name="skip event c00060_01000",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 1e 00 10"),
                    instruction_readable="push 0x1e"),
        Instruction(identifier=5, offset=0xc, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="push 0x0"),
        Instruction(identifier=9, offset=0x10, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="push 0x0"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=4, offset=0x20, pattern=parse_pattern_bytes("00 00 00 0b"),  # jump target
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=6, offset=0x28, pattern=parse_pattern_bytes("00 01 00 06"),
                    instruction_readable="ret -0x1"),
        Instruction(identifier=10, offset=-0x4, pattern=parse_pattern_bytes("00 01 00 06"),
                    instruction_readable="ret -0x1"),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 4, matches),
            new_instruction_readable="jmp"  # skipping all event logic
        ),

    ],
)
area01 = PatchPattern(
    name="skip event area01",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 01 00 06"),
                    instruction_readable="ret -0x1"),
    ],
    patchMap=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        )

    ],
)
area04 = PatchPattern(
    name="skip event area04",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
                    instruction_readable="grow_stack 0x1"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr GlobalManager"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call get_module"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=5, offset=0x48, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 5, matches),
            new_instruction_readable="jmp"  # skipping all event logic
        ),

    ],
)

area05 = PatchPattern(
    name="skip event area05",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
                    instruction_readable="grow_stack 0x1"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr GlobalManager"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call get_module"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=5, offset=0x34, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 4, matches),
            new_instruction_readable="jmp"  # skipping all event logic
        ),

    ],
)

area06 = PatchPattern(
    name="skip event area06",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 01 00 06"),
                    instruction_readable="ret -0x1"),

        Instruction(identifier=7, offset=-0x4, pattern=parse_pattern_bytes("00 02 00 06"),
                    instruction_readable="ret -0x2"),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 4, matches),
            new_instruction_readable="jmp"
        )

    ],
)
area07 = PatchPattern(
    name="skip event area07",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 01 00 06"),
                    instruction_readable="ret -0x1"),

        Instruction(identifier=7, offset=-0x4, pattern=parse_pattern_bytes("00 01 00 06"),
                    instruction_readable="ret -0x1"),
        Instruction(identifier=8, offset=-0x1c, pattern=parse_pattern_bytes("00 02 00 06"),
                    instruction_readable="ret -0x2"),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 4, matches),
            new_instruction_readable="jmp"
        )

    ],
)

chapter_event_logic = PatchPattern(
    name="skip events based on chapter",
    description="skip event and init zone correct",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
                    instruction_readable="grow_stack 0x2"),
        Instruction(identifier=2, offset=0x40, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=3, offset=0x44, pattern=parse_pattern_bytes("00 08 14 0a"),
                    instruction_readable="jeq_imm"),
        Instruction(identifier=4, offset=0xd4, pattern=parse_pattern_bytes("00 03 00 06"),
                    instruction_readable="ret -0x3"),
    ],
    patchMap=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 4, matches),
            new_instruction_readable="jmp"
        )

    ],
)


celebi_interaction = PatchPattern(
    name="celebi_interaction",
    description="Celebi Interaction to set flag when winning and removing chapter, postgame checks",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
                    instruction_readable="grow_stack 0x8"),


        # request f9901TalkCelebi flag
        Instruction(identifier=2, offset=0x4c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr f9901TalkCelebi"),
        Instruction(identifier=3, offset=0x50, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=4, offset=0x54, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=5, offset=0x58, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),
        Instruction(identifier=6, offset=0x5c, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=7, offset=0x60, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=8, offset=0x64, pattern=parse_pattern_bytes("00 0b 00 16"),
                    instruction_readable="eq"),
        Instruction(identifier=9, offset=0x68, pattern=parse_pattern_bytes("00 0c 02 08"),
                    instruction_readable="jz"),
        # end of f9901TalkCelebi flag logic
        Instruction(identifier=10, offset=0x9c, pattern=parse_pattern_bytes("00 00 00 11 3f 80 00 00"),
                    instruction_readable="push_imm 0x3f800000"),

        # post game check
        Instruction(identifier=11, offset=0xc0, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=12, offset=0xc4, pattern=parse_pattern_bytes("00 16 00 10"),
                    instruction_readable="push 0x16"),
        Instruction(identifier=13, offset=0xc8, pattern=parse_pattern_bytes("00 15 02 01"),
                    instruction_readable="SC2 0x0:0x15"),

        # postgame dialog
        Instruction(identifier=14, offset=0xf4, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),

        # removing already friend dialog with setting f9901TalkCelebi flag
        Instruction(identifier=15, offset=0x21c, pattern=parse_pattern_bytes("00 04 02 08"),
                    instruction_readable="jz"),
        Instruction(identifier=16, offset=0x220, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr 99_60180"),
        Instruction(identifier=17, offset=0x224, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=18, offset=0x228, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call FUN_??????"),
        Instruction(identifier=19, offset=0x22c, pattern=parse_pattern_bytes("00 03 00 08"),
                    instruction_readable="jmp"),
    ],
    patchMap=[

        # skip f9901TalkCelebi check
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset,10,matches),
            new_instruction_readable="jmp"
        ),
        # skip postgame check

        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 14,
                                                                                                    matches),
            new_instruction_readable="jmp"
        ),

        # set f9901TalkCelebi flag
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data,string_section_start, f9901TalkCelebi),
            new_instruction_readable="lstr f9901TalkCelebi"
        ),

        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffe000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x2" # load globalManager
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"  # opcode
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150401).to_bytes(4, 'big'),
            new_instruction_readable="SC4 0x0:0x15"
        ),
    ]
)

evAr99Zn01_Npc_Main_pattern = [
    # remove events
    C00000_00010,
    C00020_00030,
    C00060_01000,
    area01,
    area04,
    area06,
    area07,
    chapter_event_logic,
    # spawn condition
    a99_z01_init,
celebi_interaction
]
