from pathlib import Path
from typing import Any, Dict
from src.processor.base import FileProcessor

class TXTProcessor(FileProcessor):
    def process(self) -> Dict[str, Any]:
        word_count = 0
        with open(self.file_path, mode='r', encoding='utf-8') as f:
            for line in f:
                word_count += len(line.split())
                
        return {
            "file": self.file_name,
            "type": "TXT",
            "size_kb": round(self.file_size_kb, 2),
            "words": word_count
        }