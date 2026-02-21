import sys
from PySide6.QtWidgets import QApplication

from gui.main_window import RandoGUI


def run_gui():
    try:
        app = QApplication(sys.argv)

        app.setApplicationName("PokéPark Randomizer Patcher")

        app.setStyleSheet("""
            QMainWindow {
                background-color: #ecf0f1;
            }
            QWidget {
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel {
                color: #2c3e50;
            }
        """)

        window = RandoGUI()
        window.show()

        return app.exec()

    except Exception as e:
        print(f"Failed to start GUI: {e}")
        import traceback
        traceback.print_exc()

        try:
            app = QApplication.instance() or QApplication(sys.argv)
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(
                None,
                "Startup Error",
                f"Failed to start PokéPark Randomizer Patcher:\n\n{e}\n\n"
                "Please check that all required dependencies are installed."
            )
        except Exception:
            pass

        return 1




def main():
        return run_gui()


if __name__ == "__main__":
    sys.exit(main())