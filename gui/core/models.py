from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional, Callable, Protocol


class FileProcessingType(Enum):
    """Defines different types of file processing needed"""
    NESTED_DAC_U8 = "nested_dac_u8"
    MAIN_DOL = "main_dol"


@dataclass
class PatchOperation:
    offset: int
    original_value: Optional[int]  # For verification, None to skip check
    new_value: int
    size: int = 2  # bytes
    byteorder: str = "big"
    description: str = ""


@dataclass
class FilePatchConfig:
    file_id: str
    description: str
    processing_type: FileProcessingType

    primary_file_path: str
    alternative_paths: List[str] = None

    nested_archive_path: str = None
    nested_alternative_paths: List[str] = None
    target_file_path: str = None  # Path within the nested archive

    patch_operations: List[PatchOperation] = None

    def __post_init__(self):
        if self.alternative_paths is None:
            self.alternative_paths = []
        if self.nested_alternative_paths is None:
            self.nested_alternative_paths = []
        if self.patch_operations is None:
            self.patch_operations = []


class ProgressCallback(Protocol):
    def __call__(self, message: str, progress: int) -> None: ...


@dataclass
class PatchRequest:
    iso_path: str
    output_path: str
    patch_configs: List[FilePatchConfig]
    work_dir: Optional[Path] = None


@dataclass
class PatchResult:
    success: bool
    output_path: Optional[str] = None
    error_message: Optional[str] = None