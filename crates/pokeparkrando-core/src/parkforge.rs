use std::path::Path;

use parkforge::RebuildPaths;
pub use parkforge::{
    BuildConfig, BuildConfigValue, BuildDiagnostic, BuildProgress, GameId, RebuildProgress,
};
pub(crate) use parkforge::{
    BuildError, BuildPaths, CheckError, ExtractError, ExtractionProgress, IdentifyError,
    ProjectConfig, ProjectError, RebuildError,
};

pub(crate) fn build_with_paths<P, D>(
    original: &Path,
    shared_sources: &Path,
    revision_sources: &Path,
    destination: &Path,
    config: BuildConfig,
    progress: P,
    diagnostics: D,
) -> Result<(), BuildError>
where
    P: FnMut(BuildProgress),
    D: for<'a> FnMut(BuildDiagnostic<'a>),
{
    parkforge::build_with_paths(
        BuildPaths {
            original,
            shared_sources,
            revision_sources,
            destination,
        },
        config,
        progress,
        diagnostics,
    )
}

pub(crate) fn rebuild_with_paths<P>(
    source: &Path,
    destination: &Path,
    progress: P,
) -> Result<(), RebuildError>
where
    P: FnMut(RebuildProgress),
{
    parkforge::rebuild_from(
        RebuildPaths {
            source,
            destination_iso: destination,
        },
        progress,
    )
}

pub fn check_project<D>(
    project_root: &Path,
    config: &BuildConfig,
    diagnostics: D,
) -> Result<parkforge::ProjectCheckReport, CheckError>
where
    D: for<'a> FnMut(&GameId, BuildDiagnostic<'a>),
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
