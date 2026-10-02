use eframe::egui;
use pokeparkrando_core::{BuildProgress, PatchProgress, RebuildProgress};

use super::PatchState;
use crate::ui::progress_fraction;

pub(in crate::patcher) struct PatchProgressView<'a> {
    state: &'a PatchState,
}

impl<'a> PatchProgressView<'a> {
    pub(in crate::patcher) fn new(state: &'a PatchState) -> Self {
        Self { state }
    }

    pub(in crate::patcher) fn show(&self, ui: &mut egui::Ui) {
        match self.state.progress() {
            Some(PatchProgress::Preparing) => Self::show_spinner(ui, "Preparing patch..."),
            Some(PatchProgress::Building(BuildProgress::CopyingOriginal)) => {
                Self::show_spinner(ui, "Copying original game files...");
            }
            Some(PatchProgress::Building(BuildProgress::Operations { completed, total })) => {
                Self::show_counted_progress(ui, "Applying patch", *completed, *total);
            }
            Some(PatchProgress::Building(BuildProgress::Committing)) => {
                Self::show_spinner(ui, "Finalizing patched game files...");
            }
            Some(PatchProgress::Rebuild(RebuildProgress::Archives { completed, total })) => {
                Self::show_counted_progress(ui, "Rebuilding archives", *completed, *total);
            }
            Some(PatchProgress::Rebuild(RebuildProgress::Disc(progress))) => {
                let completed = progress.completed();
                let total = progress.total();
                let _progress = ui.add(
                    egui::ProgressBar::new(progress_fraction(completed, total))
                        .text(format!("Writing ISO: {completed}% / {total}%")),
                );
            }
            None if self.state.is_patching() => {
                Self::show_spinner(ui, "Starting patch...");
            }
            None => {
                if let Some(destination) = self.state.completed_destination() {
                    let _completed =
                        ui.label(format!("Patched ISO created at {}", destination.display()));
                }
            }
        }
    }

    fn show_counted_progress(ui: &mut egui::Ui, label: &str, completed: usize, total: usize) {
        let completed_count = u64::try_from(completed).unwrap_or(u64::MAX);
        let total_count = u64::try_from(total).unwrap_or(u64::MAX);
        let _progress = ui.add(
            egui::ProgressBar::new(progress_fraction(completed_count, total_count))
                .text(format!("{label}: {completed} / {total}")),
        );
    }

    fn show_spinner(ui: &mut egui::Ui, status: &str) {
        let _status = ui.horizontal(|ui| {
            let _spinner = ui.spinner();
            let _label = ui.label(status);
        });
    }
}
