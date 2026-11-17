"""
fetch_prod_model.py  [Resolve the promoted release model]
=========================================================
Purpose   Resolve the Weights & Biases (W&B) alias prod to a concrete version, e.g. model:v7
Input     config.yaml + W&B read credentials and account name
Output    Download models/model.joblib and print MODEL_VERSION for deploy.yml
Run by    deploy.yml publish-image, and you to check the promoted version

Why it matters
- An image ships an exact version, never a moving label
- Read only: never log, promote or change aliases in W&B

Tests     tests/test_fetch_prod_model.py (fake W&B API, no network)
"""
