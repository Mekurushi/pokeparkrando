use std::path::{Path, PathBuf};

use super::model::Workspace;

pub(super) enum WorkspaceState {
    Required {
        suggested: Option<PathBuf>,
        error: Option<String>,
    },
    Ready {
        workspace: Workspace,
        error: Option<String>,
    },
}

impl WorkspaceState {
    pub(super) fn required(suggested: Option<PathBuf>, error: Option<String>) -> Self {
        Self::Required { suggested, error }
    }

    pub(super) fn ready(workspace: Workspace) -> Self {
        Self::Ready {
            workspace,
            error: None,
        }
    }

    pub(super) fn workspace(&self) -> Option<&Workspace> {
        match self {
            Self::Required { .. } => None,
            Self::Ready { workspace, .. } => Some(workspace),
        }
    }

    pub(super) fn suggested(&self) -> Option<&Path> {
        match self {
            Self::Required { suggested, .. } => suggested.as_deref(),
            Self::Ready { .. } => None,
        }
    }

    pub(super) fn browse_directory(&self) -> Option<&Path> {
        match self {
            Self::Required { suggested, .. } => suggested.as_deref(),
            Self::Ready { workspace, .. } => Some(workspace.root()),
        }
    }

    pub(super) fn set_error(&mut self, message: String) {
        match self {
            Self::Required { error, .. } | Self::Ready { error, .. } => *error = Some(message),
        }
    }

    pub(super) fn error(&self) -> Option<&str> {
        match self {
            Self::Required { error, .. } | Self::Ready { error, .. } => error.as_deref(),
        }
    }
}
