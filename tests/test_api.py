"""
test_api.py  [Tests for src/api.py]
===================================
Purpose   Prove src/api.py does its one job, automatically, after every change
Run       pytest tests/test_api.py   (CI runs all tests on every Pull Request)

What to check
- /health reports healthy with a model and unhealthy without one
- /predict returns one prediction per record with the fixed schema
- Missing or unknown fields and broken business rules are rejected with clear errors

Rule      Tests use small, fake data and run offline: no real data, secrets or external services
"""
