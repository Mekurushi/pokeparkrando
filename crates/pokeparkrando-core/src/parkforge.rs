use std::path::Path;

pub fn check_project<D>(
    project_root: &Path,
    diagnostics: D,
) -> parkforge::Result<parkforge::ProjectCheckReport>
where
    D: for<'a> FnMut(&parkforge::GameId, parkforge::BuildDiagnostic<'a>),
{
    parkforge::check(project_root, diagnostics)
}
