from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch
#mnLobby and mnAttractionInfo are generic so they are basically used identically for every Minigame

prisma_check = PatchPattern(
    name="Prisma check",
    description="patching prisma check to check for checked location",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
                    instruction_readable="grow_stack 0x3"),
        Instruction(identifier=2, offset=0x10c, pattern=parse_pattern_bytes("00 08 02 08"),
                    instruction_readable="jz"),
        Instruction(identifier=3, offset=0x110, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=4, offset=0x114, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=5, offset=0x118, pattern=parse_pattern_bytes("00 51 00 10"),
                    instruction_readable="push 0x51"),
        Instruction(identifier=6, offset=0x11c, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),

    ],
    patchMap=[


        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00680010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x68"
        ),

    ],
)

postgame_check = PatchPattern(
    name="Postgame check",
    description="patching postgame check to always unlock legendary pokemon",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 07 00 07"),
                    instruction_readable="grow_stack 0x7"),
        Instruction(identifier=2, offset=0xa4, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),

    ],
    patchMap=[


        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),

    ],
)




mnLobby_pattern = [
prisma_check,
postgame_check,

]