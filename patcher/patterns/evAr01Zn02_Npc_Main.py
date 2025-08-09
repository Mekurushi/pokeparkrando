from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

NPC_Venusaur = PatchPattern(
    name="Venusaur Interaction Logic",
    description="remove croagunk and spearow requirement, and modify for friendship location",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 37 00 10"),
                    instruction_readable="push 0x37"),
        Instruction(identifier=2, offset=0x70, pattern=parse_pattern_bytes("00 00 00 14"),
                    instruction_readable="add"),
        Instruction(identifier=3, offset=0x88, pattern=parse_pattern_bytes("00 45 02 08"),
                    instruction_readable="jz"),

        # having no venusaur Prisma Path removing events
        Instruction(identifier=4, offset=0x230, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr GF0003"),
        Instruction(identifier=5, offset=0x234, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=6, offset=0x238, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=7, offset=0x23c, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),
        Instruction(identifier=8, offset=0x240, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=9, offset=0x244, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="push 0x0"),
        Instruction(identifier=10, offset=0x248, pattern=parse_pattern_bytes("00 0b 00 16"),
                    instruction_readable="eq"),
        Instruction(identifier=11, offset=0x24c, pattern=parse_pattern_bytes("00 19 02 08"),
                    instruction_readable="jz"),
        # removing chapter validation
        Instruction(identifier=12, offset=0x2c4, pattern=parse_pattern_bytes("00 03 02 08"),
                    instruction_readable="jz"),

        # having venusaur Prisma Path
        Instruction(identifier=13, offset=0x32c, pattern=parse_pattern_bytes("00 03 02 08"),
                    instruction_readable="jz"),
        # regular friendship flag path
        Instruction(identifier=14, offset=0x3d8, pattern=parse_pattern_bytes("00 0f 02 08"),
                    instruction_readable="jz"),

        # regular friendship flag in best friend path
        Instruction(identifier=15, offset=0x488, pattern=parse_pattern_bytes("00 04 02 08"),
                    instruction_readable="jz"),

        # prisma prep call
        Instruction(identifier=16, offset=0x4d4, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call prep_prisma_flag"),
    ],
    patchMap=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x2"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00450008).to_bytes(4, 'big'),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00190008).to_bytes(4, 'big'),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

        # removing regular friendship flag and only checking location when venusaur, empoleon, blaziken prisma is available
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x000f0008).to_bytes(4, 'big'),
            new_instruction_readable="jmp"
        ),
        # removing regular friendship flag in best friend path
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040008).to_bytes(4, 'big'),
            new_instruction_readable="jmp"
        ),
        # removing prep prisma call
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
    ],
)

evAr01Zn02_Npc_Main_patterns=[
NPC_Venusaur
]