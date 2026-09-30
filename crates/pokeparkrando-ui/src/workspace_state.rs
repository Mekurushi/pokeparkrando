use std::path::{Path, PathBuf};

use crate::workspace::Workspace;

pub(crate) enum WorkspaceState {
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
    pub(crate) fn required(suggested: Option<PathBuf>, error: Option<String>) -> Self {
        Self::Required { suggested, error }
    }

    pub(crate) fn ready(workspace: Workspace) -> Self {
        Self::Ready {
            workspace,
            error: None,
        }
    }

    pub(crate) fn workspace(&self) -> Option<&Workspace> {
        match self {
            Self::Required { .. } => None,
            Self::Ready { workspace, .. } => Some(workspace),
        }
    }

    pub(crate) fn suggested(&self) -> Option<&Path> {
        match self {
            Self::Required { suggested, .. } => suggested.as_deref(),
            Self::Ready { .. } => None,
        }
    }

    pub(crate) fn browse_directory(&self) -> Option<&Path> {
        match self {
            Self::Required { suggested, .. } => suggested.as_deref(),
            Self::Ready { workspace, .. } => Some(workspace.root()),
        }
    }

    pub(crate) fn set_error(&mut self, message: String) {
        match self {
            Self::Required { error, .. } | Self::Ready { error, .. } => *error = Some(message),
        }
    }

    pub(crate) fn error(&self) -> Option<&str> {
        match self {
            Self::Required { error, .. } | Self::Ready { error, .. } => error.as_deref(),
        }
    }
}
