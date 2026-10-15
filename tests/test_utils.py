"""
test_utils.py  [Tests for src/utils.py]
=======================================
Purpose   Prove src/utils.py does its one job, automatically, after every change
Run       pytest tests/test_utils.py   (CI runs all tests on every Pull Request)

What to check
- CSV and model files round-trip: what you save is what you load
- Missing folders are created, missing files raise a clear error

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
