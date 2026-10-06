use std::sync::mpsc;
use std::thread;

use eframe::egui;
use semver::Version;
use thiserror::Error;

use super::state::{PollResult, UpdaterState};
use super::view::{UpdaterAction, UpdaterView};

const REPOSITORY_OWNER: &str = "Mekurushi";
const REPOSITORY_NAME: &str = "pokeparkrando";

#[derive(Default)]
pub(crate) struct UpdaterComponent {
    open: bool,
    state: UpdaterState,
}

pub(crate) enum UpdaterEvent {
    Error(UpdaterError),
    VersionSelected(String),
}

#[derive(Debug, Error)]
pub(crate) enum UpdaterError {
    #[error("could not start the version-check worker: {0}")]
    Start(#[source] std::io::Error),
    #[error("could not fetch GitHub releases: {0}")]
    Fetch(#[source] self_update::Error),
    #[error("the version-check worker stopped before returning a result")]
    Stopped,
}

impl UpdaterComponent {
    pub(crate) fn open(&mut self, context: &egui::Context) -> Option<UpdaterEvent> {
        self.open = true;
        self.start_fetch(context)
    }

    pub(crate) fn show(&mut self, context: &egui::Context) -> Option<UpdaterEvent> {
        let event = match self.state.poll() {
            Some(PollResult::Failed(error)) => {
                self.open = false;
                Some(UpdaterEvent::Error(UpdaterError::Fetch(error)))
            }
            Some(PollResult::Disconnected) => {
                self.open = false;
                Some(UpdaterEvent::Error(UpdaterError::Stopped))
            }
            Some(PollResult::Loaded) | None => None,
        };

        if self.open {
            match UpdaterView::new(&self.state).show(context) {
                Some(UpdaterAction::Close) => self.open = false,
                Some(UpdaterAction::Refresh) => return self.start_fetch(context).or(event),
                Some(UpdaterAction::Select(version)) => self.state.select(version),
                Some(UpdaterAction::CancelSelection) => self.state.cancel_selection(),
                Some(UpdaterAction::ConfirmSelection) => {
                    let version = self.state.selected_version()?.to_owned();
                    self.state.cancel_selection();
                    self.open = false;
                    return Some(UpdaterEvent::VersionSelected(version));
                }
                None => {}
            }
        }

        event
    }

    fn start_fetch(&mut self, context: &egui::Context) -> Option<UpdaterEvent> {
        let (sender, receiver) = mpsc::channel();
        let context = context.clone();
        let worker = thread::Builder::new()
            .name("release-list".to_owned())
            .spawn(move || {
                let result = fetch_versions();
                let _sent = sender.send(result);
                context.request_repaint();
            });

        match worker {
            Ok(worker) => {
                self.state.begin(receiver);
                drop(worker);
                None
            }
            Err(error) => {
                self.open = false;
                Some(UpdaterEvent::Error(UpdaterError::Start(error)))
            }
        }
    }
}

fn fetch_versions() -> Result<Vec<String>, self_update::Error> {
    self_update::backends::github::ReleaseList::configure()
        .repo_owner(REPOSITORY_OWNER)
        .repo_name(REPOSITORY_NAME)
        .build()?
        .fetch()
        .map(|releases| {
            releases
                .into_iter()
                .filter(|release| is_visible_version(release.version()))
                .map(|release| release.version().to_owned())
                .collect()
        })
}

fn is_visible_version(raw: &str) -> bool {
    Version::parse(raw)
        .is_ok_and(|version| version.pre.is_empty() && version > Version::new(1, 2, 4))
}
