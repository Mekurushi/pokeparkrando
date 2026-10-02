use std::io;
use std::path::{Path, PathBuf};

use crate::Appkprk;
use crate::bundled_project::BundledProject;
use crate::error::{BuildPatchError, BundledProjectError, ImportOriginalError};
use crate::original::{
    ImportOriginalProgress, OriginalReadiness, import_original, original_readiness,
};
use crate::parkforge::{
    self, BuildConfig, BuildConfigValue, BuildDiagnostic, BuildProgress, GameId, RebuildProgress,
};

pub enum PatchProgress {
    Preparing,
    Building(BuildProgress),
    Rebuild(RebuildProgress),
}

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

    pub fn workspace_root(&self) -> &Path {
        &self.workspace_root
    }

    pub fn game_display_name(&self, game_id: &GameId) -> Option<&str> {
        self.project.game_display_name(game_id)
    }

    pub fn patch_to_iso<P, D>(
        &self,
        game_id: &GameId,
        appkprk: &Appkprk,
        destination_iso: &Path,
        mut progress: P,
        diagnostics: D,
    ) -> Result<PathBuf, BuildPatchError>
    where
        P: FnMut(PatchProgress),
        D: for<'a> FnMut(BuildDiagnostic<'a>),
    {
        progress(PatchProgress::Preparing);
        let sources = BundledProject::materialize_sources()
            .map_err(|source| BuildPatchError::PrepareSources { source })?;

        let original = self.workspace_root.join("original").join(game_id.as_str());
        let build_root = tempfile::Builder::new()
            .prefix("pokeparkrando-build-")
            .tempdir()
            .map_err(BuildPatchError::CreateTemporaryBuild)?;
        let build_destination = build_root.path().join(game_id.as_str());
        let shared_sources = sources.shared();
        let revision_sources = sources.revision(game_id);
        parkforge::build_with_paths(
            &original,
            &shared_sources,
            &revision_sources,
            &build_destination,
            Self::build_config(appkprk),
            |build_progress| progress(PatchProgress::Building(build_progress)),
            diagnostics,
        )
        .map_err(|source| BuildPatchError::Build {
            game_id: game_id.clone(),
            destination: build_destination.clone(),
            source: Box::new(source),
        })?;
        parkforge::rebuild_with_paths(&build_destination, destination_iso, |rebuild_progress| {
            progress(PatchProgress::Rebuild(rebuild_progress));
        })
        .map_err(|source| BuildPatchError::Rebuild {
            destination: destination_iso.to_path_buf(),
            source: Box::new(source),
        })?;

        Ok(destination_iso.to_path_buf())
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
