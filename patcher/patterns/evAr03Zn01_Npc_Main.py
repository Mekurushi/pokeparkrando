from patcher.helper.patttern_handler import parse_pattern_bytes, create_jmp_instruction_script, create_lstr_script, \
    compute_bl_to_function_script, create_jnz_instruction_script
from patcher.models.models import Instruction, PatchPattern, Patch

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    patternJP=[
        Instruction(identifier=1, offset=0x0,
                    pattern=parse_pattern_bytes("65 76 41 72 30 33 5a 6e 30 31 5f 4e 70 63 5f 4d 61 69 6e 00"),
                    instruction_readable="ds evAr03Zn01_Npc_Main"),

    ],
)

globalManager = PatchPattern(
    name="ds GlobalManager",
    description="using GlobalManager for lstr instructions",
    patternJP=[
        Instruction(identifier=1, offset=0x0,
                    pattern=parse_pattern_bytes("47 6c 6f 62 61 6c 4d 61 6e 61 67 65 72 00"),
                    instruction_readable="ds GlobalManager"),

    ]
)

fBippasWoodLevel = PatchPattern(
    name="ds fBippasWoodLevel",
    description="using fBippasWoodLevel for lstr instructions",
    patternJP=[
        Instruction(identifier=1, offset=0x0,
                    pattern=parse_pattern_bytes("66 42 69 70 70 61 73 57 6f 6f 64 4c 65 76 65 6c 00"),
                    instruction_readable="ds fBippasWoodLevel"),

    ]
)

get_module = PatchPattern(
    name="get module",
    description="using get module for calls",
    patternJP=[
        Instruction(identifier=1, offset=0x0,
                    pattern=parse_pattern_bytes("00 01 00 07"),
                    instruction_readable="grow_stack 0x1"),
        Instruction(identifier=2, offset=0x4,
                    pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=3, offset=0x8,
                    pattern=parse_pattern_bytes("00 10 01 01"),
                    instruction_readable="SC1 0x0:0x10"),
    ]
)

custom_prisma_check_function = PatchPattern(
    name="unused code space",
    description="Modifing gate Logic",
    patternJP=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff ff 00 0b"),
                    instruction_readable="---"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 05 00 10"),
                    instruction_readable="---"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 0f 00 16"),
                    instruction_readable="---"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 03 02 08"),
                    instruction_readable="---"),
        Instruction(identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="---"),
        Instruction(identifier=6, offset=0x14, pattern=parse_pattern_bytes("ff fe 00 0c"),
                    instruction_readable="---"),
        Instruction(identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 02 00 08"),
                    instruction_readable="---"),
        Instruction(identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="---"),
        Instruction(identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff fe 00 0c"),
                    instruction_readable="---"),
        Instruction(identifier=10, offset=0x24, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="---"),
        Instruction(identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 02 01 06"),
                    instruction_readable="---"),
    ],
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010007).to_bytes(4, 'big'),
            new_instruction_readable="grow_stack 0x1"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data, string_section_start,
                                                                                         globalManager),
            new_instruction_readable="lstr GlobalManager"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(offset, data,
                                                                                                    get_module),
            new_instruction_readable="call get_module()"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000c).to_bytes(4, 'big'),
            new_instruction_readable="store_arg -0x1"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x0000000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0xffff000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(4, 'big'),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0x00020106).to_bytes(4, 'big'),
            new_instruction_readable="retv -0x2"
        ),

    ],
)

eEvent02090 = PatchPattern(
    name="eEvent02090",
    description="eEvent02090",
    patternJP=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 1b 00 07"),
                    instruction_readable="grow_stack 0xe"),


        Instruction(identifier=2, offset=0x870, pattern=parse_pattern_bytes("08 34 00 10"),
                    instruction_readable="push 0x834"),
        Instruction(identifier=3, offset=0x874, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call set_chapter"),

        Instruction(identifier=4, offset=0x460, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call set_chapter"),
    ],
    patchMapJP=[
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay 0"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay 0"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay 0"
        ),
    ]
)


bidoof_quest_condition = PatchPattern(
    name="bidoof_bridge_quest_condition",
    description="Init of Bidoof bridge quest condition to be Pelipper Prisma not chapter",
    patternJP=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 07"),
                    instruction_readable="grow_stack 0xe"),


        # condition
        Instruction(identifier=2, offset=0x3a4, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr f0301BippaFlag"),
        Instruction(identifier=3, offset=0x3a8, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=4, offset=0x3ac, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="push 0x0"),
        Instruction(identifier=5, offset=0x3b0, pattern=parse_pattern_bytes("00 15 04 01"),
                    instruction_readable="SC4 0x0:0x15"),

        Instruction(identifier=6, offset=0x33c, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr f0301BippaFlag"),
        Instruction(identifier=7, offset=0x340, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=8, offset=0x344, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=9, offset=0x348, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),

        Instruction(identifier=10, offset=0x35c, pattern=parse_pattern_bytes("00 00 00 11"),
                    instruction_readable="push imm part1"),
        Instruction(identifier=11, offset=0x360, pattern=parse_pattern_bytes("3f 80 00 00"),
                    instruction_readable="push imm part2"),
        Instruction(identifier=12, offset=0x364, pattern=parse_pattern_bytes("00 00 00 11"),
                    instruction_readable="push imm part1"),
        Instruction(identifier=13, offset=0x368, pattern=parse_pattern_bytes("3f 80 00 00"),
                    instruction_readable="push imm part2"),
        Instruction(identifier=14, offset=0x36c, pattern=parse_pattern_bytes("00 00 00 10"),
                    instruction_readable="push 0x0"),
        Instruction(identifier=15, offset=0x370, pattern=parse_pattern_bytes("0a 40 00 10"),
                    instruction_readable="push 0xa40"),
        Instruction(identifier=16, offset=0x374, pattern=parse_pattern_bytes("ff f3 00 0b"),
                    instruction_readable="load_arg -0xd"),
        Instruction(identifier=17, offset=0x378, pattern=parse_pattern_bytes("00 28 00 10"),
                    instruction_readable="push 0x28"),
        Instruction(identifier=18, offset=0x37c, pattern=parse_pattern_bytes("00 15 06 01"),
                    instruction_readable="SC6 0x0:0x15"),
        Instruction(identifier=19, offset=0x380, pattern=parse_pattern_bytes("00 0a 00 10"),
                    instruction_readable="push 0xa"),

        # end of specific interaction
        Instruction(identifier=20, offset=0x414, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call"),

        # end of complete bidoof
        Instruction(identifier=21, offset=0xacc, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="ret"),

        Instruction(identifier=22, offset=0x580, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
    ],
    patchMapJP=[
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data,string_section_start,fBippasWoodLevel),
            new_instruction_readable="lstr fBippasWoodLevel"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffd000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x3"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150301).to_bytes(4, 'big'),
            new_instruction_readable="SC3 0x0:0x15"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000012).to_bytes(4, 'big'),
            new_instruction_readable="push_result"
        ),

        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, matches: create_jnz_instruction_script(offset, 20,matches),
            new_instruction_readable="jnz"
        ),

        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, matches: (0x0000000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg 0x0"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, matches: compute_bl_to_function_script(offset,data,eEvent02090),
            new_instruction_readable="call event"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, matches: create_jmp_instruction_script(offset,21,matches),
            new_instruction_readable="call event"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches:(0x00060010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x6"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00510010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x51"
        ),

        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),
    ]
)

evAr03Zn01_Npc_Main_pattern = [
#bidoof_quest_condition,
#eEvent02090,
#custom_prisma_check_function

]
