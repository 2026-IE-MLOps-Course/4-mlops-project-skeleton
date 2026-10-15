"""
test_tracking.py  [Tests for src/tracking.py]
=============================================
Purpose   Prove src/tracking.py does its one job, automatically, after every change
Run       pytest tests/test_tracking.py   (CI runs all tests on every Pull Request)

What to check
- With tracking disabled, every function runs and does nothing
- No test needs internet access or a real account

Rule      Tests use small, fake data and run offline: no real data, secrets or external services
"""
