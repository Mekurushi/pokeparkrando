use std::sync::mpsc;
use std::thread;

use eframe::egui;
use semver::Version;
use thiserror::Error;

use super::state::{InstallEvent, PollResult, UpdaterState};
use super::view::{UpdaterAction, UpdaterView};

const REPOSITORY_OWNER: &str = "Mekurushi";
const REPOSITORY_NAME: &str = "pokeparkrando";
const BIN_NAME: &str = "pokeparkrando";
const ASSET_NAME_WINDOWS: &str = "pokeparkrando-windows-x86_64.zip";
const UPDATE_PUBLIC_KEY: self_update::VerifyingKey =
    *include_bytes!("../../../../assets/pokeparkrando-public.key");

#[derive(Default)]
pub(crate) struct UpdaterComponent {
    open: bool,
    state: UpdaterState,
}

pub(crate) enum UpdaterEvent {
    Error(UpdaterError),
    Installed(String),
    CloseApplication,
}

#[derive(Debug, Error)]
pub(crate) enum UpdaterError {
    #[error("could not start the version-check worker: {0}")]
    Start(#[source] std::io::Error),
    #[error("could not fetch GitHub releases: {0}")]
    Fetch(#[source] self_update::Error),
    #[error("the version-check worker stopped before returning a result")]
    FetchStopped,
    #[error("could not start the update worker: {0}")]
    StartInstall(#[source] std::io::Error),
    #[error("self-update is not supported on {os} {arch}")]
    UnsupportedPlatform {
        os: &'static str,
        arch: &'static str,
    },
    #[error("could not install the selected version: {0}")]
    Install(#[source] self_update::Error),
    #[error("the update worker stopped before returning a result")]
    InstallStopped,
}

impl UpdaterComponent {
    pub(crate) fn open(&mut self, context: &egui::Context) -> Option<UpdaterEvent> {
        self.open = true;
        self.start_fetch(context)
    }

    pub(crate) fn show(&mut self, context: &egui::Context) -> Option<UpdaterEvent> {
        let event = match self.state.poll().or_else(|| self.state.poll_install()) {
            Some(PollResult::FetchFailed(error)) => {
                self.open = false;
                Some(UpdaterEvent::Error(UpdaterError::Fetch(error)))
            }
            Some(PollResult::FetchDisconnected) => {
                self.open = false;
                Some(UpdaterEvent::Error(UpdaterError::FetchStopped))
            }
            Some(PollResult::Installed(version)) => Some(UpdaterEvent::Installed(version)),
            Some(PollResult::InstallFailed(error)) => {
                self.open = false;
                Some(UpdaterEvent::Error(UpdaterError::Install(error)))
            }
            Some(PollResult::InstallDisconnected) => {
                self.open = false;
                Some(UpdaterEvent::Error(UpdaterError::InstallStopped))
            }
            Some(PollResult::Loaded) | None => None,
        };

        if self.open {
            match UpdaterView::new(&self.state).show(context) {
                Some(UpdaterAction::Close) => self.open = false,
                Some(UpdaterAction::CloseApplication) => {
                    return Some(UpdaterEvent::CloseApplication);
                }
                Some(UpdaterAction::Refresh) => return self.start_fetch(context).or(event),
                Some(UpdaterAction::Select(version)) => self.state.select(version),
                Some(UpdaterAction::CancelSelection) => self.state.cancel_selection(),
                Some(UpdaterAction::ConfirmSelection) => {
                    let version = self.state.selected_version()?.to_owned();
                    return self.start_install(version, context).or(event);
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

    fn start_install(&mut self, version: String, context: &egui::Context) -> Option<UpdaterEvent> {
        let Some(asset_name) = target_asset_name() else {
            return Some(UpdaterEvent::Error(UpdaterError::UnsupportedPlatform {
                os: std::env::consts::OS,
                arch: std::env::consts::ARCH,
            }));
        };
        let (sender, receiver) = mpsc::channel();
        let worker_version = version.clone();
        let context = context.clone();
        let worker = thread::Builder::new()
            .name("self-update".to_owned())
            .spawn(move || {
                let progress_sender = sender.clone();
                let progress_context = context.clone();
                let result =
                    install_version(&worker_version, asset_name, move |downloaded, total| {
                        let _sent =
                            progress_sender.send(InstallEvent::Progress { downloaded, total });
                        progress_context.request_repaint();
                    });
                let _sent = sender.send(InstallEvent::Finished(result));
                context.request_repaint();
            });

        match worker {
            Ok(worker) => {
                self.state.begin_install(version, receiver);
                drop(worker);
                None
            }
            Err(error) => Some(UpdaterEvent::Error(UpdaterError::StartInstall(error))),
        }
    }
}

fn install_version(
    version: &str,
    asset_name: &'static str,
    progress: impl Fn(u64, Option<u64>) + Send + Sync + 'static,
) -> Result<(), self_update::Error> {
    let mut builder = self_update::backends::github::Update::configure();
    let _builder = builder
        .repo_owner(REPOSITORY_OWNER)
        .repo_name(REPOSITORY_NAME)
        .bin_name(BIN_NAME)
        .release_tag(version)
        .current_version(env!("CARGO_PKG_VERSION"))
        .asset_matcher(move |assets| {
            assets
                .iter()
                .find(|asset| asset.name() == asset_name)
                .cloned()
        })
        .verifying_keys([UPDATE_PUBLIC_KEY])
        .check_install_path_writable(true)
        .progress_callback(progress)
        .unattended();

    let _status = builder.build()?.update()?;
    Ok(())
}

fn target_asset_name() -> Option<&'static str> {
    match (std::env::consts::OS, std::env::consts::ARCH) {
        ("windows", "x86_64") => Some(ASSET_NAME_WINDOWS),
        _ => None,
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
    // 1.2.4 and lower are the old patcher that don't support the self-updating
    Version::parse(raw)
        .is_ok_and(|version| version.pre.is_empty() && version > Version::new(1, 2, 4))
}
