use eframe::egui;

mod app;
mod error;
mod patcher;
mod ui;
mod updater;
mod workspace;

use app::PokeparkRandoApp;

const APP_ID: &str = "pokeparkrando";
const APP_TITLE: &str = concat!(
    "Pokepark Archipelago Patcher Version ",
    env!("CARGO_PKG_VERSION")
);
const ICON: &[u8] = include_bytes!("../../../assets/icon.png");

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let icon = eframe::icon_data::from_png_bytes(ICON)?;
    let options = eframe::NativeOptions {
        centered: true,
        viewport: egui::ViewportBuilder::default()
            .with_app_id(APP_ID)
            .with_title(APP_TITLE)
            .with_icon(icon),
        ..Default::default()
    };

    eframe::run_native(
        APP_TITLE,
        options,
        Box::new(|context| Ok(Box::new(PokeparkRandoApp::new(context)))),
    )?;
    Ok(())
}
