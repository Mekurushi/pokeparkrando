use std::path::Path;

pub use parkforge::{BuildConfig, BuildConfigValue, GameId};
pub(crate) use parkforge::{
    CheckError, ExtractError, ExtractionProgress, IdentifyError, ProjectConfig, ProjectError,
};

pub fn check_project<D>(
    project_root: &Path,
    config: &BuildConfig,
    diagnostics: D,
) -> Result<parkforge::ProjectCheckReport, CheckError>
where
    D: for<'a> FnMut(&GameId, parkforge::BuildDiagnostic<'a>),
{
    parkforge::check_with_config(project_root, config, diagnostics)
}

pub(crate) fn identify(input_iso: &Path) -> Result<GameId, IdentifyError> {
    parkforge::identify(input_iso)
}

pub(crate) fn extract_to<F>(
    input_iso: &Path,
    destination: &Path,
    progress: F,
) -> Result<GameId, ExtractError>
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
