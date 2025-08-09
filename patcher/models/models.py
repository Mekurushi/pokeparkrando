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
    alternate_offset: int | None = None


@dataclass
class Patch:
    identifier: int
    patch_function: Callable[[[Any], [Any], [Any], [Any]], bytes]
    new_instruction_readable: str

@dataclass
class MemoryData:
    address: int
    value: bytes

@dataclass
class PatternMatch:
    """Represents a single pattern match"""
    base_address: int
    matched_instructions: dict[int,MemoryData]


@dataclass
class PatchPattern:
    name: str
    pattern: list[Instruction]
    patchMap: list[Patch] = field(default_factory=list)
    matches: list[PatternMatch] | None = None
    description: str = ""

    def __post_init__(self):
        identifiers = [instr.identifier for instr in self.pattern]
        identifier_duplicates = {id for id in identifiers if identifiers.count(id) > 1}
        if identifier_duplicates:
            raise ValueError(f"Duplicate identifiers found: {identifier_duplicates}")
        offsets = [instr.offset for instr in self.pattern]
        offsets_duplicates = {offset for offset in offsets if offsets.count(offset) > 1}
        if offsets_duplicates:
            raise ValueError(f"Duplicate offsets found: {offsets_duplicates}")

        anchor_pattern = next(
            (instr for instr in self.pattern
             if instr.offset == 0 or (hasattr(instr, 'alternate_offset') and instr.alternate_offset == 0)),
            None
        )

        if anchor_pattern is None:
            raise ValueError("No instruction with offset 0 or alternate_offset 0 found")

        # Ensure anchor pattern contains only integers (no None wildcards)
        if any(byte is None for byte in anchor_pattern.pattern):
            raise ValueError(
                f"Anchor pattern (instruction '{anchor_pattern.identifier}') must contain only integers, no wildcards (None)")


class FileProcessingType(Enum):
    """Defines different types of file processing needed"""
    NESTED_DAC_U8 = "nested_dac_u8"
    MAIN_DOL = "main_dol"
    DAC_U8 = "dac_u8"


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

    patch_patterns:List[PatchPattern] = None
    file_group: List[Tuple[str, str, str]] = None
    def __post_init__(self):
        if self.patch_patterns is None:
            self.patch_operations = []
        if self.file_group is None:
            self.file_group = []

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