use std::path::{Path, PathBuf};

use eframe::{CreationContext, Storage, egui};
use rfd::FileDialog;

use crate::APP_NAME;
use crate::workspace::Workspace;
use crate::workspace_view::{WorkspaceAction, WorkspaceState};

const WORKSPACE_KEY: &str = "workspace";

pub(crate) struct PokeparkRandoApp {
    workspace_state: WorkspaceState,
}

impl PokeparkRandoApp {
    pub(crate) fn new(context: &CreationContext<'_>) -> Self {
        let saved = context
            .storage
            .and_then(|storage| eframe::get_value::<PathBuf>(storage, WORKSPACE_KEY));
        let workspace_state = match saved {
            Some(root) => match Workspace::open(root) {
                Ok(workspace) => WorkspaceState::ready(workspace),
                Err(error) => {
                    WorkspaceState::required(executable_directory(), Some(error.to_string()))
                }
            },
            None => WorkspaceState::required(executable_directory(), None),
        };
        Self { workspace_state }
    }

    fn handle_workspace_action(&mut self, action: WorkspaceAction, frame: &mut eframe::Frame) {
        match action {
            WorkspaceAction::UseSuggested => self.use_suggested_workspace(frame),
            WorkspaceAction::ChooseDirectory => self.choose_workspace(frame),
        }
    }

    fn use_suggested_workspace(&mut self, frame: &mut eframe::Frame) {
        let Some(root) = self.workspace_state.suggested().map(Path::to_path_buf) else {
            return;
        };
        self.activate_workspace(root, frame);
    }

    fn choose_workspace(&mut self, frame: &mut eframe::Frame) {
        let mut dialog = FileDialog::new().set_title("Select workspace");
        if let Some(root) = self
            .workspace_state
            .browse_directory()
            .filter(|root| root.is_dir())
        {
            dialog = dialog.set_directory(root);
        }
        if let Some(root) = dialog.pick_folder() {
            self.activate_workspace(root, frame);
        }
    }

    fn activate_workspace(&mut self, root: PathBuf, frame: &mut eframe::Frame) {
        let workspace = match Workspace::open(root) {
            Ok(workspace) => workspace,
            Err(error) => {
                self.workspace_state.set_error(error.to_string());
                return;
            }
        };

        self.workspace_state = WorkspaceState::ready(workspace);
        if let Some(storage) = frame.storage_mut() {
            store_workspace(storage, self.persisted_workspace());
            storage.flush();
        }
    }

    fn persisted_workspace(&self) -> Option<&Workspace> {
        self.workspace_state.workspace()
    }
}

impl eframe::App for PokeparkRandoApp {
    fn ui(&mut self, ui: &mut egui::Ui, frame: &mut eframe::Frame) {
        let workspace = egui::Panel::top("workspace").show(ui, |ui| self.workspace_state.show(ui));
        if let Some(action) = workspace.inner {
            self.handle_workspace_action(action, frame);
        }

        let _panel = egui::CentralPanel::default().show(ui, |ui| {
            let _heading = ui.heading(egui::RichText::new(APP_NAME).strong().size(19.0));
            let _label = if self.workspace_state.workspace().is_none() {
                ui.label(egui::RichText::new("Choose a Workspace to continue").size(16.0))
            } else {
                ui.label("Import prototype WIP")
            };
        });
    }

    fn save(&mut self, storage: &mut dyn Storage) {
        store_workspace(storage, self.persisted_workspace());
    }
}

fn executable_directory() -> Option<PathBuf> {
    std::env::current_exe()
        .ok()?
        .parent()
        .map(Path::to_path_buf)
}

fn store_workspace(storage: &mut dyn Storage, workspace: Option<&Workspace>) {
    match workspace {
        Some(workspace) => {
            eframe::set_value(storage, WORKSPACE_KEY, &workspace.root().to_path_buf());
        }
        None => storage.remove_string(WORKSPACE_KEY),
    }
}
