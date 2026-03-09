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

use crate::rando::{give_death, give_item, print_archipelago_text, ARCHIPELAGO_DATA_INTERFACE};

#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    // println!("{}", info);
    loop {}
}

#[no_mangle]
fn main_routine(arg: u32) -> u32 {
    give_item();
    give_death();
    if unsafe { ARCHIPELAGO_DATA_INTERFACE.should_print_ap_buffer != 0 } {
        print_archipelago_text();
    }
    arg
}
