use std::path::{Path, PathBuf};

use super::model::Workspace;

pub(super) enum WorkspaceState {
    Required { suggested: Option<PathBuf> },
    Ready { workspace: Workspace },
}

impl WorkspaceState {
    pub(super) fn required(suggested: Option<PathBuf>) -> Self {
        Self::Required { suggested }
    }

    pub(super) fn ready(workspace: Workspace) -> Self {
        Self::Ready { workspace }
    }

    pub(super) fn workspace(&self) -> Option<&Workspace> {
        match self {
            Self::Required { .. } => None,
            Self::Ready { workspace } => Some(workspace),
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
            Self::Ready { workspace } => Some(workspace.root()),
        }
    }
}
