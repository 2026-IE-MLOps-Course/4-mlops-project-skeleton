"""
test_train.py  [Tests for src/train.py]
=======================================
Purpose   Prove src/train.py does its one job, automatically, after every change
Run       pytest tests/test_train.py   (CI runs all tests on every Pull Request)

What to check
- It returns a fitted pipeline that can predict
- Same data + same seed gives the same model
- Empty data or mismatched X and y raise a clear error

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
