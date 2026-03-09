mod items;

use crate::game::global_manager::{lookup_global_manager, FlagName};
use crate::game::scene_manager::{lookup_scene_manager, SceneName};
use crate::rando::items::{
    get_dash_params, get_health_params, get_iron_tail_params, get_item_detail,
    get_thunderbolt_params, Itemflag,
};
use crate::utils::console::Console;
use crate::utils::module::{lookup_module, ModuleName};
use core::{fmt::Write, str::from_utf8};

#[repr(C)]
pub struct ArchipelagoDataInterface {
    // constants
    pub patcher_version_major: u32,
    pub patcher_version_minor: u32,
    pub patcher_version_patch: u32,
    pub player_name:           [u8; 0x40],

    // changeable by client
    pub give_death:              u32,
    pub give_item_array:         [u16; 10],
    pub should_print_ap_buffer:  u32,
    pub archipelago_text_buffer: [u8; 0x200],
}

#[link_section = "data"]
#[no_mangle]
pub static mut ARCHIPELAGO_DATA_INTERFACE: ArchipelagoDataInterface = ArchipelagoDataInterface {
    patcher_version_major: 0,
    patcher_version_minor: 0,
    patcher_version_patch: 0,
    player_name:           [0; 64],

    give_death:              0xFFFFFFFF,
    give_item_array:         [0xFFFF; 10],
    should_print_ap_buffer:  0,
    archipelago_text_buffer: [0; 0x200],
};

#[no_mangle]
pub fn give_item() -> u32 {
    unsafe {
        // buffer to safeguard against inconsistencies during processing
        let buffer = ARCHIPELAGO_DATA_INTERFACE.give_item_array;

        for i in 0..buffer.len() {
            let item_id = buffer[i];
            if item_id != 0xFFFF {
                if let Some(details) = get_item_detail(item_id) {
                    let module = lookup_module(&details.module.as_ptr());
                    let vtable = (*module).vtable;
                    let syscall_handler = (*vtable).syscall_handler;

                    let mut params = details.params;

                    // used to avoid dangling pointers and is a safe fallback so game doesn't crash
                    #[allow(unused_assignments)]
                    let mut flag_params = [0u32; 2];

                    // special cases
                    if item_id == Itemflag::PROGRESSIVE_DASH as u16 {
                        params = get_dash_params();
                    }
                    if item_id == Itemflag::PROGRESSIVE_THUNDERBOLT as u16 {
                        params = get_thunderbolt_params();
                    }
                    if item_id == Itemflag::PROGRESSIVE_HEALTH as u16 {
                        params = get_health_params();
                    }
                    if item_id == Itemflag::PROGRESSIVE_IRON_TAIL as u16 {
                        params = get_iron_tail_params();
                    }
                    // flags pointer needs to be retrieved at runtime
                    if details.module == ModuleName::GlobalManager && details.opcode == 0 {
                        if let Some(flag_name) = FlagName::from_u32(*details.params) {
                            flag_params = [flag_name.as_ptr() as u32, 0x1];
                            params = flag_params.as_ptr();
                        }
                    }

                    // item execution
                    syscall_handler(module, details.opcode, params);
                }
                // reset only processed items
                if ARCHIPELAGO_DATA_INTERFACE.give_item_array[i] == item_id {
                    ARCHIPELAGO_DATA_INTERFACE.give_item_array[i] = 0xFFFF;
                }
            }
        }
    }
    1
}

#[no_mangle]
pub fn give_death() -> u32 {
    unsafe {
        // TODO: Improve params usage
        // TODO: check Attraction logic
        if ARCHIPELAGO_DATA_INTERFACE.give_death == 0x1 {
            let global_manager = lookup_global_manager();
            let global_manager_vtable = (*global_manager).vtable;
            let global_manager_syscall_handler = (*global_manager_vtable).syscall_handler;
            let params: [u32; 3] = [
                (*global_manager).zone as u32,
                (*global_manager).area as u32,
                (*global_manager).position as u32,
            ];
            global_manager_syscall_handler(global_manager, 0x78, params.as_ptr());

            let scene_manager = lookup_scene_manager();
            let scene_manager_vtable = (*scene_manager).vtable;
            let scene_manager_syscall_handler = (*scene_manager_vtable).syscall_handler;

            let params: [u32; 2] = [SceneName::ZoneChange.as_ptr() as u32, 0x1];
            scene_manager_syscall_handler(scene_manager, 0x6, params.as_ptr());
            // params just for typing
            // unused for that syscall
            scene_manager_syscall_handler(scene_manager, 0x3, params.as_ptr());
        }
        ARCHIPELAGO_DATA_INTERFACE.give_death = 0xFFFFFFFF
    }
    1
}

#[no_mangle]
pub fn print_archipelago_text() -> u32 {
    let text_cstr = unsafe { ARCHIPELAGO_DATA_INTERFACE.archipelago_text_buffer };
    if text_cstr[0] != 0 {
        let mut top_height = 430f32;
        for char in text_cstr.iter() {
            // We want to move the text box up for each newline so it's bottom-justified
            if *char == b'\n' {
                top_height -= 14f32;
            }
        }
        let text = from_utf8(&text_cstr).unwrap();
        let mut console = Console::with_pos(0f32, top_height);
        console.set_bg_color(0x00000055);
        console.set_font_color(0xFFFFFFFF);
        console.set_font_size(0.35f32);
        let _ = console.write_str(text);
        console.draw(false);
    }

    // Return 1 to tell the game to continue running
    1
}
