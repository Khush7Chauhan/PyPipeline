import os
from pathlib import Path
from typing import Any

class FileLockManager:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.lock_file = filepath.with_suffix(filepath.suffix + '.lock')

    def __enter__(self) -> 'FileLockManager':
        self.lock_file.touch()
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        if self.lock_file.exists():
            self.lock_file.unlink()