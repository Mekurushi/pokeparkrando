use eframe::egui;
use pokeparkrando_core::OriginalReadiness;

use crate::patcher_state::PatcherState;

pub(crate) fn show_readiness(ui: &mut egui::Ui, state: &PatcherState) {
    let Some(originals) = state.originals() else {
        return;
    };

    let _heading = ui.label(
        egui::RichText::new("Supported originals")
            .strong()
            .size(15.0),
    );
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
                    Ok(OriginalReadiness::Ready) => {
                        let _status = ui.label("Ready");
                    }
                    Ok(OriginalReadiness::Missing) => {
                        let _status = ui.weak("Missing");
                    }
                    Ok(OriginalReadiness::Invalid) => {
                        let _status = ui.colored_label(ui.visuals().error_fg_color, "Invalid");
                    }
                    Err(error) => {
                        let _status = ui.colored_label(ui.visuals().error_fg_color, error);
                    }
                }
                ui.end_row();
            }
        });
}
