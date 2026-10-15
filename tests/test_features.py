"""
test_features.py  [Tests for src/features.py]
=============================================
Purpose   Prove src/features.py does its one job, automatically, after every change
Run       pytest tests/test_features.py   (CI runs all tests on every Pull Request)

What to check
- It returns an UNFITTED transformer
- After fitting on sample data, the output has the expected number of columns
- Unknown or missing column lists are handled clearly

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
