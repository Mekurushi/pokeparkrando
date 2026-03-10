.open "main.dol"
.org 0x80031174 ; called every frame
bl main_routine
addi r11, sp, 0x20
bl main_loop_restore
lwz r0, 0x24 (sp)
mtlr r0
addi sp, sp, 0x20
blr
.org 0x80366348 ; free space for pointers
.long PATCHER_VERSION
.long PLAYER_NAME
.long GIVE_ITEM_ARRAY
.long ARCHIPELAGO_TEXT_BUFFER
.long DEATH_TRIGGER
.long SHOULD_PRINT_AP_BUFFER
.org 0x80338a60 ; globalManager vtable
.long global_manager_syscall_wrapper
.close