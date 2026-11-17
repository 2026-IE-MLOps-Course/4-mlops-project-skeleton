# MLOps Project Skeleton (reference only)

This repo is a **map, not a codebase**. Every file is a placeholder: no code, only a short note on
what the file does, where it sits in the pipeline and which files it talks to.

Start from the helper's end state: `SETTINGS` in `src/main.py`, unused `config.yaml`, and `print()` with
`TODO: replace print with logging`. The quality gate already runs in `main()`; no continuous integration
or service secrets are required at that point. Stage 3 notes explain what moves or is added and why.

API means application programming interface. CI/CD means continuous integration and continuous deployment.
W&B means Weights & Biases. PR means Pull Request. MD5 is the file checksum used by Data Version Control (DVC).

## Stages = branches

| Branch | Stage | Sessions | What it adds |
|---|---|---|---|
| `main` | 1. Kickoff | 1 to 3 | Folder structure, business case, one placeholder per pipeline step |
| `stage-2-modular` | 2. Modular code | 4 to 9 | Tested modules, SETTINGS, local style checks and a quality gate in main() |
| `stage-3-cicd` (you are here) | 3. CI/CD | 10 to 14 | Config loader, logging, data versioning (DVC), experiment tracking, API, Docker, release-gated deployment |

## What stage 3 adds

- **Config, not code:** `SETTINGS` moves to `config.yaml`, read once by `src/config.py`; secrets go to `.env`
- **Logging:** `src/logger.py` replaces `print()` with timestamped logs to console and `logs/`
- **Data versioning:** `dvc.yaml` runs the pipeline as one stage; the data lives on DagsHub and Git keeps only the `.dvc` pointers and `dvc.lock`
- **Experiment tracking:** `src/tracking.py` records runs, metrics and model versions (e.g. Weights & Biases, W&B)
- **Quality gate:** keep the decision already made in `main()`; move its settings to `config.yaml` and reuse the comparison through `evaluate.py`
- **Serving:** `src/api.py` exposes the model as a web API (FastAPI)
- **Containers:** a two-stage `Dockerfile` installs `conda-lock.yml` exactly; the release image carries the code and ONE promoted model
- **CI/CD:** add automation to the local commands from assignment 1; `ci.yml` checks every Pull Request (lint, `dvc pull` + `dvc repro` with the quality gate, 90 % branch coverage, Docker build); `deploy.yml` ships a GitHub Release from `main` (guard, CI again, image with the W&B `prod` model, smoke test, push to `ghcr.io`, Render deploys that image); rollback redeploys an older release image

> **Windows:** always run inside the activated environment (`conda activate <your-env>`, then `python -m src.main`), or use `conda run -n <your-env> python -m src.main`. Calling the environment's `python.exe` directly, for example from a VS Code interpreter that did not activate the environment, can crash with `0xC06D007F` during model calibration because Windows cannot find the environment's maths libraries.

## Architecture

```text
 TRAINING (python -m src.main)                         SERVING (uvicorn src.api:app)
 config.yaml + .env --> config.py, logger.py           client --HTTP--> api.py
          |                                                              |
 load -> clean -> validate -> split -> features             clean -> validate -> infer
          -> train -> evaluate -> QUALITY GATE                           ^
                                       | pass                            | loads model
          test audit -> save + register (tracking.py)    models/model.joblib baked into release image
                                                       (W&B alias prod only for local development)

 DELIVERY  (a person moves the W&B alias prod: WHAT ships; a person publishes a Release from main: WHEN)
 feature --PR--> dev --PR--> main --Release--> deploy.yml: guard -> ci -> publish-image -> deploy
              ci.yml      ci.yml               prod model baked into one image, smoke test,
                                               ghcr.io, Render pulls that image, live smoke test
```

## Stage 3 structure (new items marked +)

```text
.
├── README.md / LICENSE / .gitignore / .flake8 / pytest.ini
├── config.yaml               # now read by src/config.py (all non-secret settings)
├── .env.example              # now lists real secret names
├── environment.yml           # human-readable dependencies
├── conda-lock.yml            + exact versions for CI and Docker
├── dvc.yaml, dvc.lock        + pipeline stage and data hashes
├── .dvcignore               + what DVC never scans
├── .dvc/                    + created by dvc init (remote settings; local secrets ignored)
├── Dockerfile                + serving container recipe
├── .dockerignore             + what never enters the image
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       ├── ci.yml            # extended quality gate
│       ├── deploy.yml        + release-gated deployment
│       └── release-guard.yml + a release must come from main
├── scripts/
│   ├── fetch_prod_model.py   + resolve prod to a concrete model version
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
│   ├── test_fetch_prod_model.py + tests the release model download offline
│   └── test_config.py, test_tracking.py, test_api.py  + (plus stage 2 tests)
├── logs/                     + pipeline log files (generated)
└── data/ models/ notebooks/ reports/
```
