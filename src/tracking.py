"""
tracking.py  [Experiment tracking and model registry]
=====================================================
Purpose   Record each run: settings, metrics, plots, data and model versions (e.g. Weights & Biases, W&B)
Called by main.py (training runs) and api.py (batched prediction logs, monitoring)
Settings  config.yaml (project, run name, what to log) + .env (API key)

Why it matters
- Every model is traceable to the exact data, code and settings that produced it
- Registered model versions with aliases (e.g. "prod") let the API load the approved model
- Safe when switched off: every function does nothing if tracking is disabled, so tests and CI run offline

Tests     tests/test_tracking.py
"""
