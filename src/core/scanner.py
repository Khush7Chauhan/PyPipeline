from pathlib import Path
from typing import Generator
from src.utils.logger import logger

def generate_target_files(directory: Path, extensions: tuple[str, ...]) -> Generator[Path, None, None]:
    logger.info(f"Scanning {directory} for extensions: {extensions}")
    
    if not directory.exists():
        logger.error(f"Directory {directory} does not exist.")
        return

    for file_path in directory.rglob('*.*'):
        if file_path.suffix.lower() in extensions:
            yield file_path