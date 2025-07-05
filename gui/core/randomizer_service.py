import shutil
import time
from pathlib import Path
from typing import List

import disc_riider_py

from gui.core.models import PatchRequest, ProgressCallback, PatchResult, FilePatchConfig
from gui.core.patchers import PatcherFactory


class PatcherService:

    def __init__(self):
        self.base_work_dir = Path("pokepark_randomizer_temp")
        self.extract_dir = self.base_work_dir / "iso_extracted"
        self.patcher_work_dir = self.base_work_dir / "patcher_work"
        self._canceled = False

    def patch(self, request: PatchRequest, progress_callback: ProgressCallback) -> PatchResult:
        try:
            self._canceled = False
            self._setup_working_directories()

            # Step 1: Extract ISO (0-20%)
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")

            self._extract_iso(request.iso_path, progress_callback)

            # Step 2: Apply all configured patches (20-80%)
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")

            patches_applied = self._apply_all_patches(request.patch_configs, progress_callback)

            # Step 3: Rebuild ISO (80-95%)
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")

            final_output = self._rebuild_iso(request.output_path, progress_callback)

            # Step 4: Cleanup (95-100%)
            self._cleanup_working_directories()

            if not self._canceled:
                progress_callback("Randomization complete!", 100)
                return PatchResult(
                    success=True,
                    output_path=final_output,
                )
            else:
                return PatchResult(success=False, error_message="Canceled by user")

        except Exception as e:
            self._cleanup_working_directories()
            return PatchResult(success=False, error_message=str(e))

    def cancel(self):
        self._canceled = True

    def _setup_working_directories(self):
        try:
            # Remove any existing temp directories
            if self.base_work_dir.exists():
                shutil.rmtree(self.base_work_dir, ignore_errors=True)
                time.sleep(0.1)

            # Create all working directories
            directories = [
                self.base_work_dir,
                self.extract_dir,
                self.patcher_work_dir,
            ]

            for directory in directories:
                directory.mkdir(parents=True, exist_ok=True)

        except Exception as e:
            raise Exception(f"Failed to setup working directories: {e}")

    def _extract_iso(self, iso_path: str, progress_callback: ProgressCallback):
        try:
            progress_callback("Initializing ISO extraction...", 5)

            if not Path(iso_path).exists():
                raise Exception(f"ISO file not found: {iso_path}")

            extractor = disc_riider_py.WiiIsoExtractor(iso_path)
            extractor.prepare_extract_section("DATA")

            def extraction_progress(current, total):
                if not self._canceled:
                    progress = int(5 + (current / total) * 15)
                    progress_callback(f"Extracting ISO... ({current:,}/{total:,} files)", progress)

            try:
                extractor.extract_to(str(self.extract_dir), extraction_progress)
            except TypeError:
                extractor.extract_to(str(self.extract_dir))

            progress_callback("ISO extraction complete", 20)

        except Exception as e:
            raise Exception(f"ISO extraction failed: {e}")

    def _apply_all_patches(self, patch_configs: List[FilePatchConfig], progress_callback: ProgressCallback) -> int:
        try:
            total_configs = len(patch_configs)
            if total_configs == 0:
                progress_callback("No patches configured", 80)
                return 0

            progress_callback(f"Applying {total_configs} patch configurations...", 22)

            for i, config in enumerate(patch_configs):
                if self._canceled:
                    return i

                # Calculate progress range for this patch (20-80% total)
                base_progress = 20 + (i * 60 // total_configs)
                max_progress = 20 + ((i + 1) * 60 // total_configs)

                def patch_progress(message, progress):
                    actual_progress = base_progress + (progress * (max_progress - base_progress) // 100)
                    progress_callback(f"[{i + 1}/{total_configs}] {message}", actual_progress)

                patcher = PatcherFactory.create_patcher(config, self.patcher_work_dir)

                patch_progress(f"Starting {config.description}", 0)

                success = patcher.process_file(self.extract_dir, patch_progress)

                if not success:
                    raise Exception(f"Failed to apply patch: {config.description}")

                patch_progress(f"Completed {config.description}", 100)

            progress_callback("All patches applied successfully", 80)
            return total_configs

        except Exception as e:
            raise Exception(f"Patch application failed: {e}")

    def _rebuild_iso(self, output_path: str, progress_callback: ProgressCallback) -> str:
        try:
            progress_callback("Preparing output path...", 82)

            output_path = Path(output_path)
            if output_path.suffix.lower() != '.iso':
                output_path = output_path.with_suffix('.iso')

            output_dir = output_path.parent
            output_dir.mkdir(parents=True, exist_ok=True)

            if output_path.exists():
                try:
                    output_path.chmod(0o666)
                    output_path.unlink()
                except PermissionError:
                    timestamp = int(time.time())
                    new_name = f"{output_path.stem}_{timestamp}{output_path.suffix}"
                    output_path = output_path.parent / new_name

            progress_callback("Rebuilding ISO...", 85)

            def rebuild_progress(current, total):
                if not self._canceled:
                    progress = int(85 + (current / total) * 10)
                    progress_callback(f"Building ISO... ({current:,}/{total:,})", progress)

            try:
                disc_riider_py.rebuild_from_directory(
                    str(self.extract_dir),
                    str(output_path),
                    rebuild_progress,
                )
            except TypeError:
                disc_riider_py.rebuild_from_directory(
                    str(self.extract_dir),
                    str(output_path),
                )

            if not output_path.exists():
                raise Exception("ISO rebuild completed but output file not found")

            output_size = output_path.stat().st_size
            if output_size < 1024 * 1024:
                raise Exception(f"Output ISO file seems too small: {output_size} bytes")

            progress_callback("ISO rebuild complete", 95)
            return str(output_path)

        except Exception as e:
            raise Exception(f"ISO rebuild failed: {e}")

    def _cleanup_working_directories(self):
        """Clean up all temporary files and directories"""
        try:
            if self.base_work_dir.exists():
                shutil.rmtree(self.base_work_dir, ignore_errors=True)
                time.sleep(0.1)
        except Exception as e:
            print(f"Cleanup warning: {e}")