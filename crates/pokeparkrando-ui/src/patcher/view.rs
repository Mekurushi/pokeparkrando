use eframe::egui;
use pokeparkrando_core::OriginalReadiness;

use super::state::{OriginalStatusReadiness, PatcherState};

#[derive(Clone, Copy)]
pub(super) enum PatcherAction {
    ImportOriginal,
}

pub(super) struct PatcherView<'a> {
    state: &'a PatcherState,
}

impl<'a> PatcherView<'a> {
    pub(super) fn new(state: &'a PatcherState) -> Self {
        Self { state }
    }

    pub(super) fn show_readiness(
        &self,
        ui: &mut egui::Ui,
        actions_enabled: bool,
    ) -> Option<PatcherAction> {
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
        action
    }

    pub(super) fn show_content(&self, ui: &mut egui::Ui) {
        // TODO: unify show logic for patcher
        if self.state.is_failed() {
            let _error = ui.colored_label(ui.visuals().error_fg_color, "Patcher unavailable");
        }
    }
}
