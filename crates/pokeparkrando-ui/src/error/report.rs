use crate::workspace::WorkspaceError;

pub(super) struct ErrorReport {
    pub(super) title: String,
    pub(super) message: String,
    pub(super) details: Option<String>,
}

impl From<WorkspaceError> for ErrorReport {
    fn from(error: WorkspaceError) -> Self {
        match error {
            WorkspaceError::NotDirectory { path } => Self {
                title: "Workspace unavailable".to_owned(),
                message: "The selected workspace is not an existing directory.".to_owned(),
                details: Some(format!("Workspace: {}", path.display())),
            },
        }
    }
}
