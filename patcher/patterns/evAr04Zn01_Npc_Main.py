from patcher.helper.patttern_handler import parse_pattern_bytes, create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch

special_spawn_conditions = PatchPattern(
    name="special spawn conditions",
    description="replacing special spawn conditions",
    patternJP=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
                    instruction_readable="grow_stack 0x7"),


        Instruction(identifier=2, offset=0x24, pattern=parse_pattern_bytes("00 c6 02 08"),
                    instruction_readable="jz"),

        Instruction(
            identifier=3, offset=0x340, pattern=parse_pattern_bytes("00 08 00 06"),
            instruction_readable="push 0x3d"
            ),


    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset,3,matches),
            new_instruction_readable="jmp"
        ),


    ]
)

gimmic_spawn_conditions = PatchPattern(
    name="gimmic spawn conditions",
    description="replacing gimmic spawn conditions",
    patternJP=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
                    instruction_readable="grow_stack 0x5"),


        Instruction(identifier=2, offset=0x24, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call get_chapter"),
        Instruction(
            identifier=3, offset=0x28, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
            ),
        Instruction(
            identifier=4, offset=0x2c, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="store_arg -0x3"
            ),
        Instruction(
            identifier=5, offset=0x30, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
            ),
        Instruction(
            identifier=6, offset=0x34, pattern=parse_pattern_bytes("10 04 00 10"),
            instruction_readable="push 0x1004"
            ),
        Instruction(
            identifier=7, offset=0x38, pattern=parse_pattern_bytes("00 0e 00 16"),
            instruction_readable="gt"
            ),
        Instruction(
            identifier=8, offset=0x3c, pattern=parse_pattern_bytes("00 18 02 08"),
            instruction_readable="jz"
        ),
        Instruction(
            identifier=9, offset=0xa0, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0401RailA"
        ),
        Instruction(
            identifier=10, offset=0x160, pattern=parse_pattern_bytes("00 06 00 06"),
            instruction_readable="ret -0x6"
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
            patch_function=lambda offset, data, plando_dict, matches: (0x00090010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x9"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffe000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(4, 'big'),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00180108).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset, 10,
                                                                                                    matches),
            new_instruction_readable="jmp"
        ),
    ]
)

evAr04Zn01_Npc_Main_patterns = [
special_spawn_conditions,
gimmic_spawn_conditions
]
