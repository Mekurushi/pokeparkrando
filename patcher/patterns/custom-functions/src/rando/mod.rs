
use core::{
    fmt::Write,
    str::from_utf8,
};
use crate::{
    utils::console::Console,
};

#[link_section = "data"]
#[no_mangle]
static mut archipelago_text_buffer: [u8; 0x200] = [0; 0x200];
#[no_mangle]
pub fn print_archipelago_text() -> u32 {
    let text_cstr = unsafe { archipelago_text_buffer };
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