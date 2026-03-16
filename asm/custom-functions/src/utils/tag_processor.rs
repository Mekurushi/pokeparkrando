#[repr(C)]
pub struct TagProcessor {
    vtable:             *const TagProcessorVTable,
    stuff0:             [u8; 0x908],
    msg_window_subtype: u8,          // 0x90C
    stuff1:             [u8; 0x5D4], // 0xEF4 - 0x90D
    pub is_shadow_text: bool,        // 0xEE1
    stuff2:             [u8; 0x12],  // 0xEF4 - 0xEE2
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
    pub unknown:    unsafe extern "C" fn(&mut TagProcessor, u32, *mut u32) -> u32,
    pub process:    extern "C" fn(&mut TagProcessor, *const u32, u32, *mut u32) -> u32,
}

extern "C" {
    fn __dt__15dTagProcessor_cFv(processor: *mut TagProcessor, _: i32);

    // no clue why there are 2 function variants
    fn process_tag_original(
        processor: *mut TagProcessor,
        param2: *const u32,
        param3: u32,
        param4: *mut u32,
    ) -> u32;
    fn process_tag_shortened_params_original(
        processor: *mut TagProcessor,
        param2: u32,
        param3: *mut u32,
    ) -> u32;

    // no clue what this function is
    fn process_color(packet: *mut u8);
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
            stuff0:             [0; 0x908],
            stuff1:             [0; 0x5D4],
            stuff2:             [0; 0x12],
        }
    }
}

#[no_mangle]
extern "C" fn process_tag_shortened_params(
    tag_processor: &mut TagProcessor,
    tag_kind: u32,
    tags: *mut u32,
) -> u32 {
    if tag_kind != 0xE {
        let uvar1 = unsafe { process_tag_shortened_params_original(tag_processor, tag_kind, tags) };
        return uvar1;
    }
    let mut tag_length: u8 = 0;
    let mut tag_type: i32 = 0;
    let mut color_index_ptr: u32 = 0;

    unsafe {
        let tag_ptr = *((tags as *const u8).add(4) as *const *const u8);

        parse_tag_header(
            0xE,
            tag_ptr,
            &mut tag_length as *mut u8,
            &mut tag_type as *mut i32,
            &mut color_index_ptr as *mut u32,
        );
    }
    if tag_type == 3 {
        unsafe {
            if tag_processor.is_shadow_text == false {
                color_tag_processing_short(
                    tag_processor,
                    tags,
                    tag_length,
                    color_index_ptr as *const u32,
                );
            }
        }
    }
    unsafe {
        let current_pos = *((tags as *const u8).add(4) as *const u32);
        let advance = (tag_length & 0xFE) as u32;
        *((tags as *mut u8).add(4) as *mut u32) = current_pos + advance;
    }
    return 0;
}

#[no_mangle]
pub extern "C" fn process_tag(
    tag_processor: &mut TagProcessor,
    src: *const u32,
    tag_kind: u32,
    tags: *mut u32,
) -> u32 {
    if tag_kind != 0xE {
        let uvar1 = unsafe { process_tag_original(tag_processor, src, tag_kind, tags) };
        return uvar1;
    }
    let mut tag_length: u8 = 0; // stb at stack+0x8
    let mut tag_type: i32 = 0; // stw at stack+0x10
    let mut color_index_ptr: u32 = 0; // stw at stack+0xc

    unsafe {
        let tag_ptr = *((tags as *const u8).add(4) as *const *const u8);

        parse_tag_header(
            0xE,
            tag_ptr,
            &mut tag_length as *mut u8,
            &mut tag_type as *mut i32,
            &mut color_index_ptr as *mut u32,
        );
    }
    if tag_type == 3 {
        unsafe {
            if tag_processor.is_shadow_text == false {
                color_tag_processing(
                    tag_processor,                 // r3 = param_1
                    src,                           // r4 = param_2
                    tags,                          // r5 = param_4
                    tag_length,                    // r6 = abStack_28[0]
                    color_index_ptr as *const u32, // r7 = uStack_24
                );
            }
        }
    }
    unsafe {
        let current_pos = *((tags as *const u8).add(4) as *const u32);
        let advance = (tag_length & 0xFE) as u32; // & 0xFFFFFFFE = clear lowest bit
        *((tags as *mut u8).add(4) as *mut u32) = current_pos + advance;
    }
    return 0;
}
fn parse_tag_header(
    _param1: u32,
    tags: *const u8,
    tag_length: *mut u8,
    tag_type: *mut i32,
    color_index_ptr: *mut u32,
) {
    unsafe {
        *tag_type = *(tags as *const u32) as i32;
        let length = *(tags.add(4) as *const u16) as u8 + 6;

        *tag_length = length;

        if 6 < *tag_length {
            *color_index_ptr = tags as u32 + 6;
        } else {
            *color_index_ptr = 0;
        }
    }
}

