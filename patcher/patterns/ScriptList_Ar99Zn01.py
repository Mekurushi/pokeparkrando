from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

Ar99Zn01Init = PatchPattern(
    name="Ar99Zn01Init",
    description="always use Ar99Zn01Init",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 ff fe"),
            instruction_readable="---"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000001).to_bytes(4, 'big'),
            new_instruction_readable="---"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000001).to_bytes(4, 'big'),
            new_instruction_readable="---"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x0000ffff).to_bytes(4, 'big'),
            new_instruction_readable="---"
        ),
    ],
)

enterZoneScriptListInit = PatchPattern(
    name="enterZoneScriptListInit",
    description="remove ch0000_0010 enter chapter condition",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 09"),
            instruction_readable="---"
        ),

    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000001).to_bytes(4, 'big'),
            new_instruction_readable="---"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000001).to_bytes(4, 'big'),
            new_instruction_readable="---"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000001).to_bytes(4, 'big'),
            new_instruction_readable="---"
        ),
    ],
)

ScriptList_Ar99Zn01_patterns = [
    Ar99Zn01Init,
    enterZoneScriptListInit
]
