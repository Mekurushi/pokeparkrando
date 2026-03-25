from patcher.helper.patttern_handler import parse_pattern_bytes, create_lstr_instruction_fsb
from patcher.models.models import PatchPattern, Instruction, Patch

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("47 6b 52 65 63 79 63 6c 65 53 61 6e 62 61 73 69 41 00"),
            instruction_readable="ds GkRecycleSanbasiA"
        ),

    ],
)

error_slFindModule = PatchPattern(
    name="ds ERROR: slFindModule",
    description="replacing EventManager string with string of other flag, breaking the next flag string",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("45 52 52 4f 52 3a 20 73 6c 46 69 6e 64 4d 6f 64 75 6c 65 0a 00"),
            instruction_readable="ds ERROR: slFindModule"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (
                0x664d617030333031427269646765314275696c6400).to_bytes(21, 'big'),
            new_instruction_readable="ds fMap0301Bridge1Build"
        ),

    ],
)

step01 = PatchPattern(
    name="step01 for bridge 1",
    description="replacing fBippasWoodLevel condition for the bridge spawn with fMap0301Bridge1Build",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 05 00 07"),
            instruction_readable="grow_stack 0x5"
        ),
        Instruction(
            identifier=2, offset=0x28, pattern=parse_pattern_bytes("?? ?? ?? 13"),
            instruction_readable="lstr fBippasWoodLevel"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: create_lstr_instruction_fsb(
                patch_patterns, string_section_start.name,
                error_slFindModule.name
            ),
            new_instruction_readable="lstr fMap0301Bridge1Build"
        ),

    ],
)

gkRecycleSanbasiA_pattern = [
    string_section_start,
    step01,

    error_slFindModule
]
