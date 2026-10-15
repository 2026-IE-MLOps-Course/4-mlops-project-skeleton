"""
test_validate.py  [Tests for src/validate.py]
=============================================
Purpose   Prove src/validate.py does its one job, automatically, after every change
Run       pytest tests/test_validate.py   (CI runs all tests on every Pull Request)

What to check
- Valid data passes
- Missing columns, wrong types, invalid target values or broken business rules raise an error
- It never modifies the data

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
