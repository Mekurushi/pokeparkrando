use crate::utils::module::{lookup_module, ModuleName};

extern "C" {
    pub fn global_manager_syscall_handler(
        module: *mut GlobalManagerModule,
        opcode: u32,
        data: *const u32,
    ) -> bool;
}

#[repr(C)]
pub struct GlobalManagerSyscallData {
    pub opcode:     u32,
    pub parameter1: u32,
    pub parameter2: u32,
    pub parameter3: u32,
}
#[no_mangle]
pub fn lookup_global_manager() -> *mut GlobalManagerModule {
    unsafe { lookup_module(&ModuleName::GlobalManager.as_ptr()) as *mut GlobalManagerModule }
}

// ============================================================================
// GlobalManagerModule
// ============================================================================

#[repr(C)]
pub struct GlobalManagerModule {
    // incomplete assumed len 0x5FFF
    /// 0x0000: vtable pointer
    pub vtable: *const GlobalManagerVTable,
    /// 0x0004: hardcoded 0
    _0:         u32,
    /// 0x0008: hardcoded 3
    _3:         u32,

    /// 0x000c–0x000F: unknown
    _unknown_0c: u32,

    /// PTR_PTR_s_nsDelhi_nsGlobal_GlobalFlagSav
    pub flag_save:            GlobalFlagBase,
    pub global_flag_sav_data: [u32; 89], /* unsure if everything of that is the bitfieldArray,
                                          * doesn't
                                          * match with total bits */

    /// 0x0190: PTR_PTR_s_nsDelhi_nsGlobal_GlobalFlagRes
    pub flag_resident: GlobalFlagBase,
    pub unknown: u32,
    pub pointer_flag_save: *mut GlobalFlagBase,
    pub pointer_flag_resident: *mut GlobalFlagBase,
    pub ptr_ptr_global_flag_zone: u32, // unsure
    // sub structure probably here
    pub ptr_unknown: u32, // uknown vtable
    pub gl_flag_name_string: [u8; 11],
    _pad: u8,
    _empty: u32,
    _ptr_unknown2: u32,
    _ptr_unknown3: u32,
    _ptr_unknown4: u32,
    ptr_ptr_s_ns_delhi_ns_global_friend_note_sin: u32,
    _pad_to_zone: [u8; 0x5D14],
    pub zone: u8,
    pub area: u8,
    pub position: u16,
}

// ============================================================================
// Sub-structs
// ============================================================================

#[repr(C)]
pub struct GlobalFlagBase {
    pub vtable:     *const (), // 0x00
    pub data_ptr:   *mut u32,  // 0x04
    pub total_bits: u32,       // 0x08
    _unknown_0c:    u32,       // 0x0C
    pub handle:     u64,       // 0x10 // unsure about that
    initialized:    bool,      // 0x18
    _pad:           [u8; 0x3], // 0x19–0x1B — alignment
}

#[repr(C)]
pub struct GlobalManagerVTable {
    pub ptr_s_ns_delhi_ns_global_global_manager: u32,
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
        unsafe extern "C" fn(this: *mut GlobalManagerModule, opcode: u32, data: *const u32) -> bool,

    /// 0x14
    pub fun5: u32,

    /// 0x18
    pub fun6: u32,

    /// 0x1c
    pub fun7: u32,

    /// 0x20
    pub fun8: u32,
}

extern "C" {
    fn read_bits(global_flag: &GlobalFlagBase, bit_offset: u32, bit_count: u32) -> u32;
    fn write_bits(global_flag: &GlobalFlagBase, bit_offset: u32, bit_count: u32, value: u32);
}

#[repr(u32)]
pub enum FlagName {
    F0101FuwarideTaxiStop = 0,
    F0301FuwarideTaxiStop = 1,
    F0302FuwarideTaxiStop = 2,
    F0401FuwarideTaxiStop = 3,
    F0402FuwarideTaxiStop = 4,
    F0501FuwarideTaxiStop = 5,
    F0601FuwarideTaxiStop = 6,
    F0602FuwarideTaxiStop = 7,
    FMap0301Bridge1Build  = 8,
    FMap0301Bridge3Build  = 9,
    F0402FireWallA        = 10,
    F0502DoorA            = 11,
    FPondFreeze           = 12,
    F0302Lift             = 13,
}

impl FlagName {
    pub const fn as_ptr(&self) -> *const u8 {
        match self {
            Self::F0101FuwarideTaxiStop => FLAG_NAMES.f0101fuwaride_taxi_stop.as_ptr(),
            Self::F0301FuwarideTaxiStop => FLAG_NAMES.f0301fuwaride_taxi_stop.as_ptr(),
            Self::F0302FuwarideTaxiStop => FLAG_NAMES.f0302fuwaride_taxi_stop.as_ptr(),
            Self::F0401FuwarideTaxiStop => FLAG_NAMES.f0401fuwaride_taxi_stop.as_ptr(),
            Self::F0402FuwarideTaxiStop => FLAG_NAMES.f0402fuwaride_taxi_stop.as_ptr(),
            Self::F0501FuwarideTaxiStop => FLAG_NAMES.f0501fuwaride_taxi_stop.as_ptr(),
            Self::F0601FuwarideTaxiStop => FLAG_NAMES.f0601fuwaride_taxi_stop.as_ptr(),
            Self::F0602FuwarideTaxiStop => FLAG_NAMES.f0602fuwaride_taxi_stop.as_ptr(),
            Self::FMap0301Bridge1Build => FLAG_NAMES.fmap0301bridge1build.as_ptr(),
            Self::FMap0301Bridge3Build => FLAG_NAMES.fmap0301bridge3build.as_ptr(),
            Self::F0402FireWallA => FLAG_NAMES.f0402fire_wall_a.as_ptr(),
            Self::F0502DoorA => FLAG_NAMES.f0502door_a.as_ptr(),
            Self::FPondFreeze => FLAG_NAMES.fpond_freeze.as_ptr(),
            Self::F0302Lift => FLAG_NAMES.f0302lift.as_ptr(),
        }
    }
    pub fn from_u32(val: u32) -> Option<Self> {
        match val {
            0 => Some(Self::F0101FuwarideTaxiStop),
            1 => Some(Self::F0301FuwarideTaxiStop),
            2 => Some(Self::F0302FuwarideTaxiStop),
            3 => Some(Self::F0401FuwarideTaxiStop),
            4 => Some(Self::F0402FuwarideTaxiStop),
            5 => Some(Self::F0501FuwarideTaxiStop),
            6 => Some(Self::F0601FuwarideTaxiStop),
            7 => Some(Self::F0602FuwarideTaxiStop),
            8 => Some(Self::FMap0301Bridge1Build),
            9 => Some(Self::FMap0301Bridge3Build),
            10 => Some(Self::F0402FireWallA),
            11 => Some(Self::F0502DoorA),
            12 => Some(Self::FPondFreeze),
            13 => Some(Self::F0302Lift),
            _ => None,
        }
    }
}

#[repr(C)]
pub struct FlagNames {
    pub f0101fuwaride_taxi_stop: [u8; 22],
    pub f0301fuwaride_taxi_stop: [u8; 22],
    pub f0302fuwaride_taxi_stop: [u8; 22],
    pub f0401fuwaride_taxi_stop: [u8; 22],
    pub f0402fuwaride_taxi_stop: [u8; 22],
    pub f0501fuwaride_taxi_stop: [u8; 22],
    pub f0601fuwaride_taxi_stop: [u8; 22],
    pub f0602fuwaride_taxi_stop: [u8; 22],
    pub fmap0301bridge1build:    [u8; 21],
    pub fmap0301bridge3build:    [u8; 21],
    pub f0402fire_wall_a:        [u8; 15],
    pub f0502door_a:             [u8; 11],
    pub fpond_freeze:            [u8; 12],
    pub f0302lift:               [u8; 10],
}

pub const FLAG_NAMES: FlagNames = FlagNames {
    f0101fuwaride_taxi_stop: *b"f0101FuwarideTaxiStop\0",
    f0301fuwaride_taxi_stop: *b"f0301FuwarideTaxiStop\0",
    f0302fuwaride_taxi_stop: *b"f0302FuwarideTaxiStop\0",
    f0401fuwaride_taxi_stop: *b"f0401FuwarideTaxiStop\0",
    f0402fuwaride_taxi_stop: *b"f0402FuwarideTaxiStop\0",
    f0501fuwaride_taxi_stop: *b"f0501FuwarideTaxiStop\0",
    f0601fuwaride_taxi_stop: *b"f0601FuwarideTaxiStop\0",
    f0602fuwaride_taxi_stop: *b"f0602FuwarideTaxiStop\0",
    fmap0301bridge1build:    *b"fMap0301Bridge1Build\0",
    fmap0301bridge3build:    *b"fMap0301Bridge3Build\0",
    f0402fire_wall_a:        *b"f0402FireWallA\0",
    f0502door_a:             *b"f0502DoorA\0",
    fpond_freeze:            *b"fPondFreeze\0",
    f0302lift:               *b"f0302Lift\0",
};

