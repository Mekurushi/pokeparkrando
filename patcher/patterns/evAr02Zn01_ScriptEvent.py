from patcher.helper.entrance_exit_names import TREEHOUSE_BEACH_PASSAGE_BEACH_ZONE_CONNECTION, \
    TREEHOUSE_CAVERN_PASSAGE_CAVERN_ZONE_CONNECTION, TREEHOUSE_GRANITE_PASSAGE_GRANITE_ZONE_CONNECTION, \
    TREEHOUSE_HAUNTED_PASSAGE_HAUNTED_ZONE_CONNECTION, \
    TREEHOUSE_MEADOW_PASSAGE_MEADOW_ZONE_CONNECTION
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

EMAPA01_Z01 = PatchPattern(
    name="EMAPA01_Z01",
    description="Treehouse -> Meadow Zone Connection",
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
                TREEHOUSE_MEADOW_PASSAGE_MEADOW_ZONE_CONNECTION, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_MEADOW_PASSAGE_MEADOW_ZONE_CONNECTION, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_MEADOW_PASSAGE_MEADOW_ZONE_CONNECTION, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)

EMAPA03_Z01 = PatchPattern(
    name="EMAPA03_Z01",
    description="Treehouse -> Beach Zone Connection",
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
                TREEHOUSE_BEACH_PASSAGE_BEACH_ZONE_CONNECTION, "zone"
            ),
            new_instruction_readable="update target zone based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_BEACH_PASSAGE_BEACH_ZONE_CONNECTION, "area"
            ),
            new_instruction_readable="update target area based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_BEACH_PASSAGE_BEACH_ZONE_CONNECTION, "position"
            ),
            new_instruction_readable="update target position based on exit"
        ),
    ]
)

EMAPA04_Z01 = PatchPattern(
    name="EMAPA04_Z01",
    description="Treehouse -> Cavern Zone Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x34,
            pattern=parse_pattern_bytes("00 04 00 10"),
            instruction_readable="push 0x4"
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
                TREEHOUSE_CAVERN_PASSAGE_CAVERN_ZONE_CONNECTION, "zone"
            ),
            new_instruction_readable="update target zone based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_CAVERN_PASSAGE_CAVERN_ZONE_CONNECTION, "area"
            ),
            new_instruction_readable="update target area based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_CAVERN_PASSAGE_CAVERN_ZONE_CONNECTION, "position"
            ),
            new_instruction_readable="update target position based on exit"
        ),
    ]
)

EMAPA05_Z01 = PatchPattern(
    name="EMAPA05_Z01",
    description="Treehouse -> Haunted Zone Connection",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 09 00 07"),
            instruction_readable="grow_stack 0x9"
        ),
        Instruction(
            identifier=2, offset=0x34,
            pattern=parse_pattern_bytes("00 05 00 10"),
            instruction_readable="push 0x5"
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
                TREEHOUSE_HAUNTED_PASSAGE_HAUNTED_ZONE_CONNECTION, "zone"
            ),
            new_instruction_readable="update target zone based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_HAUNTED_PASSAGE_HAUNTED_ZONE_CONNECTION, "area"
            ),
            new_instruction_readable="update target area based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_HAUNTED_PASSAGE_HAUNTED_ZONE_CONNECTION, "position"
            ),
            new_instruction_readable="update target position based on exit"
        ),
    ]
)
EMAPA06_Z01 = PatchPattern(
    name="EMAPA06_Z01",
    description="Treehouse -> Granite Zone Connection",
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
                TREEHOUSE_GRANITE_PASSAGE_GRANITE_ZONE_CONNECTION, "zone"
            ),
            new_instruction_readable="update target zone based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_GRANITE_PASSAGE_GRANITE_ZONE_CONNECTION, "area"
            ),
            new_instruction_readable="update target area based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: get_exit_zone_area_position_data(
                plando_dict,
                TREEHOUSE_GRANITE_PASSAGE_GRANITE_ZONE_CONNECTION, "position"
            ),
            new_instruction_readable="update target position based on exit"
        ),
    ]
)

evAr02Zn01_ScriptEvent_patch_pattern = [
    EMAPA01_Z01,
    EMAPA03_Z01,
    EMAPA04_Z01,
    EMAPA05_Z01,
    EMAPA06_Z01,
]
