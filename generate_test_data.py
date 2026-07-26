import json
import csv
from pathlib import Path

raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

print("Generating test files...")

for i in range(1, 6):
    with open(raw_dir / f"test_data_{i}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "value"])
        writer.writerows([[1, "Alice", 100 * i], [2, "Bob", 200 * i]])

    with open(raw_dir / f"test_config_{i}.json", "w") as f:
        json.dump({"setting_a": i, "setting_b": True, "items": [1, 2, 3]}, f)

    with open(raw_dir / f"test_log_{i}.txt", "w") as f:
        f.write(f"Log entry {i}: System initialized successfully.\n")
        f.write(f"Log entry {i}: No errors detected.\n")

print(f"Successfully generated 15 test files in {raw_dir.resolve()}")