pub mod global_flag_save_flag_table {
    /// Each constant is (bit_offset, bit_count).
    pub const MAP_0301_BRIDGE_1_BUILD: (u32, u32) = (0, 1); // fMap0301Bridge1Build
    pub const MAP_0301_BRIDGE_3_BUILD: (u32, u32) = (1, 1); // fMap0301Bridge3Build
    pub const MAP_0302_LAKE_FREEZE: (u32, u32) = (2, 1); // fMap0302LakeFreeze
    pub const MAP_0402_BRIDGE_OPEN: (u32, u32) = (3, 1); // fMap0402BridgeOpen
    pub const MAP_0502_HIDDEN_ROOM_OPEN: (u32, u32) = (4, 1); // fMap0502HiddenRoomOpen
    pub const MAP_0601_ROT_BRIDGE: (u32, u32) = (5, 1); // fMap0601RotBridge
    pub const MAP_0601_HIDDEN_ROOM_OPEN: (u32, u32) = (6, 1); // fMap0601HiddenRoomOpen
    pub const MAP_0701_PILLAR_UP: (u32, u32) = (7, 1); // fMap0701PillarUp
    pub const CHAPTER: (u32, u32) = (8, 16); // Chapter
    pub const GF0001: (u32, u32) = (24, 1); // GF0001
    pub const GF0002: (u32, u32) = (25, 1); // GF0002
    pub const GF0003: (u32, u32) = (26, 1); // GF0003
    pub const GF0004: (u32, u32) = (27, 3); // GF0004
    pub const GF0005: (u32, u32) = (30, 1); // GF0005
    pub const RET_ATTRACTION: (u32, u32) = (31, 6); // fRetAttraction
    pub const BIPPAS_WOOD_LEVEL: (u32, u32) = (37, 3); // fBippasWoodLevel
    pub const RECYCLE_BOX: (u32, u32) = (40, 4); // fRecycleBox
    pub const KAMAKURA: (u32, u32) = (44, 3); // fKamakura
    pub const SNOW_MAN: (u32, u32) = (47, 1); // fSnowMan
    pub const CHRISTMAS_TREE: (u32, u32) = (48, 3); // fChristmasTree
    pub const ORDILE_STONE: (u32, u32) = (51, 2); // fOrdileStone
    pub const SEA_TALK_GYARADOS: (u32, u32) = (53, 1); // fSeaTalkGyarados
    pub const SEA_TALK_PELIPPER: (u32, u32) = (54, 3); // fSeaTalkPelipper
    pub const SEA_TALK_LAPLAS: (u32, u32) = (57, 1); // fSeaTalkLaplas
    pub const ICE_TALK_POTTAISHI: (u32, u32) = (58, 1); // fIceTalkPottaishi
    pub const ICE_TALK_EMPERTE: (u32, u32) = (59, 1); // fIceTalkEmperte
    pub const F0302_GATE_OPEN: (u32, u32) = (60, 1); // f0302GateOpen
    pub const POND_FREEZE: (u32, u32) = (61, 1); // fPondFreeze
    pub const F0401_RAIL_A: (u32, u32) = (62, 1); // f0401RailA
    pub const F0401_RAIL_B: (u32, u32) = (63, 1); // f0401RailB
    pub const F0401_ONSEN: (u32, u32) = (64, 1); // f0401Onsen
    pub const F0401_TRUCK_A: (u32, u32) = (65, 1); // f0401TruckA
    pub const F0401_TRUCK_B: (u32, u32) = (66, 1); // f0401TruckB
    pub const F0402_SWITCH: (u32, u32) = (67, 1); // f0402Switch
    pub const F0402_BRIDGE: (u32, u32) = (68, 1); // f0402Bridge
    pub const F0402_GATE_OPEN: (u32, u32) = (69, 1); // f0402GateOpen
    pub const LAPLACE_MOVE: (u32, u32) = (70, 1); // fLaplaceMove
    pub const ROCK_TALK_TORIDE_PS: (u32, u32) = (71, 1); // fRockTalkToridePS
    pub const F0601_DOOR_A_OPEN: (u32, u32) = (72, 1); // f0601DoorAOpen
    pub const F0601_DOOR_B_OPEN: (u32, u32) = (73, 1); // f0601DoorBOpen
    pub const F0601_FIRE_WALL_A: (u32, u32) = (74, 1); // f0601FireWallA
    pub const FIRE_KAPOERER_TOP: (u32, u32) = (75, 1); // fFireKapoererTop
    pub const RUINS_TALK_ABSOL: (u32, u32) = (76, 1); // fRuinsTalkAbsol
    pub const RUINS_GATE_KEY: (u32, u32) = (77, 1); // fRuinsGateKey
    pub const F0602_MIRROR: (u32, u32) = (78, 1); // f0602Mirror
    pub const F0602_FLOWER: (u32, u32) = (79, 1); // f0602Flower
    pub const RUINS_TALK_BOHMANDER: (u32, u32) = (80, 1); // fRuinsTalkBohmander
    pub const RUINS_TALK_WATACCO: (u32, u32) = (81, 2); // fRuinsTalkWatacco
    pub const F0602_TALK_SYEIMI: (u32, u32) = (83, 1); // f0602TalkSyeimi
    pub const F0602_TALK_KIREIHANA: (u32, u32) = (84, 3); // f0602TalkKireihana
    pub const F0602_TALK_MANENE: (u32, u32) = (87, 3); // f0602TalkManene
    pub const F0602_TALK_KIRULIA: (u32, u32) = (90, 3); // f0602TalkKirulia
    pub const F0602_TALK_REKKUUZA: (u32, u32) = (93, 2); // f0602TalkRekkuuza
    pub const F0501_TALK_MOZYANBO: (u32, u32) = (95, 3); // f0501TalkMozyanbo
    pub const F0501_TALK_DONKARASU: (u32, u32) = (98, 1); // f0501TalkDonkarasu
    pub const F0502_TALK_YONOIR: (u32, u32) = (99, 2); // f0502TalkYonoir
    pub const F0502_TALK_YAMIRAMI: (u32, u32) = (101, 2); // f0502TalkYamirami
    pub const F0503_TALK_ROTOM: (u32, u32) = (103, 1); // f0503TalkRotom
    pub const F0401_FOUND_RAILS: (u32, u32) = (104, 4); // f0401FoundRails
    pub const F0401_DIALOG_KUCHEAT: (u32, u32) = (108, 4); // f0401DialogKucheat
    pub const F0401_DIALOG_COKODORA: (u32, u32) = (112, 4); // f0401DialogCokodora
    pub const F0401_DIALOG_DIGDA: (u32, u32) = (116, 4); // f0401DialogDigda
    pub const F0401_DIALOG_DUGTRIO: (u32, u32) = (120, 4); // f0401DialogDugtrio
    pub const F0201_TALK_ELEBOO: (u32, u32) = (124, 1); // f0201TalkEleboo
    pub const F0201_TALK_MUMA: (u32, u32) = (125, 2); // f0201TalkMuma
    pub const F0201_TALK_PONYTA: (u32, u32) = (127, 1); // f0201TalkPonyta
    pub const F0201_TALK_BUDEW: (u32, u32) = (128, 1); // f0201TalkBudew
    pub const F0201_TALK_OKORIZARU: (u32, u32) = (129, 1); // f0201TalkOkorizaru
    pub const F0401_KABIGON_AWAKE: (u32, u32) = (130, 2); // f0401KabigonAwake
    pub const F0201_LEVEL_ELEBOO: (u32, u32) = (132, 4); // f0201LevelEleboo
    pub const F0201_LEVEL_PONYTA: (u32, u32) = (136, 4); // f0201LevelPonyta
    pub const F0201_LEVEL_BUDEW: (u32, u32) = (140, 4); // f0201LevelBudew
    pub const F0201_LEVEL_OKORIZARU: (u32, u32) = (144, 4); // f0201LevelOkorizaru
    pub const F0501_FUNSUI: (u32, u32) = (148, 1); // f0501Funsui
    pub const F0501_GATE_A: (u32, u32) = (149, 1); // f0501GateA
    pub const F0501_LOCK: (u32, u32) = (150, 1); // f0501Lock
    pub const F0501_SEKIHI: (u32, u32) = (151, 1); // f0501Sekihi
    pub const F0502_PIANO_WIRE: (u32, u32) = (152, 1); // f0502PianoWire
    pub const F0502_PIANO_HAMMER: (u32, u32) = (153, 1); // f0502PianoHammer
    pub const F0502_DOOR_A: (u32, u32) = (154, 1); // f0502DoorA
    pub const F0502_DOOR_B: (u32, u32) = (155, 1); // f0502DoorB
    pub const F0502_DOOR_CD: (u32, u32) = (156, 1); // f0502DoorCD
    pub const F0502_DOOR_E: (u32, u32) = (157, 1); // f0502DoorE
    pub const F0502_BOOK_SHELF: (u32, u32) = (158, 1); // f0502BookShelf
    pub const F0402_TALKED_DOSIDON: (u32, u32) = (159, 2); // f0402TalkedDosidon
    pub const F0403_TALKED_BASHARMO: (u32, u32) = (161, 1); // f0403TalkedBasharmo
    pub const F0101_ATTRACTION_PLAY: (u32, u32) = (162, 4); // f0101AttractionPlay
    pub const F0101_TALK_FUSHIGIDANE_BEFORE: (u32, u32) = (166, 1); // f0101TalkFushigidaneBefore
    pub const F0101_TALK_FUSHIGIDANE_AFTER: (u32, u32) = (167, 1); // f0101TalkFushigidaneAfter
    pub const F0101_TALK_MANKEY: (u32, u32) = (168, 1); // f0101TalkMankey
    pub const BALLOON_MOVE: (u32, u32) = (169, 1); // fBalloonMove
    pub const TALK_FUWARIDE: (u32, u32) = (170, 1); // fTalkFuwaride
    pub const F0402_DRILL: (u32, u32) = (171, 1); // f0402Drill
    pub const F0302_LIFT: (u32, u32) = (172, 1); // f0302Lift
    pub const ICE_TALK_INOMOO: (u32, u32) = (173, 1); // fIceTalkInomoo
    pub const F0401_CLEAR_TORIDE_PS: (u32, u32) = (174, 1); // f0401ClearToridePS
    pub const F0402_CLEAR_DOSIDON: (u32, u32) = (175, 1); // f0402ClearDosidon
    pub const FUWARIDE_DAMO: (u32, u32) = (176, 1); // fFuwarideDamo
    pub const F0201_TREE_HOUSE: (u32, u32) = (177, 4); // f0201TreeHouse
    pub const F0402_TALKED_GOLONYA: (u32, u32) = (181, 1); // f0402TalkedGolonya
    pub const F0502_CASEI: (u32, u32) = (182, 2); // f0502Casei
    pub const F0302_DELIBIRD_PRESENT: (u32, u32) = (184, 4); // f0302DelibirdPresent
    pub const F0302_DELIBIRD_TALK: (u32, u32) = (188, 1); // f0302DelibirdTalk
    pub const F0302_PRESENT_TAMAZARASHI: (u32, u32) = (189, 2); // f0302PresentTamazarashi
    pub const F0302_PRESENT_MUCHUL: (u32, u32) = (191, 2); // f0302PresentMuchul
    pub const F0302_PRESENT_INOMOO: (u32, u32) = (193, 2); // f0302PresentInomoo
    pub const F0302_PRESENT_LAPLAS: (u32, u32) = (195, 2); // f0302PresentLaplas
    pub const F0502_ITOMARU_WIRE: (u32, u32) = (197, 1); // f0502ItomaruWire
    pub const F0402_IRON_STICK: (u32, u32) = (198, 1); // f0402IronStick
    pub const F0402_IRON_DISK: (u32, u32) = (199, 1); // f0402IronDisk
    pub const F0402_GOLD_INGOT: (u32, u32) = (200, 1); // f0402GoldIngot
    pub const F0402_GOLD_TOP: (u32, u32) = (201, 1); // f0402GoldTop
    pub const FUWARIDE_SERVICE: (u32, u32) = (202, 8); // fFuwarideService
    pub const TALK_FUWARIDE_SERVICE: (u32, u32) = (210, 2); // fTalkFuwarideService
    pub const WANDERING_HIKOZARU: (u32, u32) = (212, 1); // fWanderingHikozaru
    pub const F0301_BIPPA_FLAG: (u32, u32) = (213, 3); // f0301BippaFlag
    pub const ICE_TALK_ONIGOHRI: (u32, u32) = (216, 1); // fIceTalkOnigohri
    pub const ICE_TALK_YUKIMENOKO: (u32, u32) = (217, 1); // fIceTalkYukimenoko
    pub const F0301_TALK_KIBANBA: (u32, u32) = (218, 1); // f0301TalkKibanba
    pub const F0301_TALK_SAMEHADDER: (u32, u32) = (219, 1); // f0301TalkSamehadder
    pub const F0301_TALK_WHALOH: (u32, u32) = (220, 1); // f0301TalkWhaloh
    pub const F0401_DIALOG_GARAGARA: (u32, u32) = (221, 4); // f0401DialogGaragara
    pub const F0402_TALK_HITOKAGE: (u32, u32) = (225, 1); // f0402TalkHitokage
    pub const F0402_TRAP_ASANAN: (u32, u32) = (226, 1); // f0402TrapAsanan
    pub const F0402_TRAP_KAMONEEGI: (u32, u32) = (227, 1); // f0402TrapKamoneegi
    pub const F0402_TALK_BAKUUDA: (u32, u32) = (228, 1); // f0402TalkBakuuda
    pub const F0402_IRON_COUNT: (u32, u32) = (229, 5); // f0402IronCount
    pub const F0301_TRAP_SOHNANO: (u32, u32) = (234, 1); // f0301TrapSohnano
    pub const F0402_DRILL_INIT: (u32, u32) = (235, 1); // f0402DrillInit
    pub const F0302_TALK_GLACIA: (u32, u32) = (236, 1); // f0302TalkGlacia
    pub const F0401_TRUCK_POS: (u32, u32) = (237, 1); // f0401TruckPos
    pub const F0000_DEBUG_MODE: (u32, u32) = (238, 1); // f0000DebugMode
    pub const F0701_TALK_POCHAMA: (u32, u32) = (239, 2); // f0701TalkPochama
    pub const F0701_TALK_MEW: (u32, u32) = (241, 1); // f0701TalkMew
    pub const F0601_TALK_PORYGON_Z: (u32, u32) = (242, 1); // f0601TalkPorygonZ
    pub const RUINS_TALK_HANECCO: (u32, u32) = (243, 1); // fRuinsTalkHanecco
    pub const F0601_TALK_TOGEKISS: (u32, u32) = (244, 1); // f0601TalkTogekiss
    pub const F0601_FIRE_WALL_B: (u32, u32) = (245, 1); // f0601FireWallB
    pub const F0201_POWER_UP_DASH: (u32, u32) = (246, 1); // f0201PowerUpDash
    pub const F0402_FIRE_WALL_A: (u32, u32) = (247, 1); // f0402FireWallA
    pub const F0402_FIRE_WALL_B: (u32, u32) = (248, 1); // f0402FireWallB
    pub const F0301_TALK_ORDILE: (u32, u32) = (249, 1); // f0301TalkOrdile
    pub const F0301_TRAP_SUNNYGO: (u32, u32) = (250, 1); // f0301TrapSunnygo
    pub const F0101_TALK_AT03_AFTER: (u32, u32) = (251, 1); // f0101TalkAT03After
    pub const F0101_EVENT_TE03: (u32, u32) = (252, 1); // f0101EventTE03
    pub const F9901_TALK_CELEBI: (u32, u32) = (253, 1); // f9901TalkCelebi
    pub const F0101_ATHLETIC: (u32, u32) = (254, 1); // f0101Athletic
    pub const F0101_HIDE_AND_SEEK: (u32, u32) = (255, 1); // f0101HideAndSeek
    pub const F0101_TALK_KIMORI: (u32, u32) = (256, 1); // f0101TalkKimori
    pub const F0101_BATTLE: (u32, u32) = (257, 1); // f0101Battle
    pub const F0101_ITEM_BOX: (u32, u32) = (258, 1); // f0101ItemBox
    pub const F0401_TRUCK_MOVE: (u32, u32) = (259, 1); // f0401TruckMove
    pub const F0401_TRUCK_MAP_CHANGE: (u32, u32) = (260, 1); // f0401TruckMapChange
    pub const F0402_FIRE_WALL_SWITCH_A: (u32, u32) = (261, 2); // f0402FireWallSwitchA
    pub const F0402_FIRE_WALL_SWITCH_B: (u32, u32) = (263, 2); // f0402FireWallSwitchB
    pub const F0402_DRILL_SWITCH: (u32, u32) = (265, 2); // f0402Drill_Switch
    pub const F0401_RAIL_WAY: (u32, u32) = (267, 1); // f0401RailWay
    pub const F0201_TALK_PERAP: (u32, u32) = (268, 1); // f0201TalkPerap
    pub const F0402_BRIDGE_SWITCH: (u32, u32) = (269, 2); // f0402BridgeSwitch
    pub const F0402_DRILL_COUNT: (u32, u32) = (271, 4); // f0402Drill_Count
    pub const F0401_TALK_FUKAMARU: (u32, u32) = (275, 1); // f0401TalkFukamaru
    pub const F0301_TRAP_KIBANBA: (u32, u32) = (276, 2); // f0301TrapKibanba
    pub const F0502_BOOK: (u32, u32) = (278, 1); // f0502Book
    pub const F0101_TALK_FUSHIGIDANE: (u32, u32) = (279, 1); // f0101TalkFushigidane
    pub const F0101_FUWARIDE_TAXI_STOP: (u32, u32) = (280, 1); // f0101FuwarideTaxiStop
    pub const F0301_FUWARIDE_TAXI_STOP: (u32, u32) = (281, 1); // f0301FuwarideTaxiStop
    pub const F0302_FUWARIDE_TAXI_STOP: (u32, u32) = (282, 1); // f0302FuwarideTaxiStop
    pub const F0401_FUWARIDE_TAXI_STOP: (u32, u32) = (283, 1); // f0401FuwarideTaxiStop
    pub const F0402_FUWARIDE_TAXI_STOP: (u32, u32) = (284, 1); // f0402FuwarideTaxiStop
    pub const F0501_FUWARIDE_TAXI_STOP: (u32, u32) = (285, 1); // f0501FuwarideTaxiStop
    pub const F0601_FUWARIDE_TAXI_STOP: (u32, u32) = (286, 1); // f0601FuwarideTaxiStop
    pub const F0602_FUWARIDE_TAXI_STOP: (u32, u32) = (287, 1); // f0602FuwarideTaxiStop
    pub const F0101_TALK_ONISUZUME: (u32, u32) = (288, 1); // f0101TalkOnisuzume
    pub const F0101_TALK_GONBE: (u32, u32) = (289, 1); // f0101TalkGonbe
    pub const F0302_TALK_HIMEGUMA: (u32, u32) = (290, 1); // f0302TalkHimeguma
    pub const F9901_WOOD_BOX: (u32, u32) = (291, 1); // f9901WoodBox
    pub const F9901_DASH: (u32, u32) = (292, 1); // f9901Dash
    pub const F0503_TALK_ROTOM_2: (u32, u32) = (293, 1); // f0503TalkRotom2
    pub const F0601_TALK_KAMEX: (u32, u32) = (294, 1); // f0601TalkKamex
    pub const F0601_TALK_ELEKIBLE: (u32, u32) = (295, 1); // f0601TalkElekible
    pub const F0402_TRAP_FIRE_SWITCH: (u32, u32) = (296, 1); // f0402TrapFireSwitch
    pub const F9901_TALK_MEMO: (u32, u32) = (297, 1); // f9901TalkMemo
    pub const F0302_TALK_TREE: (u32, u32) = (298, 1); // f0302TalkTree
    pub const F0701_BATTLE_MEW_2: (u32, u32) = (299, 1); // f0701BattleMew2
    pub const F0701_BATTLE_BOOBURN: (u32, u32) = (300, 1); // f0701BattleBooburn
    pub const F0701_BATTLE_GABURIAS: (u32, u32) = (301, 1); // f0701BattleGaburias
    pub const F0701_BATTLE_BANGIRAS: (u32, u32) = (302, 1); // f0701BattleBangiras
    pub const F0502_WAND_GANGER: (u32, u32) = (303, 1); // f0502WandGanger
    pub const F0401_TALK_ZUBAT: (u32, u32) = (304, 1); // f0401TalkZubat
    pub const F0401_TALK_KAIRIKI: (u32, u32) = (305, 1); // f0401TalkKairiki
    pub const F0101_TALK_KIMORI_BEFORE: (u32, u32) = (306, 1); // f0101TalkKimoriBefore
    pub const F0701_RAINBOW_LEVEL: (u32, u32) = (307, 4); // f0701RainbowLevel
    pub const F0101_BATTLE_COUNTER: (u32, u32) = (311, 1); // f0101BattleCounter
    pub const F0302_BATTLE_COUNTER: (u32, u32) = (312, 1); // f0302BattleCounter
    pub const F0401_BATTLE_COUNTER: (u32, u32) = (313, 1); // f0401BattleCounter
    pub const F0402_BATTLE_COUNTER: (u32, u32) = (314, 1); // f0402BattleCounter
    pub const F0502_BATTLE_COUNTER: (u32, u32) = (315, 1); // f0502BattleCounter
    pub const F0601_BATTLE_COUNTER: (u32, u32) = (316, 1); // f0601BattleCounter
    pub const F0602_BATTLE_COUNTER: (u32, u32) = (317, 1); // f0602BattleCounter
    pub const F0101_BIPPA_FLAG: (u32, u32) = (318, 1); // f0101BippaFlag
}

