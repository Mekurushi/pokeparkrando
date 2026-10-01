use std::{collections::BTreeMap, fs::File, io::Read, path::Path};

use base64::{Engine as _, engine::general_purpose::STANDARD};
use serde::Deserialize;
use zip::{ZipArchive, result::ZipError};

use crate::ReadAppkprkError;

const PLANDO_ENTRY: &str = "plando";
const PATCHER_VERSION_MAJOR: &str = env!("CARGO_PKG_VERSION_MAJOR");
const PATCHER_VERSION_MINOR: &str = env!("CARGO_PKG_VERSION_MINOR");

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct AppkprkVersion {
    major: u64,
    minor: u64,
    patch: u64,
}

impl AppkprkVersion {
    pub fn major(self) -> u64 {
        self.major
    }

    pub fn minor(self) -> u64 {
        self.minor
    }

    pub fn patch(self) -> u64 {
        self.patch
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum Goal {
    Mew,
    Postgame,
}

#[derive(Clone, Debug, Eq, PartialEq)]
#[allow(clippy::struct_excessive_bools)]
pub struct PatchOptions {
    goal: Goal,
    required_battle_count: u64,
    required_prisma_count: u64,
    remove_errand_power_comp_locations: bool,
    harder_enemy_ai: bool,
    each_zone: bool,
    unlock_fast_travel_with_taxi_stop: bool,
    show_client_text_ingame: bool,
    fps_enhancement_patch: bool,
}

impl PatchOptions {
    pub fn goal(&self) -> Goal {
        self.goal
    }

    pub fn required_battle_count(&self) -> u64 {
        self.required_battle_count
    }

    pub fn required_prisma_count(&self) -> u64 {
        self.required_prisma_count
    }

    pub fn remove_errand_power_comp_locations(&self) -> bool {
        self.remove_errand_power_comp_locations
    }

    pub fn harder_enemy_ai(&self) -> bool {
        self.harder_enemy_ai
    }

    pub fn each_zone(&self) -> bool {
        self.each_zone
    }

    pub fn unlock_fast_travel_with_taxi_stop(&self) -> bool {
        self.unlock_fast_travel_with_taxi_stop
    }

    pub fn show_client_text_ingame(&self) -> bool {
        self.show_client_text_ingame
    }

    pub fn fps_enhancement_patch(&self) -> bool {
        self.fps_enhancement_patch
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct Appkprk {
    version: AppkprkVersion,
    seed: String,
    slot: u64,
    player_name: String,
    options: PatchOptions,
    entrances: BTreeMap<String, String>,
}

impl Appkprk {
    pub fn read(path: &Path) -> Result<Self, ReadAppkprkError> {
        let archive_file = File::open(path).map_err(|source| ReadAppkprkError::Open {
            path: path.to_path_buf(),
            source,
        })?;
        let mut archive =
            ZipArchive::new(archive_file).map_err(|source| ReadAppkprkError::InvalidArchive {
                path: path.to_path_buf(),
                source,
            })?;
        let mut plando = match archive.by_name(PLANDO_ENTRY) {
            Ok(plando) => plando,
            Err(ZipError::FileNotFound) => {
                return Err(ReadAppkprkError::MissingPlando {
                    path: path.to_path_buf(),
                });
            }
            Err(source) => {
                return Err(ReadAppkprkError::InvalidArchive {
                    path: path.to_path_buf(),
                    source,
                });
            }
        };

        let mut encoded = Vec::new();
        let _ =
            plando
                .read_to_end(&mut encoded)
                .map_err(|source| ReadAppkprkError::ReadPlando {
                    path: path.to_path_buf(),
                    source,
                })?;

        let decoded =
            STANDARD
                .decode(encoded)
                .map_err(|source| ReadAppkprkError::DecodePlando {
                    path: path.to_path_buf(),
                    source,
                })?;
        let raw: RawAppkprk = serde_yaml_ng::from_slice(&decoded).map_err(|source| {
            ReadAppkprkError::ParsePlando {
                path: path.to_path_buf(),
                source,
            }
        })?;

        raw.try_into()
    }

    pub fn version(&self) -> AppkprkVersion {
        self.version
    }

    pub fn seed(&self) -> &str {
        &self.seed
    }

    pub fn slot(&self) -> u64 {
        self.slot
    }

    pub fn player_name(&self) -> &str {
        &self.player_name
    }

    pub fn options(&self) -> &PatchOptions {
        &self.options
    }

    pub fn entrances(&self) -> &BTreeMap<String, String> {
        &self.entrances
    }
}

#[derive(Deserialize)]
#[serde(rename_all = "PascalCase")]
struct RawAppkprk {
    version: Vec<u64>,
    seed: String,
    slot: u64,
    name: String,
    options: RawPatchOptions,
    entrances: BTreeMap<String, String>,
}

#[derive(Deserialize)]
struct RawPatchOptions {
    goal: u64,
    num_required_battle_count: u64,
    num_required_prisma_count_skygarden: u64,
    remove_errand_power_comp_locations: u64,
    harder_enemy_ai: u64,
    each_zone: u64,
    unlock_fast_travel_with_taxi_stop: u64,
    show_client_text_ingame: u64,
    fps_enhancement_patch: u64,
}

impl TryFrom<RawAppkprk> for Appkprk {
    type Error = ReadAppkprkError;

    fn try_from(raw: RawAppkprk) -> Result<Self, Self::Error> {
        let [major, minor, patch]: [u64; 3] =
            raw.version.try_into().map_err(|version: Vec<u64>| {
                ReadAppkprkError::InvalidVersionLength {
                    found: version.len(),
                }
            })?;
        if PATCHER_VERSION_MAJOR.parse::<u64>() != Ok(major)
            || PATCHER_VERSION_MINOR.parse::<u64>() != Ok(minor)
        {
            return Err(ReadAppkprkError::UnsupportedVersion {
                major,
                minor,
                patch,
                supported_major: PATCHER_VERSION_MAJOR,
                supported_minor: PATCHER_VERSION_MINOR,
            });
        }

        Ok(Self {
            version: AppkprkVersion {
                major,
                minor,
                patch,
            },
            seed: raw.seed,
            slot: raw.slot,
            player_name: raw.name,
            options: raw.options.try_into()?,
            entrances: raw.entrances,
        })
    }
}

impl TryFrom<RawPatchOptions> for PatchOptions {
    type Error = ReadAppkprkError;

    fn try_from(raw: RawPatchOptions) -> Result<Self, Self::Error> {
        Ok(Self {
            goal: match raw.goal {
                0 => Goal::Mew,
                1 => Goal::Postgame,
                value => {
                    return Err(ReadAppkprkError::InvalidOptionValue {
                        option: "goal",
                        value,
                        expected: "0 or 1",
                    });
                }
            },
            required_battle_count: raw.num_required_battle_count,
            required_prisma_count: raw.num_required_prisma_count_skygarden,
            remove_errand_power_comp_locations: toggle(
                "remove_errand_power_comp_locations",
                raw.remove_errand_power_comp_locations,
            )?,
            harder_enemy_ai: toggle("harder_enemy_ai", raw.harder_enemy_ai)?,
            each_zone: toggle("each_zone", raw.each_zone)?,
            unlock_fast_travel_with_taxi_stop: toggle(
                "unlock_fast_travel_with_taxi_stop",
                raw.unlock_fast_travel_with_taxi_stop,
            )?,
            show_client_text_ingame: toggle(
                "show_client_text_ingame",
                raw.show_client_text_ingame,
            )?,
            fps_enhancement_patch: toggle("fps_enhancement_patch", raw.fps_enhancement_patch)?,
        })
    }
}

fn toggle(option: &'static str, value: u64) -> Result<bool, ReadAppkprkError> {
    match value {
        0 => Ok(false),
        1 => Ok(true),
        value => Err(ReadAppkprkError::InvalidOptionValue {
            option,
            value,
            expected: "0 or 1",
        }),
    }
}
