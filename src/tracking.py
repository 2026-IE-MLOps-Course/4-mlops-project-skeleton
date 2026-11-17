"""
tracking.py  [Experiment tracking and model registry]
=====================================================
Purpose   Record each run: settings, metrics, plots, data and model versions (e.g. Weights & Biases, W&B)
Called by main.py (training runs); api.py owns its separate batched monitoring logs
Settings  config.yaml, wandb section (project, run name, what to log) + .env (API key)

Why it matters
- Every model is traceable to the exact data, code and settings that produced it
- A person promotes a version with the alias prod; the next release ships that exact version
- Each run records the Git commit and the raw-data md5 (lineage)
- Safe when switched off: every function does nothing if tracking is disabled, so tests and CI run offline

Tests     tests/test_tracking.py
"""
