use eframe::{CreationContext, Storage, egui};

use crate::APP_NAME;
use crate::patcher::{PatcherState, PatcherView};
use crate::workspace::{WorkspaceComponent, WorkspaceEvent};

pub(crate) struct PokeparkRandoApp {
    workspace: WorkspaceComponent,
    patcher_state: PatcherState,
}

impl PokeparkRandoApp {
    pub(crate) fn new(context: &CreationContext<'_>) -> Self {
        let workspace = WorkspaceComponent::restore(context.storage);
        let patcher_state = workspace
            .workspace()
            .map_or(PatcherState::Unavailable, PatcherState::load);
        Self {
            workspace,
            patcher_state,
        }
    }

    fn handle_workspace_event(&mut self, event: WorkspaceEvent) {
        match event {
            WorkspaceEvent::Activated => {
                self.patcher_state = self
                    .workspace
                    .workspace()
                    .map_or(PatcherState::Unavailable, PatcherState::load);
            }
        }
    }
}

impl eframe::App for PokeparkRandoApp {
    fn ui(&mut self, ui: &mut egui::Ui, frame: &mut eframe::Frame) {
        let workspace = egui::Panel::top("workspace").show(ui, |ui| {
            let event = self.workspace.show_header(ui, frame, true);
            PatcherView::new(&self.patcher_state).show(ui);
            event
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
                if let Some(error) = self.patcher_state.error() {
                    let _error = ui.colored_label(ui.visuals().error_fg_color, error);
                } else if self.patcher_state.patcher().is_some() {
                    let _status = ui.label("Patcher stub");
                } else {
                    let _status = ui.label("Patcher unavailable");
                }
            });
        }
    }

    fn save(&mut self, storage: &mut dyn Storage) {
        self.workspace.save(storage);
    }
}
