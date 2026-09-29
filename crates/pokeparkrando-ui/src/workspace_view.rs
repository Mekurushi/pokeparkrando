use std::path::{Path, PathBuf};

use eframe::egui;

use crate::workspace::Workspace;

pub(crate) enum WorkspaceState {
    Required {
        suggested: Option<PathBuf>,
        error: Option<String>,
    },
    Ready {
        workspace: Workspace,
        error: Option<String>,
    },
}

#[derive(Clone, Copy)]
pub(crate) enum WorkspaceAction {
    UseSuggested,
    ChooseDirectory,
}

impl WorkspaceState {
    pub(crate) fn required(suggested: Option<PathBuf>, error: Option<String>) -> Self {
        Self::Required { suggested, error }
    }

    pub(crate) fn ready(workspace: Workspace) -> Self {
        Self::Ready {
            workspace,
            error: None,
        }
    }

    pub(crate) fn show(&self, ui: &mut egui::Ui) -> Option<WorkspaceAction> {
        match self {
            Self::Required { suggested, error } => {
                show_required(ui, suggested.as_deref(), error.as_deref())
            }
            Self::Ready { workspace, error } => show_ready(ui, workspace, error.as_deref()),
        }
    }

    pub(crate) fn workspace(&self) -> Option<&Workspace> {
        match self {
            Self::Required { .. } => None,
            Self::Ready { workspace, .. } => Some(workspace),
        }
    }

    pub(crate) fn suggested(&self) -> Option<&Path> {
        match self {
            Self::Required { suggested, .. } => suggested.as_deref(),
            Self::Ready { .. } => None,
        }
    }

    pub(crate) fn browse_directory(&self) -> Option<&Path> {
        match self {
            Self::Required { suggested, .. } => suggested.as_deref(),
            Self::Ready { workspace, .. } => Some(workspace.root()),
        }
    }

    pub(crate) fn set_error(&mut self, message: String) {
        match self {
            Self::Required { error, .. } | Self::Ready { error, .. } => *error = Some(message),
        }
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
