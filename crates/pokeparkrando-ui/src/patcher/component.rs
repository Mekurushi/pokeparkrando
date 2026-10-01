use std::path::Path;
use std::sync::mpsc;
use std::thread;

use eframe::egui;
use rfd::FileDialog;

use super::import::{ImportEvent, ImportOutcome, ImportProgressView, ImportState};
use super::state::PatcherState;
use super::view::{PatcherAction, PatcherView};

pub(crate) struct PatcherComponent {
    state: PatcherState,
    import: ImportState,
}

impl PatcherComponent {
    pub(crate) fn new(workspace_root: Option<&Path>) -> Self {
        let state = workspace_root.map_or(PatcherState::Unavailable, PatcherState::load);
        Self {
            state,
            import: ImportState::default(),
        }
    }

    pub(crate) fn load(&mut self, workspace_root: Option<&Path>) {
        self.state = workspace_root.map_or(PatcherState::Unavailable, PatcherState::load);
        self.import = ImportState::default();
    }

    pub(crate) fn is_busy(&self) -> bool {
        self.import.is_importing()
    }

    pub(crate) fn show_readiness(&mut self, ui: &mut egui::Ui) {
        self.poll_import();
        let action = PatcherView::new(&self.state).show_readiness(ui, !self.is_busy());
        if let Some(action) = action {
            self.handle_action(action, ui.ctx());
        }
    }

    pub(crate) fn show_content(&self, ui: &mut egui::Ui) {
        PatcherView::new(&self.state).show_content(ui);
        ImportProgressView::new(&self.import).show(ui);
    }

    fn handle_action(&mut self, action: PatcherAction, context: &egui::Context) {
        match action {
            PatcherAction::ImportOriginal => self.choose_original(context),
        }
    }

    fn choose_original(&mut self, context: &egui::Context) {
        let Some(patcher) = self.state.patcher_handle() else {
            return;
        };
        let Some(input) = FileDialog::new()
            .set_title("Select original Game ISO")
            .add_filter("Wii disc image", &["iso"])
            .pick_file()
        else {
            return;
        };

        let (sender, receiver) = mpsc::channel();
        let context = context.clone();
        let worker = thread::Builder::new()
            .name("original-import".to_owned())
            .spawn(move || {
                let progress_sender = sender.clone();
                let result = patcher
                    .import_original(&input, |progress| {
                        let _sent = progress_sender.send(ImportEvent::Progress(progress));
                        context.request_repaint();
                    })
                    .map_err(|error| error.to_string());
                let _sent = sender.send(ImportEvent::Finished(result));
                context.request_repaint();
            });

        match worker {
            Ok(worker) => {
                self.import.begin(receiver);
                drop(worker);
            }
            Err(error) => self
                .import
                .fail(format!("failed to start original import: {error}")),
        }
    }

    fn poll_import(&mut self) {
        if let Some(ImportOutcome::Imported(_game_id)) = self.import.poll() {
            self.state.refresh_originals();
        }
    }
}
