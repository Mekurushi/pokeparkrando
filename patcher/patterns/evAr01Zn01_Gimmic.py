from patcher.helper.patttern_handler import parse_pattern_bytes, create_lstr_script
from patcher.models.models import PatchPattern, Instruction, Patch

f0301FuwarideTaxiStop_Ar01Zn01 = PatchPattern(
    name="f0301FuwarideTaxiStop",
    description="replacing f0301FuwarideTaxiStop string with string of other flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("66 30 33 30 31 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
                    instruction_readable="ds f0301FuwarideTaxiStop"),

    ],#66 30 33 30 31 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x663031303148696465416e645365656b00).to_bytes(17, 'big'),
            new_instruction_readable="ds f0101HideAndSeek"
        ),

    ],
)
f0302FuwarideTaxiStop_Ar01Zn01 = PatchPattern(
    name="f0302FuwarideTaxiStop",
    description="replacing f0302FuwarideTaxiStop string with string of other flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("66 30 33 30 32 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
                    instruction_readable="ds f0302FuwarideTaxiStop"),

    ],#66 30 33 30 31 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x66303130314576656e745445303300).to_bytes(15, 'big'),
            new_instruction_readable="ds f0101EventTE03"
        ),


    ],
)

f0401FuwarideTaxiStop_Ar01Zn01 = PatchPattern(
    name="f0401FuwarideTaxiStop",
    description="replacing f0401FuwarideTaxiStop string with string of other flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("66 30 34 30 31 46 75 77 61 72 69 64 65 54 61 78 69 53 74 6f 70 00"),
                    instruction_readable="ds f0401FuwarideTaxiStop"),

    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: (0x663031303154616c6b4d616e6b657900).to_bytes(16, 'big'),
            new_instruction_readable="ds f0101TalkMankey"
        ),


    ],
)

string_section_start = PatchPattern(
    name="string section start",
    description="string section start for lstr instruction computation",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("65 76 41 72 30 31 5a 6e 30 31 5f 47 69 6d 6d 69 63 00"),
                    instruction_readable="ds evAr01Zn01_Gimmic"),

    ],

)


caterpie_tree_gimmic = PatchPattern(
    name="Caterpie Tree Gimmic",
    description="setting hide_and_seek flag insted of unlocking caterpie, also instead of checking if caterpie is unlocked it checks for hide_and_seek flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0a 00 10"),
                    instruction_readable="push 0xa"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 29 00 10"),
                    instruction_readable="push 0x29"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),

        #
        Instruction(identifier=5, offset=0x1c, pattern=parse_pattern_bytes("00 e7 02 08"),
                    instruction_readable="jz"),
        Instruction(identifier=6, offset=0x20, pattern=parse_pattern_bytes("00 01 00 10"),
                    instruction_readable="push 0x1"),
        Instruction(identifier=7, offset=0x24, pattern=parse_pattern_bytes("00 ?? ?? 13"),
                    instruction_readable="lstr zfTreeCatapi"),
        #
        #
        Instruction(identifier=8, offset=0x34, pattern=parse_pattern_bytes("00 0d 00 10"),
                    instruction_readable="push 0xd"),
        Instruction(identifier=9, offset=0x40, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call unlock_pokemon(0xd)"),

    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data,string_section_start,f0301FuwarideTaxiStop_Ar01Zn01),
            new_instruction_readable="f0101HideAndSeek"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),

        #
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data, string_section_start,
                                                                                f0301FuwarideTaxiStop_Ar01Zn01),
            new_instruction_readable="f0101HideAndSeek"
        ),

        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),

    ],
)


