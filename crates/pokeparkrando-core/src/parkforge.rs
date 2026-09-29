use std::path::Path;

pub use parkforge::{BuildConfig, BuildConfigValue, GameId};
pub(crate) use parkforge::{Error, ExtractionProgress, ProjectConfig, ProjectError};

pub fn check_project<D>(
    project_root: &Path,
    config: &BuildConfig,
    diagnostics: D,
) -> parkforge::Result<parkforge::ProjectCheckReport>
where
    D: for<'a> FnMut(&GameId, parkforge::BuildDiagnostic<'a>),
{
    parkforge::check_with_config(project_root, config, diagnostics)
}

pub(crate) fn identify(input_iso: &Path) -> parkforge::Result<GameId> {
    parkforge::identify(input_iso)
}

pub(crate) fn extract_to<F>(
    input_iso: &Path,
    destination: &Path,
    progress: F,
) -> parkforge::Result<GameId>
where
    F: FnMut(ExtractionProgress),
{
    parkforge::extract_to(
        parkforge::ExtractionPaths {
            input_iso,
            destination,
        },
        progress,
    )
}
