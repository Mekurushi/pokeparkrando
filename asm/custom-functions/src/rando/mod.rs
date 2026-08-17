mod items;

use crate::game::global_manager::{
    global_manager_syscall_handler, lookup_global_manager, FlagName, GlobalManagerModule,
};
use crate::game::scene_manager::{lookup_scene_manager, SceneName};
use crate::rando::items::{
    get_dash_params, get_health_params, get_iron_tail_params, get_item_detail,
    get_thunderbolt_params, immediate_object_spawn_data, immediate_object_state_change_data,
    immediate_pokemon_spawn_data, Itemflag,
};

use crate::game::mn_field_info::lookup_mn_field_info;
use crate::println;
use crate::utils::console::Console;
use crate::utils::module::{lookup_module, Module, ModuleName};
use core::ffi::{c_void, CStr};
use core::{fmt::Write, str::from_utf8};

extern "C" {
    fn set_frame_limit(
        param1: *mut [FrameLimitEntry; 2],
        param2: u32,
        param3: u32,
        param4: u32,
    ) -> c_void;
}

#[link_section = "data"]
#[no_mangle]
pub static mut GIVE_ITEM_ARRAY: [u16; 10] = [0xFFFF; 10];

#[link_section = "data"]
#[no_mangle]
pub static mut PLAYER_NAME: [u8; 0x40] = [0xFF; 0x40];

#[link_section = "data"]
#[no_mangle]
static mut ARCHIPELAGO_TEXT_BUFFER: [u8; 0x200] = [0; 0x200];

#[link_section = "data"]
#[no_mangle]
static mut PATCHER_VERSION: [u32; 3] = [0; 3];

#[link_section = "data"]
#[no_mangle]
static mut DEATH_TRIGGER: bool = false;

#[link_section = "data"]
#[no_mangle]
static mut IS_DEATH: bool = false;

#[link_section = "data"]
#[no_mangle]
static mut FPS_ENHANCEMENT: bool = false;

#[link_section = "data"]
static mut FROM_RANDO: bool = false;

#[link_section = "data"]
#[no_mangle]
static mut TRIGGER: bool = false;

#[no_mangle]
pub fn give_item() -> u32 {
    unsafe {
        // buffer to safeguard against inconsistencies during processing
        let buffer = GIVE_ITEM_ARRAY;

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

                    // ensure that wrapper in vtable knows it's custom code
                    FROM_RANDO = true;

                    // item execution
                    syscall_handler(module, details.opcode, params);
                    apply_immediate_overworld_unlocks(item_id);

                    // reset custom code indicator
                    FROM_RANDO = false
                }
                // reset only processed items
                if GIVE_ITEM_ARRAY[i] == item_id {
                    GIVE_ITEM_ARRAY[i] = 0xFFFF;
                }
            }
        }
    }
    1
}

fn apply_immediate_overworld_unlocks(item_id: u16) {
    apply_immediate_pokemon_unlocks(item_id);
    apply_object_state_changes(item_id);
    apply_object_spawn_unlocks(item_id);
}

fn current_field() -> Option<(u8, u8)> {
    unsafe {
        let global_manager = lookup_global_manager();
        // mnFieldInfo only exists while the player is in the overworld.
        if global_manager.is_null() || lookup_mn_field_info().is_null() {
            return None;
        }
        Some(((*global_manager).zone, (*global_manager).area))
    }
}

fn apply_object_state_changes(item_id: u16) {
    let actions = immediate_object_state_change_data(item_id);
    if actions.is_empty() {
        return;
    }
    let Some((zone, area)) = current_field() else {
        println!(
            "immediate object update skipped: field unavailable, item={}",
            item_id
        );
        return;
    };

    unsafe {
        let object_manager = lookup_module(&ModuleName::ObjectManager.as_ptr());
        if object_manager.is_null() || (*object_manager).vtable.is_null() {
            println!(
                "immediate object update skipped: object manager unavailable, item={}",
                item_id
            );
            return;
        }
        let object_syscall = (*(*object_manager).vtable).syscall_handler;

        for action in actions.iter().filter(|a| a.zone == zone && a.area == area) {
            for &object_id in action.object_ids {
                let object = object_syscall(object_manager, 4, [object_id].as_ptr());
                if object == 0 {
                    println!(
                        "immediate object update skipped: object unavailable, item={}, object={}",
                        item_id, object_id
                    );
                    continue;
                }
                println!("object: {}", object);
                let object_accessor =
                    object_syscall(object_manager, 1, [object as u32].as_ptr()) as *mut Module;
                if object_accessor.is_null() || (*object_accessor).vtable.is_null() {
                    println!("immediate object update skipped: object module unavailable, item={}, object={}", item_id, object_id);
                    continue;
                }

                let params = [action.state];
                ((*(*object_accessor).vtable).syscall_handler)(object_accessor, 0, params.as_ptr());
                println!(
                    "immediate object update: item={}, zone={}, area={}, object={}",
                    item_id, zone, area, object_id
                );
            }
        }
    }
}

