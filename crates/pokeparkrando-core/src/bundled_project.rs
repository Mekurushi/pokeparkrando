use crate::error::BundledProjectError;
use crate::parkforge::{GameId, ProjectConfig};

const PROJECT_CONFIG: &str = include_str!("../../../bundled-project/project.toml");

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
}
