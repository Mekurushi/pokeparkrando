from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

attraction_result = PatchPattern(
    name="Attraction Result Prisma Check",
    description="patching prisma check to check for checked location",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 18 00 07"),
                    instruction_readable="grow_stack 0x18"),

        # prisma state request
        Instruction(identifier=2, offset=0x12c, pattern=parse_pattern_bytes("00 14 02 08"),
                    instruction_readable="jz"),
        Instruction(identifier=3, offset=0x130, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=4, offset=0x134, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=5, offset=0x138, pattern=parse_pattern_bytes("00 51 00 10"),
                    instruction_readable="push 0x51"),
        Instruction(identifier=6, offset=0x13c, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),

        # set prisma

        Instruction(identifier=7, offset=0x210, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=8, offset=0x214, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=9, offset=0x218, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=10, offset=0x21c, pattern=parse_pattern_bytes("00 52 00 10"),
                    instruction_readable="push 0x52"),
        Instruction(identifier=11, offset=0x220, pattern=parse_pattern_bytes("00 15 04 01"),
                    instruction_readable="SC4 0x0:0x15"),
    ],
    patchMap=[

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00680010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x68"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00690010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x69"
        ),
    ],
)

attraction_start_demo = PatchPattern(
    name="Attraction Start Demo Prisma Check",
    description="patching prisma check to check for checked location instead",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0c 00 07"),
                    instruction_readable="grow_stack 0xc"),

        # prisma state request
        Instruction(identifier=2, offset=0xe0, pattern=parse_pattern_bytes("00 1b 02 08"),
                    instruction_readable="jz"),
        Instruction(identifier=3, offset=0xe4, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=4, offset=0xe8, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=5, offset=0xec, pattern=parse_pattern_bytes("00 51 00 10"),
                    instruction_readable="push 0x51"),
        Instruction(identifier=6, offset=0xf0, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),

    ],
    patchMap=[

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00680010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x68"
        )
    ],
)
attraction_start_demo_end = PatchPattern(
    name="Attraction Start Demo End Prisma Check",
    description="patching prisma check to check for checked location instead",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0b 00 07"),
                    instruction_readable="grow_stack 0xb"),

        # prisma state request
        Instruction(identifier=2, offset=0xe0, pattern=parse_pattern_bytes("00 0e 02 08"),
                    instruction_readable="jz"),
        Instruction(identifier=3, offset=0xe4, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=4, offset=0xe8, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=5, offset=0xec, pattern=parse_pattern_bytes("00 51 00 10"),
                    instruction_readable="push 0x51"),
        Instruction(identifier=6, offset=0xf0, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),

    ],
    patchMap=[

        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00680010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x68"
        )
    ],
)

condition_legendary_friendship = PatchPattern(
    name="checking conditions for legendary Pokemon Friendship",
    description="patching so it checks for the checked location",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 08 00 07"),
                    instruction_readable="grow_stack 0x8"),
        # postgame check
        Instruction(identifier=2, offset=0x28, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),

        # already friend check
        Instruction(identifier=3, offset=0xd0, pattern=parse_pattern_bytes("00 3d 00 10"),
                    instruction_readable="push 0x3d"),
    ],
    patchMap=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x004b0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x4b"  # so it checks for the checked location
        ),

    ],
)

set_friendship = PatchPattern(
    name="set legendary Pokemon friendship + additional features",
    description="removing regular friendship flag and adding location check",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 01 00 07"),
                    instruction_readable="grow_stack 0x7"),
        # set friendship and best friend feature
        Instruction(identifier=2, offset=0x30, pattern=parse_pattern_bytes("00 01 00 0b"),
                    instruction_readable="load_arg 0x1"),
        Instruction(identifier=3, offset=0x34, pattern=parse_pattern_bytes("ff ff 00 0b"),
                    instruction_readable="load_arg -0x1"),
        Instruction(identifier=4, offset=0x38, pattern=parse_pattern_bytes("00 3c 00 10"),
                    instruction_readable="push 0x3c"),
        Instruction(identifier=5, offset=0x3c, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),
    ],
    patchMap=[

        # removing friendship flag
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

    ],
)

mnAttractionInfo_pattern = [
    attraction_result,
    attraction_start_demo,
    attraction_start_demo_end,
    condition_legendary_friendship,
    set_friendship
]
