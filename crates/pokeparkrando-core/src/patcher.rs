use std::io;
use std::path::{Path, PathBuf};

use crate::Appkprk;
use crate::bundled_project::BundledProject;
use crate::error::{BundledProjectError, ImportOriginalError};
use crate::original::{
    ImportOriginalProgress, OriginalReadiness, import_original, original_readiness,
};
use crate::parkforge::{BuildConfig, BuildConfigValue, GameId};

#[derive(Debug)]
pub struct Patcher {
    workspace_root: PathBuf,
    project: BundledProject,
}

impl Patcher {
    pub fn build_config(appkprk: &Appkprk) -> BuildConfig {
        BuildConfig::from_iter([
            (
                "PLAYER_NAME".to_owned(),
                BuildConfigValue::String(appkprk.player_name().to_owned()),
            ),
            (
                "BATTLE_COUNT".to_owned(),
                BuildConfigValue::Integer(appkprk.options().required_battle_count().cast_signed()),
            ),
            (
                "SHOULD_PRINT_AP_BUFFER".to_owned(),
                BuildConfigValue::Boolean(appkprk.options().show_client_text_ingame()),
            ),
            (
                "FPS_ENHANCEMENT".to_owned(),
                BuildConfigValue::Boolean(appkprk.options().fps_enhancement_patch()),
            ),
        ])
    }

    pub fn load(workspace_root: impl Into<PathBuf>) -> Result<Self, BundledProjectError> {
        Ok(Self {
            workspace_root: workspace_root.into(),
            project: BundledProject::load()?,
        })
    }

    pub fn supported_game_ids(&self) -> impl Iterator<Item = &GameId> {
        self.project.game_ids()
    }

    pub fn game_display_name(&self, game_id: &GameId) -> Option<&str> {
        self.project.game_display_name(game_id)
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
