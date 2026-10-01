use eframe::egui;
use pokeparkrando_core::ImportOriginalProgress;

use super::ImportState;
use crate::ui::progress_fraction;

pub(in crate::patcher) struct ImportProgressView<'a> {
    state: &'a ImportState,
}

impl<'a> ImportProgressView<'a> {
    pub(in crate::patcher) fn new(state: &'a ImportState) -> Self {
        Self { state }
    }

    pub(in crate::patcher) fn show(&self, ui: &mut egui::Ui) {
        if let Some(progress) = self.state.progress() {
            match progress {
                ImportOriginalProgress::Disc { completed, total } => {
                    let _progress = ui.add(
                        egui::ProgressBar::new(progress_fraction(completed, total))
                            .text(format!("Extracting disc: {completed} / {total} bytes")),
                    );
                }
                ImportOriginalProgress::Archives {
                    completed,
                    discovered,
                } => {
                    let completed_count = u64::try_from(completed).unwrap_or(u64::MAX);
                    let discovered_count = u64::try_from(discovered).unwrap_or(u64::MAX);
                    let _progress = ui.add(
                        egui::ProgressBar::new(progress_fraction(
                            completed_count,
                            discovered_count,
                        ))
                        .text(format!("Extracting archives: {completed} / {discovered}")),
                    );
                }
            }
        } else if self.state.is_importing() {
            let _preparing = ui.horizontal(|ui| {
                let _spinner = ui.spinner();
                let _status = ui.label("Preparing import...");
            });
        }
    }
}
