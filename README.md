# MLOps Project Skeleton (reference only)

This repo is a **map, not a codebase**. Every file is a placeholder: no code, only a short note on
what the file does, where it sits in the pipeline and which files it talks to.

## Stages = branches

| Branch | Stage | Sessions | What it adds |
|---|---|---|---|
| `main` | 1. Kickoff | 1 to 3 | Folder structure, business case, one placeholder per pipeline step |
| `stage-2-modular` (you are here) | 2. Modular code | 4 to 9 | Tests, style and test settings, first CI (Continuous Integration) workflow |
| `stage-3-cicd` | 3. CI/CD | 10 to 14 | Config loader, logging, experiment tracking, API, Docker, deployment |

## What stage 2 adds

- **Working modules:** each `src/` file now holds real code for your use case (here: still a note)
- **Settings in one place:** a `SETTINGS` dictionary at the top of `src/main.py`, same keys as `config.yaml`
- **Tests:** one test file per module in `tests/`, run with `pytest`
- **Style:** `.flake8` so VS Code and CI flag the same issues
- **CI:** `.github/workflows/ci.yml` runs style checks and tests on every Pull Request

> **Windows:** always run inside the activated environment (`conda activate <your-env>`, then `python -m src.main`), or use `conda run -n <your-env> python -m src.main`. Calling the environment's `python.exe` directly, for example from a VS Code interpreter that did not activate the environment, can crash with `0xC06D007F` during model calibration because Windows cannot find the environment's maths libraries.

## Quality loop

```text
 edit code --> flake8 (style) --> pytest (tests) --> python -m src.main (end to end)
     ^                                                         |
     +----------- Pull Request: CI reruns flake8 + pytest <----+
```

## Stage 2 structure (new items marked +)

```text
.
├── README.md / config.yaml / environment.yml / .env.example / .gitignore / LICENSE
├── .flake8                   + style checker settings
├── pytest.ini                + test runner settings
├── .github/
│   ├── pull_request_template.md
│   └── workflows/ci.yml      + style and tests on every Pull Request
├── notebooks/                # now imports from src/
├── src/  main, load_data, clean_data, validate, features, train, evaluate, infer, utils
├── data/  raw/ processed/ inference/
├── models/  reports/
└── tests/
    ├── __init__.py           +
    └── test_<module>.py      + one per src/ module
```
