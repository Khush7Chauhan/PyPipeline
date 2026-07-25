import json
from pathlib import Path
from typing import Any,Dict
from src.processor.base import FileProcessor

class JSONProcessor(FileProcessor):
    def process(self)->Dict[str,Any]:
        with open(self.file_path, mode='r',encoding = 'utf-8') as f:
            data = json.load(f)

        key_count = len(data.keys()) if isinstance(data,dict) else len(data)

        return {
            "file":self.file_name,
            "type":"JSON",
            "size_kb":round(self.file_size_kb,2),
            "keys_or_items":key_count
        }