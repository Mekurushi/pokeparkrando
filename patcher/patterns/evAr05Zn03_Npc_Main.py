from patcher.helper.entrance_exit_names import HAUNTED_ZONE_ROTOM_AREA_ROTOM_ATTRACTION
from patcher.helper.patttern_handler import create_jmp_instruction_script, get_attraction_id_from_dict, \
    parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, set_chapter

rotom_interaction = PatchPattern(
    name="rotom interaction",
    description="removing unwanted behavior",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 11 00 07"),
            instruction_readable="grow_stack 0x11"
        ),
        Instruction(
            identifier=2, offset=0x20, pattern=parse_pattern_bytes("01 9f 00 10"),
            instruction_readable="push 0x19f"
        ),
        Instruction(
            identifier=3, offset=0xb8, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0503TalkRotom"
        ),

        Instruction(
            identifier=4, offset=0x200, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="load_arg -0xe"
        ),
        Instruction(
            identifier=5, offset=0x334, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr f0503TalkRotom2"
        ),
        Instruction(
            identifier=6, offset=0x610, pattern=parse_pattern_bytes("ff f2 00 0b"),
            instruction_readable="load_arg -0xe"
        ),

        Instruction(
            identifier=7, offset=0x748, pattern=parse_pattern_bytes("00 0c 00 10"),  # attraction id
            instruction_readable="push 0xc"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 4, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"  # always skipping init phase
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns,
                                  pattern_name: create_jmp_instruction_script(
                offset, 6, patch_patterns, pattern_name,
                "jmp"
            ),
            new_instruction_readable="jmp"  # always skipping init phase
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: get_attraction_id_from_dict(
                plando_dict, HAUNTED_ZONE_ROTOM_AREA_ROTOM_ATTRACTION
            ),
            new_instruction_readable="update attraction id"
        ),
    ]
)

evAr05Zn03_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    rotom_interaction
]
