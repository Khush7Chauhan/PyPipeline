import asyncio
import json
from pathlib import Path

from src.core.fetcher import fetch_all_remote_data
from src.core.scanner import generate_target_files
from src.engine import run_multiprocessing_engine
from src.utils.logger import logger
from src.utils.decorator import time_it

BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "data" / "reports"

@time_it
def generate_summary_report(results: list[dict]):
    """Creates a final summary report."""
    report_path = REPORTS_DIR / "pipeline_summary.json"
    
    summary = {
        "total_files_processed": len(results),
        "details": results
    }
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=4)
        
    logger.info(f"Summary report generated at {report_path.name}")

if __name__ == "__main__":
    logger.info("=== STARTING SMART PIPELINE ===")
    
    for d in [RAW_DIR, PROCESSED_DIR, REPORTS_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    sample_urls = [
        "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv",
        "https://jsonplaceholder.typicode.com/todos"
    ]
    asyncio.run(fetch_all_remote_data(sample_urls, RAW_DIR))

    extensions_to_process = ('.csv', '.json', '.txt')
    file_generator = generate_target_files(RAW_DIR, extensions_to_process)
    results = run_multiprocessing_engine(file_generator, PROCESSED_DIR)
    generate_summary_report(results)
    
    logger.info("=== PIPELINE COMPLETED ===")