fn apply_object_spawn_unlocks(item_id: u16) {
    let actions = immediate_object_spawn_data(item_id);
    if actions.is_empty() {
        return;
    }
    let Some((zone, area)) = current_field() else {
        println!(
            "immediate object spawn skipped: field unavailable, item={}",
            item_id
        );
        return;
    };

    unsafe {
        let object_manager = lookup_module(&ModuleName::ObjectManager.as_ptr());
        if object_manager.is_null() || (*object_manager).vtable.is_null() {
            println!(
                "immediate object spawn skipped: object manager unavailable, item={}",
                item_id
            );
            return;
        }
        let object_syscall = (*(*object_manager).vtable).syscall_handler;

        for action in actions.iter().filter(|a| a.zone == zone && a.area == area) {
            for &object_id in action.object_ids {
                if object_syscall(object_manager, 10, [object_id].as_ptr()) != 0 {
                    println!(
                        "immediate object spawn skipped: object already exists, item={}, object={}",
                        item_id, object_id
                    );
                    continue;
                }
                object_syscall(object_manager, 6, [object_id, action.spawn_mode].as_ptr());
                println!(
                    "immediate object spawn: item={}, zone={}, area={}, object={}",
                    item_id, zone, area, object_id
                );
            }
        }
    }
}

fn apply_immediate_pokemon_unlocks(item_id: u16) {
    let spawn_data = immediate_pokemon_spawn_data(item_id);
    if spawn_data.is_empty() {
        return;
    }

    let Some((zone, area)) = current_field() else {
        println!(
            "immediate Pokemon spawn skipped: player is not in the overworld, item={}",
            item_id
        );
        return;
    };

    unsafe {
        let Some(spawn_group) = spawn_data
            .iter()
            .find(|group| zone == group.zone && area == group.area)
        else {
            println!(
                "immediate Pokemon spawn skipped: no spawn data match, item={}, zone={}, area={}",
                item_id, zone, area
            );
            return;
        };

        let dispos_manager = lookup_module(&ModuleName::DisposManager.as_ptr());
        if dispos_manager.is_null() {
            println!(
                "immediate Pokemon spawn skipped: dispos manager unavailable, item={}",
                item_id
            );
            return;
        }

        let object_manager = lookup_module(&ModuleName::ObjectManager.as_ptr());
        if object_manager.is_null() {
            println!(
                "immediate Pokemon spawn skipped: object manager unavailable, item={}",
                item_id
            );
            return;
        }

        let spawn = (*(*dispos_manager).vtable).syscall_handler;
        let find_object = (*(*object_manager).vtable).syscall_handler;

        for &object_id in spawn_group.object_ids {
            let params = [object_id];
            if find_object(object_manager, 10, params.as_ptr()) != 0 {
                println!(
                    "immediate Pokemon spawn skipped: Pokemon object already exists, item={}, object={}",
                    item_id, object_id
                );
                continue;
            }

            println!(
                "immediate Pokemon spawn: item={}, zone={}, area={}, object={}",
                item_id, zone, area, object_id
            );
            spawn(dispos_manager, 0x11, params.as_ptr());
        }
    }
}

