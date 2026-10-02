mod appkprk;
mod bundled_project;
mod error;
mod original;
mod parkforge;
mod patcher;

pub use appkprk::{Appkprk, AppkprkVersion, Goal, PatchOptions};
pub use bundled_project::BundledProject;
pub use error::{BuildPatchError, BundledProjectError, ImportOriginalError, ReadAppkprkError};
pub use original::{
    ImportOriginalProgress, OriginalReadiness, import_original, original_readiness,
};
pub use parkforge::{
    BuildConfig, BuildConfigValue, BuildDiagnostic, BuildProgress, GameId, RebuildProgress,
    check_project,
};
pub use patcher::{PatchProgress, Patcher};
pub const PATCHER_VERSION: &str = env!("CARGO_PKG_VERSION");
