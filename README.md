# MLOps Project Skeleton (reference only)

This repo is a **map, not a codebase**. Every file is a placeholder: no code, only a short note on
what the file does, where it sits in the pipeline and which files it talks to.

## Stages = branches

| Branch | Stage | Sessions | What it adds |
|---|---|---|---|
| `main` | 1. Kickoff | 1 to 3 | Folder structure, business case, one placeholder per pipeline step |
| `stage-2-modular` | 2. Modular code | 4 to 9 | Tests, style and test settings, first CI (Continuous Integration) workflow |
| `stage-3-cicd` (you are here) | 3. CI/CD | 10 to 14 | Config loader, logging, experiment tracking, API, Docker, deployment |

## What stage 3 adds

- **Config, not code:** `SETTINGS` moves to `config.yaml`, read once by `src/config.py`; secrets go to `.env`
- **Logging:** `src/logger.py` replaces `print()` with timestamped logs to console and `logs/`
- **Experiment tracking:** `src/tracking.py` records runs, metrics and model versions (e.g. Weights & Biases, W&B)
- **Quality gate:** the model is saved only if its validation metric beats a threshold set in config
- **Serving:** `src/api.py` exposes the model as a web API (FastAPI)
- **Containers:** `Dockerfile` + `conda-lock.yml` package the API with exact versions
- **CI/CD:** `ci.yml` checks every Pull Request; `deploy.yml` ships each GitHub Release to the cloud

## Architecture

```text
 TRAINING (python -m src.main)                         SERVING (uvicorn src.api:app)
 config.yaml + .env --> config.py, logger.py           client --HTTP--> api.py
          |                                                              |
 load -> clean -> validate -> split -> features             clean -> validate -> infer
          -> train -> evaluate -> QUALITY GATE                           ^
                                       | pass                            | loads model
          test audit -> save + register (tracking.py) ---> model.joblib / model registry

 DELIVERY
 feature branch --PR--> dev --PR--> main --Release--> deploy.yml --> cloud host --> smoke_test.py
                   ci.yml      ci.yml    (lint, tests, pipeline, Docker build)
```

## Stage 3 structure (new items marked +)

```text
.
├── README.md / LICENSE / .gitignore / .flake8 / pytest.ini
├── config.yaml               # now read by src/config.py (all non-secret settings)
├── .env.example              # now lists real secret names
├── environment.yml           # human-readable dependencies
├── conda-lock.yml            + exact versions for CI and Docker
├── Dockerfile                + serving container recipe
├── .dockerignore             + what never enters the image
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       ├── ci.yml            # extended quality gate
│       └── deploy.yml        + release-gated deployment
├── scripts/
│   ├── smoke_test.py         + checks a running API
│   └── sample_request.json   + example API payload
├── src/
│   ├── config.py             + read and check config.yaml
│   ├── logger.py             + one logging setup
│   ├── tracking.py           + experiment tracking and model registry
│   ├── api.py                + web API for live predictions
│   └── main, load_data, clean_data, validate, features, train, evaluate, infer, utils
├── tests/
│   ├── conftest.py           + shared, offline test setup
│   └── test_config.py, test_tracking.py, test_api.py  + (plus stage 2 tests)
├── logs/                     + pipeline log files (generated)
└── data/ models/ notebooks/ reports/
```