impl GlobalManagerModule {
    #[inline(always)]
    fn read_save_flag(&self, off: u32, cnt: u32) -> u32 {
        unsafe { read_bits(&self.flag_save, off, cnt) }
    }
    #[inline(always)]
    fn write_save_flag(&mut self, off: u32, cnt: u32, val: u32) {
        unsafe { write_bits(&self.flag_save, off, cnt, val) }
    }

    /// `fMap0301Bridge1Build` — bit[0], 1 bit
    #[inline]
    pub fn map_0301_bridge_1_build(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0301_BRIDGE_1_BUILD.0,
            global_flag_save_flag_table::MAP_0301_BRIDGE_1_BUILD.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0301_bridge_1_build(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0301_BRIDGE_1_BUILD.0,
            global_flag_save_flag_table::MAP_0301_BRIDGE_1_BUILD.1,
            v as u32,
        )
    }
    /// `fMap0301Bridge3Build` — bit[0], 1 bit
    #[inline]
    pub fn map_0301_bridge_3_build(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0301_BRIDGE_3_BUILD.0,
            global_flag_save_flag_table::MAP_0301_BRIDGE_3_BUILD.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0301_bridge_3_build(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0301_BRIDGE_3_BUILD.0,
            global_flag_save_flag_table::MAP_0301_BRIDGE_3_BUILD.1,
            v as u32,
        )
    }
    /// `fMap0302LakeFreeze` — bit[0], 1 bit
    #[inline]
    pub fn map_0302_lake_freeze(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0302_LAKE_FREEZE.0,
            global_flag_save_flag_table::MAP_0302_LAKE_FREEZE.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0302_lake_freeze(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0302_LAKE_FREEZE.0,
            global_flag_save_flag_table::MAP_0302_LAKE_FREEZE.1,
            v as u32,
        )
    }
    /// `fMap0402BridgeOpen` — bit[0], 1 bit
    #[inline]
    pub fn map_0402_bridge_open(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0402_BRIDGE_OPEN.0,
            global_flag_save_flag_table::MAP_0402_BRIDGE_OPEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0402_bridge_open(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0402_BRIDGE_OPEN.0,
            global_flag_save_flag_table::MAP_0402_BRIDGE_OPEN.1,
            v as u32,
        )
    }
    /// `fMap0502HiddenRoomOpen` — bit[0], 1 bit
    #[inline]
    pub fn map_0502_hidden_room_open(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0502_HIDDEN_ROOM_OPEN.0,
            global_flag_save_flag_table::MAP_0502_HIDDEN_ROOM_OPEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0502_hidden_room_open(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0502_HIDDEN_ROOM_OPEN.0,
            global_flag_save_flag_table::MAP_0502_HIDDEN_ROOM_OPEN.1,
            v as u32,
        )
    }
    /// `fMap0601RotBridge` — bit[0], 1 bit
    #[inline]
    pub fn map_0601_rot_bridge(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0601_ROT_BRIDGE.0,
            global_flag_save_flag_table::MAP_0601_ROT_BRIDGE.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0601_rot_bridge(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0601_ROT_BRIDGE.0,
            global_flag_save_flag_table::MAP_0601_ROT_BRIDGE.1,
            v as u32,
        )
    }
    /// `fMap0601HiddenRoomOpen` — bit[0], 1 bit
    #[inline]
    pub fn map_0601_hidden_room_open(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0601_HIDDEN_ROOM_OPEN.0,
            global_flag_save_flag_table::MAP_0601_HIDDEN_ROOM_OPEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0601_hidden_room_open(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0601_HIDDEN_ROOM_OPEN.0,
            global_flag_save_flag_table::MAP_0601_HIDDEN_ROOM_OPEN.1,
            v as u32,
        )
    }
    /// `fMap0701PillarUp` — bit[0], 1 bit
    #[inline]
    pub fn map_0701_pillar_up(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::MAP_0701_PILLAR_UP.0,
            global_flag_save_flag_table::MAP_0701_PILLAR_UP.1,
        ) != 0
    }
    #[inline]
    pub fn set_map_0701_pillar_up(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::MAP_0701_PILLAR_UP.0,
            global_flag_save_flag_table::MAP_0701_PILLAR_UP.1,
            v as u32,
        )
    }
    /// `Chapter` — bit[0], 16 bits
    #[inline]
    pub fn chapter(&self) -> u16 {
        self.read_save_flag(
            global_flag_save_flag_table::CHAPTER.0,
            global_flag_save_flag_table::CHAPTER.1,
        ) as u16
    }
    #[inline]
    pub fn set_chapter(&mut self, v: u16) {
        self.write_save_flag(
            global_flag_save_flag_table::CHAPTER.0,
            global_flag_save_flag_table::CHAPTER.1,
            v as u32,
        )
    }
    /// `GF0001` — bit[0], 1 bit
    #[inline]
    pub fn gf0001(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::GF0001.0,
            global_flag_save_flag_table::GF0001.1,
        ) != 0
    }
    #[inline]
    pub fn set_gf0001(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::GF0001.0,
            global_flag_save_flag_table::GF0001.1,
            v as u32,
        )
    }
    /// `GF0002` — bit[0], 1 bit
    #[inline]
    pub fn gf0002(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::GF0002.0,
            global_flag_save_flag_table::GF0002.1,
        ) != 0
    }
    #[inline]
    pub fn set_gf0002(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::GF0002.0,
            global_flag_save_flag_table::GF0002.1,
            v as u32,
        )
    }
    /// `GF0003` — bit[0], 1 bit
    #[inline]
    pub fn gf0003(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::GF0003.0,
            global_flag_save_flag_table::GF0003.1,
        ) != 0
    }
    #[inline]
    pub fn set_gf0003(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::GF0003.0,
            global_flag_save_flag_table::GF0003.1,
            v as u32,
        )
    }
    /// `GF0004` — bit[0], 3 bits
    #[inline]
    pub fn gf0004(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::GF0004.0,
            global_flag_save_flag_table::GF0004.1,
        ) as u8
    }
    #[inline]
    pub fn set_gf0004(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::GF0004.0,
            global_flag_save_flag_table::GF0004.1,
            v as u32,
        )
    }
    /// `GF0005` — bit[0], 1 bit
    #[inline]
    pub fn gf0005(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::GF0005.0,
            global_flag_save_flag_table::GF0005.1,
        ) != 0
    }
    #[inline]
    pub fn set_gf0005(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::GF0005.0,
            global_flag_save_flag_table::GF0005.1,
            v as u32,
        )
    }
    /// `fRetAttraction` — bit[0], 6 bits
    #[inline]
    pub fn ret_attraction(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::RET_ATTRACTION.0,
            global_flag_save_flag_table::RET_ATTRACTION.1,
        ) as u8
    }
    #[inline]
    pub fn set_ret_attraction(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::RET_ATTRACTION.0,
            global_flag_save_flag_table::RET_ATTRACTION.1,
            v as u32,
        )
    }
    /// `fBippasWoodLevel` — bit[0], 3 bits
    #[inline]
    pub fn bippas_wood_level(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::BIPPAS_WOOD_LEVEL.0,
            global_flag_save_flag_table::BIPPAS_WOOD_LEVEL.1,
        ) as u8
    }
    #[inline]
    pub fn set_bippas_wood_level(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::BIPPAS_WOOD_LEVEL.0,
            global_flag_save_flag_table::BIPPAS_WOOD_LEVEL.1,
            v as u32,
        )
    }
    /// `fRecycleBox` — bit[0], 4 bits
    #[inline]
    pub fn recycle_box(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::RECYCLE_BOX.0,
            global_flag_save_flag_table::RECYCLE_BOX.1,
        ) as u8
    }
    #[inline]
    pub fn set_recycle_box(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::RECYCLE_BOX.0,
            global_flag_save_flag_table::RECYCLE_BOX.1,
            v as u32,
        )
    }
    /// `fKamakura` — bit[0], 3 bits
    #[inline]
    pub fn kamakura(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::KAMAKURA.0,
            global_flag_save_flag_table::KAMAKURA.1,
        ) as u8
    }
    #[inline]
    pub fn set_kamakura(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::KAMAKURA.0,
            global_flag_save_flag_table::KAMAKURA.1,
            v as u32,
        )
    }
    /// `fSnowMan` — bit[0], 1 bit
    #[inline]
    pub fn snow_man(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::SNOW_MAN.0,
            global_flag_save_flag_table::SNOW_MAN.1,
        ) != 0
    }
    #[inline]
    pub fn set_snow_man(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::SNOW_MAN.0,
            global_flag_save_flag_table::SNOW_MAN.1,
            v as u32,
        )
    }
    /// `fChristmasTree` — bit[0], 3 bits
    #[inline]
    pub fn christmas_tree(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::CHRISTMAS_TREE.0,
            global_flag_save_flag_table::CHRISTMAS_TREE.1,
        ) as u8
    }
    #[inline]
    pub fn set_christmas_tree(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::CHRISTMAS_TREE.0,
            global_flag_save_flag_table::CHRISTMAS_TREE.1,
            v as u32,
        )
    }
    /// `fOrdileStone` — bit[0], 2 bits
    #[inline]
    pub fn ordile_stone(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::ORDILE_STONE.0,
            global_flag_save_flag_table::ORDILE_STONE.1,
        ) as u8
    }
    #[inline]
    pub fn set_ordile_stone(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::ORDILE_STONE.0,
            global_flag_save_flag_table::ORDILE_STONE.1,
            v as u32,
        )
    }
    /// `fSeaTalkGyarados` — bit[0], 1 bit
    #[inline]
    pub fn sea_talk_gyarados(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::SEA_TALK_GYARADOS.0,
            global_flag_save_flag_table::SEA_TALK_GYARADOS.1,
        ) != 0
    }
    #[inline]
    pub fn set_sea_talk_gyarados(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::SEA_TALK_GYARADOS.0,
            global_flag_save_flag_table::SEA_TALK_GYARADOS.1,
            v as u32,
        )
    }
    /// `fSeaTalkPelipper` — bit[0], 3 bits
    #[inline]
    pub fn sea_talk_pelipper(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::SEA_TALK_PELIPPER.0,
            global_flag_save_flag_table::SEA_TALK_PELIPPER.1,
        ) as u8
    }
    #[inline]
    pub fn set_sea_talk_pelipper(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::SEA_TALK_PELIPPER.0,
            global_flag_save_flag_table::SEA_TALK_PELIPPER.1,
            v as u32,
        )
    }
    /// `fSeaTalkLaplas` — bit[0], 1 bit
    #[inline]
    pub fn sea_talk_laplas(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::SEA_TALK_LAPLAS.0,
            global_flag_save_flag_table::SEA_TALK_LAPLAS.1,
        ) != 0
    }
    #[inline]
    pub fn set_sea_talk_laplas(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::SEA_TALK_LAPLAS.0,
            global_flag_save_flag_table::SEA_TALK_LAPLAS.1,
            v as u32,
        )
    }
    /// `fIceTalkPottaishi` — bit[0], 1 bit
    #[inline]
    pub fn ice_talk_pottaishi(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::ICE_TALK_POTTAISHI.0,
            global_flag_save_flag_table::ICE_TALK_POTTAISHI.1,
        ) != 0
    }
    #[inline]
    pub fn set_ice_talk_pottaishi(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::ICE_TALK_POTTAISHI.0,
            global_flag_save_flag_table::ICE_TALK_POTTAISHI.1,
            v as u32,
        )
    }
    /// `fIceTalkEmperte` — bit[0], 1 bit
    #[inline]
    pub fn ice_talk_emperte(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::ICE_TALK_EMPERTE.0,
            global_flag_save_flag_table::ICE_TALK_EMPERTE.1,
        ) != 0
    }
    #[inline]
    pub fn set_ice_talk_emperte(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::ICE_TALK_EMPERTE.0,
            global_flag_save_flag_table::ICE_TALK_EMPERTE.1,
            v as u32,
        )
    }
    /// `f0302GateOpen` — bit[0], 1 bit
    #[inline]
    pub fn f0302_gate_open(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_GATE_OPEN.0,
            global_flag_save_flag_table::F0302_GATE_OPEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_gate_open(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_GATE_OPEN.0,
            global_flag_save_flag_table::F0302_GATE_OPEN.1,
            v as u32,
        )
    }
    /// `fPondFreeze` — bit[0], 1 bit
    #[inline]
    pub fn pond_freeze(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::POND_FREEZE.0,
            global_flag_save_flag_table::POND_FREEZE.1,
        ) != 0
    }
    #[inline]
    pub fn set_pond_freeze(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::POND_FREEZE.0,
            global_flag_save_flag_table::POND_FREEZE.1,
            v as u32,
        )
    }
    /// `f0401RailA` — bit[0], 1 bit
    #[inline]
    pub fn f0401_rail_a(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_RAIL_A.0,
            global_flag_save_flag_table::F0401_RAIL_A.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_rail_a(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_RAIL_A.0,
            global_flag_save_flag_table::F0401_RAIL_A.1,
            v as u32,
        )
    }
    /// `f0401RailB` — bit[0], 1 bit
    #[inline]
    pub fn f0401_rail_b(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_RAIL_B.0,
            global_flag_save_flag_table::F0401_RAIL_B.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_rail_b(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_RAIL_B.0,
            global_flag_save_flag_table::F0401_RAIL_B.1,
            v as u32,
        )
    }
    /// `f0401Onsen` — bit[0], 1 bit
    #[inline]
    pub fn f0401_onsen(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_ONSEN.0,
            global_flag_save_flag_table::F0401_ONSEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_onsen(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_ONSEN.0,
            global_flag_save_flag_table::F0401_ONSEN.1,
            v as u32,
        )
    }
    /// `f0401TruckA` — bit[0], 1 bit
    #[inline]
    pub fn f0401_truck_a(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_A.0,
            global_flag_save_flag_table::F0401_TRUCK_A.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_truck_a(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_A.0,
            global_flag_save_flag_table::F0401_TRUCK_A.1,
            v as u32,
        )
    }
    /// `f0401TruckB` — bit[0], 1 bit
    #[inline]
    pub fn f0401_truck_b(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_B.0,
            global_flag_save_flag_table::F0401_TRUCK_B.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_truck_b(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_B.0,
            global_flag_save_flag_table::F0401_TRUCK_B.1,
            v as u32,
        )
    }
    /// `f0402Switch` — bit[0], 1 bit
    #[inline]
    pub fn f0402_switch(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_SWITCH.0,
            global_flag_save_flag_table::F0402_SWITCH.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_switch(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_SWITCH.0,
            global_flag_save_flag_table::F0402_SWITCH.1,
            v as u32,
        )
    }
    /// `f0402Bridge` — bit[0], 1 bit
    #[inline]
    pub fn f0402_bridge(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_BRIDGE.0,
            global_flag_save_flag_table::F0402_BRIDGE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_bridge(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_BRIDGE.0,
            global_flag_save_flag_table::F0402_BRIDGE.1,
            v as u32,
        )
    }
    /// `f0402GateOpen` — bit[0], 1 bit
    #[inline]
    pub fn f0402_gate_open(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_GATE_OPEN.0,
            global_flag_save_flag_table::F0402_GATE_OPEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_gate_open(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_GATE_OPEN.0,
            global_flag_save_flag_table::F0402_GATE_OPEN.1,
            v as u32,
        )
    }
    /// `fLaplaceMove` — bit[0], 1 bit
    #[inline]
    pub fn laplace_move(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::LAPLACE_MOVE.0,
            global_flag_save_flag_table::LAPLACE_MOVE.1,
        ) != 0
    }
    #[inline]
    pub fn set_laplace_move(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::LAPLACE_MOVE.0,
            global_flag_save_flag_table::LAPLACE_MOVE.1,
            v as u32,
        )
    }
    /// `fRockTalkToridePS` — bit[0], 1 bit
    #[inline]
    pub fn rock_talk_toride_ps(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::ROCK_TALK_TORIDE_PS.0,
            global_flag_save_flag_table::ROCK_TALK_TORIDE_PS.1,
        ) != 0
    }
    #[inline]
    pub fn set_rock_talk_toride_ps(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::ROCK_TALK_TORIDE_PS.0,
            global_flag_save_flag_table::ROCK_TALK_TORIDE_PS.1,
            v as u32,
        )
    }
    /// `f0601DoorAOpen` — bit[0], 1 bit
    #[inline]
    pub fn f0601_door_a_open(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_DOOR_A_OPEN.0,
            global_flag_save_flag_table::F0601_DOOR_A_OPEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_door_a_open(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_DOOR_A_OPEN.0,
            global_flag_save_flag_table::F0601_DOOR_A_OPEN.1,
            v as u32,
        )
    }
    /// `f0601DoorBOpen` — bit[0], 1 bit
    #[inline]
    pub fn f0601_door_b_open(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_DOOR_B_OPEN.0,
            global_flag_save_flag_table::F0601_DOOR_B_OPEN.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_door_b_open(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_DOOR_B_OPEN.0,
            global_flag_save_flag_table::F0601_DOOR_B_OPEN.1,
            v as u32,
        )
    }
    /// `f0601FireWallA` — bit[0], 1 bit
    #[inline]
    pub fn f0601_fire_wall_a(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_FIRE_WALL_A.0,
            global_flag_save_flag_table::F0601_FIRE_WALL_A.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_fire_wall_a(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_FIRE_WALL_A.0,
            global_flag_save_flag_table::F0601_FIRE_WALL_A.1,
            v as u32,
        )
    }
    /// `fFireKapoererTop` — bit[0], 1 bit
    #[inline]
    pub fn fire_kapoerer_top(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::FIRE_KAPOERER_TOP.0,
            global_flag_save_flag_table::FIRE_KAPOERER_TOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_fire_kapoerer_top(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::FIRE_KAPOERER_TOP.0,
            global_flag_save_flag_table::FIRE_KAPOERER_TOP.1,
            v as u32,
        )
    }
    /// `fRuinsTalkAbsol` — bit[0], 1 bit
    #[inline]
    pub fn ruins_talk_absol(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::RUINS_TALK_ABSOL.0,
            global_flag_save_flag_table::RUINS_TALK_ABSOL.1,
        ) != 0
    }
    #[inline]
    pub fn set_ruins_talk_absol(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::RUINS_TALK_ABSOL.0,
            global_flag_save_flag_table::RUINS_TALK_ABSOL.1,
            v as u32,
        )
    }
    /// `fRuinsGateKey` — bit[0], 1 bit
    #[inline]
    pub fn ruins_gate_key(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::RUINS_GATE_KEY.0,
            global_flag_save_flag_table::RUINS_GATE_KEY.1,
        ) != 0
    }
    #[inline]
    pub fn set_ruins_gate_key(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::RUINS_GATE_KEY.0,
            global_flag_save_flag_table::RUINS_GATE_KEY.1,
            v as u32,
        )
    }
    /// `f0602Mirror` — bit[0], 1 bit
    #[inline]
    pub fn f0602_mirror(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_MIRROR.0,
            global_flag_save_flag_table::F0602_MIRROR.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0602_mirror(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_MIRROR.0,
            global_flag_save_flag_table::F0602_MIRROR.1,
            v as u32,
        )
    }
    /// `f0602Flower` — bit[0], 1 bit
    #[inline]
    pub fn f0602_flower(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_FLOWER.0,
            global_flag_save_flag_table::F0602_FLOWER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0602_flower(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_FLOWER.0,
            global_flag_save_flag_table::F0602_FLOWER.1,
            v as u32,
        )
    }
    /// `fRuinsTalkBohmander` — bit[0], 1 bit
    #[inline]
    pub fn ruins_talk_bohmander(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::RUINS_TALK_BOHMANDER.0,
            global_flag_save_flag_table::RUINS_TALK_BOHMANDER.1,
        ) != 0
    }
    #[inline]
    pub fn set_ruins_talk_bohmander(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::RUINS_TALK_BOHMANDER.0,
            global_flag_save_flag_table::RUINS_TALK_BOHMANDER.1,
            v as u32,
        )
    }
    /// `fRuinsTalkWatacco` — bit[0], 2 bits
    #[inline]
    pub fn ruins_talk_watacco(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::RUINS_TALK_WATACCO.0,
            global_flag_save_flag_table::RUINS_TALK_WATACCO.1,
        ) as u8
    }
    #[inline]
    pub fn set_ruins_talk_watacco(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::RUINS_TALK_WATACCO.0,
            global_flag_save_flag_table::RUINS_TALK_WATACCO.1,
            v as u32,
        )
    }
    /// `f0602TalkSyeimi` — bit[0], 1 bit
    #[inline]
    pub fn f0602_talk_syeimi(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_TALK_SYEIMI.0,
            global_flag_save_flag_table::F0602_TALK_SYEIMI.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0602_talk_syeimi(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_TALK_SYEIMI.0,
            global_flag_save_flag_table::F0602_TALK_SYEIMI.1,
            v as u32,
        )
    }
    /// `f0602TalkKireihana` — bit[0], 3 bits
    #[inline]
    pub fn f0602_talk_kireihana(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_TALK_KIREIHANA.0,
            global_flag_save_flag_table::F0602_TALK_KIREIHANA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0602_talk_kireihana(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_TALK_KIREIHANA.0,
            global_flag_save_flag_table::F0602_TALK_KIREIHANA.1,
            v as u32,
        )
    }
    /// `f0602TalkManene` — bit[0], 3 bits
    #[inline]
    pub fn f0602_talk_manene(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_TALK_MANENE.0,
            global_flag_save_flag_table::F0602_TALK_MANENE.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0602_talk_manene(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_TALK_MANENE.0,
            global_flag_save_flag_table::F0602_TALK_MANENE.1,
            v as u32,
        )
    }
    /// `f0602TalkKirulia` — bit[0], 3 bits
    #[inline]
    pub fn f0602_talk_kirulia(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_TALK_KIRULIA.0,
            global_flag_save_flag_table::F0602_TALK_KIRULIA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0602_talk_kirulia(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_TALK_KIRULIA.0,
            global_flag_save_flag_table::F0602_TALK_KIRULIA.1,
            v as u32,
        )
    }
    /// `f0602TalkRekkuuza` — bit[0], 2 bits
    #[inline]
    pub fn f0602_talk_rekkuuza(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_TALK_REKKUUZA.0,
            global_flag_save_flag_table::F0602_TALK_REKKUUZA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0602_talk_rekkuuza(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_TALK_REKKUUZA.0,
            global_flag_save_flag_table::F0602_TALK_REKKUUZA.1,
            v as u32,
        )
    }
    /// `f0501TalkMozyanbo` — bit[0], 3 bits
    #[inline]
    pub fn f0501_talk_mozyanbo(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0501_TALK_MOZYANBO.0,
            global_flag_save_flag_table::F0501_TALK_MOZYANBO.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0501_talk_mozyanbo(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0501_TALK_MOZYANBO.0,
            global_flag_save_flag_table::F0501_TALK_MOZYANBO.1,
            v as u32,
        )
    }
    /// `f0501TalkDonkarasu` — bit[0], 1 bit
    #[inline]
    pub fn f0501_talk_donkarasu(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0501_TALK_DONKARASU.0,
            global_flag_save_flag_table::F0501_TALK_DONKARASU.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0501_talk_donkarasu(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0501_TALK_DONKARASU.0,
            global_flag_save_flag_table::F0501_TALK_DONKARASU.1,
            v as u32,
        )
    }
    /// `f0502TalkYonoir` — bit[0], 2 bits
    #[inline]
    pub fn f0502_talk_yonoir(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_TALK_YONOIR.0,
            global_flag_save_flag_table::F0502_TALK_YONOIR.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0502_talk_yonoir(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_TALK_YONOIR.0,
            global_flag_save_flag_table::F0502_TALK_YONOIR.1,
            v as u32,
        )
    }
    /// `f0502TalkYamirami` — bit[0], 2 bits
    #[inline]
    pub fn f0502_talk_yamirami(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_TALK_YAMIRAMI.0,
            global_flag_save_flag_table::F0502_TALK_YAMIRAMI.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0502_talk_yamirami(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_TALK_YAMIRAMI.0,
            global_flag_save_flag_table::F0502_TALK_YAMIRAMI.1,
            v as u32,
        )
    }
    /// `f0503TalkRotom` — bit[0], 1 bit
    #[inline]
    pub fn f0503_talk_rotom(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0503_TALK_ROTOM.0,
            global_flag_save_flag_table::F0503_TALK_ROTOM.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0503_talk_rotom(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0503_TALK_ROTOM.0,
            global_flag_save_flag_table::F0503_TALK_ROTOM.1,
            v as u32,
        )
    }
    /// `f0401FoundRails` — bit[0], 4 bits
    #[inline]
    pub fn f0401_found_rails(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_FOUND_RAILS.0,
            global_flag_save_flag_table::F0401_FOUND_RAILS.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0401_found_rails(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_FOUND_RAILS.0,
            global_flag_save_flag_table::F0401_FOUND_RAILS.1,
            v as u32,
        )
    }
    /// `f0401DialogKucheat` — bit[0], 4 bits
    #[inline]
    pub fn f0401_dialog_kucheat(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_KUCHEAT.0,
            global_flag_save_flag_table::F0401_DIALOG_KUCHEAT.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0401_dialog_kucheat(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_KUCHEAT.0,
            global_flag_save_flag_table::F0401_DIALOG_KUCHEAT.1,
            v as u32,
        )
    }
    /// `f0401DialogCokodora` — bit[0], 4 bits
    #[inline]
    pub fn f0401_dialog_cokodora(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_COKODORA.0,
            global_flag_save_flag_table::F0401_DIALOG_COKODORA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0401_dialog_cokodora(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_COKODORA.0,
            global_flag_save_flag_table::F0401_DIALOG_COKODORA.1,
            v as u32,
        )
    }
    /// `f0401DialogDigda` — bit[0], 4 bits
    #[inline]
    pub fn f0401_dialog_digda(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_DIGDA.0,
            global_flag_save_flag_table::F0401_DIALOG_DIGDA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0401_dialog_digda(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_DIGDA.0,
            global_flag_save_flag_table::F0401_DIALOG_DIGDA.1,
            v as u32,
        )
    }
    /// `f0401DialogDugtrio` — bit[0], 4 bits
    #[inline]
    pub fn f0401_dialog_dugtrio(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_DUGTRIO.0,
            global_flag_save_flag_table::F0401_DIALOG_DUGTRIO.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0401_dialog_dugtrio(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_DUGTRIO.0,
            global_flag_save_flag_table::F0401_DIALOG_DUGTRIO.1,
            v as u32,
        )
    }
    /// `f0201TalkEleboo` — bit[0], 1 bit
    #[inline]
    pub fn f0201_talk_eleboo(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_TALK_ELEBOO.0,
            global_flag_save_flag_table::F0201_TALK_ELEBOO.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0201_talk_eleboo(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_TALK_ELEBOO.0,
            global_flag_save_flag_table::F0201_TALK_ELEBOO.1,
            v as u32,
        )
    }
    /// `f0201TalkMuma` — bit[0], 2 bits
    #[inline]
    pub fn f0201_talk_muma(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_TALK_MUMA.0,
            global_flag_save_flag_table::F0201_TALK_MUMA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0201_talk_muma(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_TALK_MUMA.0,
            global_flag_save_flag_table::F0201_TALK_MUMA.1,
            v as u32,
        )
    }
    /// `f0201TalkPonyta` — bit[0], 1 bit
    #[inline]
    pub fn f0201_talk_ponyta(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_TALK_PONYTA.0,
            global_flag_save_flag_table::F0201_TALK_PONYTA.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0201_talk_ponyta(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_TALK_PONYTA.0,
            global_flag_save_flag_table::F0201_TALK_PONYTA.1,
            v as u32,
        )
    }
    /// `f0201TalkBudew` — bit[0], 1 bit
    #[inline]
    pub fn f0201_talk_budew(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_TALK_BUDEW.0,
            global_flag_save_flag_table::F0201_TALK_BUDEW.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0201_talk_budew(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_TALK_BUDEW.0,
            global_flag_save_flag_table::F0201_TALK_BUDEW.1,
            v as u32,
        )
    }
    /// `f0201TalkOkorizaru` — bit[0], 1 bit
    #[inline]
    pub fn f0201_talk_okorizaru(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_TALK_OKORIZARU.0,
            global_flag_save_flag_table::F0201_TALK_OKORIZARU.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0201_talk_okorizaru(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_TALK_OKORIZARU.0,
            global_flag_save_flag_table::F0201_TALK_OKORIZARU.1,
            v as u32,
        )
    }
    /// `f0401KabigonAwake` — bit[0], 2 bits
    #[inline]
    pub fn f0401_kabigon_awake(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_KABIGON_AWAKE.0,
            global_flag_save_flag_table::F0401_KABIGON_AWAKE.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0401_kabigon_awake(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_KABIGON_AWAKE.0,
            global_flag_save_flag_table::F0401_KABIGON_AWAKE.1,
            v as u32,
        )
    }
    /// `f0201LevelEleboo` — bit[0], 4 bits
    #[inline]
    pub fn f0201_level_eleboo(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_ELEBOO.0,
            global_flag_save_flag_table::F0201_LEVEL_ELEBOO.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0201_level_eleboo(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_ELEBOO.0,
            global_flag_save_flag_table::F0201_LEVEL_ELEBOO.1,
            v as u32,
        )
    }
    /// `f0201LevelPonyta` — bit[0], 4 bits
    #[inline]
    pub fn f0201_level_ponyta(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_PONYTA.0,
            global_flag_save_flag_table::F0201_LEVEL_PONYTA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0201_level_ponyta(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_PONYTA.0,
            global_flag_save_flag_table::F0201_LEVEL_PONYTA.1,
            v as u32,
        )
    }
    /// `f0201LevelBudew` — bit[0], 4 bits
    #[inline]
    pub fn f0201_level_budew(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_BUDEW.0,
            global_flag_save_flag_table::F0201_LEVEL_BUDEW.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0201_level_budew(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_BUDEW.0,
            global_flag_save_flag_table::F0201_LEVEL_BUDEW.1,
            v as u32,
        )
    }
    /// `f0201LevelOkorizaru` — bit[0], 4 bits
    #[inline]
    pub fn f0201_level_okorizaru(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_OKORIZARU.0,
            global_flag_save_flag_table::F0201_LEVEL_OKORIZARU.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0201_level_okorizaru(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_LEVEL_OKORIZARU.0,
            global_flag_save_flag_table::F0201_LEVEL_OKORIZARU.1,
            v as u32,
        )
    }
    /// `f0501Funsui` — bit[0], 1 bit
    #[inline]
    pub fn f0501_funsui(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0501_FUNSUI.0,
            global_flag_save_flag_table::F0501_FUNSUI.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0501_funsui(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0501_FUNSUI.0,
            global_flag_save_flag_table::F0501_FUNSUI.1,
            v as u32,
        )
    }
    /// `f0501GateA` — bit[0], 1 bit
    #[inline]
    pub fn f0501_gate_a(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0501_GATE_A.0,
            global_flag_save_flag_table::F0501_GATE_A.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0501_gate_a(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0501_GATE_A.0,
            global_flag_save_flag_table::F0501_GATE_A.1,
            v as u32,
        )
    }
    /// `f0501Lock` — bit[0], 1 bit
    #[inline]
    pub fn f0501_lock(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0501_LOCK.0,
            global_flag_save_flag_table::F0501_LOCK.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0501_lock(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0501_LOCK.0,
            global_flag_save_flag_table::F0501_LOCK.1,
            v as u32,
        )
    }
    /// `f0501Sekihi` — bit[0], 1 bit
    #[inline]
    pub fn f0501_sekihi(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0501_SEKIHI.0,
            global_flag_save_flag_table::F0501_SEKIHI.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0501_sekihi(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0501_SEKIHI.0,
            global_flag_save_flag_table::F0501_SEKIHI.1,
            v as u32,
        )
    }
    /// `f0502PianoWire` — bit[0], 1 bit
    #[inline]
    pub fn f0502_piano_wire(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_PIANO_WIRE.0,
            global_flag_save_flag_table::F0502_PIANO_WIRE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_piano_wire(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_PIANO_WIRE.0,
            global_flag_save_flag_table::F0502_PIANO_WIRE.1,
            v as u32,
        )
    }
    /// `f0502PianoHammer` — bit[0], 1 bit
    #[inline]
    pub fn f0502_piano_hammer(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_PIANO_HAMMER.0,
            global_flag_save_flag_table::F0502_PIANO_HAMMER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_piano_hammer(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_PIANO_HAMMER.0,
            global_flag_save_flag_table::F0502_PIANO_HAMMER.1,
            v as u32,
        )
    }
    /// `f0502DoorA` — bit[0], 1 bit
    #[inline]
    pub fn f0502_door_a(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_DOOR_A.0,
            global_flag_save_flag_table::F0502_DOOR_A.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_door_a(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_DOOR_A.0,
            global_flag_save_flag_table::F0502_DOOR_A.1,
            v as u32,
        )
    }
    /// `f0502DoorB` — bit[0], 1 bit
    #[inline]
    pub fn f0502_door_b(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_DOOR_B.0,
            global_flag_save_flag_table::F0502_DOOR_B.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_door_b(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_DOOR_B.0,
            global_flag_save_flag_table::F0502_DOOR_B.1,
            v as u32,
        )
    }
    /// `f0502DoorCD` — bit[0], 1 bit
    #[inline]
    pub fn f0502_door_cd(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_DOOR_CD.0,
            global_flag_save_flag_table::F0502_DOOR_CD.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_door_cd(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_DOOR_CD.0,
            global_flag_save_flag_table::F0502_DOOR_CD.1,
            v as u32,
        )
    }
    /// `f0502DoorE` — bit[0], 1 bit
    #[inline]
    pub fn f0502_door_e(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_DOOR_E.0,
            global_flag_save_flag_table::F0502_DOOR_E.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_door_e(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_DOOR_E.0,
            global_flag_save_flag_table::F0502_DOOR_E.1,
            v as u32,
        )
    }
    /// `f0502BookShelf` — bit[0], 1 bit
    #[inline]
    pub fn f0502_book_shelf(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_BOOK_SHELF.0,
            global_flag_save_flag_table::F0502_BOOK_SHELF.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_book_shelf(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_BOOK_SHELF.0,
            global_flag_save_flag_table::F0502_BOOK_SHELF.1,
            v as u32,
        )
    }
    /// `f0402TalkedDosidon` — bit[0], 2 bits
    #[inline]
    pub fn f0402_talked_dosidon(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_TALKED_DOSIDON.0,
            global_flag_save_flag_table::F0402_TALKED_DOSIDON.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0402_talked_dosidon(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_TALKED_DOSIDON.0,
            global_flag_save_flag_table::F0402_TALKED_DOSIDON.1,
            v as u32,
        )
    }
    /// `f0403TalkedBasharmo` — bit[0], 1 bit
    #[inline]
    pub fn f0403_talked_basharmo(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0403_TALKED_BASHARMO.0,
            global_flag_save_flag_table::F0403_TALKED_BASHARMO.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0403_talked_basharmo(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0403_TALKED_BASHARMO.0,
            global_flag_save_flag_table::F0403_TALKED_BASHARMO.1,
            v as u32,
        )
    }
    /// `f0101AttractionPlay` — bit[0], 4 bits
    #[inline]
    pub fn f0101_attraction_play(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_ATTRACTION_PLAY.0,
            global_flag_save_flag_table::F0101_ATTRACTION_PLAY.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0101_attraction_play(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_ATTRACTION_PLAY.0,
            global_flag_save_flag_table::F0101_ATTRACTION_PLAY.1,
            v as u32,
        )
    }
    /// `f0101TalkFushigidaneBefore` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_fushigidane_before(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_BEFORE.0,
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_BEFORE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_fushigidane_before(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_BEFORE.0,
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_BEFORE.1,
            v as u32,
        )
    }
    /// `f0101TalkFushigidaneAfter` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_fushigidane_after(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_AFTER.0,
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_AFTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_fushigidane_after(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_AFTER.0,
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE_AFTER.1,
            v as u32,
        )
    }
    /// `f0101TalkMankey` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_mankey(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_MANKEY.0,
            global_flag_save_flag_table::F0101_TALK_MANKEY.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_mankey(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_MANKEY.0,
            global_flag_save_flag_table::F0101_TALK_MANKEY.1,
            v as u32,
        )
    }
    /// `fBalloonMove` — bit[0], 1 bit
    #[inline]
    pub fn balloon_move(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::BALLOON_MOVE.0,
            global_flag_save_flag_table::BALLOON_MOVE.1,
        ) != 0
    }
    #[inline]
    pub fn set_balloon_move(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::BALLOON_MOVE.0,
            global_flag_save_flag_table::BALLOON_MOVE.1,
            v as u32,
        )
    }
    /// `fTalkFuwaride` — bit[0], 1 bit
    #[inline]
    pub fn talk_fuwaride(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::TALK_FUWARIDE.0,
            global_flag_save_flag_table::TALK_FUWARIDE.1,
        ) != 0
    }
    #[inline]
    pub fn set_talk_fuwaride(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::TALK_FUWARIDE.0,
            global_flag_save_flag_table::TALK_FUWARIDE.1,
            v as u32,
        )
    }
    /// `f0402Drill` — bit[0], 1 bit
    #[inline]
    pub fn f0402_drill(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_DRILL.0,
            global_flag_save_flag_table::F0402_DRILL.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_drill(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_DRILL.0,
            global_flag_save_flag_table::F0402_DRILL.1,
            v as u32,
        )
    }
    /// `f0302Lift` — bit[0], 1 bit
    #[inline]
    pub fn f0302_lift(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_LIFT.0,
            global_flag_save_flag_table::F0302_LIFT.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_lift(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_LIFT.0,
            global_flag_save_flag_table::F0302_LIFT.1,
            v as u32,
        )
    }
    /// `fIceTalkInomoo` — bit[0], 1 bit
    #[inline]
    pub fn ice_talk_inomoo(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::ICE_TALK_INOMOO.0,
            global_flag_save_flag_table::ICE_TALK_INOMOO.1,
        ) != 0
    }
    #[inline]
    pub fn set_ice_talk_inomoo(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::ICE_TALK_INOMOO.0,
            global_flag_save_flag_table::ICE_TALK_INOMOO.1,
            v as u32,
        )
    }
    /// `f0401ClearToridePS` — bit[0], 1 bit
    #[inline]
    pub fn f0401_clear_toride_ps(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_CLEAR_TORIDE_PS.0,
            global_flag_save_flag_table::F0401_CLEAR_TORIDE_PS.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_clear_toride_ps(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_CLEAR_TORIDE_PS.0,
            global_flag_save_flag_table::F0401_CLEAR_TORIDE_PS.1,
            v as u32,
        )
    }
    /// `f0402ClearDosidon` — bit[0], 1 bit
    #[inline]
    pub fn f0402_clear_dosidon(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_CLEAR_DOSIDON.0,
            global_flag_save_flag_table::F0402_CLEAR_DOSIDON.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_clear_dosidon(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_CLEAR_DOSIDON.0,
            global_flag_save_flag_table::F0402_CLEAR_DOSIDON.1,
            v as u32,
        )
    }
    /// `fFuwarideDamo` — bit[0], 1 bit
    #[inline]
    pub fn fuwaride_damo(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::FUWARIDE_DAMO.0,
            global_flag_save_flag_table::FUWARIDE_DAMO.1,
        ) != 0
    }
    #[inline]
    pub fn set_fuwaride_damo(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::FUWARIDE_DAMO.0,
            global_flag_save_flag_table::FUWARIDE_DAMO.1,
            v as u32,
        )
    }
    /// `f0201TreeHouse` — bit[0], 4 bits
    #[inline]
    pub fn f0201_tree_house(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_TREE_HOUSE.0,
            global_flag_save_flag_table::F0201_TREE_HOUSE.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0201_tree_house(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_TREE_HOUSE.0,
            global_flag_save_flag_table::F0201_TREE_HOUSE.1,
            v as u32,
        )
    }
    /// `f0402TalkedGolonya` — bit[0], 1 bit
    #[inline]
    pub fn f0402_talked_golonya(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_TALKED_GOLONYA.0,
            global_flag_save_flag_table::F0402_TALKED_GOLONYA.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_talked_golonya(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_TALKED_GOLONYA.0,
            global_flag_save_flag_table::F0402_TALKED_GOLONYA.1,
            v as u32,
        )
    }
    /// `f0502Casei` — bit[0], 2 bits
    #[inline]
    pub fn f0502_casei(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_CASEI.0,
            global_flag_save_flag_table::F0502_CASEI.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0502_casei(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_CASEI.0,
            global_flag_save_flag_table::F0502_CASEI.1,
            v as u32,
        )
    }
    /// `f0302DelibirdPresent` — bit[0], 4 bits
    #[inline]
    pub fn f0302_delibird_present(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_DELIBIRD_PRESENT.0,
            global_flag_save_flag_table::F0302_DELIBIRD_PRESENT.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0302_delibird_present(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_DELIBIRD_PRESENT.0,
            global_flag_save_flag_table::F0302_DELIBIRD_PRESENT.1,
            v as u32,
        )
    }
    /// `f0302DelibirdTalk` — bit[0], 1 bit
    #[inline]
    pub fn f0302_delibird_talk(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_DELIBIRD_TALK.0,
            global_flag_save_flag_table::F0302_DELIBIRD_TALK.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_delibird_talk(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_DELIBIRD_TALK.0,
            global_flag_save_flag_table::F0302_DELIBIRD_TALK.1,
            v as u32,
        )
    }
    /// `f0302PresentTamazarashi` — bit[0], 2 bits
    #[inline]
    pub fn f0302_present_tamazarashi(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_TAMAZARASHI.0,
            global_flag_save_flag_table::F0302_PRESENT_TAMAZARASHI.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0302_present_tamazarashi(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_TAMAZARASHI.0,
            global_flag_save_flag_table::F0302_PRESENT_TAMAZARASHI.1,
            v as u32,
        )
    }
    /// `f0302PresentMuchul` — bit[0], 2 bits
    #[inline]
    pub fn f0302_present_muchul(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_MUCHUL.0,
            global_flag_save_flag_table::F0302_PRESENT_MUCHUL.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0302_present_muchul(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_MUCHUL.0,
            global_flag_save_flag_table::F0302_PRESENT_MUCHUL.1,
            v as u32,
        )
    }
    /// `f0302PresentInomoo` — bit[0], 2 bits
    #[inline]
    pub fn f0302_present_inomoo(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_INOMOO.0,
            global_flag_save_flag_table::F0302_PRESENT_INOMOO.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0302_present_inomoo(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_INOMOO.0,
            global_flag_save_flag_table::F0302_PRESENT_INOMOO.1,
            v as u32,
        )
    }
    /// `f0302PresentLaplas` — bit[0], 2 bits
    #[inline]
    pub fn f0302_present_laplas(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_LAPLAS.0,
            global_flag_save_flag_table::F0302_PRESENT_LAPLAS.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0302_present_laplas(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_PRESENT_LAPLAS.0,
            global_flag_save_flag_table::F0302_PRESENT_LAPLAS.1,
            v as u32,
        )
    }
    /// `f0502ItomaruWire` — bit[0], 1 bit
    #[inline]
    pub fn f0502_itomaru_wire(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_ITOMARU_WIRE.0,
            global_flag_save_flag_table::F0502_ITOMARU_WIRE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_itomaru_wire(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_ITOMARU_WIRE.0,
            global_flag_save_flag_table::F0502_ITOMARU_WIRE.1,
            v as u32,
        )
    }
    /// `f0402IronStick` — bit[0], 1 bit
    #[inline]
    pub fn f0402_iron_stick(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_IRON_STICK.0,
            global_flag_save_flag_table::F0402_IRON_STICK.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_iron_stick(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_IRON_STICK.0,
            global_flag_save_flag_table::F0402_IRON_STICK.1,
            v as u32,
        )
    }
    /// `f0402IronDisk` — bit[0], 1 bit
    #[inline]
    pub fn f0402_iron_disk(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_IRON_DISK.0,
            global_flag_save_flag_table::F0402_IRON_DISK.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_iron_disk(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_IRON_DISK.0,
            global_flag_save_flag_table::F0402_IRON_DISK.1,
            v as u32,
        )
    }
    /// `f0402GoldIngot` — bit[0], 1 bit
    #[inline]
    pub fn f0402_gold_ingot(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_GOLD_INGOT.0,
            global_flag_save_flag_table::F0402_GOLD_INGOT.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_gold_ingot(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_GOLD_INGOT.0,
            global_flag_save_flag_table::F0402_GOLD_INGOT.1,
            v as u32,
        )
    }
    /// `f0402GoldTop` — bit[0], 1 bit
    #[inline]
    pub fn f0402_gold_top(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_GOLD_TOP.0,
            global_flag_save_flag_table::F0402_GOLD_TOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_gold_top(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_GOLD_TOP.0,
            global_flag_save_flag_table::F0402_GOLD_TOP.1,
            v as u32,
        )
    }
    /// `fFuwarideService` — bit[0], 8 bits
    #[inline]
    pub fn fuwaride_service(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::FUWARIDE_SERVICE.0,
            global_flag_save_flag_table::FUWARIDE_SERVICE.1,
        ) as u8
    }
    #[inline]
    pub fn set_fuwaride_service(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::FUWARIDE_SERVICE.0,
            global_flag_save_flag_table::FUWARIDE_SERVICE.1,
            v as u32,
        )
    }
    /// `fTalkFuwarideService` — bit[0], 2 bits
    #[inline]
    pub fn talk_fuwaride_service(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::TALK_FUWARIDE_SERVICE.0,
            global_flag_save_flag_table::TALK_FUWARIDE_SERVICE.1,
        ) as u8
    }
    #[inline]
    pub fn set_talk_fuwaride_service(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::TALK_FUWARIDE_SERVICE.0,
            global_flag_save_flag_table::TALK_FUWARIDE_SERVICE.1,
            v as u32,
        )
    }
    /// `fWanderingHikozaru` — bit[0], 1 bit
    #[inline]
    pub fn wandering_hikozaru(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::WANDERING_HIKOZARU.0,
            global_flag_save_flag_table::WANDERING_HIKOZARU.1,
        ) != 0
    }
    #[inline]
    pub fn set_wandering_hikozaru(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::WANDERING_HIKOZARU.0,
            global_flag_save_flag_table::WANDERING_HIKOZARU.1,
            v as u32,
        )
    }
    /// `f0301BippaFlag` — bit[0], 3 bits
    #[inline]
    pub fn f0301_bippa_flag(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_BIPPA_FLAG.0,
            global_flag_save_flag_table::F0301_BIPPA_FLAG.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0301_bippa_flag(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_BIPPA_FLAG.0,
            global_flag_save_flag_table::F0301_BIPPA_FLAG.1,
            v as u32,
        )
    }
    /// `fIceTalkOnigohri` — bit[0], 1 bit
    #[inline]
    pub fn ice_talk_onigohri(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::ICE_TALK_ONIGOHRI.0,
            global_flag_save_flag_table::ICE_TALK_ONIGOHRI.1,
        ) != 0
    }
    #[inline]
    pub fn set_ice_talk_onigohri(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::ICE_TALK_ONIGOHRI.0,
            global_flag_save_flag_table::ICE_TALK_ONIGOHRI.1,
            v as u32,
        )
    }
    /// `fIceTalkYukimenoko` — bit[0], 1 bit
    #[inline]
    pub fn ice_talk_yukimenoko(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::ICE_TALK_YUKIMENOKO.0,
            global_flag_save_flag_table::ICE_TALK_YUKIMENOKO.1,
        ) != 0
    }
    #[inline]
    pub fn set_ice_talk_yukimenoko(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::ICE_TALK_YUKIMENOKO.0,
            global_flag_save_flag_table::ICE_TALK_YUKIMENOKO.1,
            v as u32,
        )
    }
    /// `f0301TalkKibanba` — bit[0], 1 bit
    #[inline]
    pub fn f0301_talk_kibanba(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_TALK_KIBANBA.0,
            global_flag_save_flag_table::F0301_TALK_KIBANBA.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0301_talk_kibanba(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_TALK_KIBANBA.0,
            global_flag_save_flag_table::F0301_TALK_KIBANBA.1,
            v as u32,
        )
    }
    /// `f0301TalkSamehadder` — bit[0], 1 bit
    #[inline]
    pub fn f0301_talk_samehadder(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_TALK_SAMEHADDER.0,
            global_flag_save_flag_table::F0301_TALK_SAMEHADDER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0301_talk_samehadder(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_TALK_SAMEHADDER.0,
            global_flag_save_flag_table::F0301_TALK_SAMEHADDER.1,
            v as u32,
        )
    }
    /// `f0301TalkWhaloh` — bit[0], 1 bit
    #[inline]
    pub fn f0301_talk_whaloh(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_TALK_WHALOH.0,
            global_flag_save_flag_table::F0301_TALK_WHALOH.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0301_talk_whaloh(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_TALK_WHALOH.0,
            global_flag_save_flag_table::F0301_TALK_WHALOH.1,
            v as u32,
        )
    }
    /// `f0401DialogGaragara` — bit[0], 4 bits
    #[inline]
    pub fn f0401_dialog_garagara(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_GARAGARA.0,
            global_flag_save_flag_table::F0401_DIALOG_GARAGARA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0401_dialog_garagara(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_DIALOG_GARAGARA.0,
            global_flag_save_flag_table::F0401_DIALOG_GARAGARA.1,
            v as u32,
        )
    }
    /// `f0402TalkHitokage` — bit[0], 1 bit
    #[inline]
    pub fn f0402_talk_hitokage(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_TALK_HITOKAGE.0,
            global_flag_save_flag_table::F0402_TALK_HITOKAGE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_talk_hitokage(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_TALK_HITOKAGE.0,
            global_flag_save_flag_table::F0402_TALK_HITOKAGE.1,
            v as u32,
        )
    }
    /// `f0402TrapAsanan` — bit[0], 1 bit
    #[inline]
    pub fn f0402_trap_asanan(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_TRAP_ASANAN.0,
            global_flag_save_flag_table::F0402_TRAP_ASANAN.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_trap_asanan(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_TRAP_ASANAN.0,
            global_flag_save_flag_table::F0402_TRAP_ASANAN.1,
            v as u32,
        )
    }
    /// `f0402TrapKamoneegi` — bit[0], 1 bit
    #[inline]
    pub fn f0402_trap_kamoneegi(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_TRAP_KAMONEEGI.0,
            global_flag_save_flag_table::F0402_TRAP_KAMONEEGI.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_trap_kamoneegi(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_TRAP_KAMONEEGI.0,
            global_flag_save_flag_table::F0402_TRAP_KAMONEEGI.1,
            v as u32,
        )
    }
    /// `f0402TalkBakuuda` — bit[0], 1 bit
    #[inline]
    pub fn f0402_talk_bakuuda(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_TALK_BAKUUDA.0,
            global_flag_save_flag_table::F0402_TALK_BAKUUDA.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_talk_bakuuda(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_TALK_BAKUUDA.0,
            global_flag_save_flag_table::F0402_TALK_BAKUUDA.1,
            v as u32,
        )
    }
    /// `f0402IronCount` — bit[0], 5 bits
    #[inline]
    pub fn f0402_iron_count(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_IRON_COUNT.0,
            global_flag_save_flag_table::F0402_IRON_COUNT.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0402_iron_count(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_IRON_COUNT.0,
            global_flag_save_flag_table::F0402_IRON_COUNT.1,
            v as u32,
        )
    }
    /// `f0301TrapSohnano` — bit[0], 1 bit
    #[inline]
    pub fn f0301_trap_sohnano(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_TRAP_SOHNANO.0,
            global_flag_save_flag_table::F0301_TRAP_SOHNANO.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0301_trap_sohnano(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_TRAP_SOHNANO.0,
            global_flag_save_flag_table::F0301_TRAP_SOHNANO.1,
            v as u32,
        )
    }
    /// `f0402DrillInit` — bit[0], 1 bit
    #[inline]
    pub fn f0402_drill_init(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_DRILL_INIT.0,
            global_flag_save_flag_table::F0402_DRILL_INIT.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_drill_init(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_DRILL_INIT.0,
            global_flag_save_flag_table::F0402_DRILL_INIT.1,
            v as u32,
        )
    }
    /// `f0302TalkGlacia` — bit[0], 1 bit
    #[inline]
    pub fn f0302_talk_glacia(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_TALK_GLACIA.0,
            global_flag_save_flag_table::F0302_TALK_GLACIA.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_talk_glacia(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_TALK_GLACIA.0,
            global_flag_save_flag_table::F0302_TALK_GLACIA.1,
            v as u32,
        )
    }
    /// `f0401TruckPos` — bit[0], 1 bit
    #[inline]
    pub fn f0401_truck_pos(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_POS.0,
            global_flag_save_flag_table::F0401_TRUCK_POS.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_truck_pos(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_POS.0,
            global_flag_save_flag_table::F0401_TRUCK_POS.1,
            v as u32,
        )
    }
    /// `f0000DebugMode` — bit[0], 1 bit
    #[inline]
    pub fn f0000_debug_mode(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0000_DEBUG_MODE.0,
            global_flag_save_flag_table::F0000_DEBUG_MODE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0000_debug_mode(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0000_DEBUG_MODE.0,
            global_flag_save_flag_table::F0000_DEBUG_MODE.1,
            v as u32,
        )
    }
    /// `f0701TalkPochama` — bit[0], 2 bits
    #[inline]
    pub fn f0701_talk_pochama(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0701_TALK_POCHAMA.0,
            global_flag_save_flag_table::F0701_TALK_POCHAMA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0701_talk_pochama(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0701_TALK_POCHAMA.0,
            global_flag_save_flag_table::F0701_TALK_POCHAMA.1,
            v as u32,
        )
    }
    /// `f0701TalkMew` — bit[0], 1 bit
    #[inline]
    pub fn f0701_talk_mew(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0701_TALK_MEW.0,
            global_flag_save_flag_table::F0701_TALK_MEW.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0701_talk_mew(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0701_TALK_MEW.0,
            global_flag_save_flag_table::F0701_TALK_MEW.1,
            v as u32,
        )
    }
    /// `f0601TalkPorygonZ` — bit[0], 1 bit
    #[inline]
    pub fn f0601_talk_porygon_z(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_TALK_PORYGON_Z.0,
            global_flag_save_flag_table::F0601_TALK_PORYGON_Z.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_talk_porygon_z(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_TALK_PORYGON_Z.0,
            global_flag_save_flag_table::F0601_TALK_PORYGON_Z.1,
            v as u32,
        )
    }
    /// `fRuinsTalkHanecco` — bit[0], 1 bit
    #[inline]
    pub fn ruins_talk_hanecco(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::RUINS_TALK_HANECCO.0,
            global_flag_save_flag_table::RUINS_TALK_HANECCO.1,
        ) != 0
    }
    #[inline]
    pub fn set_ruins_talk_hanecco(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::RUINS_TALK_HANECCO.0,
            global_flag_save_flag_table::RUINS_TALK_HANECCO.1,
            v as u32,
        )
    }
    /// `f0601TalkTogekiss` — bit[0], 1 bit
    #[inline]
    pub fn f0601_talk_togekiss(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_TALK_TOGEKISS.0,
            global_flag_save_flag_table::F0601_TALK_TOGEKISS.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_talk_togekiss(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_TALK_TOGEKISS.0,
            global_flag_save_flag_table::F0601_TALK_TOGEKISS.1,
            v as u32,
        )
    }
    /// `f0601FireWallB` — bit[0], 1 bit
    #[inline]
    pub fn f0601_fire_wall_b(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_FIRE_WALL_B.0,
            global_flag_save_flag_table::F0601_FIRE_WALL_B.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_fire_wall_b(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_FIRE_WALL_B.0,
            global_flag_save_flag_table::F0601_FIRE_WALL_B.1,
            v as u32,
        )
    }
    /// `f0201PowerUpDash` — bit[0], 1 bit
    #[inline]
    pub fn f0201_power_up_dash(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_POWER_UP_DASH.0,
            global_flag_save_flag_table::F0201_POWER_UP_DASH.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0201_power_up_dash(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_POWER_UP_DASH.0,
            global_flag_save_flag_table::F0201_POWER_UP_DASH.1,
            v as u32,
        )
    }
    /// `f0402FireWallA` — bit[0], 1 bit
    #[inline]
    pub fn f0402_fire_wall_a(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_A.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_A.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_fire_wall_a(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_A.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_A.1,
            v as u32,
        )
    }
    /// `f0402FireWallB` — bit[0], 1 bit
    #[inline]
    pub fn f0402_fire_wall_b(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_B.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_B.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_fire_wall_b(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_B.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_B.1,
            v as u32,
        )
    }
    /// `f0301TalkOrdile` — bit[0], 1 bit
    #[inline]
    pub fn f0301_talk_ordile(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_TALK_ORDILE.0,
            global_flag_save_flag_table::F0301_TALK_ORDILE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0301_talk_ordile(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_TALK_ORDILE.0,
            global_flag_save_flag_table::F0301_TALK_ORDILE.1,
            v as u32,
        )
    }
    /// `f0301TrapSunnygo` — bit[0], 1 bit
    #[inline]
    pub fn f0301_trap_sunnygo(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_TRAP_SUNNYGO.0,
            global_flag_save_flag_table::F0301_TRAP_SUNNYGO.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0301_trap_sunnygo(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_TRAP_SUNNYGO.0,
            global_flag_save_flag_table::F0301_TRAP_SUNNYGO.1,
            v as u32,
        )
    }
    /// `f0101TalkAT03After` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_at03_after(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_AT03_AFTER.0,
            global_flag_save_flag_table::F0101_TALK_AT03_AFTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_at03_after(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_AT03_AFTER.0,
            global_flag_save_flag_table::F0101_TALK_AT03_AFTER.1,
            v as u32,
        )
    }
    /// `f0101EventTE03` — bit[0], 1 bit
    #[inline]
    pub fn f0101_event_te03(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_EVENT_TE03.0,
            global_flag_save_flag_table::F0101_EVENT_TE03.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_event_te03(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_EVENT_TE03.0,
            global_flag_save_flag_table::F0101_EVENT_TE03.1,
            v as u32,
        )
    }
    /// `f9901TalkCelebi` — bit[0], 1 bit
    #[inline]
    pub fn f9901_talk_celebi(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F9901_TALK_CELEBI.0,
            global_flag_save_flag_table::F9901_TALK_CELEBI.1,
        ) != 0
    }
    #[inline]
    pub fn set_f9901_talk_celebi(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F9901_TALK_CELEBI.0,
            global_flag_save_flag_table::F9901_TALK_CELEBI.1,
            v as u32,
        )
    }
    /// `f0101Athletic` — bit[0], 1 bit
    #[inline]
    pub fn f0101_athletic(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_ATHLETIC.0,
            global_flag_save_flag_table::F0101_ATHLETIC.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_athletic(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_ATHLETIC.0,
            global_flag_save_flag_table::F0101_ATHLETIC.1,
            v as u32,
        )
    }
    /// `f0101HideAndSeek` — bit[0], 1 bit
    #[inline]
    pub fn f0101_hide_and_seek(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_HIDE_AND_SEEK.0,
            global_flag_save_flag_table::F0101_HIDE_AND_SEEK.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_hide_and_seek(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_HIDE_AND_SEEK.0,
            global_flag_save_flag_table::F0101_HIDE_AND_SEEK.1,
            v as u32,
        )
    }
    /// `f0101TalkKimori` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_kimori(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_KIMORI.0,
            global_flag_save_flag_table::F0101_TALK_KIMORI.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_kimori(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_KIMORI.0,
            global_flag_save_flag_table::F0101_TALK_KIMORI.1,
            v as u32,
        )
    }
    /// `f0101Battle` — bit[0], 1 bit
    #[inline]
    pub fn f0101_battle(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_BATTLE.0,
            global_flag_save_flag_table::F0101_BATTLE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_battle(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_BATTLE.0,
            global_flag_save_flag_table::F0101_BATTLE.1,
            v as u32,
        )
    }
    /// `f0101ItemBox` — bit[0], 1 bit
    #[inline]
    pub fn f0101_item_box(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_ITEM_BOX.0,
            global_flag_save_flag_table::F0101_ITEM_BOX.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_item_box(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_ITEM_BOX.0,
            global_flag_save_flag_table::F0101_ITEM_BOX.1,
            v as u32,
        )
    }
    /// `f0401TruckMove` — bit[0], 1 bit
    #[inline]
    pub fn f0401_truck_move(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_MOVE.0,
            global_flag_save_flag_table::F0401_TRUCK_MOVE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_truck_move(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_MOVE.0,
            global_flag_save_flag_table::F0401_TRUCK_MOVE.1,
            v as u32,
        )
    }
    /// `f0401TruckMapChange` — bit[0], 1 bit
    #[inline]
    pub fn f0401_truck_map_change(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_MAP_CHANGE.0,
            global_flag_save_flag_table::F0401_TRUCK_MAP_CHANGE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_truck_map_change(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TRUCK_MAP_CHANGE.0,
            global_flag_save_flag_table::F0401_TRUCK_MAP_CHANGE.1,
            v as u32,
        )
    }
    /// `f0402FireWallSwitchA` — bit[0], 2 bits
    #[inline]
    pub fn f0402_fire_wall_switch_a(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_A.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_A.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0402_fire_wall_switch_a(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_A.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_A.1,
            v as u32,
        )
    }
    /// `f0402FireWallSwitchB` — bit[0], 2 bits
    #[inline]
    pub fn f0402_fire_wall_switch_b(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_B.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_B.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0402_fire_wall_switch_b(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_B.0,
            global_flag_save_flag_table::F0402_FIRE_WALL_SWITCH_B.1,
            v as u32,
        )
    }
    /// `f0402Drill_Switch` — bit[0], 2 bits
    #[inline]
    pub fn f0402_drill_switch(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_DRILL_SWITCH.0,
            global_flag_save_flag_table::F0402_DRILL_SWITCH.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0402_drill_switch(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_DRILL_SWITCH.0,
            global_flag_save_flag_table::F0402_DRILL_SWITCH.1,
            v as u32,
        )
    }
    /// `f0401RailWay` — bit[0], 1 bit
    #[inline]
    pub fn f0401_rail_way(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_RAIL_WAY.0,
            global_flag_save_flag_table::F0401_RAIL_WAY.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_rail_way(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_RAIL_WAY.0,
            global_flag_save_flag_table::F0401_RAIL_WAY.1,
            v as u32,
        )
    }
    /// `f0201TalkPerap` — bit[0], 1 bit
    #[inline]
    pub fn f0201_talk_perap(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0201_TALK_PERAP.0,
            global_flag_save_flag_table::F0201_TALK_PERAP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0201_talk_perap(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0201_TALK_PERAP.0,
            global_flag_save_flag_table::F0201_TALK_PERAP.1,
            v as u32,
        )
    }
    /// `f0402BridgeSwitch` — bit[0], 2 bits
    #[inline]
    pub fn f0402_bridge_switch(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_BRIDGE_SWITCH.0,
            global_flag_save_flag_table::F0402_BRIDGE_SWITCH.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0402_bridge_switch(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_BRIDGE_SWITCH.0,
            global_flag_save_flag_table::F0402_BRIDGE_SWITCH.1,
            v as u32,
        )
    }
    /// `f0402Drill_Count` — bit[0], 4 bits
    #[inline]
    pub fn f0402_drill_count(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_DRILL_COUNT.0,
            global_flag_save_flag_table::F0402_DRILL_COUNT.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0402_drill_count(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_DRILL_COUNT.0,
            global_flag_save_flag_table::F0402_DRILL_COUNT.1,
            v as u32,
        )
    }
    /// `f0401TalkFukamaru` — bit[0], 1 bit
    #[inline]
    pub fn f0401_talk_fukamaru(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TALK_FUKAMARU.0,
            global_flag_save_flag_table::F0401_TALK_FUKAMARU.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_talk_fukamaru(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TALK_FUKAMARU.0,
            global_flag_save_flag_table::F0401_TALK_FUKAMARU.1,
            v as u32,
        )
    }
    /// `f0301TrapKibanba` — bit[0], 2 bits
    #[inline]
    pub fn f0301_trap_kibanba(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_TRAP_KIBANBA.0,
            global_flag_save_flag_table::F0301_TRAP_KIBANBA.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0301_trap_kibanba(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_TRAP_KIBANBA.0,
            global_flag_save_flag_table::F0301_TRAP_KIBANBA.1,
            v as u32,
        )
    }
    /// `f0502Book` — bit[0], 1 bit
    #[inline]
    pub fn f0502_book(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_BOOK.0,
            global_flag_save_flag_table::F0502_BOOK.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_book(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_BOOK.0,
            global_flag_save_flag_table::F0502_BOOK.1,
            v as u32,
        )
    }
    /// `f0101TalkFushigidane` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_fushigidane(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE.0,
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_fushigidane(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE.0,
            global_flag_save_flag_table::F0101_TALK_FUSHIGIDANE.1,
            v as u32,
        )
    }
    /// `f0101FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0101_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0101_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0101_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0301FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0301_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0301_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0301_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0301_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0301_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0301_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0302FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0302_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0302_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0302_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0401FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0401_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0401_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0401_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0402FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0402_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0402_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0402_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0501FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0501_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0501_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0501_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0501_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0501_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0501_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0601FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0601_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0601_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0601_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0602FuwarideTaxiStop` — bit[0], 1 bit
    #[inline]
    pub fn f0602_fuwaride_taxi_stop(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0602_FUWARIDE_TAXI_STOP.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0602_fuwaride_taxi_stop(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_FUWARIDE_TAXI_STOP.0,
            global_flag_save_flag_table::F0602_FUWARIDE_TAXI_STOP.1,
            v as u32,
        )
    }
    /// `f0101TalkOnisuzume` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_onisuzume(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_ONISUZUME.0,
            global_flag_save_flag_table::F0101_TALK_ONISUZUME.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_onisuzume(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_ONISUZUME.0,
            global_flag_save_flag_table::F0101_TALK_ONISUZUME.1,
            v as u32,
        )
    }
    /// `f0101TalkGonbe` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_gonbe(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_GONBE.0,
            global_flag_save_flag_table::F0101_TALK_GONBE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_gonbe(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_GONBE.0,
            global_flag_save_flag_table::F0101_TALK_GONBE.1,
            v as u32,
        )
    }
    /// `f0302TalkHimeguma` — bit[0], 1 bit
    #[inline]
    pub fn f0302_talk_himeguma(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_TALK_HIMEGUMA.0,
            global_flag_save_flag_table::F0302_TALK_HIMEGUMA.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_talk_himeguma(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_TALK_HIMEGUMA.0,
            global_flag_save_flag_table::F0302_TALK_HIMEGUMA.1,
            v as u32,
        )
    }
    /// `f9901WoodBox` — bit[0], 1 bit
    #[inline]
    pub fn f9901_wood_box(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F9901_WOOD_BOX.0,
            global_flag_save_flag_table::F9901_WOOD_BOX.1,
        ) != 0
    }
    #[inline]
    pub fn set_f9901_wood_box(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F9901_WOOD_BOX.0,
            global_flag_save_flag_table::F9901_WOOD_BOX.1,
            v as u32,
        )
    }
    /// `f9901Dash` — bit[0], 1 bit
    #[inline]
    pub fn f9901_dash(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F9901_DASH.0,
            global_flag_save_flag_table::F9901_DASH.1,
        ) != 0
    }
    #[inline]
    pub fn set_f9901_dash(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F9901_DASH.0,
            global_flag_save_flag_table::F9901_DASH.1,
            v as u32,
        )
    }
    /// `f0503TalkRotom2` — bit[0], 1 bit
    #[inline]
    pub fn f0503_talk_rotom_2(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0503_TALK_ROTOM_2.0,
            global_flag_save_flag_table::F0503_TALK_ROTOM_2.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0503_talk_rotom_2(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0503_TALK_ROTOM_2.0,
            global_flag_save_flag_table::F0503_TALK_ROTOM_2.1,
            v as u32,
        )
    }
    /// `f0601TalkKamex` — bit[0], 1 bit
    #[inline]
    pub fn f0601_talk_kamex(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_TALK_KAMEX.0,
            global_flag_save_flag_table::F0601_TALK_KAMEX.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_talk_kamex(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_TALK_KAMEX.0,
            global_flag_save_flag_table::F0601_TALK_KAMEX.1,
            v as u32,
        )
    }
    /// `f0601TalkElekible` — bit[0], 1 bit
    #[inline]
    pub fn f0601_talk_elekible(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_TALK_ELEKIBLE.0,
            global_flag_save_flag_table::F0601_TALK_ELEKIBLE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_talk_elekible(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_TALK_ELEKIBLE.0,
            global_flag_save_flag_table::F0601_TALK_ELEKIBLE.1,
            v as u32,
        )
    }
    /// `f0402TrapFireSwitch` — bit[0], 1 bit
    #[inline]
    pub fn f0402_trap_fire_switch(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_TRAP_FIRE_SWITCH.0,
            global_flag_save_flag_table::F0402_TRAP_FIRE_SWITCH.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_trap_fire_switch(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_TRAP_FIRE_SWITCH.0,
            global_flag_save_flag_table::F0402_TRAP_FIRE_SWITCH.1,
            v as u32,
        )
    }
    /// `f9901TalkMemo` — bit[0], 1 bit
    #[inline]
    pub fn f9901_talk_memo(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F9901_TALK_MEMO.0,
            global_flag_save_flag_table::F9901_TALK_MEMO.1,
        ) != 0
    }
    #[inline]
    pub fn set_f9901_talk_memo(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F9901_TALK_MEMO.0,
            global_flag_save_flag_table::F9901_TALK_MEMO.1,
            v as u32,
        )
    }
    /// `f0302TalkTree` — bit[0], 1 bit
    #[inline]
    pub fn f0302_talk_tree(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_TALK_TREE.0,
            global_flag_save_flag_table::F0302_TALK_TREE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_talk_tree(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_TALK_TREE.0,
            global_flag_save_flag_table::F0302_TALK_TREE.1,
            v as u32,
        )
    }
    /// `f0701BattleMew2` — bit[0], 1 bit
    #[inline]
    pub fn f0701_battle_mew_2(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_MEW_2.0,
            global_flag_save_flag_table::F0701_BATTLE_MEW_2.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0701_battle_mew_2(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_MEW_2.0,
            global_flag_save_flag_table::F0701_BATTLE_MEW_2.1,
            v as u32,
        )
    }
    /// `f0701BattleBooburn` — bit[0], 1 bit
    #[inline]
    pub fn f0701_battle_booburn(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_BOOBURN.0,
            global_flag_save_flag_table::F0701_BATTLE_BOOBURN.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0701_battle_booburn(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_BOOBURN.0,
            global_flag_save_flag_table::F0701_BATTLE_BOOBURN.1,
            v as u32,
        )
    }
    /// `f0701BattleGaburias` — bit[0], 1 bit
    #[inline]
    pub fn f0701_battle_gaburias(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_GABURIAS.0,
            global_flag_save_flag_table::F0701_BATTLE_GABURIAS.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0701_battle_gaburias(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_GABURIAS.0,
            global_flag_save_flag_table::F0701_BATTLE_GABURIAS.1,
            v as u32,
        )
    }
    /// `f0701BattleBangiras` — bit[0], 1 bit
    #[inline]
    pub fn f0701_battle_bangiras(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_BANGIRAS.0,
            global_flag_save_flag_table::F0701_BATTLE_BANGIRAS.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0701_battle_bangiras(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0701_BATTLE_BANGIRAS.0,
            global_flag_save_flag_table::F0701_BATTLE_BANGIRAS.1,
            v as u32,
        )
    }
    /// `f0502WandGanger` — bit[0], 1 bit
    #[inline]
    pub fn f0502_wand_ganger(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_WAND_GANGER.0,
            global_flag_save_flag_table::F0502_WAND_GANGER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_wand_ganger(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_WAND_GANGER.0,
            global_flag_save_flag_table::F0502_WAND_GANGER.1,
            v as u32,
        )
    }
    /// `f0401TalkZubat` — bit[0], 1 bit
    #[inline]
    pub fn f0401_talk_zubat(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TALK_ZUBAT.0,
            global_flag_save_flag_table::F0401_TALK_ZUBAT.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_talk_zubat(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TALK_ZUBAT.0,
            global_flag_save_flag_table::F0401_TALK_ZUBAT.1,
            v as u32,
        )
    }
    /// `f0401TalkKairiki` — bit[0], 1 bit
    #[inline]
    pub fn f0401_talk_kairiki(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_TALK_KAIRIKI.0,
            global_flag_save_flag_table::F0401_TALK_KAIRIKI.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_talk_kairiki(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_TALK_KAIRIKI.0,
            global_flag_save_flag_table::F0401_TALK_KAIRIKI.1,
            v as u32,
        )
    }
    /// `f0101TalkKimoriBefore` — bit[0], 1 bit
    #[inline]
    pub fn f0101_talk_kimori_before(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_TALK_KIMORI_BEFORE.0,
            global_flag_save_flag_table::F0101_TALK_KIMORI_BEFORE.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_talk_kimori_before(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_TALK_KIMORI_BEFORE.0,
            global_flag_save_flag_table::F0101_TALK_KIMORI_BEFORE.1,
            v as u32,
        )
    }
    /// `f0701RainbowLevel` — bit[0], 4 bits
    #[inline]
    pub fn f0701_rainbow_level(&self) -> u8 {
        self.read_save_flag(
            global_flag_save_flag_table::F0701_RAINBOW_LEVEL.0,
            global_flag_save_flag_table::F0701_RAINBOW_LEVEL.1,
        ) as u8
    }
    #[inline]
    pub fn set_f0701_rainbow_level(&mut self, v: u8) {
        self.write_save_flag(
            global_flag_save_flag_table::F0701_RAINBOW_LEVEL.0,
            global_flag_save_flag_table::F0701_RAINBOW_LEVEL.1,
            v as u32,
        )
    }
    /// `f0101BattleCounter` — bit[0], 1 bit
    #[inline]
    pub fn f0101_battle_counter(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0101_BATTLE_COUNTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_battle_counter(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0101_BATTLE_COUNTER.1,
            v as u32,
        )
    }
    /// `f0302BattleCounter` — bit[0], 1 bit
    #[inline]
    pub fn f0302_battle_counter(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0302_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0302_BATTLE_COUNTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0302_battle_counter(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0302_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0302_BATTLE_COUNTER.1,
            v as u32,
        )
    }
    /// `f0401BattleCounter` — bit[0], 1 bit
    #[inline]
    pub fn f0401_battle_counter(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0401_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0401_BATTLE_COUNTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0401_battle_counter(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0401_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0401_BATTLE_COUNTER.1,
            v as u32,
        )
    }
    /// `f0402BattleCounter` — bit[0], 1 bit
    #[inline]
    pub fn f0402_battle_counter(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0402_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0402_BATTLE_COUNTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0402_battle_counter(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0402_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0402_BATTLE_COUNTER.1,
            v as u32,
        )
    }
    /// `f0502BattleCounter` — bit[0], 1 bit
    #[inline]
    pub fn f0502_battle_counter(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0502_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0502_BATTLE_COUNTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0502_battle_counter(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0502_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0502_BATTLE_COUNTER.1,
            v as u32,
        )
    }
    /// `f0601BattleCounter` — bit[0], 1 bit
    #[inline]
    pub fn f0601_battle_counter(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0601_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0601_BATTLE_COUNTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0601_battle_counter(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0601_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0601_BATTLE_COUNTER.1,
            v as u32,
        )
    }
    /// `f0602BattleCounter` — bit[0], 1 bit
    #[inline]
    pub fn f0602_battle_counter(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0602_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0602_BATTLE_COUNTER.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0602_battle_counter(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0602_BATTLE_COUNTER.0,
            global_flag_save_flag_table::F0602_BATTLE_COUNTER.1,
            v as u32,
        )
    }
    /// `f0101BippaFlag` — bit[0], 1 bit
    #[inline]
    pub fn f0101_bippa_flag(&self) -> bool {
        self.read_save_flag(
            global_flag_save_flag_table::F0101_BIPPA_FLAG.0,
            global_flag_save_flag_table::F0101_BIPPA_FLAG.1,
        ) != 0
    }
    #[inline]
    pub fn set_f0101_bippa_flag(&mut self, v: bool) {
        self.write_save_flag(
            global_flag_save_flag_table::F0101_BIPPA_FLAG.0,
            global_flag_save_flag_table::F0101_BIPPA_FLAG.1,
            v as u32,
        )
    }
}
