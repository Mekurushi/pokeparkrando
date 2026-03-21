use crate::utils::char_writer::{GradationMode, PrintContextWChar};

#[repr(C)]
pub struct TagProcessor {
    vtable:             *const TagProcessorVTable,
    msg_window_subtype: u8,
    pub is_shadow_text: bool,
}
impl TagProcessor {
    pub fn new() -> Self {
        let mut processor = TagProcessor::default();
        processor.vtable = &TagProcessorVTable {
            empty:      0u32,
            empty_2:    0u32,
            destructor: __dt__15dTagProcessor_cFv,
            unknown:    process_tag_shortened_params,
            process:    process_tag,
        };
        processor
    }

    pub fn with_window_subtype(window_subtype: u8) -> Self {
        let mut processor = TagProcessor::new();
        processor.msg_window_subtype = window_subtype;
        processor
    }
}

#[repr(C)]
pub struct TagProcessorVTable {
    pub empty:      u32,
    pub empty_2:    u32,
    pub destructor: unsafe extern "C" fn(*mut TagProcessor, i32),
    pub unknown:    unsafe extern "C" fn(&mut TagProcessor, u32, *mut PrintContextWChar) -> u32,
    pub process: extern "C" fn(&mut TagProcessor, *const u32, u32, *mut PrintContextWChar) -> u32,
}

extern "C" {
    fn __dt__15dTagProcessor_cFv(processor: *mut TagProcessor, _: i32);

    // no clue why there are 2 function variants
    fn process_tag_original(
        processor: *mut TagProcessor,
        param2: *const u32,
        param3: u32,
        param4: *mut PrintContextWChar,
    ) -> u32;
    fn process_tag_shortened_params_original(
        processor: *mut TagProcessor,
        param2: u32,
        param3: *mut PrintContextWChar,
    ) -> u32;
}

impl Drop for TagProcessor {
    fn drop(&mut self) {
        unsafe {
            __dt__15dTagProcessor_cFv(self, -1);
        }
    }
}

impl Default for TagProcessor {
    fn default() -> Self {
        Self {
            vtable:             core::ptr::null(),
            msg_window_subtype: 0,
            is_shadow_text:     false,
        }
    }
}

#[no_mangle]
extern "C" fn process_tag_shortened_params(
    tag_processor: &mut TagProcessor,
    tag_kind: u32,
    print_context: *mut PrintContextWChar,
) -> u32 {
    if tag_kind != 0xE {
        let uvar1 = unsafe {
            process_tag_shortened_params_original(tag_processor, tag_kind, print_context)
        };
        return uvar1;
    }

    let string_ptr = unsafe { (*print_context).str };

    let (tag_type, tag_length, color_index_ptr) = parse_tag_header(string_ptr);

    if tag_type == 3 {
        if tag_processor.is_shadow_text == false {
            color_tag_processing(tag_processor, print_context, color_index_ptr);
        }
    }
    unsafe {
        let advance: usize = (tag_length & 0xFE) as usize;
        (*print_context).str = (*print_context).str.byte_add(advance);
    }
    0
}

#[no_mangle]
pub extern "C" fn process_tag(
    tag_processor: &mut TagProcessor,
    _unk: *const u32,
    tag_kind: u32,
    print_context: *mut PrintContextWChar,
) -> u32 {
    if tag_kind != 0xE {
        let uvar1 = unsafe { process_tag_original(tag_processor, _unk, tag_kind, print_context) };
        return uvar1;
    }

    let string_ptr = unsafe { (*print_context).str };

    let (tag_type, tag_length, color_index_ptr) = parse_tag_header(string_ptr);
    if tag_type == 3 {
        if tag_processor.is_shadow_text == false {
            color_tag_processing(tag_processor, print_context, color_index_ptr);
        }
    }
    unsafe {
        let advance: usize = (tag_length & 0xFE) as usize;
        (*print_context).str = (*print_context).str.byte_add(advance);
    }
    0
}
fn parse_tag_header(string_ptr: *const u16) -> (i32, u8, *const u16) {
    unsafe {
        let tag_type = *(string_ptr as *const u32) as i32;
        let tag_length = *string_ptr.add(2) as u8 + 6;
        let color_index = if tag_length > 6 {
            string_ptr.byte_add(6)
        } else {
            core::ptr::null()
        };

        (tag_type, tag_length, color_index)
    }
}

#[no_mangle]
fn color_tag_processing(
    tag_processor: &mut TagProcessor,
    ctx: *mut PrintContextWChar,
    color_index: *const u16,
) {
    let color_idx: u16 = unsafe { *(color_index) };
    if color_idx == 0xFFFF {
        fallback_color(ctx, tag_processor.msg_window_subtype);
    } else {
        let font_color_1 = unsafe { FONT_COLORS_1[color_idx as usize] };
        let font_color_2 = unsafe { FONT_COLORS_2[color_idx as usize] };

        let writer = unsafe { (*ctx).writer };

        unsafe { (*writer).set_gradation_mode(GradationMode::VERTICAL) };
        unsafe { (*writer).set_font_color(font_color_1, font_color_2) };
    }
}

#[no_mangle]
fn fallback_color(ctx: *mut PrintContextWChar, msg_window_subtype: u8) {
    let color_idx = match msg_window_subtype {
        2 => 0xB, // fallback white
        _ => 0xB,
    };
    let base = unsafe { FONT_COLORS_2[color_idx] };

    let writer = unsafe { (*ctx).writer };
    unsafe { (*writer).set_gradation_mode(GradationMode::VERTICAL) };
    unsafe { (*writer).set_font_color(base, base) };
}
static mut FONT_COLORS_1: [u32; 12] = [
    0x000000FF, // 0x00 - black
    0xEE0000FF, // 0x01 - red
    0xFF7700FF, // 0x02 - orange
    0x6495EDFF, // 0x03 - blue
    0x00FF7FFF, // 0x04 - green
    0xFAFAD2FF, // 0x05 - yellow
    0xAF99EFFF, // 0x06 - plum
    0x00EEEEFF, // 0x07 - cyan
    0xFA8072FF, // 0x08 - salmon
    0xEE00EEFF, // 0x09 - magenta
    0x6D8BE8FF, // 0x0a - slateblue
    0xFFFFFFFF, // 0x0b - white (fallback for window_subtype 2 now)
];

static mut FONT_COLORS_2: [u32; 12] = [
    0x000000FF, // 0x00 - black
    0xEE0000FF, // 0x01 - red
    0xFF7700FF, // 0x02 - orange
    0x6495EDFF, // 0x03 - blue
    0x00FF7FFF, // 0x04 - green
    0xFAFAD2FF, // 0x05 - yellow
    0xAF99EFFF, // 0x06 - plum
    0x00EEEEFF, // 0x07 - cyan
    0xFA8072FF, // 0x08 - salmon
    0xEE00EEFF, // 0x09 - magenta
    0x6D8BE8FF, // 0x0a - slateblue
    0xFFFFFFFF, // 0x0b - white (fallback for window_subtype 2 now)
];
