import shutil
import traceback
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

import libWiiPy
import nlzss11

from patcher.helper.patttern_handler import search_pattern
from patcher.models.models import FilePatchConfig, ProgressCallback, FileProcessingType


class BasePatcher(ABC):
    """Abstract base class for different file patchers"""

    def __init__(self, config: FilePatchConfig, work_dir: Path, plando_dict):
        self.config = config
        self.work_dir = work_dir
        self.plando_dict = plando_dict
        self.backup_files = []

    @abstractmethod
    def process_file(self, extract_dir: Path, progress_callback: ProgressCallback) -> bool:
        """Process and patch the file. Returns True if successful."""
        pass

    def _find_file(self, base_path: Path, primary_path: str) -> Optional[Path]:
        """Helper to find a file in primary or alternative locations"""
        all_paths = [primary_path]

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
        """Apply pattern-based binary patches directly to the file"""
        if not self.config.patch_patterns:
            print(f"Warning: No patch patterns defined for {self.config.file_id}")
            return True

        self._create_backup(file_path)

        try:
            with open(file_path, "rb") as f:
                file_data = bytearray(f.read())

            for patchpattern in self.config.patch_patterns:
                matches = search_pattern(file_data, patchpattern.pattern)

                if not matches:
                    print(f"ERROR: No match found for pattern: {patchpattern.name}")
                    return False

                if len(matches) > 1:
                    print(f"ERROR: Ambiguous match ({len(matches)}) for pattern: {patchpattern.name}")
                    return False

                print(f"Match found for pattern: {patchpattern.name}")
                match = matches[0].matched_instructions

                for patch in patchpattern.patchMap:
                    mem_data = match.get(patch.identifier)
                    if not mem_data:
                        raise Exception(
                            f"Identifier {patch.identifier} missing in match for pattern {patchpattern.name}")

                    offset = mem_data.address
                    old_bytes = mem_data.value
                    new_bytes = patch.patch_function(offset, file_data, self.plando_dict, match)

                    if old_bytes != file_data[offset:offset + len(old_bytes)]:
                        print(
                            f"WARNING: Expected {old_bytes.hex()} at 0x{offset:08X}, but found {file_data[offset:offset + len(old_bytes)].hex()}")

                    file_data[offset:offset + len(new_bytes)] = new_bytes

                    # Verify patch
                    verify_bytes = file_data[offset:offset + len(new_bytes)]
                    if verify_bytes != new_bytes:
                        raise Exception(f"Patch verification failed at 0x{offset:08X} for pattern {patchpattern.name}")

                    print(
                        f"SUCCESS: {patchpattern.name} - Patched 0x{offset:08X} from {old_bytes.hex()} to {new_bytes.hex()}")

            # Write back patched file
            with open(file_path, "wb") as f:
                f.write(file_data)

            print(f"Patched file saved: {file_path}")
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
        for index, (primary_file_path, nested_archive_path, target_file_path) in enumerate(self.config.file_group):

            dac_file_path = self._find_file(extract_dir, primary_file_path)

            if not dac_file_path:
                print(f"DAC file not found for {self.config.file_id}: {primary_file_path}")
                return index == 1
            filename = primary_file_path.split("/")[-1].split(".")[0]
            temp_dir = self.work_dir / f"temp_{self.config.file_id}_{filename}"
            u8_main_dir = temp_dir / "u8_main"
            u8_nested_dir = temp_dir / "u8_nested"
            temp_dir.mkdir(parents=True, exist_ok=True)
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

                nested_file_path = self._find_file(u8_main_dir, nested_archive_path)

                if not nested_file_path:
                    raise Exception(f"Nested archive not found: {nested_archive_path}")

                with open(nested_file_path, 'rb') as f:
                    nested_data = f.read()

                if not nested_data.startswith(b'U\xaa8-'):
                    raise Exception("Nested file is not a valid U8 archive")

                libWiiPy.archive.extract_u8(nested_data, str(u8_nested_dir))

                # Step 4: Apply patches to target file
                progress_callback(f"Applying patches", 55)

                target_file_path = u8_nested_dir / target_file_path

                if not target_file_path.exists():
                    raise Exception(f"Target file not found: {target_file_path}")

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
        return True

class DacU8Patcher(BasePatcher):
    def process_file(self, extract_dir: Path, progress_callback: ProgressCallback) -> bool:
        progress_callback(f"Processing nested DAC/U8: {self.config.description}", 0)
        for index, (primary_file_path, _, target_file_path) in enumerate(self.config.file_group):

            dac_file_path = self._find_file(extract_dir, primary_file_path)

            if not dac_file_path:
                print(f"DAC file not found for {self.config.file_id}: {primary_file_path}")
                return index == 1
            filename = primary_file_path.split("/")[-1].split(".")[0]
            temp_dir = self.work_dir / f"temp_{self.config.file_id}_{filename}"
            u8_main_dir = temp_dir / "u8_main"
            temp_dir.mkdir(parents=True, exist_ok=True)
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

                # Step 4: Apply patches to target file
                progress_callback(f"Applying patches", 55)

                target_file_path = u8_main_dir / target_file_path

                if not target_file_path.exists():
                    raise Exception(f"Target file not found: {target_file_path}")

                if not self._apply_patch_operations(target_file_path):
                    return False


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
        return True

class MainDolPatcher(BasePatcher):

    def process_file(self, extract_dir: Path, progress_callback: ProgressCallback) -> bool:
        progress_callback(f"Processing DOL file: {self.config.description}", 0)
        first_entry = self.config.file_group[0] if self.config.file_group else None
        primary_file_path = first_entry[0]
        main_dol_file_path = self._find_file(extract_dir, primary_file_path)

        if not main_dol_file_path:
            print(f"main dol file not found for {self.config.file_id}: {primary_file_path}")
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


class PatcherFactory:
    @staticmethod
    def create_patcher(config: FilePatchConfig, work_dir: Path, plando_dict) -> BasePatcher:
        if config.processing_type == FileProcessingType.NESTED_DAC_U8:
            return NestedDacU8Patcher(config, work_dir, plando_dict)
        elif config.processing_type == FileProcessingType.MAIN_DOL:
            return MainDolPatcher(config, work_dir, plando_dict)
        elif config.processing_type == FileProcessingType.DAC_U8:
            return  DacU8Patcher(config, work_dir, plando_dict)
        else:
            raise ValueError(f"Unknown processing type: {config.processing_type}")
