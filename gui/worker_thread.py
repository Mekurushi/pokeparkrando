from PySide6.QtCore import QThread, Signal

from patcher.models.models import PatchRequest
from patcher.randomizer_service import PatcherService


class PatcherWorkerThread(QThread):

    update_progress = Signal(str, int)  # message, progress
    patching_complete = Signal(object)
    error_occurred = Signal(str)

    def __init__(self, request: PatchRequest):
        super().__init__()
        self.request = request
        self.service = PatcherService()

    def run(self):
        try:
            def progress_callback(message: str, progress: int):
                self.update_progress.emit(message, progress)

            result = self.service.patch(self.request, progress_callback)

            if result.success:
                self.patching_complete.emit(result)
            else:
                self.error_occurred.emit(result.error_message)

        except Exception as e:
            self.error_occurred.emit(f"Unexpected error: {str(e)}")

    def cancel_patching(self):
        self.service.cancel()
