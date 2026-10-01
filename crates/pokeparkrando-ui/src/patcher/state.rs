use std::path::Path;
use std::sync::Arc;

use pokeparkrando_core::{BundledProjectError, GameId, OriginalReadiness, Patcher};

pub(super) enum PatcherState {
    Unavailable,
    Ready {
        patcher: Arc<Patcher>,
        originals: Vec<OriginalStatus>,
    },
    Failed,
}

pub(super) struct OriginalStatus {
    game_id: GameId,
    display_name: Option<String>,
    readiness: OriginalStatusReadiness,
}

#[derive(Clone, Copy)]
pub(super) enum OriginalStatusReadiness {
    Available(OriginalReadiness),
    Unavailable,
}

pub(super) struct ReadinessFailure {
    pub(super) game_id: GameId,
    pub(super) source: std::io::Error,
}

impl PatcherState {
    pub(super) fn load(
        workspace_root: &Path,
    ) -> Result<(Self, Vec<ReadinessFailure>), BundledProjectError> {
        let patcher = Patcher::load(workspace_root)?;
        let mut state = Self::Ready {
            patcher: Arc::new(patcher),
            originals: Vec::new(),
        };
        let failures = state.refresh_originals();
        Ok((state, failures))
    }

    pub(super) fn patcher_handle(&self) -> Option<Arc<Patcher>> {
        match self {
            Self::Ready { patcher, .. } => Some(Arc::clone(patcher)),
            Self::Unavailable | Self::Failed => None,
        }
    }

    pub(super) fn refresh_originals(&mut self) -> Vec<ReadinessFailure> {
        let mut failures = Vec::new();
        if let Self::Ready { patcher, originals } = self {
            *originals = patcher
                .supported_game_ids()
                .map(|game_id| {
                    let readiness = match patcher.original_readiness(game_id) {
                        Ok(readiness) => OriginalStatusReadiness::Available(readiness),
                        Err(source) => {
                            failures.push(ReadinessFailure {
                                game_id: game_id.clone(),
                                source,
                            });
                            OriginalStatusReadiness::Unavailable
                        }
                    };
                    OriginalStatus {
                        game_id: game_id.clone(),
                        display_name: patcher.game_display_name(game_id).map(str::to_owned),
                        readiness,
                    }
                })
                .collect();
        }
        failures
    }

    pub(super) fn originals(&self) -> Option<&[OriginalStatus]> {
        match self {
            Self::Ready { originals, .. } => Some(originals),
            Self::Unavailable | Self::Failed => None,
        }
    }

    pub(super) fn is_ready(&self) -> bool {
        matches!(self, Self::Ready { .. })
    }
}

impl OriginalStatus {
    pub(super) fn game_id(&self) -> &GameId {
        &self.game_id
    }

    pub(super) fn display_name(&self) -> Option<&str> {
        self.display_name.as_deref()
    }

    pub(super) fn readiness(&self) -> OriginalStatusReadiness {
        self.readiness
    }
}
