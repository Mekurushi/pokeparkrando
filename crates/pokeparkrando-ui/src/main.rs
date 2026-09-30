use eframe::egui;

mod app;
mod patcher;
mod workspace;

use app::PokeparkRandoApp;

const APP_ID: &str = "pokeparkrando";
const APP_NAME: &str = "Pokepark Archipelago Patcher";
const ICON: &[u8] = include_bytes!("../../../assets/icon.png");

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let icon = eframe::icon_data::from_png_bytes(ICON)?;
    let options = eframe::NativeOptions {
        centered: true,
        viewport: egui::ViewportBuilder::default()
            .with_app_id(APP_ID)
            .with_icon(icon),
        ..Default::default()
    };

    eframe::run_native(
        APP_NAME,
        options,
        Box::new(|context| Ok(Box::new(PokeparkRandoApp::new(context)))),
    )?;
    Ok(())
}
