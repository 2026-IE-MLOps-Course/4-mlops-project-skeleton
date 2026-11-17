"""
load_data.py  [Step 1: LOAD]
============================
Stage 3   Keep the data-loading boundary; main.py gets the path from config.yaml instead of SETTINGS
          Replace print() with shared logging; DVC restores the input before the loader reads it
Purpose   Read the raw dataset into a DataFrame, exactly as it is on disk
Input     Path to the raw file (config: paths.raw_data)
Output    Raw pandas DataFrame, untouched
Called by main.py          Uses   utils.py (file reading)
Next      clean_data.py

Baseline  load_raw_data(raw_data_path: Path) -> pd.DataFrame
Baseline  The helper raises FileNotFoundError for missing files, IsADirectoryError for folders,
          and ValueError for empty files, including header-only files; data restoration does not change that contract

Why it matters
- One entry point for data: swap CSV for a database or API later without touching other files
- Read only: the raw file is never modified, so every run is reproducible
- Fail fast with a clear message if the file is missing, a folder, or empty

Tests     tests/test_load_data.py (stage 2)
"""
