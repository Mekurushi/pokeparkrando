use std::path::{Path, PathBuf};

use thiserror::Error;

#[derive(Debug, Clone)]
pub(crate) struct Workspace {
    root: PathBuf,
}

impl Workspace {
    pub(crate) fn open(root: PathBuf) -> Result<Self, WorkspaceError> {
        if root.is_dir() {
            Ok(Self { root })
        } else {
            Err(WorkspaceError::NotDirectory { path: root })
        }
    }

    pub(crate) fn root(&self) -> &Path {
        &self.root
    }
}

#[derive(Debug, Error)]
pub(crate) enum WorkspaceError {
    #[error("workspace is not an existing directory: {}", path.display())]
    NotDirectory { path: PathBuf },
}
