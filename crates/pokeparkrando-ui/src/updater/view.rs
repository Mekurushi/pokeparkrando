use eframe::egui;

use super::state::UpdaterState;
use crate::ui::progress_fraction;

pub(super) enum UpdaterAction {
    Close,
    CloseApplication,
    Refresh,
    Select(String),
    CancelSelection,
    ConfirmSelection,
}

pub(super) struct UpdaterView<'a> {
    state: &'a UpdaterState,
}

impl<'a> UpdaterView<'a> {
    pub(super) fn new(state: &'a UpdaterState) -> Self {
        Self { state }
    }

    pub(super) fn show(&self, context: &egui::Context) -> Option<UpdaterAction> {
        let response = egui::Modal::new(egui::Id::new("versions-modal")).show(context, |ui| {
            if let Some(version) = self.state.installed_version() {
                return Self::show_installed(ui, version);
            }
            if let Some((version, downloaded, total)) = self.state.install_progress() {
                Self::show_installing(ui, version, downloaded, total);
                return None;
            }
            if let Some(version) = self.state.selected_version() {
                return Self::show_confirmation(ui, version);
            }

            let mut action = None;
            let _heading = ui.heading("Published versions");
            ui.add_space(8.0);

            if self.state.is_loading() {
                let _loading = ui.horizontal(|ui| {
                    let _spinner = ui.spinner();
                    let _label = ui.label("Loading versions from GitHub...");
                });
            } else if let Some(versions) = self.state.versions() {
                if versions.is_empty() {
                    let _empty = ui.label("No published versions were found");
                } else {
                    let _versions = egui::ScrollArea::vertical()
                        .max_height(320.0)
                        .show(ui, |ui| {
                            for version in versions {
                                let normalized = version.strip_prefix('v').unwrap_or(version);
                                let current = normalized == env!("CARGO_PKG_VERSION");
                                let _version = ui.horizontal(|ui| {
                                    if current {
                                        let _label = ui.label(format!("{version}  (current)"));
                                    } else {
                                        let _label = ui.label(version);
                                        if ui.button("Select").clicked() {
                                            action = Some(UpdaterAction::Select(version.clone()));
                                        }
                                    }
                                });
                            }
                        });
                }
            }

            ui.add_space(8.0);
            let _actions = ui.horizontal(|ui| {
                if ui
                    .add_enabled(!self.state.is_loading(), egui::Button::new("Refresh"))
                    .clicked()
                {
                    action = Some(UpdaterAction::Refresh);
                }
                if ui.button("Close").clicked() {
                    action = Some(UpdaterAction::Close);
                }
            });
            action
        });

        let should_close = response.should_close() && !self.state.is_installing();
        response
            .inner
            .or_else(|| should_close.then_some(UpdaterAction::Close))
    }

    fn show_confirmation(ui: &mut egui::Ui, version: &str) -> Option<UpdaterAction> {
        let _heading = ui.heading("Change version");
        ui.add_space(8.0);
        let _message = ui.label(format!(
            "Replace version {} with {version}?",
            env!("CARGO_PKG_VERSION")
        ));
        ui.add_space(8.0);

        let mut action = None;
        let _actions = ui.horizontal(|ui| {
            if ui.button("Cancel").clicked() {
                action = Some(UpdaterAction::CancelSelection);
            }
            if ui.button("Continue").clicked() {
                action = Some(UpdaterAction::ConfirmSelection);
            }
        });
        action
    }

    fn show_installing(ui: &mut egui::Ui, version: &str, downloaded: u64, total: Option<u64>) {
        let _heading = ui.heading(format!("Installing {version}"));
        ui.add_space(8.0);
        match total.filter(|total| *total > 0) {
            Some(total) => {
                let progress = progress_fraction(downloaded, total);
                let _progress = ui.add(
                    egui::ProgressBar::new(progress)
                        .show_percentage()
                        .text(format!("{downloaded} / {total} bytes")),
                );
            }
            None => {
                let _progress = ui.horizontal(|ui| {
                    let _spinner = ui.spinner();
                    let _label = ui.label(format!("Downloaded {downloaded} bytes"));
                });
            }
        }
    }

    fn show_installed(ui: &mut egui::Ui, version: &str) -> Option<UpdaterAction> {
        let _heading = ui.heading("Version installed");
        ui.add_space(8.0);
        let _message = ui.label(format!(
            "Version {version} was installed. Restart the application to use it"
        ));
        ui.add_space(8.0);
        ui.button("Close application")
            .clicked()
            .then_some(UpdaterAction::CloseApplication)
    }
}
