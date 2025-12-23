from patcher.helper.entrance_exit_names import MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

EMAPA01_Z01 = PatchPattern(
    name="EMAPA01_Z01",
    description="Meadow Zone Venusaur -> Meadow Zone Main Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x34,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=3, offset=0x3c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x44,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr01Zn02_ScriptEvent_patch_pattern = [
    EMAPA01_Z01,
]
