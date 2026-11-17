"""
test_features.py  [Tests for src/features.py]
=============================================
Stage 3   Keep the unfitted-recipe tests while feature lists move from SETTINGS to config.yaml
          Moving settings must not change transformations or learn from validation data
Purpose   Prove src/features.py does its one job, automatically, after every change
Run       pytest tests/test_features.py   (CI runs all tests on every Pull Request)

What to check
- It returns an UNFITTED transformer
- After fitting on sample data, the output has the expected number of columns
- Unknown or missing column lists are handled clearly

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
