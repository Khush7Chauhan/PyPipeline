import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict
from src.utils.lock_manager import FileLockManager

class FileProcessor(ABC):
    def __init__(self,file_path:Path):
        self.file_path = file_path
        self.file_name = file_path.name
        self.file_size_kb = file_path.stat().st_size/1024

    @abstractmethod
    def process(self)->Dict[str,Any]:
        pass

    def save(self,destination_dir: Path)->None:
        dest_path = destination_dir/self.file_name
        with FileLockManager(self.file_path):
            shutil.move(str(self.file_path),str(dest_path))