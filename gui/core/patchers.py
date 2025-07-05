import shutil
import traceback
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional

import libWiiPy
import nlzss11

from gui.core.DOL import DOL
from gui.core.models import FilePatchConfig, ProgressCallback, FileProcessingType


class BasePatcher(ABC):
    """Abstract base class for different file patchers"""

    def __init__(self, config: FilePatchConfig, work_dir: Path):
        self.config = config
        self.work_dir = work_dir
        self.backup_files = []

    @abstractmethod
    def process_file(self, extract_dir: Path, progress_callback: ProgressCallback) -> bool:
        """Process and patch the file. Returns True if successful."""
        pass

    def _find_file(self, base_path: Path, primary_path: str, alternatives: List[str]) -> Optional[Path]:
        """Helper to find a file in primary or alternative locations"""
        all_paths = [primary_path] + alternatives

        for path_str in all_paths:
            file_path = base_path / path_str
            if file_path.exists():
                return file_path

        return None

    def _create_backup(self, file_path: Path) -> Path:
        """Create a backup of the file"""
        backup_path = file_path.with_suffix(file_path.suffix + '.backup')
        shutil.copy2(file_path, backup_path)
        self.backup_files.append(backup_path)
        return backup_path

    def _apply_patch_operations(self, file_path: Path) -> bool:
        """Apply the configured patch operations to a file"""
        if not self.config.patch_operations:
            print(f"Warning: No patch operations defined for {self.config.file_id}")
            return True

        # Create backup
        self._create_backup(file_path)

        try:

            with open(file_path, 'r+b') as f:
                for operation in self.config.patch_operations:
                    f.seek(operation.offset)

                    if operation.original_value is not None:
                        current_bytes = f.read(operation.size)
                        if len(current_bytes) != operation.size:
                            raise Exception(f"Could not read {operation.size} bytes at offset 0x{operation.offset:08x}")

                        current_value = int.from_bytes(current_bytes, byteorder=operation.byteorder)
                        if current_value != operation.original_value:
                            print(
                                f"WARNING: Expected 0x{operation.original_value:04x} but found 0x{current_value:04x} at offset 0x{operation.offset:08x}")

                    # Apply patch
                    f.seek(operation.offset)
                    new_bytes = operation.new_value.to_bytes(operation.size, byteorder=operation.byteorder)
                    f.write(new_bytes)

                    # Verify patch was applied
                    f.seek(operation.offset)
                    verify_bytes = f.read(operation.size)
                    verify_value = int.from_bytes(verify_bytes, byteorder=operation.byteorder)

                    if verify_value != operation.new_value:
                        raise Exception(
                            f"Patch verification failed at 0x{operation.offset:08x}: expected 0x{operation.new_value:04x}, got 0x{verify_value:04x}")

                    print(
                        f"SUCCESS: {operation.description} - Patched 0x{operation.offset:08x} to 0x{operation.new_value:04x}")

            return True

        except Exception as e:
            print(f"Patch operation failed for {self.config.file_id}: {e}")
            print(f"Error in patcher: {self.__class__.__name__}")
            print("Full stack trace:")
            print(traceback.format_exc())
            return False


class NestedDacU8Patcher(BasePatcher):

    def process_file(self, extract_dir: Path, progress_callback: ProgressCallback) -> bool:
        progress_callback(f"Processing nested DAC/U8: {self.config.description}", 0)

        dac_file_path = self._find_file(extract_dir, self.config.primary_file_path, self.config.alternative_paths)

        if not dac_file_path:
            print(f"DAC file not found for {self.config.file_id}: {self.config.primary_file_path}")
            return False

        temp_dir = self.work_dir / f"temp_{self.config.file_id}"
        u8_main_dir = temp_dir / "u8_main"
        u8_nested_dir = temp_dir / "u8_nested"
        temp_dir.mkdir(parents=True, exist_ok=True)
        print(self.config.patch_operations)
        try:
            # Step 1: Decompress DAC file
            progress_callback(f"Decompressing {dac_file_path.name}", 10)

            with open(dac_file_path, 'rb') as f:
                dac_data = f.read()

            decompressed_data = nlzss11.decompress(dac_data)
            decompressed_bin = temp_dir / "decompressed.bin"

            with open(decompressed_bin, 'wb') as f:
                f.write(decompressed_data)

            # Step 2: Extract main U8 archive
            progress_callback(f"Extracting main U8 archive", 25)

            if not decompressed_data.startswith(b'U\xaa8-'):
                raise Exception("Decompressed data is not a valid U8 archive")

            libWiiPy.archive.extract_u8(decompressed_data, str(u8_main_dir))

            # Step 3: Extract nested U8 archive
            progress_callback(f"Extracting nested archive", 40)

            nested_file_path = self._find_file(u8_main_dir, self.config.nested_archive_path,
                                               self.config.nested_alternative_paths)

            if not nested_file_path:
                raise Exception(f"Nested archive not found: {self.config.nested_archive_path}")

            with open(nested_file_path, 'rb') as f:
                nested_data = f.read()

            if not nested_data.startswith(b'U\xaa8-'):
                raise Exception("Nested file is not a valid U8 archive")

            libWiiPy.archive.extract_u8(nested_data, str(u8_nested_dir))

            # Step 4: Apply patches to target file
            progress_callback(f"Applying patches", 55)

            target_file_path = u8_nested_dir / self.config.target_file_path

            if not target_file_path.exists():
                raise Exception(f"Target file not found: {self.config.target_file_path}")

            if not self._apply_patch_operations(target_file_path):
                return False

            # Step 5: Repack nested archive
            progress_callback(f"Repacking nested archive", 70)

            nested_packed_data = libWiiPy.archive.pack_u8(str(u8_nested_dir))

            with open(nested_file_path, 'wb') as f:
                f.write(nested_packed_data)

            # Step 6: Repack main archive
            progress_callback(f"Repacking main archive", 85)

            main_packed_data = libWiiPy.archive.pack_u8(str(u8_main_dir))

            # Step 7: Recompress and write back to DAC
            progress_callback(f"Recompressing DAC file", 95)

            # Create backup of original DAC
            self._create_backup(dac_file_path)

            compressed_data = nlzss11.compress(main_packed_data)

            with open(dac_file_path, 'wb') as f:
                f.write(compressed_data)

            progress_callback(f"Completed {self.config.description}", 100)
            return True

        except Exception as e:
            print(f"Nested DAC/U8 processing failed for {self.config.file_id}: {e}")
            print(f"Error in patcher: {self.__class__.__name__}")
            print("Full stack trace:")
            print(traceback.format_exc())
            return False
        finally:
            # Cleanup temp directory
            if temp_dir.exists():
                shutil.rmtree(temp_dir, ignore_errors=True)


