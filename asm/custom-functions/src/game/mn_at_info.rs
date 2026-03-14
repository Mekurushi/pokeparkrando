#[repr(u8)]
pub enum AttractionString {
    AtClear,
}

impl AttractionString {
    pub fn as_ptr(&self) -> *const u8 {
        match self {
            Self::AtClear => ATTRACTION_STRINGS.at_clear.as_ptr(),
        }
    }
}

#[repr(C)]
pub struct AttractionStrings {
    pub at_clear: [u8; 8],
}

#[link_section = ".rodata"]
static ATTRACTION_STRINGS: AttractionStrings = AttractionStrings {
    at_clear: *b"AtClear\0",
};
