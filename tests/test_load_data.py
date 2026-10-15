"""
test_load_data.py  [Tests for src/load_data.py]
===============================================
Purpose   Prove src/load_data.py does its one job, automatically, after every change
Run       pytest tests/test_load_data.py   (CI runs all tests on every Pull Request)

What to check
- A valid file loads with the expected rows and columns
- A missing path, a folder or an empty file raises a clear error
- The raw file is unchanged after loading

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
