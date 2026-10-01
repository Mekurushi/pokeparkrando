mod component;
mod report;

pub(crate) use component::ErrorComponent;

use crate::patcher::PatcherError;
use crate::workspace::WorkspaceError;

pub(crate) enum AppError {
    Workspace(WorkspaceError),
    Patcher(PatcherError),
}

impl From<WorkspaceError> for AppError {
    fn from(error: WorkspaceError) -> Self {
        Self::Workspace(error)
    }
}

impl From<PatcherError> for AppError {
    fn from(error: PatcherError) -> Self {
        Self::Patcher(error)
    }
}
