use crate::APP_TITLE;
use crate::error::ErrorComponent;
use crate::patcher::{PatcherComponent, PatcherEvent};
use crate::updater::{UpdaterComponent, UpdaterEvent};
use crate::workspace::{WorkspaceComponent, WorkspaceEvent};
use eframe::{CreationContext, Storage, egui};

pub(crate) struct PokeparkRandoApp {
    workspace: WorkspaceComponent,
    patcher: PatcherComponent,
    updater: UpdaterComponent,
    errors: ErrorComponent,
}

impl PokeparkRandoApp {
    pub(crate) fn new(context: &CreationContext<'_>) -> Self {
        let workspace = WorkspaceComponent::restore(context.storage);
        let patcher = PatcherComponent::new(workspace.root());
        Self {
            workspace,
            patcher,
            updater: UpdaterComponent::default(),
            errors: ErrorComponent::default(),
        }
    }

    fn handle_workspace_event(&mut self, event: WorkspaceEvent) {
        match event {
            WorkspaceEvent::Activated => {
                self.patcher.load(self.workspace.root());
            }
            WorkspaceEvent::Error(error) => self.errors.push(error),
        }
    }

    fn handle_patcher_event(&mut self, event: PatcherEvent) {
        match event {
            PatcherEvent::Error(error) => self.errors.push(error),
        }
    }

    fn handle_updater_event(&mut self, event: UpdaterEvent, context: &egui::Context) {
        match event {
            UpdaterEvent::Error(error) => self.errors.push(error),
            UpdaterEvent::Installed(_version) => {}
            UpdaterEvent::CloseApplication => {
                context.send_viewport_cmd(egui::ViewportCommand::Close);
            }
        }
    }
}

impl eframe::App for PokeparkRandoApp {
    fn ui(&mut self, ui: &mut egui::Ui, frame: &mut eframe::Frame) {
        let actions_enabled = !self.patcher.is_busy();
        let workspace = egui::Panel::top("workspace").show(ui, |ui| {
            let _title = ui.vertical_centered(|ui| {
                let _header = ui.horizontal(|ui| {
                    let _heading = ui.heading(egui::RichText::new(APP_TITLE).strong().size(19.0));
                    if ui
                        .add_enabled(actions_enabled, egui::Button::new("Versions..."))
                        .clicked()
                        && let Some(event) = self.updater.open(ui.ctx())
                    {
                        self.handle_updater_event(event, ui.ctx());
                    }
                });
            });
            ui.add_space(10.0);
            self.workspace.show_header(ui, frame, actions_enabled)
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
                if let Some(event) = self.patcher.show(ui) {
                    self.handle_patcher_event(event);
                }
            });
        }

        if let Some(event) = self.updater.show(ui.ctx()) {
            self.handle_updater_event(event, ui.ctx());
        }
        self.errors.show(ui.ctx());
    }

    fn save(&mut self, storage: &mut dyn Storage) {
        self.workspace.save(storage);
    }
}