#[no_mangle]
fn color_tag_processing_short(
    tag_processor: &mut TagProcessor,
    param3: *mut u32,
    _tag_size: u8, // never used
    color_index: *const u32,
) {
    let color_idx: u16 = unsafe { *(color_index as *const u16) };
    if color_idx == 0xFFFF {
        unsafe {
            fallback_color(tag_processor, param3, tag_processor.msg_window_subtype);
        }
    } else {
        let mut font_color_1 = unsafe { FONT_COLORS_1[color_idx as usize] };
        let mut font_color_2 = unsafe { FONT_COLORS_2[color_idx as usize] };

        let u_var2 = 0xFF;

        // Mark packet type = 2
        unsafe { *((*param3 as *mut u8).add(0x20) as *mut u32) = 2 };
        unsafe { process_color(*param3 as *mut u8) };
        let packet = unsafe { *param3 as *mut u8 };
        unsafe { *packet.add(0x18) = (font_color_1 >> 0x18) as u8 };
        unsafe { *packet.add(0x19) = (font_color_1 >> 0x10) as u8 };
        unsafe { *packet.add(0x1A) = (font_color_1 >> 0x8) as u8 };

        unsafe { *packet.add(0x1B) = u_var2 };
        unsafe { *packet.add(0x1C) = (font_color_2 >> 0x18) as u8 };
        unsafe { *packet.add(0x1D) = (font_color_2 >> 0x10) as u8 };
        unsafe { *packet.add(0x1E) = (font_color_2 >> 0x8) as u8 };
        unsafe { *packet.add(0x1F) = u_var2 };

        unsafe { process_color(packet) };
    }
}

#[no_mangle]
fn color_tag_processing(
    tag_processor: &mut TagProcessor,
    _param2: *const u32, // never used
    param3: *mut u32,
    _tag_size: u8, // never used
    color_index: *const u32,
) {
    let color_idx: u16 = unsafe { *(color_index as *const u16) };
    let mut u_var2 = 0;
    if color_idx == 0xFFFF {
        unsafe {
            fallback_color(tag_processor, param3, tag_processor.msg_window_subtype);
        }
    } else {
        let mut font_color_1 = unsafe { FONT_COLORS_1[color_idx as usize] };
        let mut font_color_2 = unsafe { FONT_COLORS_2[color_idx as usize] };

        u_var2 = 0xFF;
        if tag_processor.stuff0[0] != 0 {
            u_var2 = tag_processor.stuff0[0xB9];
        }

        unsafe { *((*param3 as *mut u8).add(0x20) as *mut u32) = 2 };
        unsafe { process_color(*param3 as *mut u8) };
        let packet = unsafe { *param3 as *mut u8 };
        unsafe { *packet.add(0x18) = (font_color_1 >> 0x18) as u8 };
        unsafe { *packet.add(0x19) = (font_color_1 >> 0x10) as u8 };
        unsafe { *packet.add(0x1A) = (font_color_1 >> 0x8) as u8 };

        unsafe { *packet.add(0x1B) = u_var2 };
        unsafe { *packet.add(0x1C) = (font_color_2 >> 0x18) as u8 };
        unsafe { *packet.add(0x1D) = (font_color_2 >> 0x10) as u8 };
        unsafe { *packet.add(0x1E) = (font_color_2 >> 0x8) as u8 };
        unsafe { *packet.add(0x1F) = u_var2 };

        unsafe { process_color(packet) };
    }
}

#[no_mangle]
fn fallback_color(tag_processor: &mut TagProcessor, param2: *mut u32, mut param3: u8) {
    let float = 255.0;
    let double = 4503601774854144.0;
    if (tag_processor.stuff2[0] != b'\0') {
        param3 = 1;
    }
    let i_var3 = match param3 {
        2 => 0xB, // fallback white
        _ => 0xB,
    };
    let base = unsafe { FONT_COLORS_2[i_var3] };

    let local_30: u32 = match param3 {
        _ => base,
    };

    let u_var5: u32 = 0xFF;
    unsafe {
        *((*param2 as *mut u8).add(0x20) as *mut u32) = 2;

        process_color((*param2 as *mut u8));
        let packet = *param2 as *mut u8;

        *packet.add(0x18) = (base >> 24) as u8;
        *packet.add(0x19) = (base >> 16) as u8;
        *packet.add(0x1A) = (base >> 8) as u8;

        let raw_a = (base & 0xFF) * u_var5 ^ 0x80000000;
        let concat: u64 = (0x43300000u64 << 32) | raw_a as u64;
        let as_f64 = f64::from_bits(concat);
        *packet.add(0x1B) = ((as_f64 - double) as f32 / float) as u8;

        *packet.add(0x1C) = (local_30 >> 24) as u8;
        *packet.add(0x1D) = (local_30 >> 16) as u8;
        *packet.add(0x1E) = (local_30 >> 8) as u8;

        let raw_b = (local_30 & 0xFF) * u_var5 ^ 0x80000000;
        let concat2: u64 = (0x43300000u64 << 32) | raw_b as u64;
        let as_f64b = f64::from_bits(concat2);
        *packet.add(0x1F) = ((as_f64b - double) as f32 / float) as u8;

        process_color(packet);
    }
}
static mut FONT_COLORS_1: [u32; 49] = [
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
    // rest unused
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
];

static mut FONT_COLORS_2: [u32; 49] = [
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
    // rest unused
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
    0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
];
