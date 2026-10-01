use std::sync::mpsc::{Receiver, TryRecvError};

use pokeparkrando_core::{GameId, ImportOriginalProgress};

#[derive(Default)]
pub(in crate::patcher) enum ImportState {
    #[default]
    Idle,
    Importing {
        receiver: Receiver<ImportEvent>,
        progress: Option<ImportOriginalProgress>,
    },
    Failed(String),
}

pub(in crate::patcher) enum ImportEvent {
    Progress(ImportOriginalProgress),
    Finished(Result<GameId, String>),
}

pub(in crate::patcher) enum ImportOutcome {
    Imported(GameId),
    Failed,
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
                *self = Self::Failed(error);
                Some(ImportOutcome::Failed)
            }
            (None, true) => {
                *self = Self::Failed("original import stopped unexpectedly".to_owned());
                Some(ImportOutcome::Failed)
            }
            (None, false) => None,
        }
    }

    pub(in crate::patcher) fn fail(&mut self, error: String) {
        *self = Self::Failed(error);
    }

    pub(in crate::patcher) fn is_importing(&self) -> bool {
        matches!(self, Self::Importing { .. })
    }

    pub(in crate::patcher) fn progress(&self) -> Option<ImportOriginalProgress> {
        match self {
            Self::Importing { progress, .. } => *progress,
            Self::Idle | Self::Failed(_) => None,
        }
    }

    pub(in crate::patcher) fn error(&self) -> Option<&str> {
        match self {
            Self::Failed(error) => Some(error),
            Self::Idle | Self::Importing { .. } => None,
        }
    }
}
