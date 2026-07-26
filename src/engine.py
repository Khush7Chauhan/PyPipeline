import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any, Dict

from src.processor.csv_proc import CSVProcessor
from src.processor.json_proc import JSONProcessor
from src.processor.txt_proc import TXTProcessor
from src.utils.logger import logger
from src.utils.decorator import retry

def get_processor(file_path: Path):
    ext = file_path.suffix.lower()
    if ext == '.csv':
        return CSVProcessor(file_path)
    elif ext == '.json':
        return JSONProcessor(file_path)
    elif ext == '.txt':
        return TXTProcessor(file_path)
    else:
        raise ValueError(f"Unsupported extension: {ext}")

@retry(retries=2)
def process_single_file(file_path: Path, processed_dir: Path) -> Dict[str, Any]:
    """Worker function for the multiprocessing pool."""
    processor = get_processor(file_path)
    result = processor.process()
    processor.save(processed_dir)
    return result

def run_multiprocessing_engine(file_generator, processed_dir: Path) -> list[Dict[str, Any]]:
    results = []
    cores = multiprocessing.cpu_count()
    logger.info(f"Starting multiprocessing engine with {cores} cores.")

    with ProcessPoolExecutor(max_workers=cores) as executor:
        futures = {executor.submit(process_single_file, file, processed_dir): file for file in file_generator}
        
        for future in futures:
            try:
                result = future.result()
                results.append(result)
                logger.info(f"Processed successfully: {result['file']}")
            except Exception as e:
                logger.error(f"Error processing a file: {e}")
                
    return results