from patcher.helper.entrance_exit_names import MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE, \
    MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION, \
    MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

EMAPA02_Z01 = PatchPattern(
    name="EMAPA02_Z01",
    description="Meadow Zone -> Treehouse Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x34,
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
        ),
        Instruction(
            identifier=3, offset=0x3c,
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
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
                MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

EMAPA01_Z02 = PatchPattern(
    name="EMAPA01_Z02",
    description="Meadow Zone -> Meadow Venusaur Connection",
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
            pattern=parse_pattern_bytes("00 02 00 10"),
            instruction_readable="push 0x2"
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
                MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

EMAPA99_Z01 = PatchPattern(
    name="EMAPA99_Z01",
    description="Meadow Zone -> Pokepark Entrance Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x34,
            pattern=parse_pattern_bytes("00 63 00 10"),
            instruction_readable="push 0x63"
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
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

evAr01Zn01_ScriptEvent_patch_pattern = [
    EMAPA02_Z01,
    EMAPA01_Z02,
    EMAPA99_Z01,

]
