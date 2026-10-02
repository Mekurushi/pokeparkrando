use std::fs;
use std::path::PathBuf;

use include_dir::{Dir, include_dir};
use tempfile::TempDir;

use crate::error::BundledProjectError;
use crate::parkforge::{GameId, ProjectConfig};

const PROJECT_CONFIG: &str = include_str!("../../../bundled-project/project.toml");
static PROJECT_SOURCES: Dir<'_> = include_dir!("$CARGO_MANIFEST_DIR/../../bundled-project/src");

#[derive(Debug)]
pub struct BundledProject {
    config: ProjectConfig,
}

impl BundledProject {
    pub fn load() -> Result<Self, BundledProjectError> {
        let config = ProjectConfig::from_toml_str(PROJECT_CONFIG).map_err(|source| {
            BundledProjectError::ParseConfig {
                source: Box::new(source),
            }
        })?;
        Ok(Self { config })
    }

    pub fn game_ids(&self) -> impl Iterator<Item = &GameId> {
        self.config.game_ids()
    }

    pub(crate) fn materialize_sources() -> Result<MaterializedSources, BundledProjectError> {
        let directory = tempfile::Builder::new()
            .prefix("pokeparkrando-sources-")
            .tempdir()
            .map_err(BundledProjectError::CreateTemporarySources)?;
        PROJECT_SOURCES
            .extract(directory.path())
            .map_err(BundledProjectError::ExtractSources)?;

        let shared = directory.path().join("shared");
        fs::create_dir_all(&shared).map_err(|source| BundledProjectError::CreateSharedSources {
            path: shared,
            source,
        })?;

        Ok(MaterializedSources { directory })
    }

    pub(crate) fn game_display_name(&self, game_id: &GameId) -> Option<&str> {
        self.config
            .games
            .get(game_id)
            .and_then(|game| game.display_name.as_deref())
    }
}

pub(crate) struct MaterializedSources {
    directory: TempDir,
}

impl MaterializedSources {
    pub(crate) fn shared(&self) -> PathBuf {
        self.directory.path().join("shared")
    }

    pub(crate) fn revision(&self, game_id: &GameId) -> PathBuf {
        self.directory.path().join(game_id.as_str())
    }
}
