import io
import os
import shutil
import sys
import traceback
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

import libWiiPy
import nlzss11
import yaml

from asm.patcher import apply_dol_patch
from patcher.helper.patttern_handler import search_all_pattern
from patcher.models.DOL import DOL
from patcher.models.models import FilePatchConfig, MakerMetadata, ProgressCallback, FileProcessingType
from patcher.patterns.dol.pattern_helper import get_enemy_ai_option, get_player_name_from_dict
from path import RANDO_ROOT_PATH

IS_DEV = not getattr(sys, 'frozen', False)

MAKER_METADATA: dict[str, MakerMetadata] = {
    "R8AJ01": MakerMetadata(
        asm_dir="R8AJ",
        original_dol_size=0x36C540,
        original_free_space_ram_address=0x80486ba0,
        pointer1_high=0x8020dde0, pointer1_low=0x8020ddec,
        pointer2_high=0x8020dddc, pointer2_low=0x8020dde4,
        pointer3_high=0x802049b8, pointer3_low=0x802049bc,
        pointer4_high=0x80004234, pointer4_low=0x80004238,
    ),
    "R8AE01": MakerMetadata(
        asm_dir="R8AE",
        original_dol_size=0x36E9E0,
        original_free_space_ram_address=0x8048a040,
        pointer1_high=0x8020ff30, pointer1_low=0x8020ff3c,
        pointer2_high=0x8020ff2c, pointer2_low=0x8020ff34,
        pointer3_high=0x80206b08, pointer3_low=0x80206b0c,
        pointer4_high=0x80004234, pointer4_low=0x80004238,
    ),
    "R8AP01": MakerMetadata(
        asm_dir="R8AP",
        original_dol_size=0x36EF40,
        original_free_space_ram_address=0x8048a620,
        pointer1_high=0x80210210, pointer1_low=0x8021021c,
        pointer2_high=0x8021020c, pointer2_low=0x80210214,
        pointer3_high=0x80206de8, pointer3_low=0x80206dec,
        pointer4_high=0x80004234, pointer4_low=0x80004238,
    ),
}


