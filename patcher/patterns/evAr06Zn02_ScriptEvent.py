from patcher.helper.entrance_exit_names import FLOWER_ZONE_MAIN_AREA_GRANITE_ZONE_GATE
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

EMAPA06_Z01_pattern_PALNA = [
    Instruction(
        identifier=1, offset=0x0,
        pattern=parse_pattern_bytes("00 0b 00 07"),
        instruction_readable="grow_stack 0xb"
    ),
    Instruction(
        identifier=2, offset=0x34,
        pattern=parse_pattern_bytes("00 06 00 10"),
        instruction_readable="push 0x6"
    ),
    Instruction(
        identifier=3, offset=0x3c,
        pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1"
    ),
    Instruction(
        identifier=4, offset=0x44,
        pattern=parse_pattern_bytes("00 01 00 10"),
        instruction_readable="push 0x1"
    ),
]

EMAPA06_Z01 = PatchPattern(
    name="EMAPA06_Z01",
    description="Flower Zone -> Granite Zone Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x34,
            pattern=parse_pattern_bytes("00 06 00 10"),
            instruction_readable="push 0x6"
        ),
        Instruction(
            identifier=3, offset=0x3c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x44,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

    ],
    patternPAL=EMAPA06_Z01_pattern_PALNA,
    patternNA=EMAPA06_Z01_pattern_PALNA,
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                FLOWER_ZONE_MAIN_AREA_GRANITE_ZONE_GATE, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                FLOWER_ZONE_MAIN_AREA_GRANITE_ZONE_GATE, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                FLOWER_ZONE_MAIN_AREA_GRANITE_ZONE_GATE, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr06Zn02_ScriptEvent_patch_pattern = [
    EMAPA06_Z01,
]
