use std::path::Path;

use eframe::egui;

use super::state::PatcherState;
use super::view::PatcherView;

pub(crate) struct PatcherComponent {
    state: PatcherState,
}

impl PatcherComponent {
    pub(crate) fn new(workspace_root: Option<&Path>) -> Self {
        let state = workspace_root.map_or(PatcherState::Unavailable, PatcherState::load);
        Self { state }
    }

    pub(crate) fn load(&mut self, workspace_root: Option<&Path>) {
        self.state = workspace_root.map_or(PatcherState::Unavailable, PatcherState::load);
    }

    pub(crate) fn show_readiness(&self, ui: &mut egui::Ui) {
        PatcherView::new(&self.state).show_readiness(ui);
    }

    pub(crate) fn show_content(&self, ui: &mut egui::Ui) {
        PatcherView::new(&self.state).show_content(ui);
    }
}
