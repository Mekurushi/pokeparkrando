.open "main.dol"
.org 0x80030f54 ; called every frame
bl main_routine
addi r11, sp, 0x20
bl main_loop_restore
lwz r0, 0x24 (sp)
mtlr r0
addi sp, sp, 0x20
blr
.close