class BasePatcher(ABC):
    """Abstract base class for different file patchers"""

    def __init__(self, config: FilePatchConfig, work_dir: Path, plando_dict, maker_id: str | None):
        self.config = config
        self.work_dir = work_dir
        self.plando_dict = plando_dict
        self.backup_files = []
        self.maker_id = maker_id
        self.free_space_start_offsets = {}

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

    def _apply_patch_operations(self, file_path: Path) -> bool:
        """Apply pattern-based binary patches directly to the file"""
        if not self.config.patch_patterns:
            print(f"Warning: No patch patterns defined for {self.config.file_id}")
            return True

        try:
            with open(file_path, "rb") as f:
                file_data = bytearray(f.read())

            # find all patterns
            pattern_results = []
            for patchpattern in self.config.patch_patterns:
                search_all_pattern(file_data, patchpattern)
                matches = patchpattern.get_matches()
                if isinstance(self, MainDolPatcher):
                    dol = DOL()
                    stream = io.BytesIO(file_data)
                    dol.read(stream)
                    found_address = hex(dol.convert_offset_to_address(matches[0].base_address)) if matches else "N/A"
                else:
                    found_address = hex(matches[0].base_address) if matches else "N/A"

                pattern_results.append(
                    {
                        "name": patchpattern.name,
                        "address": found_address,
                        "matches": len(matches)
                    }
                )
                print(
                    f"Found {len(matches)} match(es) for pattern: {patchpattern.name}, address: "
                    f"{found_address}"
                )

            # writing debug logs:
            if IS_DEV and self.maker_id:
                self._write_pattern_log(file_path, pattern_results)

            # patch all found matches
            for patchpattern in self.config.patch_patterns:
                match = patchpattern.get_matches()[0].matched_instructions
                print(f"Match found for pattern: {patchpattern.name}")
                for patch in patchpattern.get_patchmap():
                    mem_data = match.get(patch.identifier)
                    if not mem_data:
                        raise Exception(
                            f"Identifier {patch.identifier} missing in match for pattern {patchpattern.name}"
                        )

                    offset = mem_data.address
                    old_bytes = mem_data.value
                    new_bytes = patch.patch_function(
                        offset, file_data, self.plando_dict, self.config.patch_patterns,
                        patchpattern.name
                    )

                    if new_bytes is None:
                        continue

                    if old_bytes != file_data[offset:offset + len(old_bytes)]:
                        print(
                            f"WARNING: Expected {old_bytes.hex()} at 0x{offset:08X}, but found {file_data[offset:offset + len(old_bytes)].hex()}"
                        )

                    file_data[offset:offset + len(new_bytes)] = new_bytes

                    # Verify patch
                    verify_bytes = file_data[offset:offset + len(new_bytes)]
                    if verify_bytes != new_bytes:
                        raise Exception(f"Patch verification failed at 0x{offset:08X} for pattern {patchpattern.name}")

                    print(
                        f"SUCCESS: {patchpattern.name} - Patched 0x{offset:08X} from {old_bytes.hex()} to {new_bytes.hex()}"
                    )

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

    def _write_pattern_log(self, file_path: Path, pattern_results: list[dict]):
        """Write found patterns and addresses to a log file named after maker_id"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        log_path = log_dir / f"{self.maker_id}.txt"
        existing_content = log_path.read_text() if log_path.exists() else ""

        if f"[{file_path.name}]" not in existing_content:
            with open(log_path, "a") as f:  # append so multiple files accumulate
                f.write(f"[{file_path.name}]\n")
                for result in pattern_results:
                    f.write(f"  {result['name']}: {result['address']} ({result['matches']} match(es))\n")
                f.write("\n")


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


def get_patcher_version_bytes():
    from patcher.randomizer_service import VERSION
    return VERSION[0].to_bytes(0x4, 'big') + VERSION[1].to_bytes(0x4, 'big') + VERSION[2].to_bytes(0x4, 'big')


class MainDolPatcher(BasePatcher):

    def __init__(self, config: FilePatchConfig, work_dir: Path, plando_dict, maker_id: str | None):
        super().__init__(config, work_dir, plando_dict, maker_id)
        self.original_symbols = None
        self.custom_symbols = None
        self.pointer4_low = None
        self.pointer4_high = None
        self.pointer3_low = None
        self.pointer3_high = None
        self.pointer2_low = None
        self.pointer2_high = None
        self.pointer1_low = None
        self.pointer1_high = None
        self.ORIGINAL_FREE_SPACE_RAM_ADDRESS = None
        self.ORIGINAL_DOL_SIZE = None

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

    def _meta(self) -> MakerMetadata:
        try:
            return MAKER_METADATA[self.maker_id]
        except KeyError:
            raise ValueError(f"Unknown maker_id: {self.maker_id}")

    def get_patch_diffs_path(self) -> Path:
        return RANDO_ROOT_PATH / "asm" / self._meta().asm_dir / "patch_diffs"

    def load_free_space_start_offsets(self):
        path = RANDO_ROOT_PATH / "asm" / self._meta().asm_dir / "free_space_start_offsets.txt"
        with open(path, "r") as f:
            self.free_space_start_offsets = yaml.safe_load(f)

    def load_symbols(self):
        path = RANDO_ROOT_PATH / "asm" / self._meta().asm_dir / "custom_symbols.txt"
        with open(path, "r") as f:
            self.custom_symbols = yaml.safe_load(f)

        path = RANDO_ROOT_PATH / "asm" / self._meta().asm_dir / "original_symbols.txt"
        with open(path, "r") as f:
            self.original_symbols = yaml.safe_load(f)

    def fill_dol_metadata(self):
        m = self._meta()
        self.ORIGINAL_DOL_SIZE = m.original_dol_size
        self.ORIGINAL_FREE_SPACE_RAM_ADDRESS = m.original_free_space_ram_address
        self.pointer1_high = m.pointer1_high
        self.pointer1_low = m.pointer1_low
        self.pointer2_high = m.pointer2_high
        self.pointer2_low = m.pointer2_low
        self.pointer3_high = m.pointer3_high
        self.pointer3_low = m.pointer3_low
        self.pointer4_high = m.pointer4_high
        self.pointer4_low = m.pointer4_low

    def _apply_patch_operations(self, file_path: Path) -> bool:
        """Apply pattern-based binary patches directly to the file"""

        try:
            with open(file_path, "rb") as f:
                file_data = bytearray(f.read())

            # create DOL object
            dol = DOL()
            stream = io.BytesIO(file_data)
            dol.read(stream)

            # find all patterns for logging purposes
            pattern_results = []
            for patchpattern in self.config.patch_patterns:
                search_all_pattern(file_data, patchpattern)
                matches = patchpattern.get_matches()
                found_address = hex(dol.convert_offset_to_address(matches[0].base_address)) if matches else "N/A"
                pattern_results.append(
                    {
                        "name": patchpattern.name,
                        "address": found_address,
                        "matches": len(matches)
                    }
                )
                print(
                    f"Found {len(matches)} match(es) for pattern: {patchpattern.name}, address: "
                    f"{found_address}"
                )

            # writing debug logs:
            if IS_DEV and self.maker_id:
                self._write_pattern_log(file_path, pattern_results)

            # patching based on asm

            diffs_path = self.get_patch_diffs_path()
            self.load_free_space_start_offsets()

            self.fill_dol_metadata()

            self.load_symbols()

            for diff_file in os.listdir(diffs_path):
                with open(os.path.join(diffs_path, diff_file)) as f:
                    diffs = yaml.safe_load(f.read())

                if "main.dol" in diffs:
                    apply_dol_patch(self, dol, diffs["main.dol"])

            # additional patches
            self.dol_data_patches(dol)

            # Write back patched dol
            dol.save_changes()

            with open(file_path, "wb") as f:
                f.write(dol.data.getvalue())
            print(f"Patched file saved: {file_path}")
            return True

        except Exception as e:
            print(f"Patch operation failed for {self.config.file_id}: {e}")
            print(f"Error in patcher: {self.__class__.__name__}")
            print("Full stack trace:")
            print(traceback.format_exc())
            return False

    def dol_data_patches(self, dol: DOL):
        dol.write_data_bytes(
            self.custom_symbols["main.dol"]["PLAYER_NAME"],
            get_player_name_from_dict(self.plando_dict)
        )
        print(
            f"Applied player name patch: {get_player_name_from_dict(self.plando_dict)} at address {hex(self.custom_symbols['main.dol']['PLAYER_NAME'])}"
        )
        dol.write_data_bytes(
            self.custom_symbols["main.dol"]["PATCHER_VERSION"],
            get_patcher_version_bytes()
        )
        print(
            f"Applied patcher version patch: {get_patcher_version_bytes().hex()} at address {hex(self.custom_symbols['main.dol']['PATCHER_VERSION'])}"
        )
        dol.write_data_bytes(
            self.original_symbols["main.dol"]["ai_difficulty_request"],
            get_enemy_ai_option(self.plando_dict)
        )
        print(
            f"Applied enemy AI difficulty patch: {get_enemy_ai_option(self.plando_dict).hex()} at address {hex(self.original_symbols['main.dol']['ai_difficulty_request'])}"
            )


class DacCopyFilePatcher(BasePatcher):

    def process_file(self, extract_dir: Path, progress_callback: ProgressCallback) -> bool:
        progress_callback(f"Processing nested DAC/U8: {self.config.description}", 0)
        for index, (primary_file_path, source_file_path, target_file_path) in enumerate(self.config.file_group):

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
                # Step 4: copy file to target path
                progress_callback(f"Applying patches", 55)

                source_file_path = u8_main_dir / source_file_path
                target_file_path = u8_main_dir / target_file_path

                if not self.copy_file(source_file_path, target_file_path):
                    return False

                # Step 6: Repack main archive
                progress_callback(f"Repacking main archive", 85)

                main_packed_data = libWiiPy.archive.pack_u8(str(u8_main_dir))

                # Step 7: Recompress and write back to DAC
                progress_callback(f"Recompressing DAC file", 95)

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

    def copy_file(self, source: Path, target: Path):
        try:

            if not source.exists():
                raise FileNotFoundError(f"Source file not found: {source}")

            if not source.is_file():
                raise IsADirectoryError(f"Source path is not a file: {target}")

            shutil.copy2(source, target)
            return True
        except Exception as e:
            print(f"Copy operation failed for {self.config.file_id}: {e}")
            print(f"Error in patcher: {self.__class__.__name__}")
            print("Full stack trace:")
            print(traceback.format_exc())
            return False


class PatcherFactory:
    @staticmethod
    def create_patcher(config: FilePatchConfig, work_dir: Path, plando_dict, maker_id: str) -> BasePatcher:
        if config.processing_type == FileProcessingType.NESTED_DAC_U8:
            return NestedDacU8Patcher(config, work_dir, plando_dict, maker_id)
        elif config.processing_type == FileProcessingType.MAIN_DOL:
            return MainDolPatcher(config, work_dir, plando_dict, maker_id)
        elif config.processing_type == FileProcessingType.DAC_U8:
            return DacU8Patcher(config, work_dir, plando_dict, maker_id)
        elif config.processing_type == FileProcessingType.DacCopyFilePatcher:
            return DacCopyFilePatcher(config, work_dir, plando_dict, maker_id)
        else:
            raise ValueError(f"Unknown processing type: {config.processing_type}")
