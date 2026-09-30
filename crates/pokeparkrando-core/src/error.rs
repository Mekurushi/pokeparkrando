use std::path::PathBuf;

use thiserror::Error;

use crate::parkforge::{self, GameId};

#[derive(Debug, Error)]
pub enum BundledProjectError {
    #[error("embedded project configuration is invalid: {source}")]
    ParseConfig {
        #[source]
        source: Box<parkforge::ProjectError>,
    },
}

#[derive(Debug, Error)]
pub enum ImportOriginalError {
    #[error("failed to identify ISO {}: {source}", input.display())]
    Identify {
        input: PathBuf,
        #[source]
        source: Box<parkforge::Error>,
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
        source: Box<parkforge::Error>,
    },
}
