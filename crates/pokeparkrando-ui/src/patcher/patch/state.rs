use std::path::PathBuf;
use std::sync::mpsc::{Receiver, TryRecvError};

use pokeparkrando_core::{BuildPatchError, PatchProgress};

#[derive(Default)]
pub(in crate::patcher) enum PatchState {
    #[default]
    Idle,
    Patching {
        receiver: Receiver<PatchEvent>,
        progress: Option<PatchProgress>,
    },
    Completed {
        destination: PathBuf,
    },
}

pub(in crate::patcher) enum PatchEvent {
    Progress(PatchProgress),
    Finished(Result<PathBuf, BuildPatchError>),
}

pub(in crate::patcher) enum PatchOutcome {
    Patched(PathBuf),
    Failed(PatchFailure),
}

pub(in crate::patcher) enum PatchFailure {
    Patch(BuildPatchError),
    Disconnected,
}

impl PatchState {
    pub(in crate::patcher) fn begin(&mut self, receiver: Receiver<PatchEvent>) {
        *self = Self::Patching {
            receiver,
            progress: None,
        };
    }

    pub(in crate::patcher) fn poll(&mut self) -> Option<PatchOutcome> {
        let Self::Patching { receiver, progress } = self else {
            return None;
        };

        let (finished, disconnected) = loop {
            match receiver.try_recv() {
                Ok(PatchEvent::Progress(next)) => *progress = Some(next),
                Ok(PatchEvent::Finished(result)) => break (Some(result), false),
                Err(TryRecvError::Empty) => break (None, false),
                Err(TryRecvError::Disconnected) => break (None, true),
            }
        };

        match (finished, disconnected) {
            (Some(Ok(destination)), _) => {
                let outcome_destination = destination.clone();
                *self = Self::Completed { destination };
                Some(PatchOutcome::Patched(outcome_destination))
            }
            (Some(Err(error)), _) => {
                *self = Self::Idle;
                Some(PatchOutcome::Failed(PatchFailure::Patch(error)))
            }
            (None, true) => {
                *self = Self::Idle;
                Some(PatchOutcome::Failed(PatchFailure::Disconnected))
            }
            (None, false) => None,
        }
    }

    pub(in crate::patcher) fn is_patching(&self) -> bool {
        matches!(self, Self::Patching { .. })
    }

    pub(in crate::patcher) fn progress(&self) -> Option<&PatchProgress> {
        match self {
            Self::Patching { progress, .. } => progress.as_ref(),
            Self::Idle | Self::Completed { .. } => None,
        }
    }

    pub(in crate::patcher) fn completed_destination(&self) -> Option<&PathBuf> {
        match self {
            Self::Completed { destination } => Some(destination),
            Self::Idle | Self::Patching { .. } => None,
        }
    }
}
