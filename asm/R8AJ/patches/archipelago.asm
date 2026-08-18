.open "main.dol"
.org 0x80034410 ; called every frame
bl main_routine
lwz r31, 0xc (sp)
lwz r0, 0x14 (sp)
mtlr r0
addi sp, sp, 0x10
blr

.org 0x80366348 ; free space for pointers
.long PATCHER_VERSION
.long PLAYER_NAME
.long GIVE_ITEM_ARRAY
.long SHOULD_PRINT_AP_BUFFER
.long ARCHIPELAGO_TEXT_BUFFER
.long IS_DEATH
.long DEATH_TRIGGER
.long FPS_ENHANCEMENT; fps enhancement trigger
.long 0x80374fe0 ; GLobalManager Data space
.long 0x80482fb8 ; MenuScriptStart pointer only active in title screen
.long 0x80483338 ; game initialized once up to title screen
.long 0x8039CA48 ; attraction ID

.org 0x803365e0 ; globalManager vtable
.long global_manager_syscall_wrapper

.org 0x8017aa24 ; attraction data setup cmpwi r30, 0x7
cmpwi r30, 0xff
.org 0x8017aa2c ; attraction data setup cmpwi r30, 0xd
cmpwi r30, 0xff

.org 0x80123da0 ; default spawn stage
li r5, 0x2
li r4, 0x1
li r0, 0x5

.org 0x80124f80 ; spawn load from savefile
lhz r0, 0x5f02 (r31)

.org 0x80169668 ; wrapping set_frame_limit
bl set_frame_limit_wrapper

.org 0x80169d80 ; wrapping set_frame_limit
bl set_frame_limit_wrapper

.close