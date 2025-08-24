from patcher.helper.patttern_handler import parse_pattern_bytes, create_jmp_instruction_script
from patcher.models.models import PatchPattern, Instruction, Patch

mansion_door = PatchPattern(
    name="mansion door condition",
    description="replacing chapter condition with tangrowth prisma",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0d 00 07"),
            instruction_readable="grow_stack 0xd"
        ),

        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("?? ?? ?? 03"),
            instruction_readable="call get_chapter"
        ),
        Instruction(
            identifier=3, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),
        Instruction(
            identifier=4, offset=0x30, pattern=parse_pattern_bytes("ff fd 00 0c"),
            instruction_readable="store_arg -0x3"
        ),
        Instruction(
            identifier=5, offset=0x34, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=6, offset=0x38, pattern=parse_pattern_bytes("1b 58 00 10"),
            instruction_readable="push 0x1b58"
        ),
        Instruction(
            identifier=7, offset=0x3c, pattern=parse_pattern_bytes("00 0f 00 16"),
            instruction_readable="le"
        ),
        # no prisma path
        Instruction(
            identifier=8, offset=0x74, pattern=parse_pattern_bytes("ff fd 00 0b"),
            instruction_readable="load_arg -0x3"
        ),
        Instruction(
            identifier=9, offset=0x78, pattern=parse_pattern_bytes("17 98 00 10"),
            instruction_readable="push 0x1798"
        ),
        Instruction(
            identifier=10, offset=0x7c, pattern=parse_pattern_bytes("00 0b 00 16"),
            instruction_readable="eq"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x3"  # tangrowth prisma id
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x1"  # global manager
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x51"  # prisma request opcode
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffd000c).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="store_arg -0x3"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffd000b).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="load_arg -0x3"
        ),
    ]
)

evAr05Zn01_Gimmic_patterns = [
    mansion_door
]
