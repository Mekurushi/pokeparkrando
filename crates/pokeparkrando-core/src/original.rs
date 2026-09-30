use std::fs;
use std::io;
use std::path::Path;

use crate::error::ImportOriginalError;
use crate::parkforge::{self, ExtractionProgress, GameId};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OriginalReadiness {
    Missing,
    Ready,
    Invalid,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ImportOriginalProgress {
    Disc { completed: u64, total: u64 },
    Archives { completed: usize, discovered: usize },
}

pub fn original_readiness(
    workspace_root: &Path,
    game_id: &GameId,
) -> io::Result<OriginalReadiness> {
    let original = workspace_root.join("original").join(game_id.as_str());
    match fs::symlink_metadata(original) {
        Ok(metadata) if metadata.is_dir() => Ok(OriginalReadiness::Ready),
        Ok(_) => Ok(OriginalReadiness::Invalid),
        Err(error) if error.kind() == io::ErrorKind::NotFound => Ok(OriginalReadiness::Missing),
        Err(error) => Err(error),
    }
}

pub fn import_original<F>(
    workspace_root: &Path,
    input_iso: &Path,
    supported_game_ids: &[GameId],
    mut progress: F,
) -> Result<GameId, ImportOriginalError>
where
    F: FnMut(ImportOriginalProgress),
{
    let game_id =
        parkforge::identify(input_iso).map_err(|source| ImportOriginalError::Identify {
            input: input_iso.to_path_buf(),
            source: Box::new(source),
        })?;

    if !supported_game_ids.contains(&game_id) {
        return Err(ImportOriginalError::UnsupportedGame { game_id });
    }

    let original_root = workspace_root.join("original");
    fs::create_dir_all(&original_root).map_err(|source| {
        ImportOriginalError::CreateOriginalDirectory {
            path: original_root.clone(),
            source,
        }
    })?;
    let destination = original_root.join(game_id.as_str());
    parkforge::extract_to(input_iso, &destination, |event| {
        progress(map_extraction_progress(event));
    })
    .map_err(|source| ImportOriginalError::Extract {
        input: input_iso.to_path_buf(),
        destination,
        source: Box::new(source),
    })
}

fn map_extraction_progress(progress: ExtractionProgress) -> ImportOriginalProgress {
    match progress {
        ExtractionProgress::Disc(progress) => ImportOriginalProgress::Disc {
            completed: progress.completed(),
            total: progress.total(),
        },
        ExtractionProgress::Archives {
            completed,
            discovered,
        } => ImportOriginalProgress::Archives {
            completed,
            discovered,
        },
    }
}
