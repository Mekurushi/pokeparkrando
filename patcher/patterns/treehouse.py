from patcher.helper.patttern_handler import parse_pattern_bytes, compute_bl_to_function_script
from patcher.models.models import PatchPattern, Instruction, Patch

wait1 = PatchPattern(
    name="Wait1",
    description="Wait1 calling Wait4 (full state Treehouse",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
                    instruction_readable="grow_stack 0x2"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=3, offset=0x18, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="push 0x0"),
        Instruction(identifier=4, offset=0x54, pattern=parse_pattern_bytes("00 03 00 06"),
                    instruction_readable="ret -0x3"),
    ],
    patchMap=[

        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(offset,data, wait4),
            new_instruction_readable="call Wait4"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000006).to_bytes(4, 'big'),
            new_instruction_readable="ret 0x0"
        ),

    ],
)
wait2 = PatchPattern(
    name="Wait2",
    description="Wait2 calling Wait4 (full state Treehouse",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
                    instruction_readable="grow_stack 0x2"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=3, offset=0x18, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=4, offset=0x54, pattern=parse_pattern_bytes("00 03 00 06"),
                    instruction_readable="ret -0x3"),
    ],
    patchMap=[

        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(offset,data, wait4),
            new_instruction_readable="call Wait4"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000006).to_bytes(4, 'big'),
            new_instruction_readable="ret 0x0"
        ),

    ],
)

wait3 = PatchPattern(
    name="Wait3",
    description="Wait23 calling Wait4 (full state Treehouse",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
                    instruction_readable="grow_stack 0x2"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=3, offset=0x18, pattern=parse_pattern_bytes("00 02 00 10"),
                    instruction_readable="push 0x2"),
        Instruction(identifier=4, offset=0x54, pattern=parse_pattern_bytes("00 03 00 06"),
                    instruction_readable="ret -0x3"),
    ],
    patchMap=[

        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(offset,data, wait4),
            new_instruction_readable="call Wait4"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000006).to_bytes(4, 'big'),
            new_instruction_readable="ret 0x0"
        ),

    ],
)
wait4 = PatchPattern(
    name="Wait4",
    description="Wait2 calling Wait4 (full state Treehouse",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
                    instruction_readable="grow_stack 0x2"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=3, offset=0x18, pattern=parse_pattern_bytes("00 03 00 10"),
                    instruction_readable="push 0x3"),
        Instruction(identifier=4, offset=0x54, pattern=parse_pattern_bytes("00 03 00 06"),
                    instruction_readable="ret -0x3"),
    ]
)



treehouse_pattern = [
wait1,
    wait2,
    wait3
]