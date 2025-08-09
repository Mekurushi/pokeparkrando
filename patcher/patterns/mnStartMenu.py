from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import PatchPattern, Instruction, Patch

load_new_file_pattern = PatchPattern(
    name="load new File Logic",
    description="skip opening on new file and init status Menu Flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff f9 00 0b"),
                    instruction_readable="load_arg -0x7"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 05 02 08"),
                    instruction_readable="jz identifier 8"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("?? ?? 00 03"),
                    instruction_readable="call start_opening"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 23 00 10"),
                    instruction_readable="push 0x23"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),
        Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("ff ff 00 0b"),
                    instruction_readable="load_arg -0x1"),
    ],
    patchMap=[
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x001e0010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1e"
        ),

    ],
)