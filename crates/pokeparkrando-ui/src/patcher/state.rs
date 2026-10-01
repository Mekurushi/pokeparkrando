use std::path::Path;

use pokeparkrando_core::{GameId, OriginalReadiness, Patcher};

pub(super) enum PatcherState {
    Unavailable,
    Ready {
        patcher: Patcher,
        originals: Vec<OriginalStatus>,
    },
    Failed(String),
}

pub(super) struct OriginalStatus {
    game_id: GameId,
    display_name: Option<String>,
    readiness: Result<OriginalReadiness, String>,
}

impl PatcherState {
    pub(super) fn load(workspace_root: &Path) -> Self {
        match Patcher::load(workspace_root) {
            Ok(patcher) => {
                let originals = patcher
                    .supported_game_ids()
                    .map(|game_id| OriginalStatus {
                        game_id: game_id.clone(),
                        display_name: patcher.game_display_name(game_id).map(str::to_owned),
                        readiness: patcher
                            .original_readiness(game_id)
                            .map_err(|error| error.to_string()),
                    })
                    .collect();
                Self::Ready { patcher, originals }
            }
            Err(error) => Self::Failed(error.to_string()),
        }
    }

    pub(super) fn patcher(&self) -> Option<&Patcher> {
        match self {
            Self::Ready { patcher, .. } => Some(patcher),
            Self::Unavailable | Self::Failed(_) => None,
        }
    }

    pub(super) fn originals(&self) -> Option<&[OriginalStatus]> {
        match self {
            Self::Ready { originals, .. } => Some(originals),
            Self::Unavailable | Self::Failed(_) => None,
        }
    }

    pub(super) fn error(&self) -> Option<&str> {
        match self {
            Self::Failed(error) => Some(error),
            Self::Unavailable | Self::Ready { .. } => None,
        }
    }
}

impl OriginalStatus {
    pub(super) fn game_id(&self) -> &GameId {
        &self.game_id
    }

    pub(super) fn display_name(&self) -> Option<&str> {
        self.display_name.as_deref()
    }

    pub(super) fn readiness(&self) -> Result<OriginalReadiness, &str> {
        self.readiness.as_ref().copied().map_err(String::as_str)
    }
}
