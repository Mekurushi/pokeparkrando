use std::io;
use std::path::{Path, PathBuf};

use crate::bundled_project::BundledProject;
use crate::error::{BundledProjectError, ImportOriginalError};
use crate::original::{
    ImportOriginalProgress, OriginalReadiness, import_original, original_readiness,
};
use crate::parkforge::GameId;

#[derive(Debug)]
pub struct Patcher {
    workspace_root: PathBuf,
    project: BundledProject,
}

impl Patcher {
    pub fn load(workspace_root: impl Into<PathBuf>) -> Result<Self, BundledProjectError> {
        Ok(Self {
            workspace_root: workspace_root.into(),
            project: BundledProject::load()?,
        })
    }

    pub fn supported_game_ids(&self) -> impl Iterator<Item = &GameId> {
        self.project.game_ids()
    }

    pub fn original_readiness(&self, game_id: &GameId) -> io::Result<OriginalReadiness> {
        original_readiness(&self.workspace_root, game_id)
    }

    pub fn import_original<F>(
        &self,
        input_iso: &Path,
        progress: F,
    ) -> Result<GameId, ImportOriginalError>
    where
        F: FnMut(ImportOriginalProgress),
    {
        let supported_game_ids = self.project.game_ids().cloned().collect::<Vec<_>>();
        import_original(
            &self.workspace_root,
            input_iso,
            &supported_game_ids,
            progress,
        )
    }
}
