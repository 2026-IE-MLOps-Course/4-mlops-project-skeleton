"""
test_evaluate.py  [Tests for src/evaluate.py]
=============================================
Purpose   Prove src/evaluate.py does its one job, automatically, after every change
Run       pytest tests/test_evaluate.py   (CI runs all tests on every Pull Request)

What to check
- Metrics are plain numbers in the expected range
- The right metrics are used for each problem type
- An object without .predict() is rejected

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
