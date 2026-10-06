use std::sync::mpsc::{Receiver, TryRecvError};

#[derive(Default)]
pub(super) enum UpdaterState {
    #[default]
    Idle,
    Loading(Receiver<Result<Vec<String>, self_update::Error>>),
    Loaded {
        versions: Vec<String>,
        selected: Option<String>,
    },
}

pub(super) enum PollResult {
    Loaded,
    Failed(self_update::Error),
    Disconnected,
}

impl UpdaterState {
    pub(super) fn begin(&mut self, receiver: Receiver<Result<Vec<String>, self_update::Error>>) {
        *self = Self::Loading(receiver);
    }

    pub(super) fn poll(&mut self) -> Option<PollResult> {
        let Self::Loading(receiver) = self else {
            return None;
        };

        match receiver.try_recv() {
            Ok(Ok(versions)) => {
                *self = Self::Loaded {
                    versions,
                    selected: None,
                };
                Some(PollResult::Loaded)
            }
            Ok(Err(error)) => {
                *self = Self::Idle;
                Some(PollResult::Failed(error))
            }
            Err(TryRecvError::Disconnected) => {
                *self = Self::Idle;
                Some(PollResult::Disconnected)
            }
            Err(TryRecvError::Empty) => None,
        }
    }

    pub(super) fn is_loading(&self) -> bool {
        matches!(self, Self::Loading(_))
    }

    pub(super) fn versions(&self) -> Option<&[String]> {
        match self {
            Self::Loaded { versions, .. } => Some(versions),
            Self::Idle | Self::Loading(_) => None,
        }
    }

    pub(super) fn selected_version(&self) -> Option<&str> {
        match self {
            Self::Loaded { selected, .. } => selected.as_deref(),
            Self::Idle | Self::Loading(_) => None,
        }
    }

    pub(super) fn select(&mut self, version: String) {
        if let Self::Loaded { selected, .. } = self {
            *selected = Some(version);
        }
    }

    pub(super) fn cancel_selection(&mut self) {
        if let Self::Loaded { selected, .. } = self {
            *selected = None;
        }
    }
}
