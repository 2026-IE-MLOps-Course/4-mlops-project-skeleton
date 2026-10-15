"""
test_clean_data.py  [Tests for src/clean_data.py]
=================================================
Purpose   Prove src/clean_data.py does its one job, automatically, after every change
Run       pytest tests/test_clean_data.py   (CI runs all tests on every Pull Request)

What to check
- Column names are standardized
- Duplicates and rows without a target are removed, the index is reset
- A missing target column raises a clear error
- Running it twice gives the same result

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
