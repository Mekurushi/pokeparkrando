from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern

bridgeSwitch = PatchPattern(
    name="BridgeSwitch",
    description="remove bridgeSwitch trigger",
    patternJP=[
        Instruction(
            identifier=1, offset=0x0,
            pattern=parse_pattern_bytes("00 00 4e 31"),
            instruction_readable="bridgeswitch objectId"
        ),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: (0x00000000).to_bytes(
                4,
                'big'
            ),
            new_instruction_readable="removed objectId"
        ),
    ]
)
ScriptList_Ar04Zn02_patterns = [
    bridgeSwitch
]
