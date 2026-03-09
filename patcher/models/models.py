from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import List, Optional, Callable, Protocol, Literal, Any, Union, Tuple


@dataclass
class Instruction:
    offset: int
    pattern: list[int | None]
    identifier: int
    instruction_readable: str


@dataclass
class Patch:
    identifier: int
    patch_function: Callable[[[int], [bytearray], [Any], [list["PatchPattern"]], [str]], Optional[bytes]]
    new_instruction_readable: str


@dataclass
class MemoryData:
    address: int
    value: bytes


@dataclass
class PatternMatch:
    """Represents a single pattern match"""
    base_address: int
    matched_instructions: dict[int, MemoryData]


@dataclass
class PatchPattern:
    name: str
    patternJP: list[Instruction]
    patternPAL: list[Instruction] | None = None
    patternNA: list[Instruction] | None = None
    patchMapJP: list[Patch] = field(default_factory=list)
    patchMapPAL: list[Patch] = field(default_factory=list)
    patchMapNA: list[Patch] = field(default_factory=list)
    matchesJP: list[PatternMatch] | None = None
    matchesPAL: list[PatternMatch] | None = None
    matchesNA: list[PatternMatch] | None = None
    description: str = ""

    def __post_init__(self):
        if not self.patternPAL:
            self.patternPAL = self.patternJP
        if not self.patternNA:
            self.patternNA = self.patternJP

        if not self.patchMapPAL:
            self.patchMapPAL = self.patchMapJP
        if not self.patchMapNA:
            self.patchMapNA = self.patchMapJP

        identifiers = [instr.identifier for instr in self.patternJP]
        identifier_duplicates = {id for id in identifiers if identifiers.count(id) > 1}
        if identifier_duplicates:
            raise ValueError(f"Duplicate identifiers found: {identifier_duplicates}")
        offsets = [instr.offset for instr in self.patternJP]
        offsets_duplicates = {offset for offset in offsets if offsets.count(offset) > 1}
        if offsets_duplicates:
            raise ValueError(f"Duplicate offsets found: {offsets_duplicates}")

        anchor_pattern = next(
            (instr for instr in self.patternJP
             if instr.offset == 0),
            None
        )

        if anchor_pattern is None:
            raise ValueError("No instruction with offset 0 or alternate_offset 0 found")

        # Ensure anchor pattern contains only integers (no None wildcards)
        if any(byte is None for byte in anchor_pattern.pattern):
            raise ValueError(
                f"Anchor pattern (instruction '{anchor_pattern.identifier}') must contain only integers,no wildcards (None)"
            )

    def get_patchmap(self):
        if self.matchesPAL:
            return self.patchMapPAL
        elif self.matchesNA:
            return self.patchMapNA
        elif self.matchesJP:
            return self.patchMapJP
        else:
            raise ValueError(f"No valid PatchMap available for pattern '{self.name}' - no matches found in any region")

    def get_matches(self):
        if self.matchesPAL:
            return self.matchesPAL
        elif self.matchesNA:
            return self.matchesNA
        elif self.matchesJP:
            return self.matchesJP
        else:
            raise ValueError(
                f"No valid matches available for pattern '{self.name}' - search_all_pattern() may not have been called"
            )

    def get_matched_region(self) -> str:
        """Get the name of the region that has matches"""
        regions_with_matches = []
        if self.matchesJP:
            regions_with_matches.append("JP")
        if self.matchesPAL:
            regions_with_matches.append("PAL")
        if self.matchesNA:
            regions_with_matches.append("NA")

        if not regions_with_matches:
            raise ValueError(f"No matches found for pattern '{self.name}'")

        if len(regions_with_matches) == 3:
            return "All"
        elif len(regions_with_matches) == 2:
            return f"Multi({'+'.join(regions_with_matches)})"
        else:
            return regions_with_matches[0]


class FileProcessingType(Enum):
    """Defines different types of file processing needed"""
    NESTED_DAC_U8 = "nested_dac_u8"
    MAIN_DOL = "main_dol"
    DAC_U8 = "dac_u8"
    DacCopyFilePatcher = "dac_copy_file"


@dataclass
class PatchOperation:
    offset: int
    original_value: Optional[int]  # For verification, None to skip check
    new_value: int
    size: int = 2  # bytes
    byteorder: Literal["little", "big"] = "big"
    description: str = ""


class ProgressCallback(Protocol):
    def __call__(self, message: str, progress: int) -> None: ...


@dataclass
class FilePatchConfig:
    file_id: str
    description: str
    processing_type: FileProcessingType

    patch_patterns: List[PatchPattern] = None
    file_group: List[Tuple[str, str, str]] = None

    def __post_init__(self):
        if self.patch_patterns is None:
            self.patch_operations = []
        if self.file_group is None:
            self.file_group = []
        if self.patch_patterns:
            names = [obj.name for obj in self.patch_patterns]
            duplicates = [name for name, count in Counter(names).items() if count > 1]
            assert not duplicates, f"Duplicate name values found: {duplicates}"


@dataclass
class PatchRequest:
    iso_path: str
    appkprk_path: str
    output_path: str
    patch_configs: List[FilePatchConfig]
    work_dir: Optional[Path] = None


@dataclass
class PatchResult:
    success: bool
    output_path: Optional[str] = None
    error_message: Optional[str] = None


@dataclass
class MakerMetadata:
    asm_dir: str  # e.g. "R8AJ"
    original_dol_size: int
    original_free_space_ram_address: int
    pointer1_high: int
    pointer1_low: int
    pointer2_high: int
    pointer2_low: int
    pointer3_high: int
    pointer3_low: int
    pointer4_high: int
    pointer4_low: int
