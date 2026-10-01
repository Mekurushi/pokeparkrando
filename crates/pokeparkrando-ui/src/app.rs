use eframe::{CreationContext, Storage, egui};

use crate::APP_NAME;
use crate::patcher::PatcherComponent;
use crate::workspace::{WorkspaceComponent, WorkspaceEvent};

pub(crate) struct PokeparkRandoApp {
    workspace: WorkspaceComponent,
    patcher: PatcherComponent,
}

impl PokeparkRandoApp {
    pub(crate) fn new(context: &CreationContext<'_>) -> Self {
        let workspace = WorkspaceComponent::restore(context.storage);
        let patcher = PatcherComponent::new(workspace.root());
        Self { workspace, patcher }
    }

    fn handle_workspace_event(&mut self, event: WorkspaceEvent) {
        match event {
            WorkspaceEvent::Activated => {
                self.patcher.load(self.workspace.root());
            }
        }
    }
}

impl eframe::App for PokeparkRandoApp {
    fn ui(&mut self, ui: &mut egui::Ui, frame: &mut eframe::Frame) {
        let workspace_actions_enabled = !self.patcher.is_busy();
        let workspace = egui::Panel::top("workspace").show(ui, |ui| {
            self.workspace
                .show_header(ui, frame, workspace_actions_enabled)
        });
        if let Some(event) = workspace.inner {
            self.handle_workspace_event(event);
        }

        if self.workspace.requires_selection() {
            let _panel = egui::CentralPanel::default().show(ui, |ui| {
                self.workspace.show_required_content(ui);
            });
        } else {
            let _panel = egui::CentralPanel::default().show(ui, |ui| {
                let _heading = ui.heading(egui::RichText::new(APP_NAME).strong().size(19.0));
                self.patcher.show_readiness(ui);
                self.patcher.show_content(ui);
            });
        }
    }

    fn save(&mut self, storage: &mut dyn Storage) {
        self.workspace.save(storage);
    }
}
