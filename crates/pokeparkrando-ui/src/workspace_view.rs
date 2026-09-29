use std::path::Path;

use eframe::egui;

use crate::workspace::Workspace;
use crate::workspace_state::WorkspaceState;

#[derive(Clone, Copy)]
pub(crate) enum WorkspaceAction {
    UseSuggested,
    ChooseDirectory,
}

pub(crate) fn show(ui: &mut egui::Ui, state: &WorkspaceState) -> Option<WorkspaceAction> {
    match state {
        WorkspaceState::Required { suggested, error } => {
            show_required(ui, suggested.as_deref(), error.as_deref())
        }
        WorkspaceState::Ready { workspace, error } => show_ready(ui, workspace, error.as_deref()),
    }
}

fn show_required(
    ui: &mut egui::Ui,
    suggested: Option<&Path>,
    error: Option<&str>,
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
    show_error(ui, error);

    let mut action = None;
    let _actions = ui.horizontal(|ui| {
        if suggested.is_some() && ui.button("Use suggested").clicked() {
            action = Some(WorkspaceAction::UseSuggested);
        }
        if ui.button("Choose another folder...").clicked() {
            action = Some(WorkspaceAction::ChooseDirectory);
        }
    });
    action
}

fn show_ready(
    ui: &mut egui::Ui,
    workspace: &Workspace,
    error: Option<&str>,
) -> Option<WorkspaceAction> {
    let mut action = None;
    let _workspace = ui.horizontal(|ui| {
        let _label = ui.strong("Workspace");
        let _path = ui.monospace(workspace.root().display().to_string());
        if ui.button("Change...").clicked() {
            action = Some(WorkspaceAction::ChooseDirectory);
        }
    });
    show_error(ui, error);
    action
}

fn show_error(ui: &mut egui::Ui, error: Option<&str>) {
    if let Some(error) = error {
        let _error = ui.colored_label(ui.visuals().error_fg_color, error);
    }
}
