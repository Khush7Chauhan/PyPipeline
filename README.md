# Smart File Processing Pipeline

A high-performance, asynchronous, and parallel processing pipeline built with advanced Python concepts. This project efficiently downloads, scans, processes, and archives large volumes of files without blocking I/O or overwhelming system memory.

## 🚀 Features

This project serves as a comprehensive implementation of advanced Python mechanics:

*   **Asyncio & Aiohttp:** Non-blocking asynchronous network requests to download remote files concurrently.
*   **Generators & Iterators:** Memory-efficient custom directory scanning that `yields` files one by one, capable of handling directories with hundreds of thousands of files without crashing.
*   **Multiprocessing:** Utilizes `ProcessPoolExecutor` to distribute CPU-bound file processing tasks across all available CPU cores.
*   **Object-Oriented Programming (OOP):** Abstract Base Classes (ABC) define a strict contract for `CSVProcessor`, `JSONProcessor`, and `TXTProcessor`.
*   **Custom Context Managers:** A custom `FileLockManager` prevents race conditions by simulating safe file locking during processing and moving.
*   **Decorators:** Includes `@time_it` for execution profiling and `@retry` for robust error handling.
*   **Python Fundamentals:** Comprehensive use of type hints, logging, and pure Python standard libraries.

## 🏗️ Architecture

1.  **Ingestion Phase (Network-Bound):** Fetches remote data asynchronously and drops it into `data/raw/`.
2.  **Discovery Phase (Memory-Bound):** A generator crawls the `data/raw/` directory and streams file paths to the engine.
3.  **Processing Phase (CPU-Bound):** The engine dynamically assigns the correct OOP processor based on file extension and distributes the workload across CPU cores.
4.  **Aggregation Phase:** Results are aggregated, files are safely moved to `data/processed/`, and a detailed JSON report is generated in `data/reports/`.

## 📁 Project Structure

```text
smart_pipeline/
├── data/
│   ├── raw/                 # Incoming data waiting to be processed
│   ├── processed/           # Completed data archives
│   └── reports/             # Aggregated JSON metadata reports
├── src/
│   ├── core/
│   │   ├── fetcher.py       # Asyncio download logic
│   │   └── scanner.py       # Generator-based directory traversal
│   ├── processors/
│   │   ├── base.py          # Abstract Base Class
│   │   ├── csv_proc.py      # CSV handling
│   │   ├── json_proc.py     # JSON handling
│   │   └── txt_proc.py      # TXT handling
│   ├── utils/
│   │   ├── decorators.py    # @time_it, @retry
│   │   ├── lock_manager.py  # Context managers for safe I/O
│   │   └── logger.py        # Centralized logging
│   └── engine.py            # Multiprocessing orchestrator
├── main.py                  # Pipeline entry point
├── generate_test_data.py    # Script to create dummy files
├── requirements.txt         # Dependencies (aiohttp)
└── .gitignore               # Ignored files and folders
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd smart_pipeline
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate test data:**
   Populates the `data/raw/` directory with dummy CSV, JSON, and TXT files.
   ```bash
   python generate_test_data.py
   ```

5. **Run the pipeline:**
   ```bash
   python main.py
   ```

## 📈 Checking the Output
After running the pipeline, check the `data/reports/pipeline_summary.json` file for the extracted metadata (row counts, keys, word counts). You will also see that all files have been safely transferred from `data/raw/` to `data/processed/`.
