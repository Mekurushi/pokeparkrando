use std::fs;
use std::io;
use std::path::Path;

use parkforge::GameId;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OriginalReadiness {
    Missing,
    Ready,
    Invalid,
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
