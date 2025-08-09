from patcher.helper.patttern_handler import parse_pattern_bytes, create_lstr_script
from patcher.models.models import PatchPattern, Instruction, Patch

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("47 6b 57 6f 6f 64 42 6f 78 4b 69 6e 6f 00"),
                    instruction_readable="ds GkWoodBoxKino"),

    ],
)

eventManager = PatchPattern(
    name="ds EventManager",
    description="replacing EventManager string with string of other flag, breaking the next flag string",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("45 76 65 6e 74 4d 61 6e 61 67 65 72 00"),
                    instruction_readable="ds EventManager"),

    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x663031303154616c6b4d616e6b657900).to_bytes(16, 'big'),
            new_instruction_readable="ds f0101TalkMankey"
        ),

    ],
)

shroomish_box_wait = PatchPattern(
    name="Shroomish Box Wait",
    description="Modyfing Shroomish Crate to spawn only when Location is not checked",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
                    instruction_readable="grow_stack 0x5"),
        Instruction(identifier=2, offset=0x38, pattern=parse_pattern_bytes("ff fd 00 0c"),
                    instruction_readable="store_arg -0x3"),
        Instruction(identifier=3, offset=0x3c, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=4, offset=0x40, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=5, offset=0x44, pattern=parse_pattern_bytes("00 29 00 10"),
                    instruction_readable="push 0x29"),
        Instruction(identifier=6, offset=0x48, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),

    ],
    patchMap=[

        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data, string_section_start,
                                                                                eventManager),
            new_instruction_readable="lstr f0101TalkMankey"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),

    ],
)

gkWoodBoxKinoPattern = [
    shroomish_box_wait,
    # String Section
    eventManager
]
