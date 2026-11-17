"""
fetch_prod_model.py  [Resolve the promoted release model]
=========================================================
Stage 3   A release must fetch the approved registry model rather than ship the model from CI
          Resolve the moving prod alias once, so the image carries a fixed model version
Purpose   Resolve the Weights & Biases (W&B) alias prod to a concrete version, e.g. model:v7
Input     config.yaml + W&B read credentials and account name
Output    Download models/model.joblib, print MODEL_VERSION and write the workflow output for deploy.yml
Run by    deploy.yml publish-image, and you to check the promoted version

Why it matters
- An image ships an exact version, never a moving label
- Read only: never log, promote or change aliases in W&B

Tests     tests/test_fetch_prod_model.py (fake W&B API, no network)
"""
