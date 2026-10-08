use std::path::PathBuf;
use std::process::ExitCode;

use pokeparkrando_core::{BuildConfig, BuildConfigValue};

fn main() -> ExitCode {
    let project_root = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../bundled-project");
    let config = build_config();
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

#[allow(clippy::too_many_lines)]
fn build_config() -> BuildConfig {
    BuildConfig::from_iter([
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
        (
            "UNLOCK_FAST_TRAVEL_WITH_TAXI_STOP".into(),
            BuildConfigValue::Boolean(true),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_BULBASAUR_ATTRACTION_ID".into(),
            BuildConfigValue::Integer(0xf),
        ),
        (
            "MEADOW_ZONE_VENUSAUR_AREA_VENUSAUR_ATTRACTION_ID".into(),
            BuildConfigValue::Integer(0x2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION_ZONE".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION_AREA".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION_POSITION".into(),
            BuildConfigValue::Integer(0),
        ),
        (
            "MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE_ZONE".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE_AREA".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE_POSITION".into(),
            BuildConfigValue::Integer(0),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE_ZONE".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE_AREA".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE_POSITION".into(),
            BuildConfigValue::Integer(0),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE_ZONE".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE_AREA".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE_POSITION".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(5),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(3),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(3),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(4),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(4),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(5),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(6),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(1),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL_ZONE".into(),
            BuildConfigValue::Integer(6),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL_AREA".into(),
            BuildConfigValue::Integer(2),
        ),
        (
            "MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL_POSITION".into(),
            BuildConfigValue::Integer(1),
        ),
    ])
}
