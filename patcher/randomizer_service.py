import os
import shutil
import time
import zipfile
from base64 import b64decode
from pathlib import Path
from typing import List

import disc_riider_py
from libWiiPy.archive import IMETHeader
from ruamel.yaml import YAML

yaml = YAML(typ="safe")

yaml_dumper = YAML(typ="rt")  # Use RoundTripDumper for pretty-formatted dumps.
from patcher.logic.patchers import PatcherFactory
from patcher.models.models import PatchRequest, ProgressCallback, PatchResult, FilePatchConfig

VERSION = (1, 0, 2)


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

            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")

            plando_dict = self._extract_appkprk(request.appkprk_path, progress_callback)

            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")

            self._check_version(plando_dict)

            # Step 1: Extract ISO (0-20%)
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")

            self._extract_iso(request.iso_path, progress_callback)

            # Step 2: Apply all configured patches (20-80%)
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")

            patches_applied = self._apply_all_patches(request.patch_configs, progress_callback, plando_dict)

            # Step 3: Update Maker Code
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")
            self._update_maker_code()

            # Step 4: Update Banner Titles
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")
            self._update_banner_title()

            # Step 5: remove unnecessary files
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")
            self._remove_unneeded_files()

            # Step 6: Rebuild ISO (80-95%)
            if self._canceled:
                return PatchResult(success=False, error_message="Canceled by user")
            filename = f"Pokepark {request.appkprk_path.split('/')[-1]}"
            final_output = self._rebuild_iso(request.output_path + "/" + filename, progress_callback)

            # Step 7: Cleanup (95-100%)
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

    def _check_version(self, plando_dict):
        """
        Check if plando version is compatible with current randomizer Patcher version.

        Versioning follows SemVer principles:
            - Major version (X.y.z): breaking changes to core features
            - Minor version (x.Y.z): backward-incompatible changes or new features
            - Patch version (x.y.Z): bug fixes, safe for all clients
        """
        if "Version" not in plando_dict:
            raise Exception("Missing 'Version' key in .appkprk")

        plando_version = plando_dict["Version"]
        if not (isinstance(plando_version, (list, tuple)) and all(isinstance(x, int) for x in plando_version)):
            raise Exception("Version must be a list or tuple of integers")

        major, minor = plando_version[0], plando_version[1]
        patch = plando_version[2] if len(plando_version) > 2 else 0

        patcher_major, patcher_minor, patcher_patch = VERSION

        # Major version must match exactly (breaking changes)
        if major != patcher_major:
            raise Exception(
                f"Incompatible major version: Randomizer Patcher v{patcher_major}.{patcher_minor}.{patcher_patch} "
                f"vs APWorld v{major}.{minor}.{patch}"
            )

        # Check for minor version mismatch (breaking feature changes)
        if minor > patcher_minor:
            raise Exception(
                f"Incompatible minor version: Randomizer Patcher v{patcher_major}.{patcher_minor}.{patcher_patch} "
                f"vs APWorld v{major}.{minor}.{patch}"
            )

        if patch != patcher_patch:
            print(
                f"Warning: Patch version differs: Randomizer Patcher v{patcher_major}.{patcher_minor}.{patcher_patch} "
                f"vs APWorld v{major}.{minor}.{patch} (safe to continue)"
            )

        return major, minor, patch

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

    def _extract_appkprk(self, appokprk_path: str, progress_callback: ProgressCallback):
        if not os.access(appokprk_path, os.R_OK):
            raise Exception(
                """The pkprk file could not be opened.<br><br>
                Please ensure that the program has read permissions for the file and try again."""
            )

        try:
            with zipfile.ZipFile(appokprk_path, "r") as z:
                with z.open("plando") as plando_in_zip:
                    plando_dict = yaml.load(b64decode(plando_in_zip.read()))
        except:
            try:
                with open(appokprk_path, "r") as f:
                    plando_dict = yaml.load(f)
            except:
                raise Exception(
                    """There was an error trying to read the pkprk file.<br><br>
                    Please ensure that the file has not been modified or corrupted and try again."""
                )
        else:
            return plando_dict

    def _apply_all_patches(self, patch_configs: List[FilePatchConfig], progress_callback: ProgressCallback,
                           plando_dict) -> int:
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

                patcher = PatcherFactory.create_patcher(config, self.patcher_work_dir, plando_dict)

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

    def _update_maker_code(self):
        try:
            file_path = self.extract_dir / "DATA/sys/boot.bin"
            with open(file_path, "r+b") as f:
                f.seek(4)
                f.write(0x3939.to_bytes(2))
                f.seek(0x20)
                f.write("Pokepark Archipelago".encode('ascii'))

            file_path = self.extract_dir / "DATA/disc/header.bin"
            with open(file_path, "r+b") as f:
                f.seek(4)
                f.write(0x3939.to_bytes(2))
                f.seek(0x20)
                f.write("Pokepark Archipelago".encode('ascii'))

            file_path = self.extract_dir / "DATA/tmd.bin"
            with open(file_path, "r+b") as f:
                f.seek(0x0000018C)
                f.write(0x0099.to_bytes(2))
                f.seek(0x00000198)
                f.write(0x3939.to_bytes(2))

            file_path = self.extract_dir / "DATA/ticket.bin"
            with open(file_path, "r+b") as f:
                f.seek(0x000001DC)
                f.write(0x0099.to_bytes(2))

        except Exception as e:
            raise Exception(f"Updating Maker Code failed: {e}")

    def _update_banner_title(self):
        try:
            file_path = self.extract_dir / "DATA/files/opening.bnr"
            with open(file_path, "r+b") as f:
                header = IMETHeader()
                data = f.read()
                header.load(data)

                num_channels = 10
                channel_names = [(header.LocalizedTitles(i), "Pokepark Archipelago") for i in range(num_channels)]
                header.set_channel_names(channel_names)

                f.seek(0)
                f.write(header.dump())
        except Exception as e:
            raise Exception(f"Updating Banner Titles failed: {e}")

    def _remove_unneeded_files(self):
        files_to_remove = [
            "DATA/files/Thp/Opening.thp",
            "DATA/files/Thp/Ending.thp",
        ]

        try:
            for file_path in files_to_remove:
                full_path = self.extract_dir / file_path
                if full_path.exists():
                    full_path.unlink()
                    print(f"Removed: {file_path}")
                else:
                    print(f"File not found (skipping): {file_path}")

        except Exception as e:
            raise Exception(f"Error removing unneeded files: {e}")

    def _cleanup_working_directories(self):
        """Clean up all temporary files and directories"""
        try:
            if self.base_work_dir.exists():
                shutil.rmtree(self.base_work_dir, ignore_errors=True)
                time.sleep(0.1)
        except Exception as e:
            print(f"Cleanup warning: {e}")
