"""
test_main.py  [Tests for src/main.py]
=====================================
Purpose   Prove src/main.py does its one job, automatically, after every change
Run       pytest tests/test_main.py   (CI runs all tests on every Pull Request)

What to check
- Split math: sizes add up, no row appears in two splits, class balance is kept
- End to end in a temporary folder: the pipeline runs and writes the model and predictions
- main.py contains no cleaning, feature or model logic of its own

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
