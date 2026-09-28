use std::path::PathBuf;
use std::process::ExitCode;

use pokeparkrando_core::{BuildConfig, BuildConfigValue};

fn main() -> ExitCode {
    let project_root = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../bundled-project");
    let config = BuildConfig::from_iter([
        ("BATTLE_COUNT".into(), BuildConfigValue::Integer(5)),
        (
            "PLAYER_NAME".into(),
            BuildConfigValue::String("Player1".into()),
        ),
        (
            "SHOULD_PRINT_AP_BUFFER".into(),
            BuildConfigValue::Boolean(true),
        ),
        ("FPS_ENHANCEMENT".into(), BuildConfigValue::Boolean(true)),
    ]);
    let report =
        match pokeparkrando_core::check_project(&project_root, &config, |game_id, diagnostic| {
            eprintln!(
                "{game_id}: {:?}: {} ({})",
                diagnostic.severity,
                diagnostic.message,
                diagnostic.source_path.display()
            );
        }) {
            Ok(report) => report,
            Err(error) => {
                eprintln!("Failed to check bundled project: {error}");
                return ExitCode::FAILURE;
            }
        };

    for revision in report.revisions() {
        match revision.result() {
            Ok(report) => {
                for error in report.errors() {
                    eprintln!("{}: {error}", revision.game_id());
                }
            }
            Err(error) => eprintln!("{}: {error}", revision.game_id()),
        }
    }

    if report.is_success() {
        eprintln!("Bundled project check succeeded");
        ExitCode::SUCCESS
    } else {
        ExitCode::FAILURE
    }
}
