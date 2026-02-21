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


mod utils;
mod system;
mod rando;

#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    // println!("{}", info);
    loop {}
}