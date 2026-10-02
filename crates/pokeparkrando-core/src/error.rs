use std::path::PathBuf;

use thiserror::Error;

use crate::parkforge::{self, GameId};

#[derive(Debug, Error)]
pub enum ReadAppkprkError {
    #[error("failed to open .appkprk file {}: {source}", path.display())]
    Open {
        path: PathBuf,
        #[source]
        source: std::io::Error,
    },

    #[error("{} is not a valid .appkprk archive: {source}", path.display())]
    InvalidArchive {
        path: PathBuf,
        #[source]
        source: zip::result::ZipError,
    },

    #[error(".appkprk archive {} does not contain a plando entry", path.display())]
    MissingPlando { path: PathBuf },

    #[error("failed to read the plando entry from {}: {source}", path.display())]
    ReadPlando {
        path: PathBuf,
        #[source]
        source: std::io::Error,
    },

    #[error("plando entry in {} is not valid Base64: {source}", path.display())]
    DecodePlando {
        path: PathBuf,
        #[source]
        source: base64::DecodeError,
    },

    #[error("decoded plando entry in {} is not valid YAML: {source}", path.display())]
    ParsePlando {
        path: PathBuf,
        #[source]
        source: serde_yaml_ng::Error,
    },

    #[error(".appkprk version must contain exactly three components, found {found}")]
    InvalidVersionLength { found: usize },

    #[error(
        "unsupported .appkprk version {major}.{minor}.{patch}; supported format is {supported_major}.{supported_minor}.x"
    )]
    UnsupportedVersion {
        major: u64,
        minor: u64,
        patch: u64,
        supported_major: &'static str,
        supported_minor: &'static str,
    },

    #[error("invalid value {value} for option {option}; expected {expected}")]
    InvalidOptionValue {
        option: &'static str,
        value: u64,
        expected: &'static str,
    },
}

#[derive(Debug, Error)]
pub enum BundledProjectError {
    #[error("embedded project configuration is invalid: {source}")]
    ParseConfig {
        #[source]
        source: Box<parkforge::ProjectError>,
    },

    #[error("failed to create a temporary directory for bundled project sources: {0}")]
    CreateTemporarySources(#[source] std::io::Error),

    #[error("failed to extract bundled project sources: {0}")]
    ExtractSources(#[source] std::io::Error),

    #[error("failed to create shared source directory {}: {source}", path.display())]
    CreateSharedSources {
        path: PathBuf,
        #[source]
        source: std::io::Error,
    },
}

#[derive(Debug, Error)]
pub enum ImportOriginalError {
    #[error("NKit ISO {} is not supported", input.display())]
    UnsupportedNkitIso { input: PathBuf },

    #[error("ISO {} contains an invalid Wii game ID: {raw:?}", input.display())]
    InvalidGameId { input: PathBuf, raw: [u8; 6] },

    #[error("failed to identify ISO {}: {source}", input.display())]
    Identify {
        input: PathBuf,
        #[source]
        source: Box<parkforge::IdentifyError>,
    },

    #[error("game revision {game_id} is not supported")]
    UnsupportedGame { game_id: GameId },

    #[error("failed to create original directory {}: {source}", path.display())]
    CreateOriginalDirectory {
        path: PathBuf,
        #[source]
        source: std::io::Error,
    },

    #[error(
        "failed to extract ISO {} to {}: {source}",
        input.display(),
        destination.display()
    )]
    Extract {
        input: PathBuf,
        destination: PathBuf,
        #[source]
        source: Box<parkforge::ExtractError>,
    },
}

#[derive(Debug, Error)]
pub enum BuildPatchError {
    #[error("failed to prepare bundled patch sources: {source}")]
    PrepareSources {
        #[source]
        source: BundledProjectError,
    },

    #[error("failed to create a temporary directory for build data: {0}")]
    CreateTemporaryBuild(#[source] std::io::Error),

    #[error("failed to build game revision {game_id} at {}: {source}", destination.display())]
    Build {
        game_id: GameId,
        destination: PathBuf,
        #[source]
        source: Box<parkforge::BuildError>,
    },

    #[error("failed to rebuild patched ISO at {}: {source}", destination.display())]
    Rebuild {
        destination: PathBuf,
        #[source]
        source: Box<parkforge::RebuildError>,
    },
}
