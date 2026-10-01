use eframe::egui;
use pokeparkrando_core::OriginalReadiness;

use super::patch_file::PatchFileState;
use super::state::{OriginalStatusReadiness, PatcherState};

#[derive(Clone, Copy)]
pub(super) enum PatcherAction {
    ImportOriginal,
    SelectPatchFile,
}

pub(super) struct PatcherView<'a> {
    state: &'a PatcherState,
    patch_file: Option<&'a PatchFileState>,
}

impl<'a> PatcherView<'a> {
    pub(super) fn new(state: &'a PatcherState, patch_file: Option<&'a PatchFileState>) -> Self {
        Self { state, patch_file }
    }

    pub(super) fn show(&self, ui: &mut egui::Ui, actions_enabled: bool) -> Option<PatcherAction> {
        match self.state {
            PatcherState::Unavailable => None,
            PatcherState::Ready { .. } => {
                let readiness_action = self.show_readiness(ui, actions_enabled);
                let patch_file_action = self.show_patch_file(ui, actions_enabled);
                patch_file_action.or(readiness_action)
            }
            PatcherState::Failed => {
                Self::show_failed(ui);
                None
            }
        }
    }

    fn show_patch_file(&self, ui: &mut egui::Ui, actions_enabled: bool) -> Option<PatcherAction> {
        let mut action = None;
        let _header = ui.horizontal(|ui| {
            let _heading = ui.label(egui::RichText::new("Patch file").strong().size(15.0));
            if ui
                .add_enabled(actions_enabled, egui::Button::new("Select .appkprk..."))
                .clicked()
            {
                action = Some(PatcherAction::SelectPatchFile);
            }
        });
        match self.patch_file {
            Some(patch_file) => {
                let _path = ui.label(patch_file.path().display().to_string());
                let contents = patch_file.contents();
                let _summary = ui.label(format!(
                    "Player: {}  -  Seed: {}",
                    contents.player_name(),
                    contents.seed()
                ));
            }
            None => {
                let _missing = ui.weak("No patch file selected");
            }
        }
        action
    }

    fn show_readiness(&self, ui: &mut egui::Ui, actions_enabled: bool) -> Option<PatcherAction> {
        let originals = self.state.originals()?;

        let mut action = None;
        let _header = ui.horizontal(|ui| {
            let _heading = ui.label(
                egui::RichText::new("Supported originals")
                    .strong()
                    .size(15.0),
            );
            if ui
                .add_enabled(actions_enabled, egui::Button::new("Import original ISO..."))
                .clicked()
            {
                action = Some(PatcherAction::ImportOriginal);
            }
        });
        let _statuses = egui::Grid::new("original-readiness")
            .num_columns(2)
            .show(ui, |ui| {
                for original in originals {
                    let game_id = original.game_id().as_str();
                    let name = original
                        .display_name()
                        .map_or_else(|| game_id.to_owned(), |name| format!("{name} ({game_id})"));
                    let _game = ui.label(name);
                    match original.readiness() {
                        OriginalStatusReadiness::Available(OriginalReadiness::Ready) => {
                            let _status = ui.label("Ready");
                        }
                        OriginalStatusReadiness::Available(OriginalReadiness::Missing) => {
                            let _status = ui.weak("Missing");
                        }
                        OriginalStatusReadiness::Available(OriginalReadiness::Invalid) => {
                            let _status = ui.colored_label(ui.visuals().error_fg_color, "Invalid");
                        }
                        OriginalStatusReadiness::Unavailable => {
                            let _status =
                                ui.colored_label(ui.visuals().error_fg_color, "Unavailable");
                        }
                    }
                    ui.end_row();
                }
            });
        let _separator = ui.separator();
        action
    }

    fn show_failed(ui: &mut egui::Ui) {
        let _failure = ui.group(|ui| {
            let _heading = ui.heading(
                egui::RichText::new("Patcher unavailable")
                    .color(ui.visuals().error_fg_color)
                    .size(16.0),
            );
            let _description = ui.label(
                "Patch data could not be loaded. Patching is disabled. \
            Try reinstalling or contact the creator",
            );
        });
    }
}
