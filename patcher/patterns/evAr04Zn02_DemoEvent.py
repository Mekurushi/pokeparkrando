from patcher.helper.entrance_exit_names import MAGMA_ZONE_MAIN_AREA_CAVERN_ZONE_TRUCK
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

ZONECHANGETR = PatchPattern(
    name="ZONECHANGETR",
    description="Magma Zone -> Cavern Zone Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 06 00 07"),
            instruction_readable="grow_stack 0x6"
        ),
        Instruction(
            identifier=2, offset=0x14,
            pattern=parse_pattern_bytes("00 04 00 10"),
            instruction_readable="push 0x4"
        ),
        Instruction(
            identifier=3, offset=0x1c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),
        Instruction(
            identifier=4, offset=0x24,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MAGMA_ZONE_MAIN_AREA_CAVERN_ZONE_TRUCK, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MAGMA_ZONE_MAIN_AREA_CAVERN_ZONE_TRUCK, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MAGMA_ZONE_MAIN_AREA_CAVERN_ZONE_TRUCK, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr04Zn02_DemoEvent_patch_pattern = [
    ZONECHANGETR,
]
