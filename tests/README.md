# tests/  [Automated tests, from stage 2]

- **Purpose:** prove each module does its one job, every time code changes
- **Convention:** one test file per module: `src/clean_data.py` -> `tests/test_clean_data.py`
- **Stage 3:** keep assignment 1 tests and add config, tracking and API tests with fake services
- **Why:** the new continuous integration workflow runs the local checks automatically on Pull Requests
- **Run:** `pytest` from the repo root; this skeleton contains teaching notes, not working tests
- **Naming:** at least 2 `test_unit_*` and 1 `test_integration_*` tests per module
- **Coverage:** `pytest --cov=src --cov-branch`, at least 90 % branch
