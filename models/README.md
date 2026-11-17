# models/  [Trained model, generated]

- **Stage 3:** Keep the gated local model and also register versions for release promotion
- **Why:** A release image needs one approved version, separate from the model trained as CI evidence

- **Purpose:** holds the saved model, e.g. `model.joblib`
- **Written by:** `src/main.py` after the model passes evaluation (through `utils.py`)
- **Read by:** the API (`src/api.py`); `main.py` passes the fitted model to `src/infer.py`
- **Key idea:** ONE file with preprocessing + model together, so training and serving cannot drift apart
- **Git:** ignored. Stage 3 versions models in a model registry instead
- **Release:** deploy.yml bakes the prod model into the image
