from patcher.helper.patttern_handler import parse_pattern_bytes
from patcher.models.models import Instruction, Patch, PatchPattern
from patcher.patterns.main import compute_bl_to_function, get_addr16_ha, get_addr16_lo

custom_functions_cgu0_print_archipelago_text = PatchPattern(
    name=f"custom_functions_cgu0_print_archipelago_text",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c0802a6'),
            new_instruction_readable="mflr    r0"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9421f870'),
            new_instruction_readable="stwu    r1,-1936(r1)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90010794'),
            new_instruction_readable="stw     r0,1940(r1)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_archipelago_text_buffer.name, 1),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93a10744'),
            new_instruction_readable="stw     r29,1860(r1)"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3ba10008'),
            new_instruction_readable="addi    r29,r1,8"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3883'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_archipelago_text_buffer.name, 1),
            new_instruction_readable="addi    r4,r3,0"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00200'),
            new_instruction_readable="li      r5,512"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93210734'),
            new_instruction_readable="stw     r25,1844(r1)"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410738'),
            new_instruction_readable="stw     r26,1848(r1)"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9361073c'),
            new_instruction_readable="stw     r27,1852(r1)"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810740'),
            new_instruction_readable="stw     r28,1856(r1)"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93c10748'),
            new_instruction_readable="stw     r30,1864(r1)"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3bc00200'),
            new_instruction_readable="li      r30,512"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('db010750'),
            new_instruction_readable="stfd    f24,1872(r1)"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('db210758'),
            new_instruction_readable="stfd    f25,1880(r1)"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('db410760'),
            new_instruction_readable="stfd    f26,1888(r1)"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('db610768'),
            new_instruction_readable="stfd    f27,1896(r1)"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('db810770'),
            new_instruction_readable="stfd    f28,1904(r1)"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('dba10778'),
            new_instruction_readable="stfd    f29,1912(r1)"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('dbc10780'),
            new_instruction_readable="stfd    f30,1920(r1)"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('dbe10788'),
            new_instruction_readable="stfd    f31,1928(r1)"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_memcpy.name, 1
                ),
            new_instruction_readable="bl memcpy"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('88610008'),
            new_instruction_readable="lbz     r3,8(r1)"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28030000'),
            new_instruction_readable="cmplwi  r3,0"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('418209e0'),
            new_instruction_readable="beq     a48 <print_archipelago_text+0xa48>"
        ),
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c80'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 1),
            new_instruction_readable="lis     r4,0"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c3e4'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 1),
            new_instruction_readable="lfs     f31,0(r4)"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c80'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 2),
            new_instruction_readable="lis     r4,0"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c004'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 2),
            new_instruction_readable="lfs     f0,0(r4)"
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610007'),
            new_instruction_readable="addi    r3,r1,7"
        ),
        Patch(
            identifier=33,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fc903a6'),
            new_instruction_readable="mtctr   r30"
        ),
        Patch(
            identifier=34,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000008'),
            new_instruction_readable="b       8c <print_archipelago_text+0x8c>"
        ),
        Patch(
            identifier=35,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('42400018'),
            new_instruction_readable="bdz     a0 <print_archipelago_text+0xa0>"
        ),
        Patch(
            identifier=36,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('8c830001'),
            new_instruction_readable="lbzu    r4,1(r3)"
        ),
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2804000a'),
            new_instruction_readable="cmplwi  r4,10"
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4082fff4'),
            new_instruction_readable="bne     88 <print_archipelago_text+0x88>"
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('efff002a'),
            new_instruction_readable="fadds   f31,f31,f0"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4bffffec'),
            new_instruction_readable="b       88 <print_archipelago_text+0x88>"
        ),
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c1000b'),
            new_instruction_readable="addi    r6,r1,11"
        ),
        Patch(
            identifier=42,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3ce0'
                ) + get_addr16_ha(
                data, patch_patterns, custom_functions_cgu0__Lanon_c56ae961650860ac32e9b2618d293ecb_6.name, 1
                ),
            new_instruction_readable="lis     r7,0"
        ),
        Patch(
            identifier=43,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3d008080'),
            new_instruction_readable="lis     r8,-32640"
        ),
        Patch(
            identifier=44,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('54ca003a'),
            new_instruction_readable="clrrwi  r10,r6,2"
        ),
        Patch(
            identifier=45,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610009'),
            new_instruction_readable="addi    r3,r1,9"
        ),
        Patch(
            identifier=46,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38810000'),
            new_instruction_readable="addi    r4,r1,0"
        ),
        Patch(
            identifier=47,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39200000'),
            new_instruction_readable="li      r9,0"
        ),
        Patch(
            identifier=48,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a10007'),
            new_instruction_readable="addi    r5,r1,7"
        ),
        Patch(
            identifier=49,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '38c7'
                ) + get_addr16_lo(
                data, patch_patterns, custom_functions_cgu0__Lanon_c56ae961650860ac32e9b2618d293ecb_6.name, 1
                ),
            new_instruction_readable="addi    r6,r7,0"
        ),
        Patch(
            identifier=50,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7cfd5050'),
            new_instruction_readable="subf    r7,r29,r10"
        ),
        Patch(
            identifier=51,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('61088080'),
            new_instruction_readable="ori     r8,r8,32896"
        ),
        Patch(
            identifier=52,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d9d48ae'),
            new_instruction_readable="lbzx    r12,r29,r9"
        ),
        Patch(
            identifier=53,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d8b0775'),
            new_instruction_readable="extsb.  r11,r12"
        ),
        Patch(
            identifier=54,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41800088'),
            new_instruction_readable="blt     15c <print_archipelago_text+0x15c>"
        ),
        Patch(
            identifier=55,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d493850'),
            new_instruction_readable="subf    r10,r9,r7"
        ),
        Patch(
            identifier=56,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('714a0003'),
            new_instruction_readable="andi.   r10,r10,3"
        ),
        Patch(
            identifier=57,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('408201f0'),
            new_instruction_readable="bne     2d0 <print_archipelago_text+0x2d0>"
        ),
        Patch(
            identifier=58,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901f8'),
            new_instruction_readable="cmplwi  r9,504"
        ),
        Patch(
            identifier=59,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41810048'),
            new_instruction_readable="bgt     130 <print_archipelago_text+0x130>"
        ),
        Patch(
            identifier=60,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('216901f1'),
            new_instruction_readable="subfic  r11,r9,497"
        ),
        Patch(
            identifier=61,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280b01f1'),
            new_instruction_readable="cmplwi  r11,497"
        ),
        Patch(
            identifier=62,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41810008'),
            new_instruction_readable="bgt     fc <print_archipelago_text+0xfc>"
        ),
        Patch(
            identifier=63,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000008'),
            new_instruction_readable="b       100 <print_archipelago_text+0x100>"
        ),
        Patch(
            identifier=64,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39600000'),
            new_instruction_readable="li      r11,0"
        ),
        Patch(
            identifier=65,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d444a14'),
            new_instruction_readable="add     r10,r4,r9"
        ),
        Patch(
            identifier=66,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('396b0007'),
            new_instruction_readable="addi    r11,r11,7"
        ),
        Patch(
            identifier=67,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('556be8fe'),
            new_instruction_readable="srwi    r11,r11,3"
        ),
        Patch(
            identifier=68,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('396b0001'),
            new_instruction_readable="addi    r11,r11,1"
        ),
        Patch(
            identifier=69,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d6903a6'),
            new_instruction_readable="mtctr   r11"
        ),
        Patch(
            identifier=70,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('856a0008'),
            new_instruction_readable="lwzu    r11,8(r10)"
        ),
        Patch(
            identifier=71,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('818a0004'),
            new_instruction_readable="lwz     r12,4(r10)"
        ),
        Patch(
            identifier=72,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d8b5b78'),
            new_instruction_readable="or      r11,r12,r11"
        ),
        Patch(
            identifier=73,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d6b4039'),
            new_instruction_readable="and.    r11,r11,r8"
        ),
        Patch(
            identifier=74,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40820014'),
            new_instruction_readable="bne     138 <print_archipelago_text+0x138>"
        ),
        Patch(
            identifier=75,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39290008'),
            new_instruction_readable="addi    r9,r9,8"
        ),
        Patch(
            identifier=76,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4200ffe8'),
            new_instruction_readable="bdnz    114 <print_archipelago_text+0x114>"
        ),
        Patch(
            identifier=77,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901ff'),
            new_instruction_readable="cmplwi  r9,511"
        ),
        Patch(
            identifier=78,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('418101a8'),
            new_instruction_readable="bgt     2dc <print_archipelago_text+0x2dc>"
        ),
        Patch(
            identifier=79,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d454a14'),
            new_instruction_readable="add     r10,r5,r9"
        ),
        Patch(
            identifier=80,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('21690200'),
            new_instruction_readable="subfic  r11,r9,512"
        ),
        Patch(
            identifier=81,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d6903a6'),
            new_instruction_readable="mtctr   r11"
        ),
        Patch(
            identifier=82,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('8d6a0001'),
            new_instruction_readable="lbzu    r11,1(r10)"
        ),
        Patch(
            identifier=83,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d6b0775'),
            new_instruction_readable="extsb.  r11,r11"
        ),
        Patch(
            identifier=84,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41800188'),
            new_instruction_readable="blt     2d4 <print_archipelago_text+0x2d4>"
        ),
        Patch(
            identifier=85,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39290001'),
            new_instruction_readable="addi    r9,r9,1"
        ),
        Patch(
            identifier=86,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4200fff0'),
            new_instruction_readable="bdnz    144 <print_archipelago_text+0x144>"
        ),
        Patch(
            identifier=87,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000184'),
            new_instruction_readable="b       2dc <print_archipelago_text+0x2dc>"
        ),
        Patch(
            identifier=88,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d4660ae'),
            new_instruction_readable="lbzx    r10,r6,r12"
        ),
        Patch(
            identifier=89,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280a0004'),
            new_instruction_readable="cmplwi  r10,4"
        ),
        Patch(
            identifier=90,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820064'),
            new_instruction_readable="beq     1c8 <print_archipelago_text+0x1c8>"
        ),
        Patch(
            identifier=91,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280a0003'),
            new_instruction_readable="cmplwi  r10,3"
        ),
        Patch(
            identifier=92,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4182002c'),
            new_instruction_readable="beq     198 <print_archipelago_text+0x198>"
        ),
        Patch(
            identifier=93,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280a0002'),
            new_instruction_readable="cmplwi  r10,2"
        ),
        Patch(
            identifier=94,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40820920'),
            new_instruction_readable="bne     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=95,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901ff'),
            new_instruction_readable="cmplwi  r9,511"
        ),
        Patch(
            identifier=96,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41c20918'),
            new_instruction_readable="beq-    a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=97,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d4348ae'),
            new_instruction_readable="lbzx    r10,r3,r9"
        ),
        Patch(
            identifier=98,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d4a0774'),
            new_instruction_readable="extsb   r10,r10"
        ),
        Patch(
            identifier=99,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c0affbf'),
            new_instruction_readable="cmpwi   r10,-65"
        ),
        Patch(
            identifier=100,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41c10908'),
            new_instruction_readable="bgt-    a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=101,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39290001'),
            new_instruction_readable="addi    r9,r9,1"
        ),
        Patch(
            identifier=102,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4800013c'),
            new_instruction_readable="b       2d0 <print_archipelago_text+0x2d0>"
        ),
        Patch(
            identifier=103,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901ff'),
            new_instruction_readable="cmplwi  r9,511"
        ),
        Patch(
            identifier=104,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41c208f8'),
            new_instruction_readable="beq-    a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=105,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d5d4a14'),
            new_instruction_readable="add     r10,r29,r9"
        ),
        Patch(
            identifier=106,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('880a0001'),
            new_instruction_readable="lbz     r0,1(r10)"
        ),
        Patch(
            identifier=107,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280c00e0'),
            new_instruction_readable="cmplwi  r12,224"
        ),
        Patch(
            identifier=108,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c000774'),
            new_instruction_readable="extsb   r0,r0"
        ),
        Patch(
            identifier=109,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820050'),
            new_instruction_readable="beq     200 <print_archipelago_text+0x200>"
        ),
        Patch(
            identifier=110,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280c00ed'),
            new_instruction_readable="cmplwi  r12,237"
        ),
        Patch(
            identifier=111,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40820074'),
            new_instruction_readable="bne     22c <print_archipelago_text+0x22c>"
        ),
        Patch(
            identifier=112,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c00ffa0'),
            new_instruction_readable="cmpwi   r0,-96"
        ),
        Patch(
            identifier=113,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('418000f4'),
            new_instruction_readable="blt     2b4 <print_archipelago_text+0x2b4>"
        ),
        Patch(
            identifier=114,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('480008d0'),
            new_instruction_readable="b       a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=115,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901ff'),
            new_instruction_readable="cmplwi  r9,511"
        ),
        Patch(
            identifier=116,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41c208c8'),
            new_instruction_readable="beq-    a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=117,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d5d4a14'),
            new_instruction_readable="add     r10,r29,r9"
        ),
        Patch(
            identifier=118,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('880a0001'),
            new_instruction_readable="lbz     r0,1(r10)"
        ),
        Patch(
            identifier=119,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280c00f0'),
            new_instruction_readable="cmplwi  r12,240"
        ),
        Patch(
            identifier=120,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c1e0774'),
            new_instruction_readable="extsb   r30,r0"
        ),
        Patch(
            identifier=121,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820030'),
            new_instruction_readable="beq     210 <print_archipelago_text+0x210>"
        ),
        Patch(
            identifier=122,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280c00f4'),
            new_instruction_readable="cmplwi  r12,244"
        ),
        Patch(
            identifier=123,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40820068'),
            new_instruction_readable="bne     250 <print_archipelago_text+0x250>"
        ),
        Patch(
            identifier=124,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c1eff8f'),
            new_instruction_readable="cmpwi   r30,-113"
        ),
        Patch(
            identifier=125,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('418108a4'),
            new_instruction_readable="bgt     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=126,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901fd'),
            new_instruction_readable="cmplwi  r9,509"
        ),
        Patch(
            identifier=127,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40810078'),
            new_instruction_readable="ble     270 <print_archipelago_text+0x270>"
        ),
        Patch(
            identifier=128,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000898'),
            new_instruction_readable="b       a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=129,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('540b0034'),
            new_instruction_readable="clrrwi  r11,r0,5"
        ),
        Patch(
            identifier=130,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c0bffa0'),
            new_instruction_readable="cmpwi   r11,-96"
        ),
        Patch(
            identifier=131,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('418200ac'),
            new_instruction_readable="beq     2b4 <print_archipelago_text+0x2b4>"
        ),
        Patch(
            identifier=132,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000888'),
            new_instruction_readable="b       a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=133,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('397e0070'),
            new_instruction_readable="addi    r11,r30,112"
        ),
        Patch(
            identifier=134,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('556b063e'),
            new_instruction_readable="clrlwi  r11,r11,24"
        ),
        Patch(
            identifier=135,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280b0030'),
            new_instruction_readable="cmplwi  r11,48"
        ),
        Patch(
            identifier=136,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40800878'),
            new_instruction_readable="bge     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=137,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901fe'),
            new_instruction_readable="cmplwi  r9,510"
        ),
        Patch(
            identifier=138,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4180004c'),
            new_instruction_readable="blt     270 <print_archipelago_text+0x270>"
        ),
        Patch(
            identifier=139,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4800086c'),
            new_instruction_readable="b       a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=140,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('398b001f'),
            new_instruction_readable="addi    r12,r11,31"
        ),
        Patch(
            identifier=141,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('558c063e'),
            new_instruction_readable="clrlwi  r12,r12,24"
        ),
        Patch(
            identifier=142,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280c000c'),
            new_instruction_readable="cmplwi  r12,12"
        ),
        Patch(
            identifier=143,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40800068'),
            new_instruction_readable="bge     2a0 <print_archipelago_text+0x2a0>"
        ),
        Patch(
            identifier=144,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c00ffbf'),
            new_instruction_readable="cmpwi   r0,-65"
        ),
        Patch(
            identifier=145,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41810854'),
            new_instruction_readable="bgt     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=146,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901fd'),
            new_instruction_readable="cmplwi  r9,509"
        ),
        Patch(
            identifier=147,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40810074'),
            new_instruction_readable="ble     2bc <print_archipelago_text+0x2bc>"
        ),
        Patch(
            identifier=148,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000848'),
            new_instruction_readable="b       a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=149,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('396b000f'),
            new_instruction_readable="addi    r11,r11,15"
        ),
        Patch(
            identifier=150,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('556b063e'),
            new_instruction_readable="clrlwi  r11,r11,24"
        ),
        Patch(
            identifier=151,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2e9effc0'),
            new_instruction_readable="cmpwi   cr5,r30,-64"
        ),
        Patch(
            identifier=152,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280b0003'),
            new_instruction_readable="cmplwi  r11,3"
        ),
        Patch(
            identifier=153,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('288901fe'),
            new_instruction_readable="cmplwi  cr1,r9,510"
        ),
        Patch(
            identifier=154,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40940830'),
            new_instruction_readable="bge     cr5,a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=155,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4e802202'),
            new_instruction_readable="crand   4*cr5+lt,lt,4*cr1+lt"
        ),
        Patch(
            identifier=156,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40940828'),
            new_instruction_readable="bge     cr5,a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=157,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('896a0002'),
            new_instruction_readable="lbz     r11,2(r10)"
        ),
        Patch(
            identifier=158,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d6b0774'),
            new_instruction_readable="extsb   r11,r11"
        ),
        Patch(
            identifier=159,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c0bffbf'),
            new_instruction_readable="cmpwi   r11,-65"
        ),
        Patch(
            identifier=160,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41810818'),
            new_instruction_readable="bgt     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=161,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c0901fd'),
            new_instruction_readable="cmpwi   r9,509"
        ),
        Patch(
            identifier=162,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820810'),
            new_instruction_readable="beq     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=163,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('894a0003'),
            new_instruction_readable="lbz     r10,3(r10)"
        ),
        Patch(
            identifier=164,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d4a0774'),
            new_instruction_readable="extsb   r10,r10"
        ),
        Patch(
            identifier=165,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c0affbf'),
            new_instruction_readable="cmpwi   r10,-65"
        ),
        Patch(
            identifier=166,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41c10800'),
            new_instruction_readable="bgt-    a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=167,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39290003'),
            new_instruction_readable="addi    r9,r9,3"
        ),
        Patch(
            identifier=168,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000034'),
            new_instruction_readable="b       2d0 <print_archipelago_text+0x2d0>"
        ),
        Patch(
            identifier=169,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('556b003c'),
            new_instruction_readable="clrrwi  r11,r11,1"
        ),
        Patch(
            identifier=170,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c0bffee'),
            new_instruction_readable="cmpwi   r11,-18"
        ),
        Patch(
            identifier=171,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('408207ec'),
            new_instruction_readable="bne     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=172,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c00ffc0'),
            new_instruction_readable="cmpwi   r0,-64"
        ),
        Patch(
            identifier=173,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('408007e4'),
            new_instruction_readable="bge     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=174,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280901fe'),
            new_instruction_readable="cmplwi  r9,510"
        ),
        Patch(
            identifier=175,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('408007dc'),
            new_instruction_readable="bge     a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=176,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('894a0002'),
            new_instruction_readable="lbz     r10,2(r10)"
        ),
        Patch(
            identifier=177,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d4a0774'),
            new_instruction_readable="extsb   r10,r10"
        ),
        Patch(
            identifier=178,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2c0affbf'),
            new_instruction_readable="cmpwi   r10,-65"
        ),
        Patch(
            identifier=179,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41c107cc'),
            new_instruction_readable="bgt-    a94 <print_archipelago_text+0xa94>"
        ),
        Patch(
            identifier=180,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39290002'),
            new_instruction_readable="addi    r9,r9,2"
        ),
        Patch(
            identifier=181,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39290001'),
            new_instruction_readable="addi    r9,r9,1"
        ),
        Patch(
            identifier=182,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28090200'),
            new_instruction_readable="cmplwi  r9,512"
        ),
        Patch(
            identifier=183,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4180fdf4'),
            new_instruction_readable="blt     cc <print_archipelago_text+0xcc>"
        ),
        Patch(
            identifier=184,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a000ff'),
            new_instruction_readable="li      r5,255"
        ),
        Patch(
            identifier=185,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=186,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90a10228'),
            new_instruction_readable="stw     r5,552(r1)"
        ),
        Patch(
            identifier=187,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3ca03eb3'),
            new_instruction_readable="lis     r5,16051"
        ),
        Patch(
            identifier=188,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b800000'),
            new_instruction_readable="li      r28,0"
        ),
        Patch(
            identifier=189,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3880ffff'),
            new_instruction_readable="li      r4,-1"
        ),
        Patch(
            identifier=190,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('98610634'),
            new_instruction_readable="stb     r3,1588(r1)"
        ),
        Patch(
            identifier=191,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600055'),
            new_instruction_readable="li      r3,85"
        ),
        Patch(
            identifier=192,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('60a53333'),
            new_instruction_readable="ori     r5,r5,13107"
        ),
        Patch(
            identifier=193,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3e1020c'),
            new_instruction_readable="stfs    f31,524(r1)"
        ),
        Patch(
            identifier=194,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3bc10230'),
            new_instruction_readable="addi    r30,r1,560"
        ),
        Patch(
            identifier=195,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810208'),
            new_instruction_readable="stw     r28,520(r1)"
        ),
        Patch(
            identifier=196,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810210'),
            new_instruction_readable="stw     r28,528(r1)"
        ),
        Patch(
            identifier=197,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810214'),
            new_instruction_readable="stw     r28,532(r1)"
        ),
        Patch(
            identifier=198,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90810224'),
            new_instruction_readable="stw     r4,548(r1)"
        ),
        Patch(
            identifier=199,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9061021c'),
            new_instruction_readable="stw     r3,540(r1)"
        ),
        Patch(
            identifier=200,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3861022e'),
            new_instruction_readable="addi    r3,r1,558"
        ),
        Patch(
            identifier=201,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90810220'),
            new_instruction_readable="stw     r4,544(r1)"
        ),
        Patch(
            identifier=202,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800201'),
            new_instruction_readable="li      r4,513"
        ),
        Patch(
            identifier=203,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9381022c'),
            new_instruction_readable="stw     r28,556(r1)"
        ),
        Patch(
            identifier=204,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90a10218'),
            new_instruction_readable="stw     r5,536(r1)"
        ),
        Patch(
            identifier=205,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00000'),
            new_instruction_readable="li      r5,0"
        ),
        Patch(
            identifier=206,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9b810630'),
            new_instruction_readable="stb     r28,1584(r1)"
        ),
        Patch(
            identifier=207,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c8903a6'),
            new_instruction_readable="mtctr   r4"
        ),
        Patch(
            identifier=208,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=209,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('70a6ffff'),
            new_instruction_readable="andi.   r6,r5,65535"
        ),
        Patch(
            identifier=210,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820010'),
            new_instruction_readable="beq     354 <print_archipelago_text+0x354>"
        ),
        Patch(
            identifier=211,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c00000'),
            new_instruction_readable="li      r6,0"
        ),
        Patch(
            identifier=212,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('420000c8'),
            new_instruction_readable="bdnz    414 <print_archipelago_text+0x414>"
        ),
        Patch(
            identifier=213,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('480000e0'),
            new_instruction_readable="b       430 <print_archipelago_text+0x430>"
        ),
        Patch(
            identifier=214,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28040200'),
            new_instruction_readable="cmplwi  r4,512"
        ),
        Patch(
            identifier=215,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('418200dc'),
            new_instruction_readable="beq     434 <print_archipelago_text+0x434>"
        ),
        Patch(
            identifier=216,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7cbd20ae'),
            new_instruction_readable="lbzx    r5,r29,r4"
        ),
        Patch(
            identifier=217,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7ca60775'),
            new_instruction_readable="extsb.  r6,r5"
        ),
        Patch(
            identifier=218,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41800014'),
            new_instruction_readable="blt     378 <print_archipelago_text+0x378>"
        ),
        Patch(
            identifier=219,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38840001'),
            new_instruction_readable="addi    r4,r4,1"
        ),
        Patch(
            identifier=220,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c00000'),
            new_instruction_readable="li      r6,0"
        ),
        Patch(
            identifier=221,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('420000a4'),
            new_instruction_readable="bdnz    414 <print_archipelago_text+0x414>"
        ),
        Patch(
            identifier=222,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('480000bc'),
            new_instruction_readable="b       430 <print_archipelago_text+0x430>"
        ),
        Patch(
            identifier=223,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d3d2214'),
            new_instruction_readable="add     r9,r29,r4"
        ),
        Patch(
            identifier=224,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('88c90001'),
            new_instruction_readable="lbz     r6,1(r9)"
        ),
        Patch(
            identifier=225,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280500df'),
            new_instruction_readable="cmplwi  r5,223"
        ),
        Patch(
            identifier=226,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('54c606be'),
            new_instruction_readable="clrlwi  r6,r6,26"
        ),
        Patch(
            identifier=227,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40810038'),
            new_instruction_readable="ble     3c0 <print_archipelago_text+0x3c0>"
        ),
        Patch(
            identifier=228,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('89090002'),
            new_instruction_readable="lbz     r8,2(r9)"
        ),
        Patch(
            identifier=229,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280500f0'),
            new_instruction_readable="cmplwi  r5,240"
        ),
        Patch(
            identifier=230,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('54a706fe'),
            new_instruction_readable="clrlwi  r7,r5,27"
        ),
        Patch(
            identifier=231,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41800040'),
            new_instruction_readable="blt     3d8 <print_archipelago_text+0x3d8>"
        ),
        Patch(
            identifier=232,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('88a90003'),
            new_instruction_readable="lbz     r5,3(r9)"
        ),
        Patch(
            identifier=233,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('50c83032'),
            new_instruction_readable="rlwimi  r8,r6,6,0,25"
        ),
        Patch(
            identifier=234,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38840004'),
            new_instruction_readable="addi    r4,r4,4"
        ),
        Patch(
            identifier=235,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('54a506be'),
            new_instruction_readable="clrlwi  r5,r5,26"
        ),
        Patch(
            identifier=236,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('510533b2'),
            new_instruction_readable="rlwimi  r5,r8,6,14,25"
        ),
        Patch(
            identifier=237,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('50e592da'),
            new_instruction_readable="rlwimi  r5,r7,18,11,13"
        ),
        Patch(
            identifier=238,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2805ffff'),
            new_instruction_readable="cmplwi  r5,65535"
        ),
        Patch(
            identifier=239,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4081ff90'),
            new_instruction_readable="ble     348 <print_archipelago_text+0x348>"
        ),
        Patch(
            identifier=240,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000034'),
            new_instruction_readable="b       3f0 <print_archipelago_text+0x3f0>"
        ),
        Patch(
            identifier=241,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('50a63572'),
            new_instruction_readable="rlwimi  r6,r5,6,21,25"
        ),
        Patch(
            identifier=242,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38840002'),
            new_instruction_readable="addi    r4,r4,2"
        ),
        Patch(
            identifier=243,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7cc53378'),
            new_instruction_readable="mr      r5,r6"
        ),
        Patch(
            identifier=244,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c00000'),
            new_instruction_readable="li      r6,0"
        ),
        Patch(
            identifier=245,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('42000044'),
            new_instruction_readable="bdnz    414 <print_archipelago_text+0x414>"
        ),
        Patch(
            identifier=246,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4800005c'),
            new_instruction_readable="b       430 <print_archipelago_text+0x430>"
        ),
        Patch(
            identifier=247,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('50c83532'),
            new_instruction_readable="rlwimi  r8,r6,6,20,25"
        ),
        Patch(
            identifier=248,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('50e86026'),
            new_instruction_readable="rlwimi  r8,r7,12,0,19"
        ),
        Patch(
            identifier=249,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38840003'),
            new_instruction_readable="addi    r4,r4,3"
        ),
        Patch(
            identifier=250,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7d054378'),
            new_instruction_readable="mr      r5,r8"
        ),
        Patch(
            identifier=251,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('2805ffff'),
            new_instruction_readable="cmplwi  r5,65535"
        ),
        Patch(
            identifier=252,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4081ff5c'),
            new_instruction_readable="ble     348 <print_archipelago_text+0x348>"
        ),
        Patch(
            identifier=253,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3cc500ff'),
            new_instruction_readable="addis   r6,r5,255"
        ),
        Patch(
            identifier=254,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('54c6b2be'),
            new_instruction_readable="srwi    r6,r6,10"
        ),
        Patch(
            identifier=255,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('54a505be'),
            new_instruction_readable="clrlwi  r5,r5,22"
        ),
        Patch(
            identifier=256,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('60c6d800'),
            new_instruction_readable="ori     r6,r6,55296"
        ),
        Patch(
            identifier=257,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('64c7ffff'),
            new_instruction_readable="oris    r7,r6,65535"
        ),
        Patch(
            identifier=258,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('60a5dc00'),
            new_instruction_readable="ori     r5,r5,56320"
        ),
        Patch(
            identifier=259,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('64a6ffff'),
            new_instruction_readable="oris    r6,r5,65535"
        ),
        Patch(
            identifier=260,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7ce53b78'),
            new_instruction_readable="mr      r5,r7"
        ),
        Patch(
            identifier=261,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('42400020'),
            new_instruction_readable="bdz     430 <print_archipelago_text+0x430>"
        ),
        Patch(
            identifier=262,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('b0a30002'),
            new_instruction_readable="sth     r5,2(r3)"
        ),
        Patch(
            identifier=263,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38630002'),
            new_instruction_readable="addi    r3,r3,2"
        ),
        Patch(
            identifier=264,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b9c0001'),
            new_instruction_readable="addi    r28,r28,1"
        ),
        Patch(
            identifier=265,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7cc53378'),
            new_instruction_readable="mr      r5,r6"
        ),
        Patch(
            identifier=266,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('70a6ffff'),
            new_instruction_readable="andi.   r6,r5,65535"
        ),
        Patch(
            identifier=267,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4082ff20'),
            new_instruction_readable="bne     348 <print_archipelago_text+0x348>"
        ),
        Patch(
            identifier=268,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4bffff28'),
            new_instruction_readable="b       354 <print_archipelago_text+0x354>"
        ),
        Patch(
            identifier=269,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b800200'),
            new_instruction_readable="li      r28,512"
        ),
        Patch(
            identifier=270,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3ba1069c'),
            new_instruction_readable="addi    r29,r1,1692"
        ),
        Patch(
            identifier=271,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=272,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=273,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00064'),
            new_instruction_readable="li      r5,100"
        ),
        Patch(
            identifier=274,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9381022c'),
            new_instruction_readable="stw     r28,556(r1)"
        ),
        Patch(
            identifier=275,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b400000'),
            new_instruction_readable="li      r26,0"
        ),
        Patch(
            identifier=276,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_memset.name, 1
                ),
            new_instruction_readable="bl memset"
        ),
        Patch(
            identifier=277,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=278,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0___ct__TextWriterBase_WChar.name, 1
                ),
            new_instruction_readable="bl __ct__TextWriterBase_WChar"
        ),
        Patch(
            identifier=279,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3c603f00'),
            new_instruction_readable="lis     r3,16128"
        ),
        Patch(
            identifier=280,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('906106c0'),
            new_instruction_readable="stw     r3,1728(r1)"
        ),
        Patch(
            identifier=281,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('906106c4'),
            new_instruction_readable="stw     r3,1732(r1)"
        ),
        Patch(
            identifier=282,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600002'),
            new_instruction_readable="li      r3,2"
        ),
        Patch(
            identifier=283,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('906106bc'),
            new_instruction_readable="stw     r3,1724(r1)"
        ),
        Patch(
            identifier=284,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('386000ff'),
            new_instruction_readable="li      r3,255"
        ),
        Patch(
            identifier=285,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('906106b4'),
            new_instruction_readable="stw     r3,1716(r1)"
        ),
        Patch(
            identifier=286,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('906106b8'),
            new_instruction_readable="stw     r3,1720(r1)"
        ),
        Patch(
            identifier=287,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=288,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CharWriter__UpdateVertexColor.name, 1
                ),
            new_instruction_readable="bl CharWriter__UpdateVertexColor"
        ),
        Patch(
            identifier=289,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3c60c080'),
            new_instruction_readable="lis     r3,-16256"
        ),
        Patch(
            identifier=290,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b610638'),
            new_instruction_readable="addi    r27,r1,1592"
        ),
        Patch(
            identifier=291,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b20ffff'),
            new_instruction_readable="li      r25,-1"
        ),
        Patch(
            identifier=292,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('906106f0'),
            new_instruction_readable="stw     r3,1776(r1)"
        ),
        Patch(
            identifier=293,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa4eb78'),
            new_instruction_readable="mr      r4,r29"
        ),
        Patch(
            identifier=294,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f63db78'),
            new_instruction_readable="mr      r3,r27"
        ),
        Patch(
            identifier=295,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00064'),
            new_instruction_readable="li      r5,100"
        ),
        Patch(
            identifier=296,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9341069c'),
            new_instruction_readable="stw     r26,1692(r1)"
        ),
        Patch(
            identifier=297,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('932106a0'),
            new_instruction_readable="stw     r25,1696(r1)"
        ),
        Patch(
            identifier=298,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_memcpy.name, 1
                ),
            new_instruction_readable="bl memcpy"
        ),
        Patch(
            identifier=299,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f63db78'),
            new_instruction_readable="mr      r3,r27"
        ),
        Patch(
            identifier=300,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93210650'),
            new_instruction_readable="stw     r25,1616(r1)"
        ),
        Patch(
            identifier=301,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93210654'),
            new_instruction_readable="stw     r25,1620(r1)"
        ),
        Patch(
            identifier=302,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CharWriter__UpdateVertexColor.name, 1
                ),
            new_instruction_readable="bl CharWriter__UpdateVertexColor"
        ),
        Patch(
            identifier=303,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3c603eb3'),
            new_instruction_readable="lis     r3,16051"
        ),
        Patch(
            identifier=304,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('60633333'),
            new_instruction_readable="ori     r3,r3,13107"
        ),
        Patch(
            identifier=305,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9061065c'),
            new_instruction_readable="stw     r3,1628(r1)"
        ),
        Patch(
            identifier=306,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610660'),
            new_instruction_readable="stw     r3,1632(r1)"
        ),
        Patch(
            identifier=307,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_get_font_data.name, 1
                ),
            new_instruction_readable="bl get_font_data"
        ),
        Patch(
            identifier=308,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('80630000'),
            new_instruction_readable="lwz     r3,0(r3)"
        ),
        Patch(
            identifier=309,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('88810634'),
            new_instruction_readable="lbz     r4,1588(r1)"
        ),
        Patch(
            identifier=310,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38630010'),
            new_instruction_readable="addi    r3,r3,16"
        ),
        Patch(
            identifier=311,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610680'),
            new_instruction_readable="stw     r3,1664(r1)"
        ),
        Patch(
            identifier=312,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 3),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=313,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c363'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 3),
            new_instruction_readable="lfs     f27,0(r3)"
        ),
        Patch(
            identifier=314,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28040000'),
            new_instruction_readable="cmplwi  r4,0"
        ),
        Patch(
            identifier=315,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4182004c'),
            new_instruction_readable="beq     534 <print_archipelago_text+0x534>"
        ),
        Patch(
            identifier=316,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('281c0000'),
            new_instruction_readable="cmplwi  r28,0"
        ),
        Patch(
            identifier=317,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('934106a8'),
            new_instruction_readable="stw     r26,1704(r1)"
        ),
        Patch(
            identifier=318,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('934106a4'),
            new_instruction_readable="stw     r26,1700(r1)"
        ),
        Patch(
            identifier=319,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('934106a0'),
            new_instruction_readable="stw     r26,1696(r1)"
        ),
        Patch(
            identifier=320,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9341069c'),
            new_instruction_readable="stw     r26,1692(r1)"
        ),
        Patch(
            identifier=321,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41c2059c'),
            new_instruction_readable="beq-    a9c <print_archipelago_text+0xa9c>"
        ),
        Patch(
            identifier=322,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('5783083c'),
            new_instruction_readable="slwi    r3,r28,1"
        ),
        Patch(
            identifier=323,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c9e1a14'),
            new_instruction_readable="add     r4,r30,r3"
        ),
        Patch(
            identifier=324,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('a084fffe'),
            new_instruction_readable="lhz     r4,-2(r4)"
        ),
        Patch(
            identifier=325,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28040000'),
            new_instruction_readable="cmplwi  r4,0"
        ),
        Patch(
            identifier=326,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820048'),
            new_instruction_readable="beq     55c <print_archipelago_text+0x55c>"
        ),
        Patch(
            identifier=327,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('281c01ff'),
            new_instruction_readable="cmplwi  r28,511"
        ),
        Patch(
            identifier=328,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4181002c'),
            new_instruction_readable="bgt     548 <print_archipelago_text+0x548>"
        ),
        Patch(
            identifier=329,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=330,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c9e1b2e'),
            new_instruction_readable="sthx    r4,r30,r3"
        ),
        Patch(
            identifier=331,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('387c0001'),
            new_instruction_readable="addi    r3,r28,1"
        ),
        Patch(
            identifier=332,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9061022c'),
            new_instruction_readable="stw     r3,556(r1)"
        ),
        Patch(
            identifier=333,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4800001c'),
            new_instruction_readable="b       54c <print_archipelago_text+0x54c>"
        ),
        Patch(
            identifier=334,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600055'),
            new_instruction_readable="li      r3,85"
        ),
        Patch(
            identifier=335,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ffc0d890'),
            new_instruction_readable="fmr     f30,f27"
        ),
        Patch(
            identifier=336,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ff40d890'),
            new_instruction_readable="fmr     f26,f27"
        ),
        Patch(
            identifier=337,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ff20d890'),
            new_instruction_readable="fmr     f25,f27"
        ),
        Patch(
            identifier=338,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000068'),
            new_instruction_readable="b       5ac <print_archipelago_text+0x5ac>"
        ),
        Patch(
            identifier=339,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b9cffff'),
            new_instruction_readable="addi    r28,r28,-1"
        ),
        Patch(
            identifier=340,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('5783083c'),
            new_instruction_readable="slwi    r3,r28,1"
        ),
        Patch(
            identifier=341,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=342,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c9e1b2e'),
            new_instruction_readable="sthx    r4,r30,r3"
        ),
        Patch(
            identifier=343,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('8381022c'),
            new_instruction_readable="lwz     r28,556(r1)"
        ),
        Patch(
            identifier=344,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610638'),
            new_instruction_readable="addi    r3,r1,1592"
        ),
        Patch(
            identifier=345,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3881069c'),
            new_instruction_readable="addi    r4,r1,1692"
        ),
        Patch(
            identifier=346,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fc5f378'),
            new_instruction_readable="mr      r5,r30"
        ),
        Patch(
            identifier=347,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f86e378'),
            new_instruction_readable="mr      r6,r28"
        ),
        Patch(
            identifier=348,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CalcStringRect_TextWriterBase_WChar.name, 1
                ),
            new_instruction_readable="bl CalcStringRect_TextWriterBase_WChar"
        ),
        Patch(
            identifier=349,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 4),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=350,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c04106a4'),
            new_instruction_readable="lfs     f2,1700(r1)"
        ),
        Patch(
            identifier=351,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c063'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 4),
            new_instruction_readable="lfs     f3,0(r3)"
        ),
        Patch(
            identifier=352,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c08106a8'),
            new_instruction_readable="lfs     f4,1704(r1)"
        ),
        Patch(
            identifier=353,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c001069c'),
            new_instruction_readable="lfs     f0,1692(r1)"
        ),
        Patch(
            identifier=354,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ec42182a'),
            new_instruction_readable="fadds   f2,f2,f3"
        ),
        Patch(
            identifier=355,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c02106a0'),
            new_instruction_readable="lfs     f1,1696(r1)"
        ),
        Patch(
            identifier=356,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ec64182a'),
            new_instruction_readable="fadds   f3,f4,f3"
        ),
        Patch(
            identifier=357,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ef220028'),
            new_instruction_readable="fsubs   f25,f2,f0"
        ),
        Patch(
            identifier=358,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c3c10208'),
            new_instruction_readable="lfs     f30,520(r1)"
        ),
        Patch(
            identifier=359,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ef430828'),
            new_instruction_readable="fsubs   f26,f3,f1"
        ),
        Patch(
            identifier=360,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c3e1020c'),
            new_instruction_readable="lfs     f31,524(r1)"
        ),
        Patch(
            identifier=361,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3210210'),
            new_instruction_readable="stfs    f25,528(r1)"
        ),
        Patch(
            identifier=362,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3410214'),
            new_instruction_readable="stfs    f26,532(r1)"
        ),
        Patch(
            identifier=363,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('8061021c'),
            new_instruction_readable="lwz     r3,540(r1)"
        ),
        Patch(
            identifier=364,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610700'),
            new_instruction_readable="stw     r3,1792(r1)"
        ),
        Patch(
            identifier=365,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3c603f80'),
            new_instruction_readable="lis     r3,16256"
        ),
        Patch(
            identifier=366,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3ba1069c'),
            new_instruction_readable="addi    r29,r1,1692"
        ),
        Patch(
            identifier=367,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610704'),
            new_instruction_readable="stw     r3,1796(r1)"
        ),
        Patch(
            identifier=368,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=369,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610718'),
            new_instruction_readable="stw     r3,1816(r1)"
        ),
        Patch(
            identifier=370,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00040'),
            new_instruction_readable="li      r5,64"
        ),
        Patch(
            identifier=371,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9061072c'),
            new_instruction_readable="stw     r3,1836(r1)"
        ),
        Patch(
            identifier=372,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=373,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410708'),
            new_instruction_readable="stw     r26,1800(r1)"
        ),
        Patch(
            identifier=374,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9341070c'),
            new_instruction_readable="stw     r26,1804(r1)"
        ),
        Patch(
            identifier=375,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410710'),
            new_instruction_readable="stw     r26,1808(r1)"
        ),
        Patch(
            identifier=376,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410714'),
            new_instruction_readable="stw     r26,1812(r1)"
        ),
        Patch(
            identifier=377,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9341071c'),
            new_instruction_readable="stw     r26,1820(r1)"
        ),
        Patch(
            identifier=378,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410720'),
            new_instruction_readable="stw     r26,1824(r1)"
        ),
        Patch(
            identifier=379,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410724'),
            new_instruction_readable="stw     r26,1828(r1)"
        ),
        Patch(
            identifier=380,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410728'),
            new_instruction_readable="stw     r26,1832(r1)"
        ),
        Patch(
            identifier=381,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410730'),
            new_instruction_readable="stw     r26,1840(r1)"
        ),
        Patch(
            identifier=382,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_memset.name, 1
                ),
            new_instruction_readable="bl memset"
        ),
        Patch(
            identifier=383,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 5),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=384,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c303'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 5),
            new_instruction_readable="lfs     f24,0(r3)"
        ),
        Patch(
            identifier=385,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('efbaf82a'),
            new_instruction_readable="fadds   f29,f26,f31"
        ),
        Patch(
            identifier=386,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ef99f02a'),
            new_instruction_readable="fadds   f28,f25,f30"
        ),
        Patch(
            identifier=387,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=388,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20f890'),
            new_instruction_readable="fmr     f1,f31"
        ),
        Patch(
            identifier=389,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc40e890'),
            new_instruction_readable="fmr     f2,f29"
        ),
        Patch(
            identifier=390,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc60f090'),
            new_instruction_readable="fmr     f3,f30"
        ),
        Patch(
            identifier=391,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc80e090'),
            new_instruction_readable="fmr     f4,f28"
        ),
        Patch(
            identifier=392,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fca0d890'),
            new_instruction_readable="fmr     f5,f27"
        ),
        Patch(
            identifier=393,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fcc0c090'),
            new_instruction_readable="fmr     f6,f24"
        ),
        Patch(
            identifier=394,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_C_MTXOrtho.name, 1
                ),
            new_instruction_readable="bl C_MTXOrtho"
        ),
        Patch(
            identifier=395,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=396,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800001'),
            new_instruction_readable="li      r4,1"
        ),
        Patch(
            identifier=397,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetProjection.name, 1
                ),
            new_instruction_readable="bl GXSetProjection"
        ),
        Patch(
            identifier=398,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20f090'),
            new_instruction_readable="fmr     f1,f30"
        ),
        Patch(
            identifier=399,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc40f890'),
            new_instruction_readable="fmr     f2,f31"
        ),
        Patch(
            identifier=400,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc60c890'),
            new_instruction_readable="fmr     f3,f25"
        ),
        Patch(
            identifier=401,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc80d090'),
            new_instruction_readable="fmr     f4,f26"
        ),
        Patch(
            identifier=402,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fca0d890'),
            new_instruction_readable="fmr     f5,f27"
        ),
        Patch(
            identifier=403,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fcc0c090'),
            new_instruction_readable="fmr     f6,f24"
        ),
        Patch(
            identifier=404,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetViewport.name, 1
                ),
            new_instruction_readable="bl GXSetViewport"
        ),
        Patch(
            identifier=405,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20f090'),
            new_instruction_readable="fmr     f1,f30"
        ),
        Patch(
            identifier=406,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_float_to_unsigned.name, 1
                ),
            new_instruction_readable="bl float_to_unsigned"
        ),
        Patch(
            identifier=407,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20f890'),
            new_instruction_readable="fmr     f1,f31"
        ),
        Patch(
            identifier=408,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c7d1b78'),
            new_instruction_readable="mr      r29,r3"
        ),
        Patch(
            identifier=409,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_float_to_unsigned.name, 1
                ),
            new_instruction_readable="bl float_to_unsigned"
        ),
        Patch(
            identifier=410,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20c890'),
            new_instruction_readable="fmr     f1,f25"
        ),
        Patch(
            identifier=411,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c7c1b78'),
            new_instruction_readable="mr      r28,r3"
        ),
        Patch(
            identifier=412,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_float_to_unsigned.name, 1
                ),
            new_instruction_readable="bl float_to_unsigned"
        ),
        Patch(
            identifier=413,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20d090'),
            new_instruction_readable="fmr     f1,f26"
        ),
        Patch(
            identifier=414,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c7b1b78'),
            new_instruction_readable="mr      r27,r3"
        ),
        Patch(
            identifier=415,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_float_to_unsigned.name, 1
                ),
            new_instruction_readable="bl float_to_unsigned"
        ),
        Patch(
            identifier=416,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c661b78'),
            new_instruction_readable="mr      r6,r3"
        ),
        Patch(
            identifier=417,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=418,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f84e378'),
            new_instruction_readable="mr      r4,r28"
        ),
        Patch(
            identifier=419,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f65db78'),
            new_instruction_readable="mr      r5,r27"
        ),
        Patch(
            identifier=420,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetScissor.name, 1
                ),
            new_instruction_readable="bl GXSetScissor"
        ),
        Patch(
            identifier=421,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610704'),
            new_instruction_readable="addi    r3,r1,1796"
        ),
        Patch(
            identifier=422,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=423,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXLoadPosMtxImm.name, 1
                ),
            new_instruction_readable="bl GXLoadPosMtxImm"
        ),
        Patch(
            identifier=424,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=425,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetCurrentMtx.name, 1
                ),
            new_instruction_readable="bl GXSetCurrentMtx"
        ),
        Patch(
            identifier=426,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXClearVtxDesc.name, 1
                ),
            new_instruction_readable="bl GXClearVtxDesc"
        ),
        Patch(
            identifier=427,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXInvalidateVtxCache.name, 1
                ),
            new_instruction_readable="bl GXInvalidateVtxCache"
        ),
        Patch(
            identifier=428,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600009'),
            new_instruction_readable="li      r3,9"
        ),
        Patch(
            identifier=429,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800001'),
            new_instruction_readable="li      r4,1"
        ),
        Patch(
            identifier=430,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetVtxDesc.name, 1
                ),
            new_instruction_readable="bl GXSetVtxDesc"
        ),
        Patch(
            identifier=431,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=432,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800009'),
            new_instruction_readable="li      r4,9"
        ),
        Patch(
            identifier=433,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00001'),
            new_instruction_readable="li      r5,1"
        ),
        Patch(
            identifier=434,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c00004'),
            new_instruction_readable="li      r6,4"
        ),
        Patch(
            identifier=435,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38e00000'),
            new_instruction_readable="li      r7,0"
        ),
        Patch(
            identifier=436,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetVtxAttrFmt.name, 1
                ),
            new_instruction_readable="bl GXSetVtxAttrFmt"
        ),
        Patch(
            identifier=437,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=438,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetNumChans.name, 1
                ),
            new_instruction_readable="bl GXSetNumChans"
        ),
        Patch(
            identifier=439,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38810700'),
            new_instruction_readable="addi    r4,r1,1792"
        ),
        Patch(
            identifier=440,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600004'),
            new_instruction_readable="li      r3,4"
        ),
        Patch(
            identifier=441,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetChanMatColor.name, 1
                ),
            new_instruction_readable="bl GXSetChanMatColor"
        ),
        Patch(
            identifier=442,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600004'),
            new_instruction_readable="li      r3,4"
        ),
        Patch(
            identifier=443,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=444,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00000'),
            new_instruction_readable="li      r5,0"
        ),
        Patch(
            identifier=445,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c00000'),
            new_instruction_readable="li      r6,0"
        ),
        Patch(
            identifier=446,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38e00000'),
            new_instruction_readable="li      r7,0"
        ),
        Patch(
            identifier=447,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39000000'),
            new_instruction_readable="li      r8,0"
        ),
        Patch(
            identifier=448,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('39200002'),
            new_instruction_readable="li      r9,2"
        ),
        Patch(
            identifier=449,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetChanCtrl.name, 1
                ),
            new_instruction_readable="bl GXSetChanCtrl"
        ),
        Patch(
            identifier=450,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=451,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetNumTexGens.name, 1
                ),
            new_instruction_readable="bl GXSetNumTexGens"
        ),
        Patch(
            identifier=452,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=453,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetNumIndStages.name, 1
                ),
            new_instruction_readable="bl GXSetNumIndStages"
        ),
        Patch(
            identifier=454,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=455,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0___GXSetIndirectMask.name, 1
                ),
            new_instruction_readable="bl __GXSetIndirectMask"
        ),
        Patch(
            identifier=456,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=457,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetNumTevStages.name, 1
                ),
            new_instruction_readable="bl GXSetNumTevStages"
        ),
        Patch(
            identifier=458,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=459,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800004'),
            new_instruction_readable="li      r4,4"
        ),
        Patch(
            identifier=460,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetTevOp.name, 1
                ),
            new_instruction_readable="bl GXSetTevOp"
        ),
        Patch(
            identifier=461,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=462,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('388000ff'),
            new_instruction_readable="li      r4,255"
        ),
        Patch(
            identifier=463,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a000ff'),
            new_instruction_readable="li      r5,255"
        ),
        Patch(
            identifier=464,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c00004'),
            new_instruction_readable="li      r6,4"
        ),
        Patch(
            identifier=465,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetTevOrder.name, 1
                ),
            new_instruction_readable="bl GXSetTevOrder"
        ),
        Patch(
            identifier=466,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('88610703'),
            new_instruction_readable="lbz     r3,1795(r1)"
        ),
        Patch(
            identifier=467,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('686300ff'),
            new_instruction_readable="xori    r3,r3,255"
        ),
        Patch(
            identifier=468,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28030000'),
            new_instruction_readable="cmplwi  r3,0"
        ),
        Patch(
            identifier=469,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40820014'),
            new_instruction_readable="bne     764 <print_archipelago_text+0x764>"
        ),
        Patch(
            identifier=470,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=471,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800001'),
            new_instruction_readable="li      r4,1"
        ),
        Patch(
            identifier=472,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00000'),
            new_instruction_readable="li      r5,0"
        ),
        Patch(
            identifier=473,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000010'),
            new_instruction_readable="b       770 <print_archipelago_text+0x770>"
        ),
        Patch(
            identifier=474,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=475,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800004'),
            new_instruction_readable="li      r4,4"
        ),
        Patch(
            identifier=476,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00005'),
            new_instruction_readable="li      r5,5"
        ),
        Patch(
            identifier=477,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c0000f'),
            new_instruction_readable="li      r6,15"
        ),
        Patch(
            identifier=478,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetBlendMode.name, 1
                ),
            new_instruction_readable="bl GXSetBlendMode"
        ),
        Patch(
            identifier=479,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=480,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetColorUpdate.name, 1
                ),
            new_instruction_readable="bl GXSetColorUpdate"
        ),
        Patch(
            identifier=481,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=482,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetAlphaUpdate.name, 1
                ),
            new_instruction_readable="bl GXSetAlphaUpdate"
        ),
        Patch(
            identifier=483,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=484,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=485,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00000'),
            new_instruction_readable="li      r5,0"
        ),
        Patch(
            identifier=486,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b800000'),
            new_instruction_readable="li      r28,0"
        ),
        Patch(
            identifier=487,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetZMode.name, 1
                ),
            new_instruction_readable="bl GXSetZMode"
        ),
        Patch(
            identifier=488,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600002'),
            new_instruction_readable="li      r3,2"
        ),
        Patch(
            identifier=489,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetCullMode.name, 1
                ),
            new_instruction_readable="bl GXSetCullMode"
        ),
        Patch(
            identifier=490,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600080'),
            new_instruction_readable="li      r3,128"
        ),
        Patch(
            identifier=491,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=492,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00004'),
            new_instruction_readable="li      r5,4"
        ),
        Patch(
            identifier=493,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXBegin.name, 1
                ),
            new_instruction_readable="bl GXBegin"
        ),
        Patch(
            identifier=494,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3c60cc01'),
            new_instruction_readable="lis     r3,-13311"
        ),
        Patch(
            identifier=495,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3c38000'),
            new_instruction_readable="stfs    f30,-32768(r3)"
        ),
        Patch(
            identifier=496,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3ba1069c'),
            new_instruction_readable="addi    r29,r1,1692"
        ),
        Patch(
            identifier=497,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3e38000'),
            new_instruction_readable="stfs    f31,-32768(r3)"
        ),
        Patch(
            identifier=498,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=499,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93838000'),
            new_instruction_readable="stw     r28,-32768(r3)"
        ),
        Patch(
            identifier=500,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00040'),
            new_instruction_readable="li      r5,64"
        ),
        Patch(
            identifier=501,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3838000'),
            new_instruction_readable="stfs    f28,-32768(r3)"
        ),
        Patch(
            identifier=502,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3e38000'),
            new_instruction_readable="stfs    f31,-32768(r3)"
        ),
        Patch(
            identifier=503,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93838000'),
            new_instruction_readable="stw     r28,-32768(r3)"
        ),
        Patch(
            identifier=504,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3838000'),
            new_instruction_readable="stfs    f28,-32768(r3)"
        ),
        Patch(
            identifier=505,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3a38000'),
            new_instruction_readable="stfs    f29,-32768(r3)"
        ),
        Patch(
            identifier=506,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93838000'),
            new_instruction_readable="stw     r28,-32768(r3)"
        ),
        Patch(
            identifier=507,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3c38000'),
            new_instruction_readable="stfs    f30,-32768(r3)"
        ),
        Patch(
            identifier=508,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d3a38000'),
            new_instruction_readable="stfs    f29,-32768(r3)"
        ),
        Patch(
            identifier=509,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93838000'),
            new_instruction_readable="stw     r28,-32768(r3)"
        ),
        Patch(
            identifier=510,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 6),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=511,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c003'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 6),
            new_instruction_readable="lfs     f0,0(r3)"
        ),
        Patch(
            identifier=512,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3c603f80'),
            new_instruction_readable="lis     r3,16256"
        ),
        Patch(
            identifier=513,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c0210208'),
            new_instruction_readable="lfs     f1,520(r1)"
        ),
        Patch(
            identifier=514,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c041020c'),
            new_instruction_readable="lfs     f2,524(r1)"
        ),
        Patch(
            identifier=515,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610704'),
            new_instruction_readable="stw     r3,1796(r1)"
        ),
        Patch(
            identifier=516,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ec21002a'),
            new_instruction_readable="fadds   f1,f1,f0"
        ),
        Patch(
            identifier=517,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610718'),
            new_instruction_readable="stw     r3,1816(r1)"
        ),
        Patch(
            identifier=518,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('ec02002a'),
            new_instruction_readable="fadds   f0,f2,f0"
        ),
        Patch(
            identifier=519,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9061072c'),
            new_instruction_readable="stw     r3,1836(r1)"
        ),
        Patch(
            identifier=520,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=521,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810708'),
            new_instruction_readable="stw     r28,1800(r1)"
        ),
        Patch(
            identifier=522,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9381070c'),
            new_instruction_readable="stw     r28,1804(r1)"
        ),
        Patch(
            identifier=523,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810714'),
            new_instruction_readable="stw     r28,1812(r1)"
        ),
        Patch(
            identifier=524,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9381071c'),
            new_instruction_readable="stw     r28,1820(r1)"
        ),
        Patch(
            identifier=525,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810724'),
            new_instruction_readable="stw     r28,1828(r1)"
        ),
        Patch(
            identifier=526,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810728'),
            new_instruction_readable="stw     r28,1832(r1)"
        ),
        Patch(
            identifier=527,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d0210710'),
            new_instruction_readable="stfs    f1,1808(r1)"
        ),
        Patch(
            identifier=528,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d0010720'),
            new_instruction_readable="stfs    f0,1824(r1)"
        ),
        Patch(
            identifier=529,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810730'),
            new_instruction_readable="stw     r28,1840(r1)"
        ),
        Patch(
            identifier=530,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_memset.name, 1
                ),
            new_instruction_readable="bl memset"
        ),
        Patch(
            identifier=531,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 7),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=532,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c3e3'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 7),
            new_instruction_readable="lfs     f31,0(r3)"
        ),
        Patch(
            identifier=533,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 8),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=534,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c3c3'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 8),
            new_instruction_readable="lfs     f30,0(r3)"
        ),
        Patch(
            identifier=535,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 3),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=536,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c3a3'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 3),
            new_instruction_readable="lfs     f29,0(r3)"
        ),
        Patch(
            identifier=537,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 9),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=538,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c0c3'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 9),
            new_instruction_readable="lfs     f6,0(r3)"
        ),
        Patch(
            identifier=539,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=540,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20e890'),
            new_instruction_readable="fmr     f1,f29"
        ),
        Patch(
            identifier=541,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc40f890'),
            new_instruction_readable="fmr     f2,f31"
        ),
        Patch(
            identifier=542,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc60e890'),
            new_instruction_readable="fmr     f3,f29"
        ),
        Patch(
            identifier=543,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc80f090'),
            new_instruction_readable="fmr     f4,f30"
        ),
        Patch(
            identifier=544,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fca0e890'),
            new_instruction_readable="fmr     f5,f29"
        ),
        Patch(
            identifier=545,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_C_MTXOrtho.name, 1
                ),
            new_instruction_readable="bl C_MTXOrtho"
        ),
        Patch(
            identifier=546,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa3eb78'),
            new_instruction_readable="mr      r3,r29"
        ),
        Patch(
            identifier=547,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800001'),
            new_instruction_readable="li      r4,1"
        ),
        Patch(
            identifier=548,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetProjection.name, 1
                ),
            new_instruction_readable="bl GXSetProjection"
        ),
        Patch(
            identifier=549,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_cst4.name, 5),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=550,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                'c0c3'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_cst4.name, 5),
            new_instruction_readable="lfs     f6,0(r3)"
        ),
        Patch(
            identifier=551,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc20e890'),
            new_instruction_readable="fmr     f1,f29"
        ),
        Patch(
            identifier=552,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc40e890'),
            new_instruction_readable="fmr     f2,f29"
        ),
        Patch(
            identifier=553,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc60f090'),
            new_instruction_readable="fmr     f3,f30"
        ),
        Patch(
            identifier=554,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fc80f890'),
            new_instruction_readable="fmr     f4,f31"
        ),
        Patch(
            identifier=555,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('fca0e890'),
            new_instruction_readable="fmr     f5,f29"
        ),
        Patch(
            identifier=556,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetViewport.name, 1
                ),
            new_instruction_readable="bl GXSetViewport"
        ),
        Patch(
            identifier=557,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610704'),
            new_instruction_readable="addi    r3,r1,1796"
        ),
        Patch(
            identifier=558,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=559,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXLoadPosMtxImm.name, 1
                ),
            new_instruction_readable="bl GXLoadPosMtxImm"
        ),
        Patch(
            identifier=560,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600000'),
            new_instruction_readable="li      r3,0"
        ),
        Patch(
            identifier=561,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetCurrentMtx.name, 1
                ),
            new_instruction_readable="bl GXSetCurrentMtx"
        ),
        Patch(
            identifier=562,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('8061022c'),
            new_instruction_readable="lwz     r3,556(r1)"
        ),
        Patch(
            identifier=563,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9381066c'),
            new_instruction_readable="stw     r28,1644(r1)"
        ),
        Patch(
            identifier=564,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28030000'),
            new_instruction_readable="cmplwi  r3,0"
        ),
        Patch(
            identifier=565,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810668'),
            new_instruction_readable="stw     r28,1640(r1)"
        ),
        Patch(
            identifier=566,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93810664'),
            new_instruction_readable="stw     r28,1636(r1)"
        ),
        Patch(
            identifier=567,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820164'),
            new_instruction_readable="beq     a3c <print_archipelago_text+0xa3c>"
        ),
        Patch(
            identifier=568,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('5464083c'),
            new_instruction_readable="slwi    r4,r3,1"
        ),
        Patch(
            identifier=569,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7cbe2214'),
            new_instruction_readable="add     r5,r30,r4"
        ),
        Patch(
            identifier=570,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('a0a5fffe'),
            new_instruction_readable="lhz     r5,-2(r5)"
        ),
        Patch(
            identifier=571,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('80c10228'),
            new_instruction_readable="lwz     r6,552(r1)"
        ),
        Patch(
            identifier=572,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28050000'),
            new_instruction_readable="cmplwi  r5,0"
        ),
        Patch(
            identifier=573,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3ca0'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_data.name, 1),
            new_instruction_readable="lis     r5,0"
        ),
        Patch(
            identifier=574,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '90c5'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_data.name, 1),
            new_instruction_readable="stw     r6,0(r5)"
        ),
        Patch(
            identifier=575,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3ca0'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_data.name, 2),
            new_instruction_readable="lis     r5,0"
        ),
        Patch(
            identifier=576,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '90c5'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_data.name, 2),
            new_instruction_readable="stw     r6,0(r5)"
        ),
        Patch(
            identifier=577,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41820030'),
            new_instruction_readable="beq     930 <print_archipelago_text+0x930>"
        ),
        Patch(
            identifier=578,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('280301ff'),
            new_instruction_readable="cmplwi  r3,511"
        ),
        Patch(
            identifier=579,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41810018'),
            new_instruction_readable="bgt     920 <print_archipelago_text+0x920>"
        ),
        Patch(
            identifier=580,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00000'),
            new_instruction_readable="li      r5,0"
        ),
        Patch(
            identifier=581,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7cbe232e'),
            new_instruction_readable="sthx    r5,r30,r4"
        ),
        Patch(
            identifier=582,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38830001'),
            new_instruction_readable="addi    r4,r3,1"
        ),
        Patch(
            identifier=583,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9081022c'),
            new_instruction_readable="stw     r4,556(r1)"
        ),
        Patch(
            identifier=584,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000008'),
            new_instruction_readable="b       924 <print_archipelago_text+0x924>"
        ),
        Patch(
            identifier=585,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3863ffff'),
            new_instruction_readable="addi    r3,r3,-1"
        ),
        Patch(
            identifier=586,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('5463083c'),
            new_instruction_readable="slwi    r3,r3,1"
        ),
        Patch(
            identifier=587,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=588,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c9e1b2e'),
            new_instruction_readable="sthx    r4,r30,r3"
        ),
        Patch(
            identifier=589,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('80610224'),
            new_instruction_readable="lwz     r3,548(r1)"
        ),
        Patch(
            identifier=590,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b610664'),
            new_instruction_readable="addi    r27,r1,1636"
        ),
        Patch(
            identifier=591,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610650'),
            new_instruction_readable="stw     r3,1616(r1)"
        ),
        Patch(
            identifier=592,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610654'),
            new_instruction_readable="stw     r3,1620(r1)"
        ),
        Patch(
            identifier=593,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610638'),
            new_instruction_readable="addi    r3,r1,1592"
        ),
        Patch(
            identifier=594,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CharWriter__UpdateVertexColor.name, 1
                ),
            new_instruction_readable="bl CharWriter__UpdateVertexColor"
        ),
        Patch(
            identifier=595,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('88610630'),
            new_instruction_readable="lbz     r3,1584(r1)"
        ),
        Patch(
            identifier=596,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('28030000'),
            new_instruction_readable="cmplwi  r3,0"
        ),
        Patch(
            identifier=597,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4182002c'),
            new_instruction_readable="beq     97c <print_archipelago_text+0x97c>"
        ),
        Patch(
            identifier=598,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_get_font_data.name, 1
                ),
            new_instruction_readable="bl get_font_data"
        ),
        Patch(
            identifier=599,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('80630000'),
            new_instruction_readable="lwz     r3,0(r3)"
        ),
        Patch(
            identifier=600,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3880002d'),
            new_instruction_readable="li      r4,45"
        ),
        Patch(
            identifier=601,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38630010'),
            new_instruction_readable="addi    r3,r3,16"
        ),
        Patch(
            identifier=602,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610680'),
            new_instruction_readable="stw     r3,1664(r1)"
        ),
        Patch(
            identifier=603,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610638'),
            new_instruction_readable="addi    r3,r1,1592"
        ),
        Patch(
            identifier=604,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CharWriter__GetFontWidth.name, 1
                ),
            new_instruction_readable="bl CharWriter__GetFontWidth"
        ),
        Patch(
            identifier=605,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=606,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('d021067c'),
            new_instruction_readable="stfs    f1,1660(r1)"
        ),
        Patch(
            identifier=607,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9861067b'),
            new_instruction_readable="stb     r3,1659(r1)"
        ),
        Patch(
            identifier=608,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83a1022c'),
            new_instruction_readable="lwz     r29,556(r1)"
        ),
        Patch(
            identifier=609,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_get_font_data.name, 1
                ),
            new_instruction_readable="bl get_font_data"
        ),
        Patch(
            identifier=610,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('80630000'),
            new_instruction_readable="lwz     r3,0(r3)"
        ),
        Patch(
            identifier=611,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3b810638'),
            new_instruction_readable="addi    r28,r1,1592"
        ),
        Patch(
            identifier=612,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38630010'),
            new_instruction_readable="addi    r3,r3,16"
        ),
        Patch(
            identifier=613,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610680'),
            new_instruction_readable="stw     r3,1664(r1)"
        ),
        Patch(
            identifier=614,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f83e378'),
            new_instruction_readable="mr      r3,r28"
        ),
        Patch(
            identifier=615,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CharWriter__SetupGX.name, 1
                ),
            new_instruction_readable="bl CharWriter__SetupGX"
        ),
        Patch(
            identifier=616,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600007'),
            new_instruction_readable="li      r3,7"
        ),
        Patch(
            identifier=617,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38800000'),
            new_instruction_readable="li      r4,0"
        ),
        Patch(
            identifier=618,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38a00000'),
            new_instruction_readable="li      r5,0"
        ),
        Patch(
            identifier=619,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38c00007'),
            new_instruction_readable="li      r6,7"
        ),
        Patch(
            identifier=620,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38e00000'),
            new_instruction_readable="li      r7,0"
        ),
        Patch(
            identifier=621,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_GXSetAlphaCompare.name, 1
                ),
            new_instruction_readable="bl GXSetAlphaCompare"
        ),
        Patch(
            identifier=622,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('807b0000'),
            new_instruction_readable="lwz     r3,0(r27)"
        ),
        Patch(
            identifier=623,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('809b0004'),
            new_instruction_readable="lwz     r4,4(r27)"
        ),
        Patch(
            identifier=624,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9061069c'),
            new_instruction_readable="stw     r3,1692(r1)"
        ),
        Patch(
            identifier=625,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('807b0008'),
            new_instruction_readable="lwz     r3,8(r27)"
        ),
        Patch(
            identifier=626,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('908106a0'),
            new_instruction_readable="stw     r4,1696(r1)"
        ),
        Patch(
            identifier=627,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c80'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_data.name, 1),
            new_instruction_readable="lis     r4,0"
        ),
        Patch(
            identifier=628,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('906106a4'),
            new_instruction_readable="stw     r3,1700(r1)"
        ),
        Patch(
            identifier=629,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '3c60'
                ) + get_addr16_ha(data, patch_patterns, custom_functions_cgu0_data.name, 2),
            new_instruction_readable="lis     r3,0"
        ),
        Patch(
            identifier=630,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '8063'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_data.name, 2),
            new_instruction_readable="lwz     r3,0(r3)"
        ),
        Patch(
            identifier=631,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex(
                '8084'
                ) + get_addr16_lo(data, patch_patterns, custom_functions_cgu0_data.name, 1),
            new_instruction_readable="lwz     r4,0(r4)"
        ),
        Patch(
            identifier=632,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83210654'),
            new_instruction_readable="lwz     r25,1620(r1)"
        ),
        Patch(
            identifier=633,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90610654'),
            new_instruction_readable="stw     r3,1620(r1)"
        ),
        Patch(
            identifier=634,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f83e378'),
            new_instruction_readable="mr      r3,r28"
        ),
        Patch(
            identifier=635,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83410650'),
            new_instruction_readable="lwz     r26,1616(r1)"
        ),
        Patch(
            identifier=636,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90810650'),
            new_instruction_readable="stw     r4,1616(r1)"
        ),
        Patch(
            identifier=637,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CharWriter__UpdateVertexColor.name, 1
                ),
            new_instruction_readable="bl CharWriter__UpdateVertexColor"
        ),
        Patch(
            identifier=638,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f83e378'),
            new_instruction_readable="mr      r3,r28"
        ),
        Patch(
            identifier=639,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fc4f378'),
            new_instruction_readable="mr      r4,r30"
        ),
        Patch(
            identifier=640,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa5eb78'),
            new_instruction_readable="mr      r5,r29"
        ),
        Patch(
            identifier=641,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_Print_TextWriterBase_WChar.name, 1
                ),
            new_instruction_readable="bl Print_TextWriterBase_WChar"
        ),
        Patch(
            identifier=642,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('806106a4'),
            new_instruction_readable="lwz     r3,1700(r1)"
        ),
        Patch(
            identifier=643,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('808106a0'),
            new_instruction_readable="lwz     r4,1696(r1)"
        ),
        Patch(
            identifier=644,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('907b0008'),
            new_instruction_readable="stw     r3,8(r27)"
        ),
        Patch(
            identifier=645,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('8061069c'),
            new_instruction_readable="lwz     r3,1692(r1)"
        ),
        Patch(
            identifier=646,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93410650'),
            new_instruction_readable="stw     r26,1616(r1)"
        ),
        Patch(
            identifier=647,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('907b0000'),
            new_instruction_readable="stw     r3,0(r27)"
        ),
        Patch(
            identifier=648,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f83e378'),
            new_instruction_readable="mr      r3,r28"
        ),
        Patch(
            identifier=649,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('909b0004'),
            new_instruction_readable="stw     r4,4(r27)"
        ),
        Patch(
            identifier=650,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('93210654'),
            new_instruction_readable="stw     r25,1620(r1)"
        ),
        Patch(
            identifier=651,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_CharWriter__UpdateVertexColor.name, 1
                ),
            new_instruction_readable="bl CharWriter__UpdateVertexColor"
        ),
        Patch(
            identifier=652,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7f83e378'),
            new_instruction_readable="mr      r3,r28"
        ),
        Patch(
            identifier=653,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fc4f378'),
            new_instruction_readable="mr      r4,r30"
        ),
        Patch(
            identifier=654,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7fa5eb78'),
            new_instruction_readable="mr      r5,r29"
        ),
        Patch(
            identifier=655,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0_Print_TextWriterBase_WChar.name, 1
                ),
            new_instruction_readable="bl Print_TextWriterBase_WChar"
        ),
        Patch(
            identifier=656,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610638'),
            new_instruction_readable="addi    r3,r1,1592"
        ),
        Patch(
            identifier=657,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3880ffff'),
            new_instruction_readable="li      r4,-1"
        ),
        Patch(
            identifier=658,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0___dt__TextWriterBase_WChar.name, 1
                ),
            new_instruction_readable="bl __dt__TextWriterBase_WChar"
        ),
        Patch(
            identifier=659,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38600001'),
            new_instruction_readable="li      r3,1"
        ),
        Patch(
            identifier=660,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cbe10788'),
            new_instruction_readable="lfd     f31,1928(r1)"
        ),
        Patch(
            identifier=661,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cbc10780'),
            new_instruction_readable="lfd     f30,1920(r1)"
        ),
        Patch(
            identifier=662,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cba10778'),
            new_instruction_readable="lfd     f29,1912(r1)"
        ),
        Patch(
            identifier=663,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cb810770'),
            new_instruction_readable="lfd     f28,1904(r1)"
        ),
        Patch(
            identifier=664,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cb610768'),
            new_instruction_readable="lfd     f27,1896(r1)"
        ),
        Patch(
            identifier=665,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cb410760'),
            new_instruction_readable="lfd     f26,1888(r1)"
        ),
        Patch(
            identifier=666,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cb210758'),
            new_instruction_readable="lfd     f25,1880(r1)"
        ),
        Patch(
            identifier=667,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('cb010750'),
            new_instruction_readable="lfd     f24,1872(r1)"
        ),
        Patch(
            identifier=668,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83c10748'),
            new_instruction_readable="lwz     r30,1864(r1)"
        ),
        Patch(
            identifier=669,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83a10744'),
            new_instruction_readable="lwz     r29,1860(r1)"
        ),
        Patch(
            identifier=670,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83810740'),
            new_instruction_readable="lwz     r28,1856(r1)"
        ),
        Patch(
            identifier=671,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('8361073c'),
            new_instruction_readable="lwz     r27,1852(r1)"
        ),
        Patch(
            identifier=672,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83410738'),
            new_instruction_readable="lwz     r26,1848(r1)"
        ),
        Patch(
            identifier=673,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('83210734'),
            new_instruction_readable="lwz     r25,1844(r1)"
        ),
        Patch(
            identifier=674,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('80010794'),
            new_instruction_readable="lwz     r0,1940(r1)"
        ),
        Patch(
            identifier=675,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38210790'),
            new_instruction_readable="addi    r1,r1,1936"
        ),
        Patch(
            identifier=676,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c0803a6'),
            new_instruction_readable="mtlr    r0"
        ),
        Patch(
            identifier=677,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('4e800020'),
            new_instruction_readable="blr"
        ),
        Patch(
            identifier=678,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('38610208'),
            new_instruction_readable="addi    r3,r1,520"
        ),
        Patch(
            identifier=679,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns,
                custom_functions_cgu0__ZN4core6result13unwrap_failed17h0125321215ca17fdE.name, 1
                ),
            new_instruction_readable="bl .text.unlikely._ZN4core6result13unwrap_failed17h0125321215ca17fdE"
        ),
        Patch(
            identifier=680,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns,
                custom_functions_cgu0__ZN4core6option13unwrap_failed17hfe475aa334a9986aE.name, 1
                ),
            new_instruction_readable="bl .text.unlikely._ZN4core6option13unwrap_failed17hfe475aa334a9986aE"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 8a 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("88 b0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 e4 8b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("e4 8e 94 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 90 63"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 89 d4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 96 46"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("8c 7c 8b da"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 00 e4 8d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 00 89 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("00 00 8a a1"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("00 00 89 91"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("e4 92 97 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("91 db 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("00 00 95 63"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("00 00 e4 9e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("00 00 89 d5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("e4 9c 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("e4 9a e4 91"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("00 00 e4 8f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("00 00 e4 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("00 00 8e e1"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("8b ea 92 97"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("00 00 93 cf"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("00 00 89 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("00 00 e4 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("e4 93 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("00 00 e4 99"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("e4 95 e4 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("00 00 fb 93"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("96 ce e4 97"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("89 d6 8a 9d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("e4 9b 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("00 00 e4 9d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("8c 73 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("e4 a1 e4 aa"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("e4 ab 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("88 a9 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("00 00 e4 b2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("88 ef 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("00 00 e4 a9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("00 00 e4 a8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("00 00 e4 a3"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("e4 a2 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("e4 a0 e4 9f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("92 83 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("91 f9 e4 a5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("e4 a4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("00 00 e4 a7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("00 00 91 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("8c 74 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("00 00 89 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("e4 a6 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("8d 72 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("91 91 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("fb 94 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("00 00 e4 b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("00 00 e4 b9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("00 00 89 d7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("00 00 89 ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("e4 b6 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("00 00 fb 95"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("00 00 e4 ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("00 00 e4 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("00 00 e4 bb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("e4 b5 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("e4 b3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("00 00 e4 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("e4 b1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("e4 ad 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("8a ce e4 af"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("e4 ba 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("e4 b0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=129, offset=0x200, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=130, offset=0x204, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=131, offset=0x208, pattern=parse_pattern_bytes("e4 bc 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=132, offset=0x20c, pattern=parse_pattern_bytes("e4 ae 94 9c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=133, offset=0x210, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=134, offset=0x214, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=135, offset=0x218, pattern=parse_pattern_bytes("00 00 97 89"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=136, offset=0x21c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=137, offset=0x220, pattern=parse_pattern_bytes("00 00 e4 b7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=138, offset=0x224, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=139, offset=0x228, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=140, offset=0x22c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=141, offset=0x230, pattern=parse_pattern_bytes("00 00 e4 cd"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=142, offset=0x234, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=143, offset=0x238, pattern=parse_pattern_bytes("00 00 e4 c5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=144, offset=0x23c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=145, offset=0x240, pattern=parse_pattern_bytes("00 00 90 9b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=146, offset=0x244, pattern=parse_pattern_bytes("00 00 fb 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=147, offset=0x248, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=148, offset=0x24c, pattern=parse_pattern_bytes("8b 65 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=149, offset=0x250, pattern=parse_pattern_bytes("8b db 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=150, offset=0x254, pattern=parse_pattern_bytes("e4 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=151, offset=0x258, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=152, offset=0x25c, pattern=parse_pattern_bytes("00 00 89 d9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=153, offset=0x260, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=154, offset=0x264, pattern=parse_pattern_bytes("8f d2 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=155, offset=0x268, pattern=parse_pattern_bytes("e4 c3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=156, offset=0x26c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=157, offset=0x270, pattern=parse_pattern_bytes("8d d8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=158, offset=0x274, pattern=parse_pattern_bytes("00 00 93 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=159, offset=0x278, pattern=parse_pattern_bytes("e4 c8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=160, offset=0x27c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=161, offset=0x280, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=162, offset=0x284, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=163, offset=0x288, pattern=parse_pattern_bytes("00 00 95 ec"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=164, offset=0x28c, pattern=parse_pattern_bytes("00 00 e4 bf"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=165, offset=0x290, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=166, offset=0x294, pattern=parse_pattern_bytes("00 00 89 d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=167, offset=0x298, pattern=parse_pattern_bytes("8c d4 95 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=168, offset=0x29c, pattern=parse_pattern_bytes("e4 c9 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=169, offset=0x2a0, pattern=parse_pattern_bytes("e4 bd 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=170, offset=0x2a4, pattern=parse_pattern_bytes("fb 97 e4 c6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=171, offset=0x2a8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=172, offset=0x2ac, pattern=parse_pattern_bytes("00 00 e4 d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=173, offset=0x2b0, pattern=parse_pattern_bytes("00 00 e4 c1"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=174, offset=0x2b4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=175, offset=0x2b8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=176, offset=0x2bc, pattern=parse_pattern_bytes("00 00 e4 c2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=177, offset=0x2c0, pattern=parse_pattern_bytes("93 b8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=178, offset=0x2c4, pattern=parse_pattern_bytes("00 00 e4 c7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=179, offset=0x2c8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=180, offset=0x2cc, pattern=parse_pattern_bytes("00 00 e4 c4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=181, offset=0x2d0, pattern=parse_pattern_bytes("96 47 e4 ca"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=182, offset=0x2d4, pattern=parse_pattern_bytes("88 de 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=183, offset=0x2d8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=184, offset=0x2dc, pattern=parse_pattern_bytes("00 00 e4 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=185, offset=0x2e0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=186, offset=0x2e4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=187, offset=0x2e8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=188, offset=0x2ec, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=189, offset=0x2f0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=190, offset=0x2f4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=191, offset=0x2f8, pattern=parse_pattern_bytes("e4 cc 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=192, offset=0x2fc, pattern=parse_pattern_bytes("e4 cb 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=193, offset=0x300, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=194, offset=0x304, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=195, offset=0x308, pattern=parse_pattern_bytes("00 00 94 8b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=196, offset=0x30c, pattern=parse_pattern_bytes("e4 d2 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=197, offset=0x310, pattern=parse_pattern_bytes("e4 dd 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=198, offset=0x314, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=199, offset=0x318, pattern=parse_pattern_bytes("00 00 8a 9e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=200, offset=0x31c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=201, offset=0x320, pattern=parse_pattern_bytes("00 00 e4 e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=202, offset=0x324, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=203, offset=0x328, pattern=parse_pattern_bytes("e4 ce 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=204, offset=0x32c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=205, offset=0x330, pattern=parse_pattern_bytes("e4 d3 97 8e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=206, offset=0x334, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=207, offset=0x338, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=208, offset=0x33c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=209, offset=0x340, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=210, offset=0x344, pattern=parse_pattern_bytes("e4 dc 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=211, offset=0x348, pattern=parse_pattern_bytes("fb 98 97 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=212, offset=0x34c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=213, offset=0x350, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=214, offset=0x354, pattern=parse_pattern_bytes("97 a8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=215, offset=0x358, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=216, offset=0x35c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=217, offset=0x360, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=218, offset=0x364, pattern=parse_pattern_bytes("00 00 92 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=219, offset=0x368, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=220, offset=0x36c, pattern=parse_pattern_bytes("00 00 8a 8b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=221, offset=0x370, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=222, offset=0x374, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=223, offset=0x378, pattern=parse_pattern_bytes("00 00 95 92"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=224, offset=0x37c, pattern=parse_pattern_bytes("e4 e2 93 9f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=225, offset=0x380, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=226, offset=0x384, pattern=parse_pattern_bytes("88 af 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=227, offset=0x388, pattern=parse_pattern_bytes("00 00 e4 db"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=228, offset=0x38c, pattern=parse_pattern_bytes("00 00 e4 d7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=229, offset=0x390, pattern=parse_pattern_bytes("91 92 e4 d1"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=230, offset=0x394, pattern=parse_pattern_bytes("e4 d9 e4 de"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=231, offset=0x398, pattern=parse_pattern_bytes("00 00 94 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=232, offset=0x39c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=233, offset=0x3a0, pattern=parse_pattern_bytes("00 00 88 a8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=234, offset=0x3a4, pattern=parse_pattern_bytes("00 00 e4 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=235, offset=0x3a8, pattern=parse_pattern_bytes("00 00 e4 df"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=236, offset=0x3ac, pattern=parse_pattern_bytes("95 98 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=237, offset=0x3b0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=238, offset=0x3b4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=239, offset=0x3b8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=240, offset=0x3bc, pattern=parse_pattern_bytes("e4 da 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=241, offset=0x3c0, pattern=parse_pattern_bytes("e4 d5 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=242, offset=0x3c4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=243, offset=0x3c8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=244, offset=0x3cc, pattern=parse_pattern_bytes("00 00 8f d3"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=245, offset=0x3d0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=246, offset=0x3d4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=247, offset=0x3d8, pattern=parse_pattern_bytes("8f 4e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=248, offset=0x3dc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=249, offset=0x3e0, pattern=parse_pattern_bytes("8e aa 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=250, offset=0x3e4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=251, offset=0x3e8, pattern=parse_pattern_bytes("00 00 96 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=252, offset=0x3ec, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=253, offset=0x3f0, pattern=parse_pattern_bytes("95 66 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=254, offset=0x3f4, pattern=parse_pattern_bytes("00 00 e4 e5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=255, offset=0x3f8, pattern=parse_pattern_bytes("00 00 e4 ee"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=256, offset=0x3fc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=257, offset=0x400, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=258, offset=0x404, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=259, offset=0x408, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=260, offset=0x40c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=261, offset=0x410, pattern=parse_pattern_bytes("00 00 e4 d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=262, offset=0x414, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=263, offset=0x418, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=264, offset=0x41c, pattern=parse_pattern_bytes("8a 97 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=265, offset=0x420, pattern=parse_pattern_bytes("fb 99 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=266, offset=0x424, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=267, offset=0x428, pattern=parse_pattern_bytes("8f f6 e4 e3"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=268, offset=0x42c, pattern=parse_pattern_bytes("00 00 e4 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=269, offset=0x430, pattern=parse_pattern_bytes("91 93 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=270, offset=0x434, pattern=parse_pattern_bytes("00 00 e4 e4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=271, offset=0x438, pattern=parse_pattern_bytes("00 00 e4 eb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=272, offset=0x43c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=273, offset=0x440, pattern=parse_pattern_bytes("92 7e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=274, offset=0x444, pattern=parse_pattern_bytes("e4 ec 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=275, offset=0x448, pattern=parse_pattern_bytes("00 00 97 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=276, offset=0x44c, pattern=parse_pattern_bytes("e4 e1 8a 57"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=277, offset=0x450, pattern=parse_pattern_bytes("00 00 e4 e7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=278, offset=0x454, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=279, offset=0x458, pattern=parse_pattern_bytes("e4 ea 96 aa"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=280, offset=0x45c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=281, offset=0x460, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=282, offset=0x464, pattern=parse_pattern_bytes("e4 ed 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=283, offset=0x468, pattern=parse_pattern_bytes("00 00 e4 e6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=284, offset=0x46c, pattern=parse_pattern_bytes("e4 e9 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=285, offset=0x470, pattern=parse_pattern_bytes("fa 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=286, offset=0x474, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=287, offset=0x478, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=288, offset=0x47c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=289, offset=0x480, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=290, offset=0x484, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=291, offset=0x488, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=292, offset=0x48c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=293, offset=0x490, pattern=parse_pattern_bytes("96 48 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=294, offset=0x494, pattern=parse_pattern_bytes("98 40 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=295, offset=0x498, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=296, offset=0x49c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=297, offset=0x4a0, pattern=parse_pattern_bytes("e4 f1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=298, offset=0x4a4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=299, offset=0x4a8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=300, offset=0x4ac, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=301, offset=0x4b0, pattern=parse_pattern_bytes("e4 f8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=302, offset=0x4b4, pattern=parse_pattern_bytes("00 00 e4 f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=303, offset=0x4b8, pattern=parse_pattern_bytes("8e c1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=304, offset=0x4bc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=305, offset=0x4c0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=306, offset=0x4c4, pattern=parse_pattern_bytes("e4 cf 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=307, offset=0x4c8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=308, offset=0x4cc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=309, offset=0x4d0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=310, offset=0x4d4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=311, offset=0x4d8, pattern=parse_pattern_bytes("00 00 95 cc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=312, offset=0x4dc, pattern=parse_pattern_bytes("00 00 96 a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=313, offset=0x4e0, pattern=parse_pattern_bytes("e4 f7 e4 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=314, offset=0x4e4, pattern=parse_pattern_bytes("00 00 e4 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=315, offset=0x4e8, pattern=parse_pattern_bytes("e4 f3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=316, offset=0x4ec, pattern=parse_pattern_bytes("89 55 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=317, offset=0x4f0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=318, offset=0x4f4, pattern=parse_pattern_bytes("00 00 e4 f5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=319, offset=0x4f8, pattern=parse_pattern_bytes("00 00 e4 ef"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=320, offset=0x4fc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=321, offset=0x500, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=322, offset=0x504, pattern=parse_pattern_bytes("92 d3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=323, offset=0x508, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=324, offset=0x50c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=325, offset=0x510, pattern=parse_pattern_bytes("e4 f4 88 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=326, offset=0x514, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=327, offset=0x518, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=328, offset=0x51c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=329, offset=0x520, pattern=parse_pattern_bytes("00 00 91 a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=330, offset=0x524, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=331, offset=0x528, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=332, offset=0x52c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=333, offset=0x530, pattern=parse_pattern_bytes("00 00 95 c1"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=334, offset=0x534, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=335, offset=0x538, pattern=parse_pattern_bytes("e4 f9 e5 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=336, offset=0x53c, pattern=parse_pattern_bytes("00 00 94 d7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=337, offset=0x540, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=338, offset=0x544, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=339, offset=0x548, pattern=parse_pattern_bytes("e4 fc 8f d4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=340, offset=0x54c, pattern=parse_pattern_bytes("8e c7 e5 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=341, offset=0x550, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=342, offset=0x554, pattern=parse_pattern_bytes("8b bc 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=343, offset=0x558, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=344, offset=0x55c, pattern=parse_pattern_bytes("00 00 fb 9a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=345, offset=0x560, pattern=parse_pattern_bytes("00 00 e5 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=346, offset=0x564, pattern=parse_pattern_bytes("00 00 95 99"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=347, offset=0x568, pattern=parse_pattern_bytes("e4 fb fb 9b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=348, offset=0x56c, pattern=parse_pattern_bytes("e4 d4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=349, offset=0x570, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=350, offset=0x574, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=351, offset=0x578, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=352, offset=0x57c, pattern=parse_pattern_bytes("00 00 e4 fa"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=353, offset=0x580, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=354, offset=0x584, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=355, offset=0x588, pattern=parse_pattern_bytes("98 6e 93 a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=356, offset=0x58c, pattern=parse_pattern_bytes("95 93 fb 9c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=357, offset=0x590, pattern=parse_pattern_bytes("00 00 e5 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=358, offset=0x594, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=359, offset=0x598, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=360, offset=0x59c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=361, offset=0x5a0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=362, offset=0x5a4, pattern=parse_pattern_bytes("00 00 e5 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=363, offset=0x5a8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=364, offset=0x5ac, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=365, offset=0x5b0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=366, offset=0x5b4, pattern=parse_pattern_bytes("e5 51 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=367, offset=0x5b8, pattern=parse_pattern_bytes("e5 44 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=368, offset=0x5bc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=369, offset=0x5c0, pattern=parse_pattern_bytes("94 96 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=370, offset=0x5c4, pattern=parse_pattern_bytes("00 00 e5 4e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=371, offset=0x5c8, pattern=parse_pattern_bytes("e5 46 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=372, offset=0x5cc, pattern=parse_pattern_bytes("e5 48 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=373, offset=0x5d0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=374, offset=0x5d4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=375, offset=0x5d8, pattern=parse_pattern_bytes("e5 52 e5 47"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=376, offset=0x5dc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=377, offset=0x5e0, pattern=parse_pattern_bytes("e5 4b 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=378, offset=0x5e4, pattern=parse_pattern_bytes("00 00 89 92"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=379, offset=0x5e8, pattern=parse_pattern_bytes("00 00 93 e3"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=380, offset=0x5ec, pattern=parse_pattern_bytes("00 00 e5 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=381, offset=0x5f0, pattern=parse_pattern_bytes("e5 4f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=382, offset=0x5f4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=383, offset=0x5f8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=384, offset=0x5fc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=385, offset=0x600, pattern=parse_pattern_bytes("e5 45 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=386, offset=0x604, pattern=parse_pattern_bytes("91 45 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=387, offset=0x608, pattern=parse_pattern_bytes("e5 49 8e 46"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=388, offset=0x60c, pattern=parse_pattern_bytes("90 64 8c 4f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=389, offset=0x610, pattern=parse_pattern_bytes("96 f2 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=390, offset=0x614, pattern=parse_pattern_bytes("96 f7 8f 92"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=391, offset=0x618, pattern=parse_pattern_bytes("fb 9e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=392, offset=0x61c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=393, offset=0x620, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=394, offset=0x624, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=395, offset=0x628, pattern=parse_pattern_bytes("00 00 e5 56"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=396, offset=0x62c, pattern=parse_pattern_bytes("e5 54 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=397, offset=0x630, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=398, offset=0x634, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=399, offset=0x638, pattern=parse_pattern_bytes("00 00 98 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=400, offset=0x63c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=401, offset=0x640, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=402, offset=0x644, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=403, offset=0x648, pattern=parse_pattern_bytes("00 00 e5 53"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=404, offset=0x64c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=405, offset=0x650, pattern=parse_pattern_bytes("00 00 97 95"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=406, offset=0x654, pattern=parse_pattern_bytes("00 00 e5 55"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=407, offset=0x658, pattern=parse_pattern_bytes("e5 57 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=408, offset=0x65c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=409, offset=0x660, pattern=parse_pattern_bytes("00 00 e5 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=410, offset=0x664, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=411, offset=0x668, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=412, offset=0x66c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=413, offset=0x670, pattern=parse_pattern_bytes("e5 5b e5 59"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=414, offset=0x674, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=415, offset=0x678, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=416, offset=0x67c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=417, offset=0x680, pattern=parse_pattern_bytes("93 a1 e5 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=418, offset=0x684, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=419, offset=0x688, pattern=parse_pattern_bytes("00 00 94 cb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=420, offset=0x68c, pattern=parse_pattern_bytes("e5 4d 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=421, offset=0x690, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=422, offset=0x694, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=423, offset=0x698, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=424, offset=0x69c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=425, offset=0x6a0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=426, offset=0x6a4, pattern=parse_pattern_bytes("00 00 8f 93"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=427, offset=0x6a8, pattern=parse_pattern_bytes("00 00 e5 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=428, offset=0x6ac, pattern=parse_pattern_bytes("e5 61 91 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=429, offset=0x6b0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=430, offset=0x6b4, pattern=parse_pattern_bytes("e5 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=431, offset=0x6b8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=432, offset=0x6bc, pattern=parse_pattern_bytes("e5 41 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=433, offset=0x6c0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=434, offset=0x6c4, pattern=parse_pattern_bytes("e5 62 91 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=435, offset=0x6c8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=436, offset=0x6cc, pattern=parse_pattern_bytes("e5 5d e5 5f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=437, offset=0x6d0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=438, offset=0x6d4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=439, offset=0x6d8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=440, offset=0x6dc, pattern=parse_pattern_bytes("00 00 e5 5e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=441, offset=0x6e0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=442, offset=0x6e4, pattern=parse_pattern_bytes("9f 50 9f 41"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=443, offset=0x6e8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=444, offset=0x6ec, pattern=parse_pattern_bytes("e5 64 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=445, offset=0x6f0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=446, offset=0x6f4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=447, offset=0x6f8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=448, offset=0x6fc, pattern=parse_pattern_bytes("e5 63 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=449, offset=0x700, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=450, offset=0x704, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=451, offset=0x708, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=452, offset=0x70c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=453, offset=0x710, pattern=parse_pattern_bytes("00 00 97 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=454, offset=0x714, pattern=parse_pattern_bytes("00 00 e1 ba"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=455, offset=0x718, pattern=parse_pattern_bytes("e5 65 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=456, offset=0x71c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=457, offset=0x720, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=458, offset=0x724, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=459, offset=0x728, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=460, offset=0x72c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=461, offset=0x730, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=462, offset=0x734, pattern=parse_pattern_bytes("00 00 e5 66"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=463, offset=0x738, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=464, offset=0x73c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=465, offset=0x740, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=466, offset=0x744, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=467, offset=0x748, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=468, offset=0x74c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=469, offset=0x750, pattern=parse_pattern_bytes("00 00 e5 67"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=470, offset=0x754, pattern=parse_pattern_bytes("8c d5 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=471, offset=0x758, pattern=parse_pattern_bytes("8b 73 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=472, offset=0x75c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=473, offset=0x760, pattern=parse_pattern_bytes("e5 69 99 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=474, offset=0x764, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=475, offset=0x768, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=476, offset=0x76c, pattern=parse_pattern_bytes("8b 95 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=477, offset=0x770, pattern=parse_pattern_bytes("97 b8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=478, offset=0x774, pattern=parse_pattern_bytes("8b f1 e5 6a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=479, offset=0x778, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=480, offset=0x77c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=481, offset=0x780, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=482, offset=0x784, pattern=parse_pattern_bytes("00 00 e5 6b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=483, offset=0x788, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=484, offset=0x78c, pattern=parse_pattern_bytes("00 00 92 8e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=485, offset=0x790, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=486, offset=0x794, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=487, offset=0x798, pattern=parse_pattern_bytes("00 00 e5 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=488, offset=0x79c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=489, offset=0x7a0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=490, offset=0x7a4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=491, offset=0x7a8, pattern=parse_pattern_bytes("00 00 93 f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=492, offset=0x7ac, pattern=parse_pattern_bytes("00 00 88 b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=493, offset=0x7b0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=494, offset=0x7b4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=495, offset=0x7b8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=496, offset=0x7bc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=497, offset=0x7c0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=498, offset=0x7c4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=499, offset=0x7c8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=500, offset=0x7cc, pattern=parse_pattern_bytes("89 e1 e5 71"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=501, offset=0x7d0, pattern=parse_pattern_bytes("e5 72 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=502, offset=0x7d4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=503, offset=0x7d8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=504, offset=0x7dc, pattern=parse_pattern_bytes("00 00 e5 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=505, offset=0x7e0, pattern=parse_pattern_bytes("00 00 8e 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=506, offset=0x7e4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=507, offset=0x7e8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=508, offset=0x7ec, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=509, offset=0x7f0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=510, offset=0x7f4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=511, offset=0x7f8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=512, offset=0x7fc, pattern=parse_pattern_bytes("00 00 e5 6e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=513, offset=0x800, pattern=parse_pattern_bytes("94 61 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=514, offset=0x804, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=515, offset=0x808, pattern=parse_pattern_bytes("00 00 e5 6f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=516, offset=0x80c, pattern=parse_pattern_bytes("e5 70 e5 7a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=517, offset=0x810, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=518, offset=0x814, pattern=parse_pattern_bytes("00 00 e5 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=519, offset=0x818, pattern=parse_pattern_bytes("e5 77 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=520, offset=0x81c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=521, offset=0x820, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=522, offset=0x824, pattern=parse_pattern_bytes("e5 73 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=523, offset=0x828, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=524, offset=0x82c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=525, offset=0x830, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=526, offset=0x834, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=527, offset=0x838, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=528, offset=0x83c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=529, offset=0x840, pattern=parse_pattern_bytes("e5 75 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=530, offset=0x844, pattern=parse_pattern_bytes("e5 76 8e d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=531, offset=0x848, pattern=parse_pattern_bytes("00 00 e5 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=532, offset=0x84c, pattern=parse_pattern_bytes("00 00 92 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=533, offset=0x850, pattern=parse_pattern_bytes("00 00 8c 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=534, offset=0x854, pattern=parse_pattern_bytes("8a 61 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=535, offset=0x858, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=536, offset=0x85c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=537, offset=0x860, pattern=parse_pattern_bytes("e5 7b 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=538, offset=0x864, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=539, offset=0x868, pattern=parse_pattern_bytes("00 00 8a 5e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=540, offset=0x86c, pattern=parse_pattern_bytes("00 00 e5 81"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=541, offset=0x870, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=542, offset=0x874, pattern=parse_pattern_bytes("e5 7c e5 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=543, offset=0x878, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=544, offset=0x87c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=545, offset=0x880, pattern=parse_pattern_bytes("94 b8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=546, offset=0x884, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=547, offset=0x888, pattern=parse_pattern_bytes("00 00 e5 7d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=548, offset=0x88c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=549, offset=0x890, pattern=parse_pattern_bytes("e5 7e 95 67"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=550, offset=0x894, pattern=parse_pattern_bytes("94 d8 e5 82"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=551, offset=0x898, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=552, offset=0x89c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=553, offset=0x8a0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=554, offset=0x8a4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=555, offset=0x8a8, pattern=parse_pattern_bytes("91 fb e5 8c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=556, offset=0x8ac, pattern=parse_pattern_bytes("00 00 e5 88"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=557, offset=0x8b0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=558, offset=0x8b4, pattern=parse_pattern_bytes("89 e9 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=559, offset=0x8b8, pattern=parse_pattern_bytes("e5 86 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=560, offset=0x8bc, pattern=parse_pattern_bytes("96 49 e5 87"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=561, offset=0x8c0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=562, offset=0x8c4, pattern=parse_pattern_bytes("e5 84 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=563, offset=0x8c8, pattern=parse_pattern_bytes("e5 85 e5 8a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=564, offset=0x8cc, pattern=parse_pattern_bytes("e5 8d 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=565, offset=0x8d0, pattern=parse_pattern_bytes("00 00 e5 8b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=566, offset=0x8d4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=567, offset=0x8d8, pattern=parse_pattern_bytes("00 00 e5 89"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=568, offset=0x8dc, pattern=parse_pattern_bytes("e5 83 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=569, offset=0x8e0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=570, offset=0x8e4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=571, offset=0x8e8, pattern=parse_pattern_bytes("92 77 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=572, offset=0x8ec, pattern=parse_pattern_bytes("e5 94 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=573, offset=0x8f0, pattern=parse_pattern_bytes("96 a8 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=574, offset=0x8f4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=575, offset=0x8f8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=576, offset=0x8fc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=577, offset=0x900, pattern=parse_pattern_bytes("00 00 e5 92"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=578, offset=0x904, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=579, offset=0x908, pattern=parse_pattern_bytes("00 00 e5 93"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=580, offset=0x90c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=581, offset=0x910, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=582, offset=0x914, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=583, offset=0x918, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=584, offset=0x91c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=585, offset=0x920, pattern=parse_pattern_bytes("e5 8e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=586, offset=0x924, pattern=parse_pattern_bytes("00 00 e5 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=587, offset=0x928, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=588, offset=0x92c, pattern=parse_pattern_bytes("00 00 e5 91"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=589, offset=0x930, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=590, offset=0x934, pattern=parse_pattern_bytes("00 00 e5 8f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=591, offset=0x938, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=592, offset=0x93c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=593, offset=0x940, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=594, offset=0x944, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=595, offset=0x948, pattern=parse_pattern_bytes("00 00 90 e4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=596, offset=0x94c, pattern=parse_pattern_bytes("00 00 98 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=597, offset=0x950, pattern=parse_pattern_bytes("e5 98 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=598, offset=0x954, pattern=parse_pattern_bytes("e5 99 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=599, offset=0x958, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=600, offset=0x95c, pattern=parse_pattern_bytes("00 00 e5 9f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=601, offset=0x960, pattern=parse_pattern_bytes("00 00 90 49"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=602, offset=0x964, pattern=parse_pattern_bytes("00 00 e5 9b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=603, offset=0x968, pattern=parse_pattern_bytes("00 00 e5 9e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=604, offset=0x96c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=605, offset=0x970, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=606, offset=0x974, pattern=parse_pattern_bytes("00 00 e5 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=607, offset=0x978, pattern=parse_pattern_bytes("e5 95 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=608, offset=0x97c, pattern=parse_pattern_bytes("00 00 e5 a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=609, offset=0x980, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=610, offset=0x984, pattern=parse_pattern_bytes("89 da 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=611, offset=0x988, pattern=parse_pattern_bytes("e5 9c 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=612, offset=0x98c, pattern=parse_pattern_bytes("e5 a1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=613, offset=0x990, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=614, offset=0x994, pattern=parse_pattern_bytes("e5 9d 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=615, offset=0x998, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=616, offset=0x99c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=617, offset=0x9a0, pattern=parse_pattern_bytes("e5 9a 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=618, offset=0x9a4, pattern=parse_pattern_bytes("92 b1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=619, offset=0x9a8, pattern=parse_pattern_bytes("e5 97 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=620, offset=0x9ac, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=621, offset=0x9b0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=622, offset=0x9b4, pattern=parse_pattern_bytes("00 00 94 88"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=623, offset=0x9b8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=624, offset=0x9bc, pattern=parse_pattern_bytes("e5 a5 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=625, offset=0x9c0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=626, offset=0x9c4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=627, offset=0x9c8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=628, offset=0x9cc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=629, offset=0x9d0, pattern=parse_pattern_bytes("00 00 97 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=630, offset=0x9d4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=631, offset=0x9d8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=632, offset=0x9dc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=633, offset=0x9e0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=634, offset=0x9e4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=635, offset=0x9e8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=636, offset=0x9ec, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=637, offset=0x9f0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=638, offset=0x9f4, pattern=parse_pattern_bytes("00 00 e5 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=639, offset=0x9f8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=640, offset=0x9fc, pattern=parse_pattern_bytes("e5 a3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=641, offset=0xa00, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=642, offset=0xa04, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=643, offset=0xa08, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=644, offset=0xa0c, pattern=parse_pattern_bytes("00 00 e5 ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=645, offset=0xa10, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=646, offset=0xa14, pattern=parse_pattern_bytes("00 00 e5 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=647, offset=0xa18, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=648, offset=0xa1c, pattern=parse_pattern_bytes("00 00 e5 ae"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=649, offset=0xa20, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=650, offset=0xa24, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=651, offset=0xa28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=652, offset=0xa2c, pattern=parse_pattern_bytes("97 86 e5 b1"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=653, offset=0xa30, pattern=parse_pattern_bytes("00 00 e5 a8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=654, offset=0xa34, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=655, offset=0xa38, pattern=parse_pattern_bytes("e5 a9 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=656, offset=0xa3c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=657, offset=0xa40, pattern=parse_pattern_bytes("e5 ad 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=658, offset=0xa44, pattern=parse_pattern_bytes("e5 b0 e5 af"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=659, offset=0xa48, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=660, offset=0xa4c, pattern=parse_pattern_bytes("00 00 e5 a7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=661, offset=0xa50, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=662, offset=0xa54, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=663, offset=0xa58, pattern=parse_pattern_bytes("e5 aa 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=664, offset=0xa5c, pattern=parse_pattern_bytes("e5 bb 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=665, offset=0xa60, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=666, offset=0xa64, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=667, offset=0xa68, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=668, offset=0xa6c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=669, offset=0xa70, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=670, offset=0xa74, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=671, offset=0xa78, pattern=parse_pattern_bytes("e5 b4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=672, offset=0xa7c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=673, offset=0xa80, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=674, offset=0xa84, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=675, offset=0xa88, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=676, offset=0xa8c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=677, offset=0xa90, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=678, offset=0xa94, pattern=parse_pattern_bytes("00 00 e5 b2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=679, offset=0xa98, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=680, offset=0xa9c, pattern=parse_pattern_bytes("e5 b3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=681, offset=0xaa0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_archipelago_text_buffer = PatchPattern(
    # 0x200 length
    name=f"custom_functions_cgu0_archipelago_text_buffer",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: b'\x00' * 0x200,
            new_instruction_readable="---"
        )
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("8a ca 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("e3 9d 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("e3 9e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("00 00 e3 9f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("00 00 fb 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("e3 a0 e3 a1"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("e3 a2 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("e3 a3 e3 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("e3 a6 e3 a5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("e3 a7 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("00 00 e3 a8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("e3 a9 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("00 00 e3 ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("e3 aa e3 ab"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("8d df 8c 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("92 75 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("94 b1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("8f 90 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("00 00 94 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("00 00 94 eb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("e3 ad 9c eb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("e3 ae e3 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("00 00 97 85"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("e3 af e3 b2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("e3 b1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("97 72 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("e3 b3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("94 fc 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("e3 b4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("e3 b7 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("00 00 e3 b6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("e3 b5 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("00 00 fb 91"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("00 00 e3 b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("8c 51 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("91 41 8b 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("e3 bc e3 b9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("e3 ba 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("e3 bd 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("e3 be e3 bb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("00 00 89 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("00 00 89 a5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("00 00 e3 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("e3 c1 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("e3 c2 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("97 82 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("8f 4b 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("e3 c4 e3 c3"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("90 89 e3 c5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("e3 c6 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("00 00 e3 c7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("00 00 8a e3"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("8a cb 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("00 00 e3 c8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("00 00 e3 c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("00 00 96 7c"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_cst4 = PatchPattern(
    name=f"custom_functions_cgu0_cst4",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('43d70000'),
            new_instruction_readable=".long 0x43d60000"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('c1600000'),
            new_instruction_readable=".long 0x00000000"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('00000000'),
            new_instruction_readable=".long 0x00000000"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40800000'),
            new_instruction_readable=".long 0x40800000"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('3f800000'),
            new_instruction_readable=".long 0x3f800000"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('40000000'),
            new_instruction_readable=".long 0x40000000"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('43f00000'),
            new_instruction_readable=".long 0x43f00000"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('44200000'),
            new_instruction_readable=".long 0x44200000"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('41200000'),
            new_instruction_readable=".long 0x41200000"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("91 40 8c 71"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 8f 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("fb 8f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("90 44 91 55"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("e3 84 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("00 00 e3 86"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("e3 87 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 e3 83"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("e3 85 00 00"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_memcpy = PatchPattern(
    # R8AE01 memcpy = .init:0x80004364; // type:function size:0x29C scope:global
    name=f"custom_functions_cgu0_memcpy",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("28 85 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("4d 86 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("7c 84 18 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("41 84 01 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("4d 86 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("38 c0 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("41 94 00 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("54 89 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("54 6a 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7d 0a 18 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("7c 00 22 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("40 82 01 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("71 4a 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("41 a2 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("38 c0 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("7d 29 30 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("39 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7d 29 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c a9 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("89 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("38 84 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("99 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("39 08 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("42 00 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("54 a6 d9 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c8 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("c8 44 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("c8 64 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("c8 84 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 84 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("d8 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("d8 48 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("d8 68 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("d8 88 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("39 08 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("42 00 ff d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("70 a6 00 1f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("38 84 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("39 08 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("8d 24 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("9d 28 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("38 c0 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("40 95 00 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("54 89 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("54 6a 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("40 82 00 84"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("38 c0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("7d 29 30 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("39 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("7c a9 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("7d 29 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("89 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 84 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("99 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("39 08 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("42 00 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("54 a6 e1 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("81 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("81 44 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("81 64 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("81 84 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("38 84 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("91 28 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("91 48 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("91 68 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("91 88 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("39 08 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("42 00 ff d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("70 a6 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("38 84 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("39 08 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("8d 24 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("9d 28 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("38 e4 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("39 03 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("7c a9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("8d 27 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("9d 28 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("7c 84 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("7d 83 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("38 c0 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("41 94 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("54 89 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("55 8a 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("40 82 00 f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("71 4a 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("41 a2 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("7d 49 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("7c aa 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("54 a6 d9 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("c8 24 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("c8 44 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("c8 64 ff e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("c8 84 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("38 84 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("d8 2c ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("d8 4c ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("d8 6c ff e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("dc 8c ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("42 00 ff dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("70 a6 00 1f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=129, offset=0x200, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=130, offset=0x204, pattern=parse_pattern_bytes("38 c0 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=131, offset=0x208, pattern=parse_pattern_bytes("7e 85 30 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=132, offset=0x20c, pattern=parse_pattern_bytes("40 95 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=133, offset=0x210, pattern=parse_pattern_bytes("54 89 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=134, offset=0x214, pattern=parse_pattern_bytes("55 8a 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=135, offset=0x218, pattern=parse_pattern_bytes("7d 4b 4a 79"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=136, offset=0x21c, pattern=parse_pattern_bytes("40 82 00 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=137, offset=0x220, pattern=parse_pattern_bytes("71 4a 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=138, offset=0x224, pattern=parse_pattern_bytes("41 a2 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=139, offset=0x228, pattern=parse_pattern_bytes("7d 49 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=140, offset=0x22c, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=141, offset=0x230, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=142, offset=0x234, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=143, offset=0x238, pattern=parse_pattern_bytes("7c aa 28 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=144, offset=0x23c, pattern=parse_pattern_bytes("54 a6 e1 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=145, offset=0x240, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=146, offset=0x244, pattern=parse_pattern_bytes("81 24 ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=147, offset=0x248, pattern=parse_pattern_bytes("81 44 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=148, offset=0x24c, pattern=parse_pattern_bytes("81 64 ff f4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=149, offset=0x250, pattern=parse_pattern_bytes("81 04 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=150, offset=0x254, pattern=parse_pattern_bytes("38 84 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=151, offset=0x258, pattern=parse_pattern_bytes("91 2c ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=152, offset=0x25c, pattern=parse_pattern_bytes("91 4c ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=153, offset=0x260, pattern=parse_pattern_bytes("91 6c ff f4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=154, offset=0x264, pattern=parse_pattern_bytes("95 0c ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=155, offset=0x268, pattern=parse_pattern_bytes("42 00 ff dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=156, offset=0x26c, pattern=parse_pattern_bytes("70 a6 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=157, offset=0x270, pattern=parse_pattern_bytes("4d 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=158, offset=0x274, pattern=parse_pattern_bytes("7c c9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=159, offset=0x278, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=160, offset=0x27c, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=161, offset=0x280, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=162, offset=0x284, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=163, offset=0x288, pattern=parse_pattern_bytes("7c a9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=164, offset=0x28c, pattern=parse_pattern_bytes("8d 24 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=165, offset=0x290, pattern=parse_pattern_bytes("9d 2c ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=166, offset=0x294, pattern=parse_pattern_bytes("42 00 ff f8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=167, offset=0x298, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0__Lanon_c56ae961650860ac32e9b2618d293ecb_6 = PatchPattern(
    name=f"custom_functions_cgu0_.Lanon.c56ae961650860ac32e9b2618d293ecb.6",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=5,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=6,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=7,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=8,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=9,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=10,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=11,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=12,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=13,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=14,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=15,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=16,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=17,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=18,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=19,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=20,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=21,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=22,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=23,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=24,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=25,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=26,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=27,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=28,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=29,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=30,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=31,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=32,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('01010101'),
            new_instruction_readable=".long 0x01010101"
        ),
        Patch(
            identifier=33,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('00000202'),
            new_instruction_readable=".long 0x00000202"
        ),
        Patch(
            identifier=34,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('02020202'),
            new_instruction_readable=".long 0x02020202"
        ),
        Patch(
            identifier=35,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('02020202'),
            new_instruction_readable=".long 0x02020202"
        ),
        Patch(
            identifier=36,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('02020202'),
            new_instruction_readable=".long 0x02020202"
        ),
        Patch(
            identifier=37,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('02020202'),
            new_instruction_readable=".long 0x02020202"
        ),
        Patch(
            identifier=38,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('02020202'),
            new_instruction_readable=".long 0x02020202"
        ),
        Patch(
            identifier=39,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('02020202'),
            new_instruction_readable=".long 0x02020202"
        ),
        Patch(
            identifier=40,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('02020202'),
            new_instruction_readable=".long 0x02020202"
        ),
        Patch(
            identifier=41,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('03030303'),
            new_instruction_readable=".long 0x03030303"
        ),
        Patch(
            identifier=42,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('03030303'),
            new_instruction_readable=".long 0x03030303"
        ),
        Patch(
            identifier=43,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('03030303'),
            new_instruction_readable=".long 0x03030303"
        ),
        Patch(
            identifier=44,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('03030303'),
            new_instruction_readable=".long 0x03030303"
        ),
        Patch(
            identifier=45,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('04040404'),
            new_instruction_readable=".long 0x04040404"
        ),
        Patch(
            identifier=46,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('04000000'),
            new_instruction_readable=".long 0x04000000"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 e3 53"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 8c 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("91 b1 e3 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("91 8e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("00 00 e3 65"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("fb 8d 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("e3 61 e3 5b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("00 00 e3 5f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("8e f8 88 db"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("e3 5a e3 62"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("e3 66 8d 6a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("96 d4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("92 d4 e3 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("00 00 fb 8c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("e3 64 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("e3 59 92 5d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("00 00 e3 5e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("88 bb 96 c8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("00 00 e3 5d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("8b d9 94 ea"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("00 00 91 8d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("00 00 97 ce"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("8f 8f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("00 00 e3 8e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("fb 8e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("e3 67 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("90 fc 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("e3 63 e3 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("e3 6a 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("92 f7 e3 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("e3 69 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("95 d2 8a c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("96 c9 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("00 00 88 dc"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_memset = PatchPattern(
    name=f"custom_functions_cgu0_memset",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff ff 39"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0___ct__TextWriterBase_WChar = PatchPattern(
    # JP 801fa670
    name=f"custom_functions_cgu0___ct__TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff e9 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c0 02 a1 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("c0 22 a1 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 0d b1 f4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d0 3f 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d0 1f 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d0 1f 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 bf 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 9f 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 1f 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternNA=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff e9 6d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c0 02 a1 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("c0 22 a1 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 0d b1 ec"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d0 3f 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d0 1f 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d0 1f 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 bf 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 9f 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 1f 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("4b ff bf cd"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c0 02 a1 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("c0 22 a1 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 0d b2 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d0 3f 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7f e3 fb 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d0 1f 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d0 1f 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 bf 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 9f 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 1f 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)

custom_functions_cgu0_CharWriter__UpdateVertexColor = PatchPattern(
    # jp 801fa230
    name=f"custom_functions_cgu0_CharWriter__UpdateVertexColor",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("88 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("88 a3 00 19"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("2c 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("88 83 00 1a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("88 03 00 1b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("98 c3 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("98 a3 00 09"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("98 83 00 0a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("98 03 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("41 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 a3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("38 a3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("88 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("98 03 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("88 85 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("98 83 00 0d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("2c 00 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("88 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("98 03 00 0e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("88 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("98 03 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("41 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("38 a3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("38 a3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("88 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("98 03 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("88 85 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("98 83 00 11"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("88 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("98 03 00 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("88 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("98 03 00 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("40 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("38 a3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("38 a3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("88 05 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("3c 80 80 81"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("98 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("39 44 80 81"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("88 03 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("88 85 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("98 83 00 15"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("88 e3 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("88 85 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("98 83 00 16"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("7c c0 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("88 83 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("88 03 00 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("89 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("7c a0 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("7c 08 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("7c 84 39 d6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("7d 0a 30 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("7c ea 20 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("7c c8 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("7c c8 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("7c ca 28 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("55 09 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("7c 87 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("7c e8 4a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("98 e3 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("7c 87 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("7c a6 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("54 e6 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("7c 8a 00 96"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("7c c7 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("98 c3 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("7c a5 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("54 a6 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("7c 04 02 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("7c 00 3e 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("7c a5 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("54 04 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("98 a3 00 13"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("7c 00 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("98 03 00 17"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)

custom_functions_cgu0_CalcStringRect_TextWriterBase_WChar = PatchPattern(
    # JP 801fdc00
    name=f"custom_functions_cgu0_CalcStringRect_TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("48 0f 40 c5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("82 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("82 23 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("82 43 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("82 63 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("82 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("82 a3 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("82 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("82 e3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("83 23 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("83 43 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 63 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 83 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 a3 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("83 c3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("83 e3 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("a1 83 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("89 63 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("89 43 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("c0 63 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("81 23 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("c0 43 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("c0 23 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("81 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("92 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("92 21 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("92 41 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("92 61 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("92 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("92 a1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("92 c1 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("92 e1 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("93 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("93 21 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("93 41 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("93 61 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("93 81 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("93 a1 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 c1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("93 e1 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("b1 81 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("99 61 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("99 41 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("d0 61 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("91 21 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("d0 41 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 21 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("90 e1 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 0e 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("4b ff b6 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("48 0f 40 1d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("80 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 21 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternNA=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("48 0f 42 f5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("82 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("82 23 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("82 43 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("82 63 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("82 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("82 a3 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("82 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("82 e3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("83 23 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("83 43 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 63 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 83 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 a3 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("83 c3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("83 e3 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("a1 83 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("89 63 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("89 43 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("c0 63 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("81 23 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("c0 43 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("c0 23 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("81 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("92 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("92 21 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("92 41 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("92 61 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("92 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("92 a1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("92 c1 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("92 e1 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("93 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("93 21 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("93 41 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("93 61 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("93 81 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("93 a1 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 c1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("93 e1 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("b1 81 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("99 61 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("99 41 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("d0 61 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("91 21 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("d0 41 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 21 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("90 e1 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 0e 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("4b ff b6 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("48 0f 42 4d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("80 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 21 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("48 0f 42 f5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("82 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("82 23 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("82 43 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("82 63 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("82 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("82 a3 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("82 c3 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("82 e3 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("83 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("83 23 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("83 43 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 63 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 83 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 a3 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("83 c3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("83 e3 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("a1 83 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("89 63 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("89 43 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("c0 63 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("81 23 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("c0 43 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("c0 23 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("81 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("92 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("92 21 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("92 41 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("92 61 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("92 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("92 a1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("92 c1 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("92 e1 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("93 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("93 21 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("93 41 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("93 61 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("93 81 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("93 a1 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 c1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("93 e1 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("b1 81 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("99 61 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("99 41 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("d0 61 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("91 21 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("d0 41 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 21 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("90 e1 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 0e 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("4b ff b6 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("39 61 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("48 0f 42 4d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("80 01 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 21 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]

)
custom_functions_cgu0_GXSetProjection = PatchPattern(
    # R8AE01 80224C60
    name=f"custom_functions_cgu0_GXSetProjection",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("2c 04 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("c0 23 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 85 05 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("c0 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("d0 25 05 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("c0 23 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("d0 05 05 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("c0 03 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("d0 25 05 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("d0 05 05 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("40 82 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("c0 03 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x38, pattern=parse_pattern_bytes("d0 05 05 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x3c, pattern=parse_pattern_bytes("c0 03 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x40, pattern=parse_pattern_bytes("d0 05 05 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x44, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x48, pattern=parse_pattern_bytes("c0 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x4c, pattern=parse_pattern_bytes("d0 05 05 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x50, pattern=parse_pattern_bytes("c0 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x54, pattern=parse_pattern_bytes("d0 05 05 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x58, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x5c, pattern=parse_pattern_bytes("64 00 08 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x60, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x64, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_C_MTXOrtho = PatchPattern(
    # JP 8021abd0
    name=f"custom_functions_cgu0_C_MTXOrtho",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("ed 64 18 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("c1 02 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("c1 42 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("ec e1 10 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("ec 06 28 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("c1 22 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("ed 8a 58 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("c0 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("d1 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("d1 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("d1 03 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("d1 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("ed 6a 38 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("d1 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("d1 03 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("d1 03 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("d1 03 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("d1 03 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("ec ea 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("d1 43 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("fc 00 30 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("ec 21 10 2a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("ec 64 18 2a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("ec c9 03 32"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("ec 00 01 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("fc 40 18 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("d0 c3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("ec 69 02 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("fc 20 08 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("d0 03 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("ec 8c 00 b2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("d0 63 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("ec 4b 00 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("ec 25 01 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("d0 83 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("d0 43 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("d0 23 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetViewport = PatchPattern(
    # R8AE01 GXSetViewport = .text:0x80225030; // type:function size:0x2C
    name=f"custom_functions_cgu0_GXSetViewport",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("d0 23 05 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("d0 43 05 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("d0 63 05 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("d0 83 05 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("d0 a3 05 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("d0 c3 05 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("80 03 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("64 00 10 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("90 03 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0_float_to_unsigned = PatchPattern(
    # JP 802f1bd8
    name=f"custom_functions_cgu0_float_to_unsigned",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("3c 80 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 84 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("c8 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("c8 64 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("c8 84 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("fc 01 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("ff 01 18 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("41 80 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("38 63 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("40 98 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("ff 81 20 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("fc 40 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("41 9c 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("fc 41 20 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("fc 40 10 1e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("d8 41 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 61 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("41 9c 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("3c 63 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetScissor = PatchPattern(
    # R8AE01 GXSetScissor = .text:0x80225080; // type:function size:0x68
    name=f"custom_functions_cgu0_GXSetScissor",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("81 02 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 84 01 56"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("39 23 01 56"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("3c e0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 08 01 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 80 05 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("51 20 62 66"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 08 01 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("7c c4 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("7c 69 2a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("38 06 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("80 a8 01 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("50 05 05 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x38, pattern=parse_pattern_bytes("38 63 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x3c, pattern=parse_pattern_bytes("50 65 62 66"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x40, pattern=parse_pattern_bytes("90 a8 01 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x44, pattern=parse_pattern_bytes("38 80 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x48, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x4c, pattern=parse_pattern_bytes("98 87 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x50, pattern=parse_pattern_bytes("80 68 01 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x54, pattern=parse_pattern_bytes("90 67 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x58, pattern=parse_pattern_bytes("98 87 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x5c, pattern=parse_pattern_bytes("80 68 01 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x60, pattern=parse_pattern_bytes("90 67 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x64, pattern=parse_pattern_bytes("b0 08 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x68, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXLoadPosMtxImm = PatchPattern(
    # R8AE01 GXLoadPosMtxImm = .text:0x80224D60; // type:function size:0x50
    name=f"custom_functions_cgu0_GXLoadPosMtxImm",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("3c a0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("98 05 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 80 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("64 00 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("38 85 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("90 05 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("e0 a3 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("e0 83 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("e0 63 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("e0 43 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("e0 23 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("e0 03 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("f0 a4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("f0 84 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("f0 64 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("f0 44 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("f0 24 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("f0 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetCurrentMtx = PatchPattern(
    # R8AE01 GXSetCurrentMtx = .text:0x80224E80; // type:function size:0x20
    name=f"custom_functions_cgu0_GXSetCurrentMtx",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 06 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("64 00 04 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0_GXClearVtxDesc = PatchPattern(
    # R8AE01 GXClearVtxDesc = .text:0x8021FAC0; // type:function size:0x34
    name=f"custom_functions_cgu0_GXClearVtxDesc",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("50 03 4d 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("90 65 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 85 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("98 85 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("98 85 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("60 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0_GXSetVtxAttrFmt = PatchPattern(
    # R8AE01 GXSetVtxAttrFmt = .text:0x8021FB00; // type:function size:0x1A0
    name=f"custom_functions_cgu0_GXSetVtxAttrFmt",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("38 04 ff f7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("81 02 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("28 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 64 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7d 08 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("41 81 01 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("3c 80 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("54 00 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 84 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("7c 84 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7c 89 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("4e 80 04 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("50 a0 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("50 c0 0f 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("50 e0 25 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("48 00 01 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("2c 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("50 c0 54 ea"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("40 82 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("60 00 02 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("64 00 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("48 00 01 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("50 a0 4d ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("54 00 00 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("48 00 00 f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("50 a0 6c a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("50 c0 73 e2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("48 00 00 dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("50 a0 8b 9c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("50 c0 92 da"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 00 c8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("80 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("50 a0 aa 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("50 c0 b1 d2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("50 e0 c8 8c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("90 08 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("48 00 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("50 a0 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("50 c0 0f 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("50 e0 25 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("48 00 00 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("50 a0 4d ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("50 c0 54 ea"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("50 e0 6b a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("50 a0 93 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("50 c0 9a 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("50 e0 b1 52"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("48 00 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("80 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("50 a0 d9 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("50 c0 e0 46"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("90 08 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("50 e0 06 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("48 00 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("50 a0 2e b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("50 c0 35 f2"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("50 e0 4c ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("48 00 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("50 a0 74 62"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("50 c0 7b a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("50 e0 92 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("48 00 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("80 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("50 a0 ba 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("50 c0 c1 4e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("50 e0 d8 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("90 08 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("54 60 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("80 85 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("7c 60 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("54 00 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("60 83 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("90 65 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("88 65 05 fb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("7c 60 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("98 05 05 fb"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0_GXInvalidateVtxCache = PatchPattern(
    # R8AE01 GXInvalidateVtxCache = .text:0x80220190; // type:function size:0x10
    name=f"custom_functions_cgu0_GXInvalidateVtxCache",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 00 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("98 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetVtxDesc = PatchPattern(
    # R8AE01 GXSetVtxDesc = .text:0x8021F4B0; // type:function size:0x264
    name=f"custom_functions_cgu0_GXSetVtxDesc",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("28 03 00 19"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("41 81 02 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("3c a0 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 60 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("38 a5 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c a5 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7c a9 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("4e 80 04 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("50 80 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("48 00 01 e4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("50 80 0f bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("48 00 01 d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("50 80 17 7a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("48 00 01 bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("50 80 1f 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("48 00 01 a8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("50 80 26 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("48 00 01 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("50 80 2e b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("48 00 01 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("50 80 36 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 01 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("50 80 3e 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("48 00 01 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("50 80 45 ee"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("48 00 01 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("50 80 4d 6c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("48 00 01 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("2c 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("41 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("98 65 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("98 05 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("90 85 05 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("48 00 01 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("98 03 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("48 00 00 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("2c 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("41 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("98 65 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("98 05 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("90 85 05 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("48 00 00 d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("98 03 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("48 00 00 c8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("50 80 6c 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("48 00 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("50 80 7b e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("90 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("48 00 00 a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("50 80 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("48 00 00 8c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("50 80 17 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("48 00 00 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("50 80 26 b6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("48 00 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("50 80 36 32"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("48 00 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("50 80 45 ae"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("48 00 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("50 80 55 2a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("48 00 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("50 80 64 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=129, offset=0x200, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=130, offset=0x204, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=131, offset=0x208, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=132, offset=0x20c, pattern=parse_pattern_bytes("50 80 74 22"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=133, offset=0x210, pattern=parse_pattern_bytes("90 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=134, offset=0x214, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=135, offset=0x218, pattern=parse_pattern_bytes("88 04 05 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=136, offset=0x21c, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=137, offset=0x220, pattern=parse_pattern_bytes("40 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=138, offset=0x224, pattern=parse_pattern_bytes("88 04 05 25"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=139, offset=0x228, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=140, offset=0x22c, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=141, offset=0x230, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=142, offset=0x234, pattern=parse_pattern_bytes("80 05 05 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=143, offset=0x238, pattern=parse_pattern_bytes("80 65 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=144, offset=0x23c, pattern=parse_pattern_bytes("50 03 5c e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=145, offset=0x240, pattern=parse_pattern_bytes("90 65 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=146, offset=0x244, pattern=parse_pattern_bytes("48 00 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=147, offset=0x248, pattern=parse_pattern_bytes("80 04 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=148, offset=0x24c, pattern=parse_pattern_bytes("54 00 05 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=149, offset=0x250, pattern=parse_pattern_bytes("90 04 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=150, offset=0x254, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=151, offset=0x258, pattern=parse_pattern_bytes("60 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=152, offset=0x25c, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=153, offset=0x260, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetNumChans = PatchPattern(
    # R8AE01 GXSetNumChans = .text:0x80222570; // type:function size:0x24
    name=f"custom_functions_cgu0_GXSetNumChans",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 26 76"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("64 00 01 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0_GXSetChanCtrl = PatchPattern(
    # R8AE01 GXSetChanCtrl = .text:0x802225A0; // type:function size:0xA4
    name=f"custom_functions_cgu0_GXSetChanCtrl",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("2c 09 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("39 40 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("50 8a 0f bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("54 6b 07 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("50 ca 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("50 aa 36 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("40 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("20 a9 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 89 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7c a4 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7c 09 00 d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("51 0a 3d f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("50 8a 55 ac"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("55 64 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("7c 00 4b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("2c 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("50 0a 5d 6a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 85 22 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("50 ea 16 ba"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 00 10 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("50 ea 3c 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("91 44 00 b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("7c 00 58 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("80 85 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("7c 80 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("40 82 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("91 45 00 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("60 00 50 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("2c 03 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("4c 82 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("91 45 00 c4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("60 00 a0 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetNumTexGens = PatchPattern(
    # R8AE01 GXSetNumTexGens = .text:0x802203F0; // type:function size:0x24
    name=f"custom_functions_cgu0_GXSetNumTexGens",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 07 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("64 00 02 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetNumIndStages = PatchPattern(
    # R8AE01 GXSetNumIndStages = .text:0x80223AD0; // type:function size:0x20
    name=f"custom_functions_cgu0_GXSetNumIndStages",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 60 83 5e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("60 00 00 06"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetChanMatColor = PatchPattern(
    # R8AE01 GXSetChanMatColor = .text:0x80222490; // type:function size:0xD8
    name=f"custom_functions_cgu0_GXSetChanMatColor",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("41 82 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("41 82 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("2c 03 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("41 82 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("2c 03 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("41 82 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("2c 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("41 82 00 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("2c 03 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("41 82 00 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("80 e3 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("50 07 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("48 00 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("39 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("80 04 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("80 e3 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("50 07 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("48 00 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("88 04 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("80 e3 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("50 07 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("48 00 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 62 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("39 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("88 04 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("80 e3 00 b4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("50 07 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("48 00 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("80 e4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("80 e4 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("39 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("80 c2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("38 60 04 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("55 00 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("80 a6 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("7c 64 40 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("7c 66 02 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("7c a0 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("90 06 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("90 e3 00 b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0___GXSetIndirectMask = PatchPattern(
    # R8AE01 __GXSetIndirectMask = .text:0x80223B50; // type:function size:0x30 scope:global
    name=f"custom_functions_cgu0___GXSetIndirectMask",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 c7 01 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 66 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("90 c7 01 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("80 67 01 74"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("90 64 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetNumTevStages = PatchPattern(
    # R8AE01 GXSetNumTevStages = .text:0x80224250; // type:function size:0x24
    name=f"custom_functions_cgu0_GXSetNumTevStages",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 03 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("80 64 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("50 03 54 aa"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("90 64 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetTevOp = PatchPattern(
    # R8AE01 GXSetTevOp = .text:0x80223BB0; // type:function size:0x94
    name=f"custom_functions_cgu0_GXSetTevOp",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("3c a0 80 35"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 a5 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("40 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("54 86 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("38 85 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 05 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7d 04 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7d 20 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("48 00 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("54 86 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 85 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("38 05 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7d 04 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("7d 20 32 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("54 60 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("80 68 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c c7 02 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("81 06 01 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("55 08 00 0e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("50 68 02 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("91 04 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("91 06 01 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("81 06 01 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("80 69 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("55 08 07 0e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("50 68 02 36"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("91 04 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("91 06 01 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetTevOrder = PatchPattern(
    # R8AE01 GXSetTevOrder = .text:0x802240F0; // type:function size:0x15C
    name=f"custom_functions_cgu0_GXSetTevOrder",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("54 ab 06 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 e0 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("54 69 0f fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("81 42 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 07 58 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("54 68 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7c 07 01 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7d 29 1a 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7c ea 42 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("2c 04 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("55 28 08 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("20 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("90 a7 05 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7c ea 42 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("7d 69 00 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("41 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("81 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("7c 00 18 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("7d 00 00 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("48 00 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("81 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("7c 00 18 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("7d 00 03 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("90 0a 05 e8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("54 60 07 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("41 82 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("81 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("2c 06 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("51 28 64 66"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("50 88 7b a0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("40 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("38 00 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("3c 60 80 35"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("54 c0 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("38 63 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("7c 03 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("2c 05 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("50 08 9a 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("41 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("54 a0 05 ef"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("40 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("50 68 93 5a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("48 00 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("81 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("2c 06 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("51 28 07 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("50 88 1e b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("40 82 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("38 00 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("48 00 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("3c 60 80 35"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("54 c0 10 3a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("38 63 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("7c 03 00 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("2c 05 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("50 08 3d b0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("41 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("54 a0 05 ef"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("40 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("50 68 36 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("91 07 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("38 00 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("98 04 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("80 a2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("80 67 01 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("90 64 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("b0 05 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("80 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("60 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("90 05 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetBlendMode = PatchPattern(
    # R8AE01 GXSetBlendMode = .text:0x80224720; // type:function size:0x50
    name=f"custom_functions_cgu0_GXSetBlendMode",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("81 42 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("38 03 ff fd"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("39 03 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("3c e0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("81 2a 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("7c 00 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("50 09 35 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("7d 08 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("38 00 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("98 07 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("50 69 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("51 09 e7 bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x38, pattern=parse_pattern_bytes("50 c9 64 26"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x3c, pattern=parse_pattern_bytes("50 89 45 6e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x40, pattern=parse_pattern_bytes("50 a9 2e 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x44, pattern=parse_pattern_bytes("91 27 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x48, pattern=parse_pattern_bytes("91 2a 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x4c, pattern=parse_pattern_bytes("b0 0a 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x50, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetColorUpdate = PatchPattern(
    # R8AE01 GXSetColorUpdate = .text:0x80224770; // type:function size:0x2C
    name=f"custom_functions_cgu0_GXSetColorUpdate",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 66 1f 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 c4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("90 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0_GXSetAlphaUpdate = PatchPattern(
    # R8AE01 GXSetAlphaUpdate = .text:0x802247A0; // type:function size:0x2C
    name=f"custom_functions_cgu0_GXSetAlphaUpdate",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c 80 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 a0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("80 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 66 26 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("98 a4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("90 c4 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("90 c7 02 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("b0 07 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetZMode = PatchPattern(
    # R8AE01 GXSetZMode = .text:0x802247D0; // type:function size:0x34
    name=f"custom_functions_cgu0_GXSetZMode",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("81 22 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("3c c0 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("38 e0 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("81 09 02 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("50 68 07 fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("50 88 0f 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("98 e6 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("50 a8 26 f6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("91 06 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x2c, pattern=parse_pattern_bytes("91 09 02 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x30, pattern=parse_pattern_bytes("b0 09 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x34, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetCullMode = PatchPattern(
    # R8AE01 GXSetCullMode = .text:0x80221250; // type:function size:0x28
    name=f"custom_functions_cgu0_GXSetCullMode",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=0, offset=0x0, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=1, offset=0x4, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x8, pattern=parse_pattern_bytes("54 65 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0xc, pattern=parse_pattern_bytes("50 65 0f bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0x10, pattern=parse_pattern_bytes("80 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x14, pattern=parse_pattern_bytes("50 a0 74 22"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x18, pattern=parse_pattern_bytes("90 04 02 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x1c, pattern=parse_pattern_bytes("80 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x20, pattern=parse_pattern_bytes("60 00 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x24, pattern=parse_pattern_bytes("90 04 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x28, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
    ,
)
custom_functions_cgu0_GXBegin = PatchPattern(
    # R8AE01 GXBegin = .text:0x80220F60; // type:function size:0x14C
    name=f"custom_functions_cgu0_GXBegin",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("83 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("93 c1 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("7c be 2b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("93 a1 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7c 9d 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("93 81 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("7c 7c 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("80 1f 05 fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("41 82 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b ff fd 49"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("40 82 00 d8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 e2 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 00 00 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("a0 a7 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("a0 87 00 06"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("7c a5 21 d7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("98 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("a0 07 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("b0 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("41 82 00 a4"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("38 65 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("38 e5 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("54 60 f0 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("28 00 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("40 81 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("28 03 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("41 80 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("7c 05 18 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("41 81 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("41 82 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("38 07 00 1f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("54 00 d9 7e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("7c 09 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("28 07 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("40 81 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("38 c6 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("42 00 ff dc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("38 05 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("7c 06 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("54 00 f0 be"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("7c 09 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("7c 06 28 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("40 80 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("90 83 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("42 00 ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("b0 1f 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("3c 60 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("7f a0 e3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("98 03 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("b3 c3 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("80 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("83 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("83 c1 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("83 a1 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("83 81 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("38 21 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_data = PatchPattern(
    name=f"custom_functions_cgu0_data",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('000000ff'),
            new_instruction_readable=".long 0xff"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('000000ff'),
            new_instruction_readable=".long 0xff"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("00 00 fb 84"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("9a f2 e2 8a"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_CharWriter__GetFontWidth = PatchPattern(
    # R8AE01 GetFontWidth__Q36nw4hbm2ut10CharWriterCFv = .text:0x802B6AD0; // type:function size:0x64
    name=f"custom_functions_cgu0_CharWriter__GetFontWidth",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff e0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("93 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("80 63 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("81 83 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("81 8c 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("7d 89 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("4e 80 04 21"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("6c 63 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("3c 00 43 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("3c 80 80 31"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("90 61 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("c8 44 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("c0 1f 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("c8 21 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("83 e1 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("ec 21 10 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("80 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("ec 20 00 72"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("38 21 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_GXSetAlphaCompare = PatchPattern(
    # R8AE01 GXSetAlphaCompare = .text:0x80224020; // type:function size:0x38
    name=f"custom_functions_cgu0_GXSetAlphaCompare",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("3d 00 cc 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("38 00 00 61"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("98 08 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("3d 20 f3 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("50 89 06 3e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("80 82 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("50 e9 44 2e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("38 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("50 69 83 5e"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("50 c9 9a 98"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("50 a9 b2 12"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("91 28 80 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("b0 04 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_CharWriter__SetupGX = PatchPattern(
    # R8AE01 SetupGX__Q36nw4hbm2ut10CharWriterFv = .text:0x802B5D70; // type:function size:0x950
    name=f"custom_functions_cgu0_CharWriter__SetupGX",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("38 00 00 ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("3b e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("3f c0 80 ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("3b de ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 9e 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("90 1e 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("93 e4 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("80 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("2c 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("40 82 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("80 83 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("3c 04 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("28 00 ff ff"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("41 82 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("80 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 81 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 01 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("80 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("38 61 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("90 01 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("48 00 12 ad"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("48 00 08 d0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("80 63 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("41 82 07 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("81 83 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("81 8c 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("7d 89 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("4e 80 04 21"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("38 03 ff fc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("28 00 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("40 81 03 c0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("28 03 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("40 81 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("38 03 ff fe"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("28 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("40 81 02 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("48 00 05 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("88 1e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("40 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("93 fe 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("98 1e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("3c 60 80 31"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("80 1e 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("c0 23 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("38 81 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("90 01 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("fc 40 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("fc 60 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("fc 80 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("38 c0 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("38 e0 00 03"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("38 80 00 11"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("38 60 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("38 c0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("39 20 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("38 60 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=81, offset=0x140, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=82, offset=0x144, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=83, offset=0x148, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=84, offset=0x14c, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=85, offset=0x150, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=86, offset=0x154, pattern=parse_pattern_bytes("39 20 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=87, offset=0x158, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=88, offset=0x15c, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=89, offset=0x160, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=90, offset=0x164, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=91, offset=0x168, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=92, offset=0x16c, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=93, offset=0x170, pattern=parse_pattern_bytes("38 c0 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=94, offset=0x174, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=95, offset=0x178, pattern=parse_pattern_bytes("39 00 00 7d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=96, offset=0x17c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=97, offset=0x180, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=98, offset=0x184, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=99, offset=0x188, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=100, offset=0x18c, pattern=parse_pattern_bytes("38 80 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=101, offset=0x190, pattern=parse_pattern_bytes("38 a0 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=102, offset=0x194, pattern=parse_pattern_bytes("38 c0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=103, offset=0x198, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=104, offset=0x19c, pattern=parse_pattern_bytes("38 60 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=105, offset=0x1a0, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=106, offset=0x1a4, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=107, offset=0x1a8, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=108, offset=0x1ac, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=109, offset=0x1b0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=110, offset=0x1b4, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=111, offset=0x1b8, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=112, offset=0x1bc, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=113, offset=0x1c0, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=114, offset=0x1c4, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=115, offset=0x1c8, pattern=parse_pattern_bytes("38 c0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=116, offset=0x1cc, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=117, offset=0x1d0, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=118, offset=0x1d4, pattern=parse_pattern_bytes("38 80 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=119, offset=0x1d8, pattern=parse_pattern_bytes("38 a0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=120, offset=0x1dc, pattern=parse_pattern_bytes("38 c0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=121, offset=0x1e0, pattern=parse_pattern_bytes("38 e0 00 0a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=122, offset=0x1e4, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=123, offset=0x1e8, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=124, offset=0x1ec, pattern=parse_pattern_bytes("38 80 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=125, offset=0x1f0, pattern=parse_pattern_bytes("38 a0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=126, offset=0x1f4, pattern=parse_pattern_bytes("38 c0 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=127, offset=0x1f8, pattern=parse_pattern_bytes("38 e0 00 07"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=128, offset=0x1fc, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=129, offset=0x200, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=130, offset=0x204, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=131, offset=0x208, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=132, offset=0x20c, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=133, offset=0x210, pattern=parse_pattern_bytes("38 e0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=134, offset=0x214, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=135, offset=0x218, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=136, offset=0x21c, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=137, offset=0x220, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=138, offset=0x224, pattern=parse_pattern_bytes("38 a0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=139, offset=0x228, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=140, offset=0x22c, pattern=parse_pattern_bytes("38 e0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=141, offset=0x230, pattern=parse_pattern_bytes("39 00 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=142, offset=0x234, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=143, offset=0x238, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=144, offset=0x23c, pattern=parse_pattern_bytes("38 80 00 09"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=145, offset=0x240, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=146, offset=0x244, pattern=parse_pattern_bytes("38 c0 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=147, offset=0x248, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=148, offset=0x24c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=149, offset=0x250, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=150, offset=0x254, pattern=parse_pattern_bytes("38 80 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=151, offset=0x258, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=152, offset=0x25c, pattern=parse_pattern_bytes("38 c0 00 05"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=153, offset=0x260, pattern=parse_pattern_bytes("38 e0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=154, offset=0x264, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=155, offset=0x268, pattern=parse_pattern_bytes("38 60 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=156, offset=0x26c, pattern=parse_pattern_bytes("38 80 00 0d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=157, offset=0x270, pattern=parse_pattern_bytes("38 a0 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=158, offset=0x274, pattern=parse_pattern_bytes("38 c0 00 02"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=159, offset=0x278, pattern=parse_pattern_bytes("38 e0 00 0f"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=160, offset=0x27c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=161, offset=0x280, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=162, offset=0x284, pattern=parse_pattern_bytes("38 60 00 09"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=163, offset=0x288, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=164, offset=0x28c, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=165, offset=0x290, pattern=parse_pattern_bytes("38 60 00 0b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=166, offset=0x294, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=167, offset=0x298, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=168, offset=0x29c, pattern=parse_pattern_bytes("38 60 00 0d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=169, offset=0x2a0, pattern=parse_pattern_bytes("38 80 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=170, offset=0x2a4, pattern=parse_pattern_bytes("4b f6 ?? ??"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=171, offset=0x2a8, pattern=parse_pattern_bytes("48 00 06 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=172, offset=0x2ac, pattern=parse_pattern_bytes("88 1e 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=173, offset=0x2b0, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=174, offset=0x2b4, pattern=parse_pattern_bytes("40 82 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=175, offset=0x2b8, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        # uncomplete pattern
    ]
    ,
)
custom_functions_cgu0_Print_TextWriterBase_WChar = PatchPattern(
    # R8AE01 Print__Q36nw4hbm2ut17TextWriterBase<w>FPCw = .text:0x802BCB20; // type:function size:0x170
    # JP 801fb760
    name=f"custom_functions_cgu0_Print_TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff 70"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("38 c0 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("db e1 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("f3 e1 00 88"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 e1 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7f 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("80 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("90 01 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("80 03 00 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("90 01 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("80 03 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("90 01 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("80 03 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("80 03 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("90 01 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 03 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("90 01 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("80 03 00 18"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("90 01 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=23, offset=0x58, pattern=parse_pattern_bytes("80 03 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=24, offset=0x5c, pattern=parse_pattern_bytes("90 01 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=25, offset=0x60, pattern=parse_pattern_bytes("80 03 00 20"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=26, offset=0x64, pattern=parse_pattern_bytes("90 01 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=27, offset=0x68, pattern=parse_pattern_bytes("80 e3 00 24"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=28, offset=0x6c, pattern=parse_pattern_bytes("80 03 00 28"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=29, offset=0x70, pattern=parse_pattern_bytes("90 01 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=30, offset=0x74, pattern=parse_pattern_bytes("90 e1 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=31, offset=0x78, pattern=parse_pattern_bytes("80 e3 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=32, offset=0x7c, pattern=parse_pattern_bytes("80 03 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=33, offset=0x80, pattern=parse_pattern_bytes("90 01 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=34, offset=0x84, pattern=parse_pattern_bytes("90 e1 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=35, offset=0x88, pattern=parse_pattern_bytes("80 03 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=36, offset=0x8c, pattern=parse_pattern_bytes("90 01 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=37, offset=0x90, pattern=parse_pattern_bytes("80 e3 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=38, offset=0x94, pattern=parse_pattern_bytes("80 03 00 3c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=39, offset=0x98, pattern=parse_pattern_bytes("90 01 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=40, offset=0x9c, pattern=parse_pattern_bytes("90 e1 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=41, offset=0xa0, pattern=parse_pattern_bytes("a0 03 00 40"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=42, offset=0xa4, pattern=parse_pattern_bytes("b0 01 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=43, offset=0xa8, pattern=parse_pattern_bytes("88 03 00 42"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=44, offset=0xac, pattern=parse_pattern_bytes("98 01 00 4a"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=45, offset=0xb0, pattern=parse_pattern_bytes("88 03 00 43"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=46, offset=0xb4, pattern=parse_pattern_bytes("98 01 00 4b"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=47, offset=0xb8, pattern=parse_pattern_bytes("c0 03 00 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=48, offset=0xbc, pattern=parse_pattern_bytes("d0 01 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=49, offset=0xc0, pattern=parse_pattern_bytes("80 03 00 48"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=50, offset=0xc4, pattern=parse_pattern_bytes("90 01 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=51, offset=0xc8, pattern=parse_pattern_bytes("c0 03 00 4c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=52, offset=0xcc, pattern=parse_pattern_bytes("d0 01 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=53, offset=0xd0, pattern=parse_pattern_bytes("c0 03 00 50"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=54, offset=0xd4, pattern=parse_pattern_bytes("d0 01 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=55, offset=0xd8, pattern=parse_pattern_bytes("c0 03 00 54"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=56, offset=0xdc, pattern=parse_pattern_bytes("d0 01 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=57, offset=0xe0, pattern=parse_pattern_bytes("80 03 00 58"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=58, offset=0xe4, pattern=parse_pattern_bytes("90 01 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=59, offset=0xe8, pattern=parse_pattern_bytes("80 03 00 5c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=60, offset=0xec, pattern=parse_pattern_bytes("90 01 00 64"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=61, offset=0xf0, pattern=parse_pattern_bytes("80 03 00 60"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=62, offset=0xf4, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=63, offset=0xf8, pattern=parse_pattern_bytes("90 01 00 68"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=64, offset=0xfc, pattern=parse_pattern_bytes("48 00 0a a5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=65, offset=0x100, pattern=parse_pattern_bytes("c0 01 00 38"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=66, offset=0x104, pattern=parse_pattern_bytes("ff e0 08 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=67, offset=0x108, pattern=parse_pattern_bytes("c0 41 00 34"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=68, offset=0x10c, pattern=parse_pattern_bytes("38 61 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=69, offset=0x110, pattern=parse_pattern_bytes("d0 5f 00 2c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=70, offset=0x114, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=71, offset=0x118, pattern=parse_pattern_bytes("d0 1f 00 30"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=72, offset=0x11c, pattern=parse_pattern_bytes("4b ff da f5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=73, offset=0x120, pattern=parse_pattern_bytes("fc 20 f8 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=74, offset=0x124, pattern=parse_pattern_bytes("e3 e1 00 88"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=75, offset=0x128, pattern=parse_pattern_bytes("cb e1 00 80"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=76, offset=0x12c, pattern=parse_pattern_bytes("83 e1 00 7c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=77, offset=0x130, pattern=parse_pattern_bytes("80 01 00 94"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=78, offset=0x134, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=79, offset=0x138, pattern=parse_pattern_bytes("38 21 00 90"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=80, offset=0x13c, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0___dt__TextWriterBase_WChar = PatchPattern(
    # R8AE01 __dt__Q36nw4hbm2ut17TextWriterBase<c>Fv = .text:0x802B8B20; // type:function size:0x58
    name=f"custom_functions_cgu0___dt__TextWriterBase_WChar",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("4b ff d1 c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("2c 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b d5 41 39"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternNA=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("4b ff d1 c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("2c 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b d5 1d b9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("2c 03 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("93 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("7c 9f 23 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("93 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("7c 7e 1b 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("41 82 00 1c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("38 80 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("4b ff d1 c9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("2c 1f 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("40 81 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4b d5 1a d9"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=16, offset=0x3c, pattern=parse_pattern_bytes("7f c3 f3 78"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=17, offset=0x40, pattern=parse_pattern_bytes("83 e1 00 0c"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=18, offset=0x44, pattern=parse_pattern_bytes("83 c1 00 08"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=19, offset=0x48, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=20, offset=0x4c, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=21, offset=0x50, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=22, offset=0x54, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)
custom_functions_cgu0__ZN4core6result13unwrap_failed17h0125321215ca17fdE = PatchPattern(
    name=f"custom_functions_cgu0__ZN4core6result13unwrap_failed17h0125321215ca17fdE",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c0802a6'),
            new_instruction_readable="mflr    r0"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9421fff0'),
            new_instruction_readable="stwu    r1,-16(r1)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90010014'),
            new_instruction_readable="stw     r0,20(r1)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns,
                custom_functions_cgu0__ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE.name, 1
            ),
            new_instruction_readable="bl .text.unlikely._ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("e3 92 e3 93"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("fa 5c 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("e3 94 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("e3 9a 93 5a"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0__ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE = PatchPattern(
    name=f"custom_functions_cgu0__ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('48000000'),
            new_instruction_readable="b       0 <_ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE>"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("e2 b1 e2 ad"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("fb 88 e2 af"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 8a c7"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 00 00"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0__ZN4core6option13unwrap_failed17hfe475aa334a9986aE = PatchPattern(
    name=f"custom_functions_cgu0__ZN4core6option13unwrap_failed17hfe475aa334a9986aE",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c0802a6'),
            new_instruction_readable="mflr    r0"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9421fff0'),
            new_instruction_readable="stwu    r1,-16(r1)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90010014'),
            new_instruction_readable="stw     r0,20(r1)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns, custom_functions_cgu0__ZN4core9panicking5panic17h83cc215b64fda1bbE.name, 1
            ),
            new_instruction_readable="bl .text.unlikely._ZN4core9panicking5panic17h83cc215b64fda1bbE"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("fb 8b 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("8d 69 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("00 00 97 8d"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("88 ba e3 52"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0__ZN4core9panicking5panic17h83cc215b64fda1bbE = PatchPattern(
    name=f"custom_functions_cgu0__ZN4core9panicking5panic17h83cc215b64fda1bbE",
    patchMapJP=[
        Patch(
            identifier=1,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('7c0802a6'),
            new_instruction_readable="mflr    r0"
        ),
        Patch(
            identifier=2,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('9421fff0'),
            new_instruction_readable="stwu    r1,-16(r1)"
        ),
        Patch(
            identifier=3,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: bytes.fromhex('90010014'),
            new_instruction_readable="stw     r0,20(r1)"
        ),
        Patch(
            identifier=4,
            patch_function=lambda offset, data, plando_dict, patch_patterns, pattern_name: compute_bl_to_function(
                offset, data, patch_patterns,
                custom_functions_cgu0__ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE.name, 1
            ),
            new_instruction_readable="bl .text.unlikely._ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE"
        ),
    ],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("91 67 e3 44"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("e3 4a 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("fb 8a 00 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("00 00 e3 45"),
            instruction_readable="---"
        ),
    ],
)
custom_functions_cgu0_get_font_data = PatchPattern(
    name=f"custom_functions_cgu0_get_font_data",
    patchMapJP=[],
    patternJP=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("88 0d af b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("40 82 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 6d af bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("48 00 13 b5"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("98 0d af b8"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 6d af bc"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ],
    patternPAL=[
        Instruction(
            identifier=1, offset=0x0, pattern=parse_pattern_bytes("94 21 ff f0"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=2, offset=0x4, pattern=parse_pattern_bytes("7c 08 02 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=3, offset=0x8, pattern=parse_pattern_bytes("90 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=4, offset=0xc, pattern=parse_pattern_bytes("88 0d b0 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=5, offset=0x10, pattern=parse_pattern_bytes("7c 00 07 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=6, offset=0x14, pattern=parse_pattern_bytes("40 82 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=7, offset=0x18, pattern=parse_pattern_bytes("38 6d b0 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=8, offset=0x1c, pattern=parse_pattern_bytes("48 00 14 75"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=9, offset=0x20, pattern=parse_pattern_bytes("38 00 00 01"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=10, offset=0x24, pattern=parse_pattern_bytes("98 0d b0 00"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=11, offset=0x28, pattern=parse_pattern_bytes("80 01 00 14"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=12, offset=0x2c, pattern=parse_pattern_bytes("38 6d b0 04"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=13, offset=0x30, pattern=parse_pattern_bytes("7c 08 03 a6"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=14, offset=0x34, pattern=parse_pattern_bytes("38 21 00 10"),
            instruction_readable="---"
        ),
        Instruction(
            identifier=15, offset=0x38, pattern=parse_pattern_bytes("4e 80 00 20"),
            instruction_readable="---"
        ),
    ]
)
custom_functions_pattern = [
    custom_functions_cgu0_print_archipelago_text,
    custom_functions_cgu0_archipelago_text_buffer,
    custom_functions_cgu0_cst4,
    custom_functions_cgu0_memcpy,
    custom_functions_cgu0__Lanon_c56ae961650860ac32e9b2618d293ecb_6,
    custom_functions_cgu0_memset,
    custom_functions_cgu0___ct__TextWriterBase_WChar,
    custom_functions_cgu0_CharWriter__UpdateVertexColor,
    custom_functions_cgu0_CalcStringRect_TextWriterBase_WChar,
    custom_functions_cgu0_GXSetProjection,
    custom_functions_cgu0_C_MTXOrtho,
    custom_functions_cgu0_GXSetViewport,
    custom_functions_cgu0_float_to_unsigned,
    custom_functions_cgu0_GXSetScissor,
    custom_functions_cgu0_GXLoadPosMtxImm,
    custom_functions_cgu0_GXSetCurrentMtx,
    custom_functions_cgu0_GXClearVtxDesc,
    custom_functions_cgu0_GXSetVtxAttrFmt,
    custom_functions_cgu0_GXInvalidateVtxCache,
    custom_functions_cgu0_GXSetVtxDesc,
    custom_functions_cgu0_GXSetNumChans,
    custom_functions_cgu0_GXSetChanCtrl,
    custom_functions_cgu0_GXSetNumTexGens,
    custom_functions_cgu0_GXSetNumIndStages,
    custom_functions_cgu0_GXSetChanMatColor,
    custom_functions_cgu0___GXSetIndirectMask,
    custom_functions_cgu0_GXSetNumTevStages,
    custom_functions_cgu0_GXSetTevOp,
    custom_functions_cgu0_GXSetTevOrder,
    custom_functions_cgu0_GXSetBlendMode,
    custom_functions_cgu0_GXSetColorUpdate,
    custom_functions_cgu0_GXSetAlphaUpdate,
    custom_functions_cgu0_GXSetZMode,
    custom_functions_cgu0_GXSetCullMode,
    custom_functions_cgu0_GXBegin,
    custom_functions_cgu0_data,
    custom_functions_cgu0_CharWriter__GetFontWidth,
    custom_functions_cgu0_GXSetAlphaCompare,
    custom_functions_cgu0_CharWriter__SetupGX,
    custom_functions_cgu0_Print_TextWriterBase_WChar,
    custom_functions_cgu0___dt__TextWriterBase_WChar,
    custom_functions_cgu0__ZN4core6result13unwrap_failed17h0125321215ca17fdE,
    custom_functions_cgu0__ZN4core9panicking9panic_fmt17h7abdb1aa5838eaaeE,
    custom_functions_cgu0__ZN4core6option13unwrap_failed17hfe475aa334a9986aE,
    custom_functions_cgu0__ZN4core9panicking5panic17h83cc215b64fda1bbE,
    custom_functions_cgu0_get_font_data
]
