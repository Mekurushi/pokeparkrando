from patcher.helper.patttern_handler import parse_pattern_bytes, create_lstr_script
from patcher.models.models import PatchPattern, Instruction, Patch

gk_kabigon_wall_wait = PatchPattern(
    name="Kabigon Wall Wait",
    description="Modyfing Kabigon Wall spawn condition",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
                    instruction_readable="grow_stack 0x3"),
        Instruction(identifier=2, offset=0x48, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr Chapter"),
        Instruction(identifier=3, offset=0x64, pattern=parse_pattern_bytes("00 03 02 08"),
                    instruction_readable="jz"),

    ],
    patchMap=[


        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

    ],
)

gkKabigonWallPattern = [
    gk_kabigon_wall_wait,

]
