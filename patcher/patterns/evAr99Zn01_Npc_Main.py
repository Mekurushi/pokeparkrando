from patcher.helper.patttern_handler import parse_pattern_bytes, create_jmp_instruction_script
from patcher.models.models import Instruction, PatchPattern, Patch

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
]
