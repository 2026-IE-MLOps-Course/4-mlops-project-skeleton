"""
api.py  [Serving: the model as a web API]
=========================================
Purpose   Answer prediction requests over HTTP with the approved model
Run       uvicorn src.api:app --reload   then open /docs
Startup   load settings (config.py), logging (logger.py), model (local file or model registry)

Request flow
    client --POST /predict--> data contract check (types, required fields)
              --> clean_data --> validate --> infer --> JSON response
    GET /health --> "model loaded?" (used by Docker, the cloud host and smoke_test.py)

Rule      NO NEW ML LOGIC HERE. Reuse clean_data, validate and infer, so live and batch results match
Monitoring log requests (logger.py) and batches of predictions (tracking.py); never break serving

Tests     tests/test_api.py
"""
