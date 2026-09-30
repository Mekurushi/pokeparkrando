use std::path::Path;

use eframe::egui;

use crate::workspace::Workspace;
use crate::workspace_state::WorkspaceState;

#[derive(Clone, Copy)]
pub(crate) enum WorkspaceAction {
    UseSuggested,
    ChooseDirectory,
}

pub(crate) struct WorkspaceView<'a> {
    state: &'a WorkspaceState,
    actions_enabled: bool,
}

impl<'a> WorkspaceView<'a> {
    pub(crate) fn new(state: &'a WorkspaceState, actions_enabled: bool) -> Self {
        Self {
            state,
            actions_enabled,
        }
    }

    pub(crate) fn show(&self, ui: &mut egui::Ui) -> Option<WorkspaceAction> {
        match self.state {
            WorkspaceState::Required { suggested, .. } => {
                self.show_required(ui, suggested.as_deref())
            }
            WorkspaceState::Ready { workspace, .. } => self.show_ready(ui, workspace),
        }
    }

    fn show_required(
        &self,
        ui: &mut egui::Ui,
        suggested: Option<&Path>,
    ) -> Option<WorkspaceAction> {
        let _heading = ui.heading(
            egui::RichText::new("Workspace required")
                .strong()
                .size(18.0),
        );
        let _description = ui.label(
            egui::RichText::new(
                "Game files will be stored here. Reuse this workspace if you want \
     to patch again",
            )
            .size(14.0),
        );

        if let Some(suggested) = suggested {
            let _suggested = ui.horizontal(|ui| {
                let _label = ui.label("Suggested:");
                let _path = ui.strong(suggested.display().to_string());
            });
        }
        Self::show_error(ui, self.state.error());

        let mut action = None;
        let _actions = ui.horizontal(|ui| {
            let use_suggested = ui.add_enabled(
                suggested.is_some() && self.actions_enabled,
                egui::Button::new("Use suggested"),
            );
            if use_suggested.clicked() {
                action = Some(WorkspaceAction::UseSuggested);
            }
            let choose = ui.add_enabled(
                self.actions_enabled,
                egui::Button::new("Choose another folder..."),
            );
            if choose.clicked() {
                action = Some(WorkspaceAction::ChooseDirectory);
            }
        });
        action
    }

    fn show_ready(&self, ui: &mut egui::Ui, workspace: &Workspace) -> Option<WorkspaceAction> {
        let mut action = None;
        let _workspace = ui.horizontal(|ui| {
            let _label = ui.strong("Workspace");
            let _path = ui.monospace(workspace.root().display().to_string());
            if ui
                .add_enabled(self.actions_enabled, egui::Button::new("Change..."))
                .clicked()
            {
                action = Some(WorkspaceAction::ChooseDirectory);
            }
        });
        Self::show_error(ui, self.state.error());
        action
    }

    fn show_error(ui: &mut egui::Ui, error: Option<&str>) {
        if let Some(error) = error {
            let _error = ui.colored_label(ui.visuals().error_fg_color, error);
        }
    }
}
