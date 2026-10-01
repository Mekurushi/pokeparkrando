use std::sync::mpsc::{Receiver, TryRecvError};

use pokeparkrando_core::{GameId, ImportOriginalError, ImportOriginalProgress};

#[derive(Default)]
pub(in crate::patcher) enum ImportState {
    #[default]
    Idle,
    Importing {
        receiver: Receiver<ImportEvent>,
        progress: Option<ImportOriginalProgress>,
    },
}

pub(in crate::patcher) enum ImportEvent {
    Progress(ImportOriginalProgress),
    Finished(Result<GameId, ImportOriginalError>),
}

pub(in crate::patcher) enum ImportOutcome {
    Imported(GameId),
    Failed(ImportFailure),
}

pub(in crate::patcher) enum ImportFailure {
    Import(ImportOriginalError),
    Disconnected,
}

impl ImportState {
    pub(in crate::patcher) fn begin(&mut self, receiver: Receiver<ImportEvent>) {
        *self = Self::Importing {
            receiver,
            progress: None,
        };
    }

    pub(in crate::patcher) fn poll(&mut self) -> Option<ImportOutcome> {
        let Self::Importing { receiver, progress } = self else {
            return None;
        };

        let (finished, disconnected) = loop {
            match receiver.try_recv() {
                Ok(ImportEvent::Progress(next)) => *progress = Some(next),
                Ok(ImportEvent::Finished(result)) => break (Some(result), false),
                Err(TryRecvError::Empty) => break (None, false),
                Err(TryRecvError::Disconnected) => break (None, true),
            }
        };

        match (finished, disconnected) {
            (Some(Ok(game_id)), _) => {
                *self = Self::Idle;
                Some(ImportOutcome::Imported(game_id))
            }
            (Some(Err(error)), _) => {
                *self = Self::Idle;
                Some(ImportOutcome::Failed(ImportFailure::Import(error)))
            }
            (None, true) => {
                *self = Self::Idle;
                Some(ImportOutcome::Failed(ImportFailure::Disconnected))
            }
            (None, false) => None,
        }
    }

    pub(in crate::patcher) fn is_importing(&self) -> bool {
        matches!(self, Self::Importing { .. })
    }

    pub(in crate::patcher) fn progress(&self) -> Option<ImportOriginalProgress> {
        match self {
            Self::Importing { progress, .. } => *progress,
            Self::Idle => None,
        }
    }
}
