# tests/  [Automated tests, from stage 2]

- **Purpose:** prove each module does its one job, every time code changes
- **Convention:** one test file per module: `src/clean_data.py` -> `tests/test_clean_data.py`
- **Run:** `pytest` locally from the repo root; continuous integration is not part of assignment 1
- **Naming:** at least 2 `test_unit_*` and 1 `test_integration_*` tests per module
- **Coverage:** `pytest --cov=src --cov-branch`, at least 90 % branch
