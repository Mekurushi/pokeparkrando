use std::path::{Path, PathBuf};

use eframe::{Storage, egui};
use rfd::FileDialog;

use super::state::WorkspaceState;
use super::view::{WorkspaceAction, WorkspaceView};
use super::{Workspace, WorkspaceError};

const WORKSPACE_KEY: &str = "workspace";

pub(crate) struct WorkspaceComponent {
    state: WorkspaceState,
    pending_error: Option<WorkspaceError>,
}

pub(crate) enum WorkspaceEvent {
    Activated,
    Error(WorkspaceError),
}

impl WorkspaceComponent {
    pub(crate) fn restore(storage: Option<&dyn Storage>) -> Self {
        let saved =
            storage.and_then(|storage| eframe::get_value::<PathBuf>(storage, WORKSPACE_KEY));
        let (state, pending_error) = match saved {
            Some(root) => match Workspace::open(root) {
                Ok(workspace) => (WorkspaceState::ready(workspace), None),
                Err(error) => (
                    WorkspaceState::required(executable_directory()),
                    Some(error),
                ),
            },
            None => (WorkspaceState::required(executable_directory()), None),
        };
        Self {
            state,
            pending_error,
        }
    }

    pub(crate) fn workspace(&self) -> Option<&Workspace> {
        self.state.workspace()
    }

    pub(crate) fn root(&self) -> Option<&Path> {
        self.workspace().map(Workspace::root)
    }

    pub(crate) fn requires_selection(&self) -> bool {
        self.workspace().is_none()
    }

    pub(crate) fn show_header(
        &mut self,
        ui: &mut egui::Ui,
        frame: &mut eframe::Frame,
        actions_enabled: bool,
    ) -> Option<WorkspaceEvent> {
        let action = WorkspaceView::new(&self.state, actions_enabled).show(ui);
        self.pending_error
            .take()
            .map(WorkspaceEvent::Error)
            .or_else(|| action.and_then(|action| self.handle_action(action, frame)))
    }

    pub(crate) fn show_required_content(&self, ui: &mut egui::Ui) {
        if self.requires_selection() {
            WorkspaceView::show_required_content(ui);
        }
    }

    pub(crate) fn save(&self, storage: &mut dyn Storage) {
        match self.workspace() {
            Some(workspace) => {
                eframe::set_value(storage, WORKSPACE_KEY, &workspace.root().to_path_buf());
            }
            None => storage.remove_string(WORKSPACE_KEY),
        }
    }

    fn handle_action(
        &mut self,
        action: WorkspaceAction,
        frame: &mut eframe::Frame,
    ) -> Option<WorkspaceEvent> {
        match action {
            WorkspaceAction::UseSuggested => self.use_suggested(frame),
            WorkspaceAction::ChooseDirectory => self.choose_directory(frame),
        }
    }

    fn use_suggested(&mut self, frame: &mut eframe::Frame) -> Option<WorkspaceEvent> {
        let root = self.state.suggested()?.to_path_buf();
        Some(self.activate(root, frame))
    }

    fn choose_directory(&mut self, frame: &mut eframe::Frame) -> Option<WorkspaceEvent> {
        let mut dialog = FileDialog::new().set_title("Select workspace");
        if let Some(root) = self.state.browse_directory().filter(|root| root.is_dir()) {
            dialog = dialog.set_directory(root);
        }
        let root = dialog.pick_folder()?;
        Some(self.activate(root, frame))
    }

    fn activate(&mut self, root: PathBuf, frame: &mut eframe::Frame) -> WorkspaceEvent {
        let workspace = match Workspace::open(root) {
            Ok(workspace) => workspace,
            Err(error) => {
                return WorkspaceEvent::Error(error);
            }
        };

        self.state = WorkspaceState::ready(workspace);
        if let Some(storage) = frame.storage_mut() {
            self.save(storage);
            storage.flush();
        }
        WorkspaceEvent::Activated
    }
}

fn executable_directory() -> Option<PathBuf> {
    std::env::current_exe()
        .ok()?
        .parent()
        .map(Path::to_path_buf)
}
