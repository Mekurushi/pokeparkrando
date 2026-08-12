#![no_std]
#![feature(split_array)]
#![feature(allocator_api)]
#![feature(ascii_char)]
#![feature(format_args_nl)]
#![feature(slice_ptr_get)]
#![feature(slice_partition_dedup)]
#![feature(waker_getters)]
#![feature(noop_waker)]
#![allow(dead_code)]
#![deny(clippy::no_mangle_with_rust_abi)]
#![deny(improper_ctypes)]
#![deny(improper_ctypes_definitions)]

mod game;
mod rando;
mod system;
mod utils;

use crate::rando::{give_death, give_item, print_archipelago_text};
use crate::utils::tag_processor::TagProcessor;

#[macro_export]
macro_rules! print {
    ($($arg:tt)*) => {{
        $crate::utils::printf::debug_print(format_args!($($arg)*));
    }};
}

#[macro_export]
macro_rules! println {
    () => {
        $crate::print!("\n")
    };
    ($($arg:tt)*) => {{
        $crate::utils::printf::debug_print(format_args_nl!($($arg)*));
    }};
}
#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    // println!("{}", info);
    loop {}
}
#[no_mangle]
#[link_section = "data"]
pub static mut SHOULD_PRINT_AP_BUFFER: bool = false;

#[no_mangle]
#[link_section = "data"]
pub static mut BUFFER_TAG_PROCESSOR: Option<TagProcessor> = None;
#[no_mangle]
fn main_routine(arg: u32) -> u32 {
    unsafe {
        if BUFFER_TAG_PROCESSOR.is_none() {
            // Create our own tag processor; subtype 2 means text defaults to white
            BUFFER_TAG_PROCESSOR = Some(TagProcessor::with_window_subtype(2));
        }
    }

    give_item();
    give_death();
    if unsafe { SHOULD_PRINT_AP_BUFFER } {
        print_archipelago_text();
    }
    arg
}
