use std::collections::VecDeque;
use std::path::Path;
use std::sync::mpsc;
use std::thread;

use eframe::egui;
use rfd::FileDialog;

use super::import::{ImportEvent, ImportFailure, ImportOutcome, ImportProgressView, ImportState};
use super::patch::{PatchEvent, PatchFailure, PatchOutcome, PatchProgressView, PatchState};
use super::patch_file::PatchFileState;
use super::state::{PatcherState, ReadinessFailure};
use super::view::{PatcherAction, PatcherView};

pub(crate) struct PatcherComponent {
    state: PatcherState,
    import: ImportState,
    patch: PatchState,
    patch_file: Option<PatchFileState>,
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
    Patch(pokeparkrando_core::BuildPatchError),
    ReadPatchFile(pokeparkrando_core::ReadAppkprkError),
    StartImport(std::io::Error),
    StartPatch(std::io::Error),
    ImportStopped,
    PatchStopped,
}

impl PatcherComponent {
    pub(crate) fn new(workspace_root: Option<&Path>) -> Self {
        let (state, pending_errors) = Self::load_state(workspace_root);
        Self {
            state,
            import: ImportState::default(),
            patch: PatchState::default(),
            patch_file: None,
            pending_errors,
        }
    }

    pub(crate) fn load(&mut self, workspace_root: Option<&Path>) {
        (self.state, self.pending_errors) = Self::load_state(workspace_root);
        self.import = ImportState::default();
        self.patch = PatchState::default();
    }

    pub(crate) fn is_busy(&self) -> bool {
        self.import.is_importing() || self.patch.is_patching()
    }

    pub(crate) fn show(&mut self, ui: &mut egui::Ui) -> Option<PatcherEvent> {
        let event = self
            .pending_errors
            .pop_front()
            .map(PatcherEvent::Error)
            .or_else(|| self.poll_import())
            .or_else(|| self.poll_patch());
        let action =
            PatcherView::new(&self.state, self.patch_file.as_ref()).show(ui, !self.is_busy());
        if self.state.is_ready() {
            ImportProgressView::new(&self.import).show(ui);
            PatchProgressView::new(&self.patch).show(ui);
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
            PatcherAction::SelectPatchFile => self.choose_patch_file(),
            PatcherAction::Patch(game_id) => self.choose_patch_destination(game_id, context),
        }
    }

    fn choose_patch_destination(
        &mut self,
        game_id: pokeparkrando_core::GameId,
        context: &egui::Context,
    ) -> Option<PatcherEvent> {
        let patch_file = self.patch_file.as_ref()?;
        let patcher = self.state.patcher_handle()?;
        let stem = patch_file.path().file_stem().map_or_else(
            || "Pokepark".to_owned(),
            |stem| stem.to_string_lossy().into_owned(),
        );
        let iso_name = format!("Pokepark {stem}.iso");
        let dialog = FileDialog::new()
            .set_title("Save patched ISO")
            .add_filter("Wii disc image", &["iso"])
            .set_file_name(iso_name)
            .set_directory(patcher.workspace_root());
        let destination = dialog.save_file()?;

        self.start_patch(game_id, destination, context)
    }

    fn start_patch(
        &mut self,
        game_id: pokeparkrando_core::GameId,
        destination: std::path::PathBuf,
        context: &egui::Context,
    ) -> Option<PatcherEvent> {
        let patcher = self.state.patcher_handle()?;
        let appkprk = self.patch_file.as_ref()?.contents().clone();
        let (sender, receiver) = mpsc::channel();
        let context = context.clone();
        let worker = thread::Builder::new()
            .name("iso-patch".to_owned())
            .spawn(move || {
                let progress_sender = sender.clone();
                let result = patcher.patch_to_iso(
                    &game_id,
                    &appkprk,
                    &destination,
                    |progress| {
                        let _sent = progress_sender.send(PatchEvent::Progress(progress));
                        context.request_repaint();
                    },
                    |_diagnostic| {},
                );
                let _sent = sender.send(PatchEvent::Finished(result));
                context.request_repaint();
            });

        match worker {
            Ok(worker) => {
                self.patch.begin(receiver);
                drop(worker);
                None
            }
            Err(error) => Some(PatcherEvent::Error(PatcherError::StartPatch(error))),
        }
    }

    fn choose_patch_file(&mut self) -> Option<PatcherEvent> {
        let path = FileDialog::new()
            .set_title("Select patch file")
            .add_filter("PokePark patch file", &["appkprk"])
            .pick_file()?;
        match PatchFileState::read(path) {
            Ok(patch_file) => {
                self.patch_file = Some(patch_file);
                None
            }
            Err(error) => Some(PatcherEvent::Error(PatcherError::ReadPatchFile(error))),
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

    fn poll_patch(&mut self) -> Option<PatcherEvent> {
        match self.patch.poll() {
            Some(PatchOutcome::Patched(_destination)) => None,
            Some(PatchOutcome::Failed(PatchFailure::Patch(error))) => {
                Some(PatcherEvent::Error(PatcherError::Patch(error)))
            }
            Some(PatchOutcome::Failed(PatchFailure::Disconnected)) => {
                Some(PatcherEvent::Error(PatcherError::PatchStopped))
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
