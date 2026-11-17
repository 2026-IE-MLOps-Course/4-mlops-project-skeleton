"""
test_config.py  [Tests for src/config.py]
=========================================
Stage 3   Add loader tests because config.yaml now replaces SETTINGS as the settings source
          Bad shared settings must fail before training or serving starts
Purpose   Prove src/config.py does its one job, automatically, after every change
Run       pytest tests/test_config.py   (CI runs all tests on every Pull Request)

What to check
- A valid config loads into a dictionary with resolved paths
- Missing sections, missing keys or wrong types raise an error that names the problem

Rule      Tests use small, fake data and run offline: no real data, secrets or external services
"""
