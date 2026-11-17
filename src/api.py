"""
api.py  [Serving: the model as a web API]
=========================================
Stage 3   Reuse the batch prediction path as an application programming interface (API)
          Clients can score new records without starting the training pipeline
Purpose   Answer prediction requests over HTTP with the approved model
Run       uvicorn src.api:app --reload   then open /docs
Startup   load settings (config.py), logging (logger.py), model = models/model.joblib
          baked into the release image (MODEL_SOURCE=local), or the W&B alias prod for local development
Interface /docs is the only user interface

Request flow
    client --POST /predict--> data contract check (types, required fields)
              --> clean_data --> validate --> infer --> JSON response
    GET /health --> model loaded? + git commit + model version (used by Docker, Render and smoke_test.py)

Rule      NO NEW ML LOGIC HERE. Reuse clean_data, validate and infer, so live and batch results match
Monitoring log requests and send batches of predictions to W&B from api.py; never break serving

Tests     tests/test_api.py
"""