#[no_mangle]
pub fn give_death() -> u32 {
    unsafe {
        if DEATH_TRIGGER {
            let attraction = lookup_module(&ModuleName::MnAtInfo.as_ptr());
            let mn_lobby = lookup_module(&ModuleName::MnLobby.as_ptr());

            if !attraction.is_null() {
                let scene_manager = lookup_scene_manager();
                let syscall = (*(*scene_manager).vtable).syscall_handler;
                let params: [u32; 2] = [SceneName::ReturnToPark.as_ptr() as u32, 0x1];
                syscall(scene_manager, 0x6, params.as_ptr());
                syscall(scene_manager, 0x3, core::ptr::null());
            } else if !mn_lobby.is_null() {
                let syscall = (*(*mn_lobby).vtable).syscall_handler;
                let params: [u32; 1] = [0x0];
                syscall(mn_lobby, 0x3, params.as_ptr());
                syscall(mn_lobby, 0x11, core::ptr::null());
            } else {
                let global_manager = lookup_global_manager();
                let syscall = (*(*global_manager).vtable).syscall_handler;
                let params: [u32; 3] = [
                    (*global_manager).zone as u32,
                    (*global_manager).area as u32,
                    (*global_manager).position as u32,
                ];
                syscall(global_manager, 0x78, params.as_ptr());

                let scene_manager = lookup_scene_manager();
                let syscall = (*(*scene_manager).vtable).syscall_handler;
                let params: [u32; 2] = [SceneName::ZoneChange.as_ptr() as u32, 0x1];
                syscall(scene_manager, 0x6, params.as_ptr());
                syscall(scene_manager, 0x3, core::ptr::null());
            }
            DEATH_TRIGGER = false;
        }
    }
    1
}

const FONT_SIZE: f32 = 0.4f32;
#[no_mangle]
pub fn print_archipelago_text() {
    let text_cstr = unsafe { ARCHIPELAGO_TEXT_BUFFER };
    let mut last_char = 0;
    if text_cstr[0] != 0 {
        let mut top_height = 436f32;
        for char in text_cstr.iter() {
            // We want to move the text box up for each newline so it's bottom-justified
            // Ignore if last character was 0x02, as that means it's part of a tag
            // processor control sequence
            if *char == b'\n' && last_char != 0x02 {
                // JP line height 20.4f32 at font size 0.4f32
                // PAL line height 20.4f32 at font size 0.4f32
                // NA line height 20.4f32 at font size 0.4f32
                top_height -= 20.4f32
            }
            last_char = *char;
        }
        let text = from_utf8(&text_cstr).unwrap();
        let mut console = Console::with_pos(0f32, top_height);
        console.set_bg_color(0x00000055);
        console.set_font_color(0xFFFFFFFF);
        console.set_font_size(FONT_SIZE);
        let _ = console.write_str(text);
        console.draw(false);
    }
}

#[no_mangle]
pub fn global_manager_syscall_wrapper(
    global_manager: *mut GlobalManagerModule,
    opcode: u32,
    params: *const u32,
) -> bool {
    if unsafe { FROM_RANDO } {
        return unsafe { global_manager_syscall_handler(global_manager, opcode, params) };
    }
    if opcode == 0x3C {
        // convert set friendship calls from script to set bestfriend
        return unsafe { global_manager_syscall_handler(global_manager, 0x4A, params) };
    }
    if opcode == 0x28 {
        // remove pokemon unlock calls from script
        return true;
    }
    if opcode == 0x0 {
        unsafe {
            let name_ptr = *params as *const u8;
            let flag = *params.add(1);
            let name = CStr::from_ptr(name_ptr as *const i8);
            if name.to_bytes_with_nul() == b"zfPowerComp\0" && flag == 0x0 {
                IS_DEATH = true;
            }
        }
    }
    unsafe { global_manager_syscall_handler(global_manager, opcode, params) }
}
#[repr(C)]
pub struct FrameLimitEntry {
    // 0x70 struct size
    _pad0:          [u8; 0x40],
    unknown_0x40:   u32,
    frame_interval: u32,
    _pad1:          [u8; 0x28],
}

#[no_mangle]
pub fn set_frame_limit_wrapper(
    frame_limit_array_ptr: *mut [FrameLimitEntry; 2],
    index: u32,
    param3: u32,
    frame_limit: u32,
) {
    unsafe {
        let new_frame_limit = match FPS_ENHANCEMENT {
            true => 0x000F7708,
            false => frame_limit,
        };
        set_frame_limit(frame_limit_array_ptr, index, param3, new_frame_limit);
    }
}
