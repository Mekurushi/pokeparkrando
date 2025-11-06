from patcher.helper.patttern_handler import create_jmp_instruction_script, parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.general import get_friendship, set_chapter

mew_interaction = PatchPattern(
    name="mew interaction",
    description="modify mew Interaction for Locations",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 18 00 07"),
            instruction_readable="grow_stack 0x18"
        ),
        Instruction(
            identifier=2, offset=0x60, pattern=parse_pattern_bytes("02 06 00 10"),
            instruction_readable="push 0x206"
        ),

        Instruction(
            identifier=3, offset=0xb8, pattern=parse_pattern_bytes("00 14 02 08"),
            instruction_readable="jz"
        ),

        Instruction(
            identifier=4, offset=0x10c, pattern=parse_pattern_bytes("00 00 00 10"),  # jmp target
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x16c, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],

    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 4, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040010).to_bytes(
                4,
                'big'
            ) if plando_dict["Options"]["goal"] != 1 else None,
            new_instruction_readable="push 0x4"
            # make postgame location only accessible when postgame goal option is used
        ),
    ]
)
mew_power_competition_patternPALNA = [
    Instruction(
        identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 22 00 07"),
        instruction_readable="grow_stack 0x22"
    ),
    Instruction(
        identifier=2, offset=0xcc, pattern=parse_pattern_bytes("00 00 00 12"),  # first postgame check
        instruction_readable="push_result"
    ),

    Instruction(
        identifier=3, offset=0x1fc8, pattern=parse_pattern_bytes("00 00 00 12"),  # second postgame check
        instruction_readable="push_result"
    ),

    Instruction(
        identifier=4, offset=0x2034, pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=5, offset=0x2084, pattern=parse_pattern_bytes("?? ?? ?? 19"),  # jmp target
        instruction_readable="lea"
    ),

    Instruction(
        identifier=6, offset=0x2118, pattern=parse_pattern_bytes("00 00 00 10"),
        instruction_readable="push 0x0"
    ),
    Instruction(
        identifier=7, offset=0x2168, pattern=parse_pattern_bytes("00 0a 00 10"),
        instruction_readable="push 0xa"
    ),
]

mew_power_competition = PatchPattern(
    name="mew power competition",
    description="modify mew Power Competition logic to suit ap implementation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 22 00 07"),
            instruction_readable="grow_stack 0x22"
        ),
        Instruction(
            identifier=2, offset=0xcc, pattern=parse_pattern_bytes("00 00 00 12"),  # first postgame check
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=3, offset=0x1f98, pattern=parse_pattern_bytes("00 00 00 12"),  # second postgame check
            instruction_readable="push_result"
        ),

        Instruction(
            identifier=4, offset=0x2004, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=5, offset=0x2054, pattern=parse_pattern_bytes("?? ?? ?? 19"),  # jmp target
            instruction_readable="lea"
        ),

        Instruction(
            identifier=6, offset=0x20e8, pattern=parse_pattern_bytes("00 00 00 10"),
            instruction_readable="push 0x0"
        ),
        Instruction(
            identifier=7, offset=0x2138, pattern=parse_pattern_bytes("00 0a 00 10"),
            instruction_readable="push 0xa"
        ),
    ],
    patternNA=mew_power_competition_patternPALNA,
    patternPAL=mew_power_competition_patternPALNA,

    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 5, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 7, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),
    ]
)

spawn_conditions = PatchPattern(
    name="mew interaction",
    description="modify mew Power Competition logic to suit ap implementation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x22"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr GlobalManager"
        ),

        Instruction(
            identifier=3, offset=0x3bc, pattern=parse_pattern_bytes("02 06 00 10"),
            instruction_readable="push 0x206"
        ),

    ],

    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(
                offset, 3, matches,
                "jmp"
            ),
            new_instruction_readable="jmp"
        ),

    ]
)

piplup_interaction = PatchPattern(
    name="piplup interaction",
    description="allowing leaving skygarden",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 11 00 07"),
            instruction_readable="grow_stack 0x11"
        ),
        Instruction(
            identifier=2, offset=0x30, pattern=parse_pattern_bytes("02 07 00 10"),
            instruction_readable="push 0x207"
        ),

        Instruction(
            identifier=3, offset=0x68, pattern=parse_pattern_bytes("00 00 00 12"),
            instruction_readable="push_result"
        ),

    ],

    patchMapJP=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="push 0x1"
        ),
    ]
)

evAr07Zn01_Npc_Main_patterns = [
    set_chapter,
    get_friendship,
    mew_interaction,
    mew_power_competition,
    spawn_conditions,
    piplup_interaction
]
