use std::sync::mpsc::{Receiver, TryRecvError};

pub(super) enum InstallEvent {
    Progress { downloaded: u64, total: Option<u64> },
    Finished(Result<(), self_update::Error>),
}

#[derive(Default)]
pub(super) enum UpdaterState {
    #[default]
    Idle,
    Loading(Receiver<Result<Vec<String>, self_update::Error>>),
    Loaded {
        versions: Vec<String>,
        selected: Option<String>,
    },
    Installing {
        version: String,
        receiver: Receiver<InstallEvent>,
        downloaded: u64,
        total: Option<u64>,
    },
    Installed {
        version: String,
    },
}

pub(super) enum PollResult {
    Loaded,
    FetchFailed(self_update::Error),
    FetchDisconnected,
    Installed(String),
    InstallFailed(self_update::Error),
    InstallDisconnected,
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
                Some(PollResult::FetchFailed(error))
            }
            Err(TryRecvError::Disconnected) => {
                *self = Self::Idle;
                Some(PollResult::FetchDisconnected)
            }
            Err(TryRecvError::Empty) => None,
        }
    }

    pub(super) fn poll_install(&mut self) -> Option<PollResult> {
        let Self::Installing {
            version,
            receiver,
            downloaded,
            total,
        } = self
        else {
            return None;
        };

        let (finished, disconnected) = loop {
            match receiver.try_recv() {
                Ok(InstallEvent::Progress {
                    downloaded: next_downloaded,
                    total: next_total,
                }) => {
                    *downloaded = next_downloaded;
                    *total = next_total;
                }
                Ok(InstallEvent::Finished(result)) => break (Some(result), false),
                Err(TryRecvError::Empty) => break (None, false),
                Err(TryRecvError::Disconnected) => break (None, true),
            }
        };

        match (finished, disconnected) {
            (Some(Ok(())), _) => {
                let installed_version = version.clone();
                *self = Self::Installed {
                    version: installed_version.clone(),
                };
                Some(PollResult::Installed(installed_version))
            }
            (Some(Err(error)), _) => {
                *self = Self::Idle;
                Some(PollResult::InstallFailed(error))
            }
            (None, true) => {
                *self = Self::Idle;
                Some(PollResult::InstallDisconnected)
            }
            (None, false) => None,
        }
    }

    pub(super) fn is_loading(&self) -> bool {
        matches!(self, Self::Loading(_))
    }

    pub(super) fn is_installing(&self) -> bool {
        matches!(self, Self::Installing { .. })
    }

    pub(super) fn versions(&self) -> Option<&[String]> {
        match self {
            Self::Loaded { versions, .. } => Some(versions),
            Self::Idle | Self::Loading(_) | Self::Installing { .. } | Self::Installed { .. } => {
                None
            }
        }
    }

    pub(super) fn selected_version(&self) -> Option<&str> {
        match self {
            Self::Loaded { selected, .. } => selected.as_deref(),
            Self::Idle | Self::Loading(_) | Self::Installing { .. } | Self::Installed { .. } => {
                None
            }
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

    pub(super) fn begin_install(&mut self, version: String, receiver: Receiver<InstallEvent>) {
        *self = Self::Installing {
            version,
            receiver,
            downloaded: 0,
            total: None,
        };
    }

    pub(super) fn install_progress(&self) -> Option<(&str, u64, Option<u64>)> {
        match self {
            Self::Installing {
                version,
                downloaded,
                total,
                ..
            } => Some((version, *downloaded, *total)),
            Self::Idle | Self::Loading(_) | Self::Loaded { .. } | Self::Installed { .. } => None,
        }
    }

    pub(super) fn installed_version(&self) -> Option<&str> {
        match self {
            Self::Installed { version } => Some(version),
            Self::Idle | Self::Loading(_) | Self::Loaded { .. } | Self::Installing { .. } => None,
        }
    }
}
