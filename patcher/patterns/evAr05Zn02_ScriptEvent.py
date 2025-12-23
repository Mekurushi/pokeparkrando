from patcher.helper.entrance_exit_names import HAUNTED_ZONE_BOOKSHELF_AREA_ROTOM_CONNECTION, \
    HAUNTED_ZONE_MANSION_AREA_MAIN_AREA_GATE
from patcher.helper.patttern_handler import get_exit_zone_area_position_data, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

EMAPA05_Z01 = PatchPattern(
    name="EMAPA05_Z01",
    description="Haunted Zone Mansion Area -> Haunted Zone Main Area Connection",
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
            pattern=parse_pattern_bytes("00 01 00 10"),
            instruction_readable="push 0x1"
        ),

    ],
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MANSION_AREA_MAIN_AREA_GATE, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MANSION_AREA_MAIN_AREA_GATE, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_MANSION_AREA_MAIN_AREA_GATE, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)
EMAPA05_Z03_pattern_PALNA = [
    Instruction(
        identifier=1, offset=0x0,
        pattern=parse_pattern_bytes("00 0a 00 07"),
        instruction_readable="grow_stack 0xa"
    ),
    Instruction(
        identifier=2, offset=0x34,
        pattern=parse_pattern_bytes("00 05 00 10"),
        instruction_readable="push 0x5"
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

]
EMAPA05_Z03 = PatchPattern(
    name="EMAPA05_Z03",
    description="Haunted Zone Mansion Area -> Haunted Zone Rotom Area Connection",
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
            pattern=parse_pattern_bytes("00 03 00 10"),
            instruction_readable="push 0x3"
        ),
        Instruction(
            identifier=4, offset=0x44,
            pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),

    ],
    patternNA=EMAPA05_Z03_pattern_PALNA,
    patternPAL=EMAPA05_Z03_pattern_PALNA,
    patchMapJP=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_BOOKSHELF_AREA_ROTOM_CONNECTION, "zone"
            ),
            new_instruction_readable="update zone target based on exit"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_BOOKSHELF_AREA_ROTOM_CONNECTION, "area"
            ),
            new_instruction_readable="update area target based on exit"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: get_exit_zone_area_position_data(
                plando_dict,
                HAUNTED_ZONE_BOOKSHELF_AREA_ROTOM_CONNECTION, "position"
            ),
            new_instruction_readable="update position target based on exit"
        ),
    ]
)
evAr05Zn02_ScriptEvent_patch_pattern = [
    EMAPA05_Z01,
    EMAPA05_Z03,
]
