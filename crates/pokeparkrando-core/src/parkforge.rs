use std::path::Path;

pub use parkforge::{BuildConfig, BuildConfigValue, GameId};

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
