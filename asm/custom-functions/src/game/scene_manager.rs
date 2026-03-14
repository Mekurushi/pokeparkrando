use crate::utils::module::{lookup_module, ModuleName};

extern "C" {
    pub fn scene_manager_syscall_handler(
        module: *mut SceneManagerModule,
        opcode: u32,
        data: *mut u32,
    ) -> bool;
}
#[repr(C)]
pub struct SceneManagerModule {
    // incomplete
    pub vtable: *const SceneManagerSyscallVTable,
}

#[repr(C)]
pub struct SceneManagerSyscallVTable {
    pub ptr_string: u32,
    pub empty:      u32,
    /// 0x00
    pub fun0:       u32,

    /// 0x04
    pub fun1: u32,

    /// 0x08
    pub fun2: u32,

    /// 0x0C
    pub fun3: u32,

    /// 0x10
    pub syscall_handler:
        unsafe extern "C" fn(this: *mut SceneManagerModule, opcode: u32, data: *const u32) -> bool,

    /// 0x14
    pub fun5: u32,

    /// 0x18
    pub fun6: u32,

    /// 0x1c
    pub fun7: u32,

    /// 0x20
    pub fun8: u32,
}

#[repr(C)]
pub struct SceneManagerSyscallData {
    pub opcode:     u32,
    pub parameter1: u32,
    pub parameter2: u32,
    pub parameter3: u32,
}
#[no_mangle]
pub fn lookup_scene_manager() -> *mut SceneManagerModule {
    unsafe { lookup_module(&ModuleName::SceneManager.as_ptr()) as *mut SceneManagerModule }
}
#[repr(u8)]
pub enum SceneName {
    ZoneChange,
    Challenge,
    ReturnToPark,
}

impl SceneName {
    pub fn as_ptr(&self) -> *const u8 {
        match self {
            Self::ZoneChange => SCENE_NAMES.zone_change.as_ptr(),
            Self::Challenge => SCENE_NAMES.challenge.as_ptr(),
            Self::ReturnToPark => SCENE_NAMES.return_to_park.as_ptr(),
        }
    }
}

#[repr(C)]
pub struct SceneNames {
    pub zone_change:    [u8; 11],
    pub challenge:      [u8; 10],
    pub return_to_park: [u8; 13],
}

#[link_section = ".rodata"]
static SCENE_NAMES: SceneNames = SceneNames {
    zone_change:    *b"ZoneChange\0",
    challenge:      *b"Challenge\0",
    return_to_park: *b"ReturnToPark\0",
};
