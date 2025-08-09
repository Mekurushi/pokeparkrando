from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QProgressBar,
    QWidget,
)
from pathlib import Path
import os


from gui.worker_thread import PatcherWorkerThread
from patcher.config.config import get_default_patch_configs
from patcher.models.models import PatchRequest, PatchResult


class RandoGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PokéPark Randomizer Patcher")
        self.setFixedSize(700, 450)
        self.patcher_thread = None
        self.iso_path = ""
        self.appkprk_path = ""
        self.output_path = str(Path.cwd())
        self.patch_configs = get_default_patch_configs()
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)

        # Title
        title_label = QLabel("PokéPark Randomizer Patcher")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 28px; 
            font-weight: bold; 
            margin: 20px;
            color: #2c3e50;
        """)
        main_layout.addWidget(title_label)

        # ISO Selection
        iso_group = QWidget()
        iso_layout = QHBoxLayout(iso_group)
        iso_label = QLabel("ISO File:")
        iso_label.setMinimumWidth(80)
        iso_label.setStyleSheet("font-weight: bold;")

        self.iso_line_edit = QLineEdit()
        self.iso_line_edit.setPlaceholderText("Select PokéPark ISO file...")
        self.iso_line_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 4px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
        """)

        iso_browse_btn = QPushButton("Browse")
        iso_browse_btn.setStyleSheet(self._get_button_style("#3498db"))
        iso_browse_btn.clicked.connect(self.browse_iso)

        iso_layout.addWidget(iso_label)
        iso_layout.addWidget(self.iso_line_edit)
        iso_layout.addWidget(iso_browse_btn)
        main_layout.addWidget(iso_group)

        # .appokprk Selection
        appokprk_group = QWidget()
        appokprk_layout = QHBoxLayout(appokprk_group)
        appokprk_label = QLabel("Patch File:")
        appokprk_label.setMinimumWidth(80)
        appokprk_label.setStyleSheet("font-weight: bold;")

        self.appkprk_line_edit = QLineEdit()
        self.appkprk_line_edit.setPlaceholderText("Select .appokprk patch file...")
        self.appkprk_line_edit.setStyleSheet(self.iso_line_edit.styleSheet())

        appokprk_browse_btn = QPushButton("Browse")
        appokprk_browse_btn.setStyleSheet(self._get_button_style("#3498db"))
        appokprk_browse_btn.clicked.connect(self.browse_appokprk)

        appokprk_layout.addWidget(appokprk_label)
        appokprk_layout.addWidget(self.appkprk_line_edit)
        appokprk_layout.addWidget(appokprk_browse_btn)
        main_layout.addWidget(appokprk_group)

        # Output File
        output_group = QWidget()
        output_layout = QHBoxLayout(output_group)
        output_label = QLabel("Output:")
        output_label.setMinimumWidth(80)
        output_label.setStyleSheet("font-weight: bold;")

        self.output_line_edit = QLineEdit()
        self.output_line_edit.setText(self.output_path)
        self.output_line_edit.setStyleSheet(self.iso_line_edit.styleSheet())

        output_browse_btn = QPushButton("Browse")
        output_browse_btn.setStyleSheet(self._get_button_style("#3498db"))
        output_browse_btn.clicked.connect(self.browse_output)

        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_line_edit)
        output_layout.addWidget(output_browse_btn)
        main_layout.addWidget(output_group)

        # Spacer
        main_layout.addStretch()

        # Progress section
        progress_group = QWidget()
        progress_layout = QVBoxLayout(progress_group)

        self.progress_label = QLabel("")
        self.progress_label.setVisible(False)
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_label.setStyleSheet("""
            font-size: 14px;
            color: #2c3e50;
            margin: 5px;
        """)
        progress_layout.addWidget(self.progress_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
                height: 25px;
            }
            QProgressBar::chunk {
                background-color: #27ae60;
                border-radius: 6px;
            }
        """)
        progress_layout.addWidget(self.progress_bar)

        main_layout.addWidget(progress_group)

        # Main button
        self.patching_btn = QPushButton("Start Patching")
        self.patching_btn.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                font-weight: bold;
                padding: 15px;
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 8px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
                color: #7f8c8d;
            }
        """)
        self.patching_btn.clicked.connect(self.start_patching)
        main_layout.addWidget(self.patching_btn)

    def _get_button_style(self, color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self._darken_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self._darken_color(color, 0.8)};
            }}
        """

    def _darken_color(self, color, factor=0.9):
        if color.startswith('#'):
            color = color[1:]
        rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
        darkened = tuple(int(c * factor) for c in rgb)
        return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"

    def browse_iso(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select PokéPark ISO",
            "",
            "ISO Files (*.iso);;All Files (*)"
        )

        if file_path:
            if not Path(file_path).exists():
                QMessageBox.warning(self, "Error", "Selected file does not exist!")
                return

            file_size = Path(file_path).stat().st_size
            if file_size < 1024 * 1024 * 100:
                result = QMessageBox.question(
                    self,
                    "Small File Warning",
                    f"The selected file is only {file_size // (1024 * 1024)}MB. "
                    "Are you sure this is a valid PokéPark ISO?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if result == QMessageBox.StandardButton.No:
                    return

            self.iso_path = file_path
            self.iso_line_edit.setText(file_path)

    def browse_output(self):
        default_dir = Path.cwd()  # Current working directory

        # Let user select folder instead of specific file
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder",
            str(default_dir),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )

        if folder_path:
            self.output_path = folder_path
            self.output_line_edit.setText(folder_path)
    def browse_appokprk(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select .appkprk Patch File",
            "",
            "PokéPark Patch Files (*.appkprk);;All Files (*)"
        )

        if file_path:
            if not Path(file_path).exists():
                QMessageBox.warning(self, "Error", "Selected patch file does not exist!")
                return

            self.appkprk_path = file_path
            self.appkprk_line_edit.setText(file_path)
    def start_patching(self):
        # Validation
        if not self._validate_inputs():
            return

        if not self._confirm_randomization():
            return

        self._set_ui_patching_state(True)

        request = PatchRequest(
            iso_path=self.iso_path,
            appkprk_path=self.appkprk_path,
            output_path=self.output_path,
            patch_configs=self.patch_configs
        )

        # Start worker thread
        self.patcher_thread = PatcherWorkerThread(request)
        self.patcher_thread.update_progress.connect(self.update_progress)
        self.patcher_thread.patching_complete.connect(self.on_patching_complete)
        self.patcher_thread.error_occurred.connect(self.on_error)
        self.patcher_thread.start()

    def _validate_inputs(self) -> bool:
        """Validate user inputs"""
        if not self.iso_path:
            QMessageBox.warning(self, "Error", "Please select an ISO file first!")
            return False

        if not Path(self.iso_path).exists():
            QMessageBox.warning(self, "Error", "Selected ISO file does not exist!")
            return False

        if not self.appkprk_path:
            QMessageBox.warning(self, "Error", "Please select an .appkprk file first!")
            return False

        if not Path(self.appkprk_path).exists():
            QMessageBox.warning(self, "Error", "Selected .appkprk file does not exist!")
            return False

        self.output_path = self.output_line_edit.text().strip()
        if not self.output_path:
            QMessageBox.warning(self, "Error", "Please specify an output file!")
            return False

        output_path = Path(self.output_path)
        self.output_path = str(output_path)
        self.output_line_edit.setText(self.output_path)

        output_dir = output_path.parent
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            test_file = output_dir / f"test_write_{os.getpid()}.tmp"
            test_file.touch()
            test_file.unlink()
        except Exception as e:
            QMessageBox.warning(
                self,
                "Output Directory Error",
                f"Cannot write to output directory:\n{output_dir}\n\nError: {e}"
            )
            return False

        return True

    def _confirm_randomization(self) -> bool:
        """Show confirmation dialog"""
        confirm_msg = (
            f"Ready to randomize:\n\n"
            f"Input: {Path(self.iso_path).name}\n"
            f"Output: {Path(self.output_path).name}\n\n"
            f"This process may take several minutes. Continue?"
        )

        result = QMessageBox.question(
            self,
            "Confirm Randomization",
            confirm_msg,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        return result == QMessageBox.StandardButton.Yes

    def _set_ui_patching_state(self, randomizing: bool):
        if randomizing:
            self.patching_btn.setEnabled(False)
            self.patching_btn.setText("Patching...")
            self.progress_bar.setVisible(True)
            self.progress_bar.setValue(0)
            self.progress_label.setVisible(True)
            self.progress_label.setText("Initializing...")
        else:
            self.patching_btn.setEnabled(True)
            self.patching_btn.setText("Start Patching")
            self.progress_bar.setVisible(False)
            self.progress_label.setVisible(False)
            self.setWindowTitle("PokéPark Randomizer Patcher")

    def update_progress(self, message: str, progress: int):
        self.progress_label.setText(message)
        self.progress_bar.setValue(progress)
        self.setWindowTitle(f"PokéPark Randomizer Patcher - {progress}% Complete")

    def on_patching_complete(self, result: PatchResult):
        self._set_ui_patching_state(False)

        try:
            original_size = Path(self.iso_path).stat().st_size
            new_size = Path(result.output_path).stat().st_size
            size_info = (
                f"\n\nFile sizes:\n"
                f"Original: {original_size // (1024 * 1024)} MB\n"
                f"Randomized: {new_size // (1024 * 1024)} MB"
            )
        except Exception:
            size_info = ""

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Randomization Complete!")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(
            f"PokéPark randomization patch completed successfully!\n\n"
            f"Output saved to:\n{result.output_path}{size_info}"
        )

        open_folder_btn = msg_box.addButton("Open Folder", QMessageBox.ButtonRole.ActionRole)
        ok_btn = msg_box.addButton(QMessageBox.StandardButton.Ok)

        msg_box.exec()

        if msg_box.clickedButton() == open_folder_btn:
            self._open_output_folder(result.output_path)

        self.patcher_thread = None

    def _open_output_folder(self, output_path: str):
        try:
            import subprocess
            import platform

            output_dir = Path(output_path).parent
            if platform.system() == "Windows":
                subprocess.run(['explorer', str(output_dir)])
            elif platform.system() == "Darwin":
                subprocess.run(['open', str(output_dir)])
            else:
                subprocess.run(['xdg-open', str(output_dir)])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not open folder: {e}")

    def on_error(self, error_message: str):
        self._set_ui_patching_state(False)

        troubleshooting_tips = (
            "\n\nTroubleshooting tips:\n"
            "• Ensure the ISO file is a valid PokéPark game\n"
            "• Check that you have sufficient disk space\n"
            "• Try running as administrator if permission errors occur\n"
            "• Close other programs that might be using the files\n"
            "• Try a different output location\n"
        )

        error_dialog = QMessageBox(self)
        error_dialog.setWindowTitle("Patching Failed")
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setText(f"Patching failed:\n\n{error_message}{troubleshooting_tips}")

        copy_btn = error_dialog.addButton("Copy Error", QMessageBox.ButtonRole.ActionRole)
        ok_btn = error_dialog.addButton(QMessageBox.StandardButton.Ok)

        error_dialog.exec()

        if error_dialog.clickedButton() == copy_btn:
            try:
                QApplication.clipboard().setText(f"PokéPark Randomizer Error:\n{error_message}")
                QMessageBox.information(self, "Copied", "Error message copied to clipboard.")
            except Exception:
                pass

        self.patcher_thread = None

    def closeEvent(self, event):
        if self.patcher_thread and self.patcher_thread.isRunning():
            result = QMessageBox.question(
                self,
                "Patching in Progress",
                "Patching is currently running. Do you want to cancel and exit?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if result == QMessageBox.StandardButton.Yes:
                self.patcher_thread.cancel_patching()
                self.progress_label.setText("Canceling...")

                if not self.patcher_thread.wait(5000):
                    self.patcher_thread.terminate()
                    self.patcher_thread.wait()

                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
