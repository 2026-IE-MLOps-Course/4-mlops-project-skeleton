"""
config.py  [Settings loader]
============================
Stage 3   Read settings moved out of src/main.py into the previously unused config.yaml
          Training and the API share the loader without importing the training entry point
Purpose   Read config.yaml once, check required keys and types, resolve file paths
Input     Path to config.yaml
Output    Plain Python dictionary of settings
Used by   main.py (training), api.py (serving), notebooks

Why it matters
- Fail fast: a typo in config stops the run at second one, not after training
- The API imports settings from here, NOT from main.py, so serving never depends on training code

Tests     tests/test_config.py
"""
