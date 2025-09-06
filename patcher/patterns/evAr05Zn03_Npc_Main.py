from patcher.helper.patttern_handler import create_jmp_instruction_script, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

set_chapter = PatchPattern(
    name="set_chapter",
    description="removing set_chapter",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 02 00 07"),
            instruction_readable="grow_stack 0x2"
        ),

        Instruction(
            identifier=2, offset=0x1c, pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

        Instruction(
            identifier=3, offset=0x20, pattern=parse_pattern_bytes("00 15 03 01"),
            instruction_readable="SC3 0x0:0x15"
        ),
        Instruction(
            identifier=4, offset=0x48, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x4c, pattern=parse_pattern_bytes("00 15 04 01"),
            instruction_readable="SC4 0x0:0x15"
        ),
        Instruction(
            identifier=6, offset=0x50, pattern=parse_pattern_bytes("00 03 00 06"),
            instruction_readable="ret -0x3"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00030006).to_bytes(4, 'big'),
            new_instruction_readable="ret -0x3"
        ),
    ]
)

rotom_interaction = PatchPattern(
    name="rotom interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 11 00 07"),
            instruction_readable="grow_stack 0x11"
        ),
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 9f 00 10"),
            instruction_readable="push 0x19f"
        ),
        Instruction(
            identifier=3, offset=0xb8, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0503TalkRotom"
        ),

        Instruction(
            identifier=4, offset=0x200, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="load_arg -0xe"
        ),
        Instruction(
            identifier=5, offset=0x334, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0503TalkRotom2"
        ),
        Instruction(
            identifier=6, offset=0x610, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="load_arg -0xe"
        ),

        Instruction(
            identifier=7, offset=0x748, pattern=parse_pattern_bytes("00 0c 00 10"),  # attraction id
            instruction_readable="push 0xc"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 4, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"  # always skipping init phase
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 6, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"  # always skipping init phase
        ),
    ]
)

evAr05Zn03_Npc_Main_patterns = [
    set_chapter,
    rotom_interaction
]
