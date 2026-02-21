from patcher.helper.entrance_exit_names import ICE_ZONE_MAIN_AREA_EMPOLEON_GATE
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

EMAPA03_Z03 = PatchPattern(
    name="EMAPA03_Z03",
    description="Ice Zone -> Ice Zone Empoleon Area Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x34,
            pattern=parse_pattern_bytes("00 03 00 10"),
            instruction_readable="push 0x3"
        ),
        Instruction(
            identifier=3, offset=0x3c,
            pattern=parse_pattern_bytes("00 03 00 10"),
            instruction_readable="push 0x3"
        ),
        Instruction(
            identifier=4, offset=0x44,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_EMPOLEON_GATE, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_EMPOLEON_GATE, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                ICE_ZONE_MAIN_AREA_EMPOLEON_GATE, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr03Zn02_ScriptEvent_patch_pattern = [
    EMAPA03_Z03,
]
