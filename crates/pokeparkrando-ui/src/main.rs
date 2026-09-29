use eframe::egui;

const APP_NAME: &str = "Pokepark Archipelago Patcher";
const ICON: &[u8] = include_bytes!("../../../assets/icon.png");

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let icon = eframe::icon_data::from_png_bytes(ICON)?;
    let options = eframe::NativeOptions {
        centered: true,
        viewport: egui::ViewportBuilder::default().with_icon(icon),
        ..Default::default()
    };

    eframe::run_native(
        APP_NAME,
        options,
        Box::new(|_context| Ok(Box::new(PokeparkRandoApp))),
    )?;
    Ok(())
}

struct PokeparkRandoApp;

impl eframe::App for PokeparkRandoApp {
    fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {
        let _panel = egui::CentralPanel::default().show(ui, |ui| {
            let _heading = ui.heading(APP_NAME);
            let _label = ui.label("import prototype WIP");
        });
    }
}