weedle_tree_gimmic_logic = PatchPattern(
    name="Weedle Tree Gimmic Logic",
    description="setting hide_and_seek flag insted of unlocking caterpie, also instead of checking if caterpie is unlocked it checks for hide_and_seek flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 0a 00 10"),
                    instruction_readable="push 0xa"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),
        Instruction(identifier=7, offset=0x1c, pattern=parse_pattern_bytes("00 f0 02 08"),
                    instruction_readable="jz"),
        Instruction(identifier=5, offset=0x24, pattern=parse_pattern_bytes("?? ?? ?? 13"),
                    instruction_readable="lstr zfTreeBeedle"),
        Instruction(identifier=6, offset=0x1d0, pattern=parse_pattern_bytes("?? ?? ?? 03"),
                    instruction_readable="call unlock_pokemon"),

    ],
    patchMap=[
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data,string_section_start,f0302FuwarideTaxiStop_Ar01Zn01),
            new_instruction_readable="f0101EventTE03"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000002).to_bytes(4, 'big'),
            new_instruction_readable="delay(0)"
        ),
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data, string_section_start,
                                                                                f0302FuwarideTaxiStop_Ar01Zn01),
            new_instruction_readable="f0101HideAndSeek"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffe000b).to_bytes(4, 'big'),
            new_instruction_readable="f0101HideAndSeek"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),


    ],
)
weedle_tree_gimmic = PatchPattern(
    name="Weedle Tree Gimmic",
    description="setting hide_and_seek flag insted of unlocking caterpie, also instead of checking if caterpie is unlocked it checks for hide_and_seek flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff fc 00 0b"),
                    instruction_readable="load_arg -0x4"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 29 00 10"),
                    instruction_readable="push 0x29"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),



    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data,string_section_start,f0302FuwarideTaxiStop_Ar01Zn01),
            new_instruction_readable="f0101EventTE03"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),


    ],
)

shroomish_box_gimmic = PatchPattern(
    name="Shroomish Box Gimmic",
    description="setting hide_and_seek flag insted of unlocking caterpie, also instead of checking if caterpie is unlocked it checks for hide_and_seek flag",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 0e 00 10"),
                    instruction_readable="push 0xe"),
        Instruction(identifier=2, offset=0x4, pattern=parse_pattern_bytes("ff fe 00 0b"),
                    instruction_readable="load_arg -0x2"),
        Instruction(identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 29 00 10"),
                    instruction_readable="push 0x29"),
        Instruction(identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),


    ],
    patchMap=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data,string_section_start,f0401FuwarideTaxiStop_Ar01Zn01),
            new_instruction_readable="f0101TalkMankey"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),



    ],
)
unlock_function = PatchPattern(
    name="unlock function",
    description="replacing the unlock function to set the flag for shroomish box location",
    pattern=[
        Instruction(identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 03 00 07"),
                    instruction_readable="grow_stack 0x3"),

        Instruction(identifier=2, offset=0x24, pattern=parse_pattern_bytes("00 00 00 0b"),
                    instruction_readable="load_arg 0x0"),
        Instruction(identifier=3, offset=0x28, pattern=parse_pattern_bytes("ff ff 00 0b"),
                    instruction_readable="load_arg -0x1"),
        Instruction(identifier=4, offset=0x2c, pattern=parse_pattern_bytes("00 04 00 10"),
                    instruction_readable="push 0x4"),
        Instruction(identifier=5, offset=0x30, pattern=parse_pattern_bytes("00 15 03 01"),
                    instruction_readable="SC3 0x0:0x15"),
        Instruction(identifier=6, offset=0x34, pattern=parse_pattern_bytes("00 00 00 12"),
                    instruction_readable="push_result"),
        Instruction(identifier=7, offset=0x38, pattern=parse_pattern_bytes("ff fd 00 0c"),
                    instruction_readable="store_arg -0x3"),
        Instruction(identifier=8, offset=0x3c, pattern=parse_pattern_bytes("ff fd 00 0b"),
                    instruction_readable="load_arg -0x3"),
    ],
    patchMap=[

        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, matches: create_lstr_script(data, string_section_start,
                                                                                f0401FuwarideTaxiStop_Ar01Zn01),
            new_instruction_readable="f0101TalkMankey"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, matches: (0xfffe000b).to_bytes(4, 'big'),
            new_instruction_readable="load_arg -0x2"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, matches: (0x00000010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x0"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, matches: (0x00150401).to_bytes(4, 'big'),
            new_instruction_readable="SC4 0x0:0x15"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, matches: (0x00010010).to_bytes(4, 'big'),
            new_instruction_readable="push 0x1"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, matches: (0x00040106).to_bytes(4, 'big'),
            new_instruction_readable="retv -0x4"
        ),

    ],
)


evAr01Zn01_Gimmic_patch_pattern = [
    caterpie_tree_gimmic,
    weedle_tree_gimmic,
    weedle_tree_gimmic_logic,
shroomish_box_gimmic,
    unlock_function,

    # string updates
f0301FuwarideTaxiStop_Ar01Zn01,
f0302FuwarideTaxiStop_Ar01Zn01,
    f0401FuwarideTaxiStop_Ar01Zn01
]