extern "C" {
    pub fn lookup_module(name: &*const u8) -> *mut Module;
}
#[repr(u8)]
#[derive(Copy, Clone, Hash, PartialEq, Eq)]
pub enum ModuleName {
    GlobalManager,
    SceneManager,
    MnFieldInfo,
    MnLobby,
    ObjectManager,
}

impl ModuleName {
    pub fn as_ptr(&self) -> *const u8 {
        match self {
            Self::GlobalManager => MODULE_NAMES.global_manager.as_ptr(),
            Self::SceneManager => MODULE_NAMES.scene_manager.as_ptr(),
            Self::MnFieldInfo => MODULE_NAMES.mn_field_info.as_ptr(),
            Self::MnLobby => MODULE_NAMES.mn_lobby.as_ptr(),
            Self::ObjectManager => MODULE_NAMES.object_manager.as_ptr(),
        }
    }
}

#[repr(C)]
pub struct ModuleNames {
    pub global_manager: [u8; 14],
    pub scene_manager:  [u8; 13],
    pub mn_field_info:  [u8; 12],
    pub mn_lobby:       [u8; 8],
    pub object_manager: [u8; 14],
}

#[link_section = ".rodata"]
static MODULE_NAMES: ModuleNames = ModuleNames {
    global_manager: *b"GlobalManager\0",
    scene_manager:  *b"SceneManager\0",
    mn_field_info:  *b"mnFieldInfo\0",
    mn_lobby:       *b"mnLobby\0",
    object_manager: *b"ObjectManager\0",
};

#[repr(C)]
pub struct Module {
    pub vtable:   *const SyscallVTable,
    _unknown_0x4: u32,
    module_type:  ModuleType,
}

#[repr(C)]
enum ModuleType {
    SceneManager    = 0,
    SoundManager    = 1,
    SequenceManager = 2,
    GlobalManager   = 3,
    EventScript     = 4,
    ObjectManager   = 5,
    DisposManager   = 6,
    EventManager    = 7,
    RenderManager   = 8,
    DebugManager    = 9,
    EffectManager   = 10,
    ThpManager      = 11,
    BokehManager    = 12,
    PowerManager    = 13,
    HbmManager      = 14,
    END             = 15,
}
#[repr(C)]
pub struct SyscallVTable {
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
        unsafe extern "C" fn(this: *mut Module, opcode: u32, data: *const u32) -> bool,

    /// 0x14
    pub fun5: u32,

    /// 0x18
    pub fun6: u32,

    /// 0x1c
    pub fun7: u32,

    /// 0x20
    pub fun8: u32,
}
