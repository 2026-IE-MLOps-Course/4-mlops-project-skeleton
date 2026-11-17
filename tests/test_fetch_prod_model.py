"""
test_fetch_prod_model.py  [Tests for scripts/fetch_prod_model.py]
================================================================
Purpose   Prove the release downloads the exact promoted model and reports its version
Run       pytest tests/test_fetch_prod_model.py

What to check
- Read registry names and the model path from config.yaml
- Resolve prod to a concrete version with a fake Weights & Biases (W&B) API
- Download the expected file to models/model.joblib in a temporary folder
- Print MODEL_VERSION and write it to the GitHub Actions output file
- Missing settings, alias or model file stop the release with a clear error

Rule      Tests use fake services and temporary folders, never a network or real credentials
"""
