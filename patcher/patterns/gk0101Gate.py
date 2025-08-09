from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

gate101_close = PatchPattern(
    name="Close Gate Function from Venusaur Gate in Meadow Zone",
    description="Modyfing the gate open condition for Venusaurs Minigame Area to be Bulbasaur Prisma Shard",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 5f 13"),
                    instruction_readable="lstr GF0002"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x01"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 0b 00 16"),
                    instruction_readable="eq"),
        Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 05 02 08"),
                    instruction_readable="jz"),
    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x000f0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0xf"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),

    ],
)