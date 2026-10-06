use pokeparkrando_core::{ImportOriginalError, ReadAppkprkError};

use super::AppError;
use crate::patcher::PatcherError;
use crate::workspace::WorkspaceError;

pub(super) struct ErrorReport {
    pub(super) title: String,
    pub(super) message: String,
    pub(super) details: Option<String>,
}

impl From<AppError> for ErrorReport {
    fn from(error: AppError) -> Self {
        match error {
            AppError::Workspace(error) => Self::from_workspace(error),
            AppError::Patcher(error) => Self::from_patcher(error),
            AppError::Updater(error) => Self {
                title: "Could not load versions".to_owned(),
                message: "The published version list could not be fetched from GitHub".to_owned(),
                details: Some(error.to_string()),
            },
        }
    }
}

impl ErrorReport {
    fn from_workspace(error: WorkspaceError) -> Self {
        match error {
            WorkspaceError::NotDirectory { path } => Self {
                title: "Workspace unavailable".to_owned(),
                message: "The selected workspace is not an existing directory".to_owned(),
                details: Some(format!("Workspace: {}", path.display())),
            },
        }
    }

    fn from_patcher(error: PatcherError) -> Self {
        match error {
            PatcherError::Load(error) => Self {
                title: "Patcher unavailable".to_owned(),
                message: "The patch data could not be loaded".to_owned(),
                details: Some(error.to_string()),
            },
            PatcherError::Readiness { game_id, source } => Self {
                title: "Could not check original game".to_owned(),
                message: format!(
                    "The original files for game revision {game_id} could not be checked"
                ),
                details: Some(source.to_string()),
            },
            PatcherError::Import(error) => Self::from_import(error),
            PatcherError::Patch(error) => Self {
                title: "Could not create patched ISO".to_owned(),
                message: "The patch operation failed".to_owned(),
                details: Some(error.to_string()),
            },
            PatcherError::ReadPatchFile(error) => Self::from_patch_file(error),
            PatcherError::StartImport(error) => Self {
                title: "Could not start import".to_owned(),
                message: "The original ISO import worker could not be started".to_owned(),
                details: Some(error.to_string()),
            },
            PatcherError::StartPatch(error) => Self {
                title: "Could not start patch".to_owned(),
                message: "The ISO patch worker could not be started".to_owned(),
                details: Some(error.to_string()),
            },
            PatcherError::ImportStopped => Self {
                title: "Import stopped unexpectedly".to_owned(),
                message: "The original ISO import ended before successfully finishing".to_owned(),
                details: None,
            },
            PatcherError::PatchStopped => Self {
                title: "Patch stopped unexpectedly".to_owned(),
                message: "The ISO patch operation ended before successfully finishing".to_owned(),
                details: None,
            },
        }
    }

    fn from_import(error: ImportOriginalError) -> Self {
        match error {
            ImportOriginalError::UnsupportedNkitIso { input } => Self {
                title: "Unsupported disc image".to_owned(),
                message: "NKit images are not supported. Use a clean standard Wii ISO instead"
                    .to_owned(),
                details: Some(format!("ISO: {}", input.display())),
            },
            ImportOriginalError::InvalidGameId { input, raw } => Self {
                title: "Invalid disc image".to_owned(),
                message: "The selected ISO does not contain a valid Wii game ID".to_owned(),
                details: Some(format!("ISO: {}\nRaw game ID: {raw:?}", input.display())),
            },
            ImportOriginalError::UnsupportedGame { game_id } => Self {
                title: "Unsupported game revision".to_owned(),
                message: format!("Game revision {game_id} is not supported"),
                details: None,
            },
            ImportOriginalError::CreateOriginalDirectory { path, source } => Self {
                title: "Could not prepare workspace".to_owned(),
                message: format!(
                    "The original game data directory could not be created at {}",
                    path.display()
                ),
                details: Some(source.to_string()),
            },
            error
            @ (ImportOriginalError::Identify { .. } | ImportOriginalError::Extract { .. }) => {
                Self {
                    title: "Could not import original ISO".to_owned(),
                    message: "The selected ISO could not be imported".to_owned(),
                    details: Some(error.to_string()),
                }
            }
        }
    }

    fn from_patch_file(error: ReadAppkprkError) -> Self {
        match error {
            error @ ReadAppkprkError::UnsupportedVersion { .. } => Self {
                title: "Incompatible patch file".to_owned(),
                message: "The selected patch file was created for a different patcher version"
                    .to_owned(),
                details: Some(error.to_string()),
            },
            error => Self {
                title: "Invalid patch file".to_owned(),
                message: "The selected file could not be read as a PokePark patch file".to_owned(),
                details: Some(error.to_string()),
            },
        }
    }
}
