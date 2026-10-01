use std::collections::VecDeque;
use std::path::Path;
use std::sync::mpsc;
use std::thread;

use eframe::egui;
use rfd::FileDialog;

use super::import::{ImportEvent, ImportFailure, ImportOutcome, ImportProgressView, ImportState};
use super::state::{PatcherState, ReadinessFailure};
use super::view::{PatcherAction, PatcherView};

pub(crate) struct PatcherComponent {
    state: PatcherState,
    import: ImportState,
    pending_errors: VecDeque<PatcherError>,
}

pub(crate) enum PatcherEvent {
    Error(PatcherError),
}

pub(crate) enum PatcherError {
    Load(pokeparkrando_core::BundledProjectError),
    Readiness {
        game_id: pokeparkrando_core::GameId,
        source: std::io::Error,
    },
    Import(pokeparkrando_core::ImportOriginalError),
    StartImport(std::io::Error),
    ImportStopped,
}

impl PatcherComponent {
    pub(crate) fn new(workspace_root: Option<&Path>) -> Self {
        let (state, pending_errors) = Self::load_state(workspace_root);
        Self {
            state,
            import: ImportState::default(),
            pending_errors,
        }
    }

    pub(crate) fn load(&mut self, workspace_root: Option<&Path>) {
        (self.state, self.pending_errors) = Self::load_state(workspace_root);
        self.import = ImportState::default();
    }

    pub(crate) fn is_busy(&self) -> bool {
        self.import.is_importing()
    }

    pub(crate) fn show(&mut self, ui: &mut egui::Ui) -> Option<PatcherEvent> {
        let event = self
            .pending_errors
            .pop_front()
            .map(PatcherEvent::Error)
            .or_else(|| self.poll_import());
        let action = PatcherView::new(&self.state).show(ui, !self.is_busy());
        if self.state.is_ready() {
            ImportProgressView::new(&self.import).show(ui);
        }
        event.or_else(|| action.and_then(|action| self.handle_action(action, ui.ctx())))
    }

    fn handle_action(
        &mut self,
        action: PatcherAction,
        context: &egui::Context,
    ) -> Option<PatcherEvent> {
        match action {
            PatcherAction::ImportOriginal => self.choose_original(context),
        }
    }

    fn choose_original(&mut self, context: &egui::Context) -> Option<PatcherEvent> {
        let patcher = self.state.patcher_handle()?;
        let input = FileDialog::new()
            .set_title("Select original Game ISO")
            .add_filter("Wii disc image", &["iso"])
            .pick_file()?;

        let (sender, receiver) = mpsc::channel();
        let context = context.clone();
        let worker = thread::Builder::new()
            .name("original-import".to_owned())
            .spawn(move || {
                let progress_sender = sender.clone();
                let result = patcher.import_original(&input, |progress| {
                    let _sent = progress_sender.send(ImportEvent::Progress(progress));
                    context.request_repaint();
                });
                let _sent = sender.send(ImportEvent::Finished(result));
                context.request_repaint();
            });

        match worker {
            Ok(worker) => {
                self.import.begin(receiver);
                drop(worker);
                None
            }
            Err(error) => Some(PatcherEvent::Error(PatcherError::StartImport(error))),
        }
    }

    fn poll_import(&mut self) -> Option<PatcherEvent> {
        match self.import.poll() {
            Some(ImportOutcome::Imported(_game_id)) => {
                let failures = self.state.refresh_originals();
                self.pending_errors
                    .extend(failures.into_iter().map(Self::readiness_error));
                self.pending_errors.pop_front().map(PatcherEvent::Error)
            }
            Some(ImportOutcome::Failed(ImportFailure::Import(error))) => {
                Some(PatcherEvent::Error(PatcherError::Import(error)))
            }
            Some(ImportOutcome::Failed(ImportFailure::Disconnected)) => {
                Some(PatcherEvent::Error(PatcherError::ImportStopped))
            }
            None => None,
        }
    }

    fn load_state(workspace_root: Option<&Path>) -> (PatcherState, VecDeque<PatcherError>) {
        let Some(workspace_root) = workspace_root else {
            return (PatcherState::Unavailable, VecDeque::new());
        };
        match PatcherState::load(workspace_root) {
            Ok((state, failures)) => (
                state,
                failures.into_iter().map(Self::readiness_error).collect(),
            ),
            Err(error) => (
                PatcherState::Failed,
                VecDeque::from([PatcherError::Load(error)]),
            ),
        }
    }

    fn readiness_error(failure: ReadinessFailure) -> PatcherError {
        PatcherError::Readiness {
            game_id: failure.game_id,
            source: failure.source,
        }
    }
}
