"""
load_data.py  [Step 1: LOAD]
============================
Purpose   Read the raw dataset into a DataFrame, exactly as it is on disk
Input     Path to the raw file, passed from SETTINGS in main.py
Output    Raw pandas DataFrame, untouched
Called by main.py          Uses   utils.py (file reading)
Next      clean_data.py

Contract  load_raw_data(raw_data_path: Path) -> pd.DataFrame
Errors    Missing file: FileNotFoundError; folder: IsADirectoryError; empty file: ValueError
          Empty includes a file with no bytes or with a header but no rows

Why it matters
- One entry point for data: swap CSV for a database or API later without touching other files
- Read only: the raw file is never modified, so every run is reproducible
- Fail fast with a clear message if the file is missing, a folder, or empty

Tests     tests/test_load_data.py (stage 2)
"""
