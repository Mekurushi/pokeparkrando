use std::collections::VecDeque;

use eframe::egui;

use super::report::ErrorReport;
use crate::workspace::WorkspaceError;

#[derive(Default)]
pub(crate) struct ErrorComponent {
    reports: VecDeque<ErrorReport>,
}

impl ErrorComponent {
    pub(crate) fn push(&mut self, error: WorkspaceError) {
        self.reports.push_back(ErrorReport::from(error));
    }

    pub(crate) fn show(&mut self, context: &egui::Context) {
        let Some(report) = self.reports.front() else {
            return;
        };

        let response = egui::Modal::new(egui::Id::new("error-modal")).show(context, |ui| {
            let _heading = ui.heading(&report.title);
            let _message = ui.label(&report.message);
            if let Some(details) = &report.details {
                ui.add_space(8.0);
                let _details = ui.monospace(details);
            }
            ui.add_space(8.0);
            ui.button("Close").clicked()
        });

        if response.inner || response.should_close() {
            let _removed = self.reports.pop_front();
        }
    }
}
