from patcher.helper.entrance_exit_names import CAVERN_ZONE_MAIN_AREA_MAGMA_ZONE_TRUCK
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

ZONECHANGETR = PatchPattern(
    name="ZONECHANGETR",
    description="Cavern Zone -> Magma Zone Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),
        Instruction(
            identifier=2, offset=0x38,
            pattern=parse_pattern_bytes("00 04 00 10"),
            instruction_readable="push 0x4"
        ),
        Instruction(
            identifier=3, offset=0x40,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=4, offset=0x48,
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
                CAVERN_ZONE_MAIN_AREA_MAGMA_ZONE_TRUCK, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                CAVERN_ZONE_MAIN_AREA_MAGMA_ZONE_TRUCK, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                CAVERN_ZONE_MAIN_AREA_MAGMA_ZONE_TRUCK, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr04Zn01_DemoEvent_patch_pattern = [
    ZONECHANGETR,
]
