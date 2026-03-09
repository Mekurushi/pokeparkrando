use crate::utils::module::{lookup_module, ModuleName};

#[no_mangle]
pub fn lookup_mn_field_info() -> *mut MnFieldInfo {
    unsafe { lookup_module(&ModuleName::MnFieldInfo.as_ptr()) as *mut MnFieldInfo }
}
#[repr(C)]
pub struct MnFieldInfo {
    pub vtable: *const MnFieldInfoVTable,
}

#[repr(C)]
pub struct MnFieldInfoVTable {
    pub ptr_s_ns_delhi_ns_object_object_manager: u32,
    pub empty: u32,
    /// 0x00
    pub fun0: u32,

    /// 0x04
    pub fun1: u32,

    /// 0x08
    pub fun2: u32,

    /// 0x0C
    pub fun3: u32,

    /// 0x10
    pub syscall_handler:
        unsafe extern "C" fn(this: *mut MnFieldInfo, opcode: u32, data: *const u32) -> bool,

    /// 0x14
    pub fun5: u32,

    /// 0x18
    pub fun6: u32,

    /// 0x1c
    pub fun7: u32,

    /// 0x20
    pub fun8: u32,
}