class MainDolPatcher(BasePatcher):

    def process_file(self, extract_dir: Path, progress_callback: ProgressCallback) -> bool:
        progress_callback(f"Processing nested DAC/U8: {self.config.description}", 0)

        main_dol_file_path = self._find_file(extract_dir, self.config.primary_file_path, self.config.alternative_paths)

        if not main_dol_file_path:
            print(f"main dol file not found for {self.config.file_id}: {self.config.primary_file_path}")
            return False

        temp_dir = self.work_dir / f"temp_{self.config.file_id}"
        temp_dir.mkdir(parents=True, exist_ok=True)

        try:
            progress_callback(f"Applying patches", 10)

            if not self._apply_patch_operations(main_dol_file_path):
                return False

            progress_callback(f"Completed {self.config.description}", 100)
            return True

        except Exception as e:
            print(f"main dol processing failed for {self.config.file_id}: {e}")
            return False
        finally:
            # Cleanup temp directory
            if temp_dir.exists():
                shutil.rmtree(temp_dir, ignore_errors=True)

    def _apply_patch_operations(self, file_path: Path) -> bool:
        """Apply the configured patch operations to a file"""
        if not self.config.patch_operations:
            print(f"Warning: No patch operations defined for {self.config.file_id}")
            return True

        # Create backup
        self._create_backup(file_path)

        try:

            with open(file_path, 'r+b') as f:
                for operation in self.config.patch_operations:
                    dol = DOL()
                    dol.read(f)
                    operation.offset = dol.convert_address_to_offset(operation.offset)

                    f.seek(operation.offset)

                    if operation.original_value is not None:
                        current_bytes = f.read(operation.size)
                        if len(current_bytes) != operation.size:
                            raise Exception(f"Could not read {operation.size} bytes at offset 0x{operation.offset:08x}")

                        current_value = int.from_bytes(current_bytes, byteorder=operation.byteorder)
                        if current_value != operation.original_value:
                            print(
                                f"WARNING: Expected 0x{operation.original_value:04x} but found 0x{current_value:04x} at offset 0x{operation.offset:08x}")

                    # Apply patch
                    f.seek(operation.offset)
                    new_bytes = operation.new_value.to_bytes(operation.size, byteorder=operation.byteorder)
                    f.write(new_bytes)

                    # Verify patch was applied
                    f.seek(operation.offset)
                    verify_bytes = f.read(operation.size)
                    verify_value = int.from_bytes(verify_bytes, byteorder=operation.byteorder)

                    if verify_value != operation.new_value:
                        raise Exception(
                            f"Patch verification failed at 0x{operation.offset:08x}: expected 0x{operation.new_value:04x}, got 0x{verify_value:04x}")

                    print(
                        f"SUCCESS: {operation.description} - Patched 0x{operation.offset:08x} to 0x{operation.new_value:04x}")

            return True

        except Exception as e:
            print(f"Patch operation failed for {self.config.file_id}: {e}")
            return False


class PatcherFactory:
    @staticmethod
    def create_patcher(config: FilePatchConfig, work_dir: Path) -> BasePatcher:
        if config.processing_type == FileProcessingType.NESTED_DAC_U8:
            return NestedDacU8Patcher(config, work_dir)
        elif config.processing_type == FileProcessingType.MAIN_DOL:
            return MainDolPatcher(config, work_dir)
        else:
            raise ValueError(f"Unknown processing type: {config.processing_type}")
