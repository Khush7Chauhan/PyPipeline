import csv
from pathlib import Path
from typing import Any, Dict
from src.processor.base import FileProcessor

class CSVProcessor(FileProcessor):
    def process(self) -> Dict[str, Any]:
        row_count = 0
        with open(self.file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            row_count = sum(1 for _ in reader)
            
        return {
            "file": self.file_name,
            "type": "CSV",
            "size_kb": round(self.file_size_kb, 2),
            "rows": row_count
        }