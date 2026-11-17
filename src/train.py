"""
train.py  [Step 5: TRAIN]
=========================
Stage 3   Read model parameters from config.yaml instead of SETTINGS and replace print() with logging
          Optional calibration still learns from training data only, so validation remains independent
Purpose   Bundle the feature recipe + the algorithm into ONE pipeline and fit it
Optional  calibrate_pipeline uses training-only cross-validation to calibrate classification probabilities
Input     X_train, y_train + unfitted recipe from features.py + model settings
Output    One fitted pipeline (preprocessing + model), saved by main.py as models/model.joblib
Called by main.py          Next   evaluate.py

Baseline  train_model(X_train: pd.DataFrame, y_train: pd.Series, preprocessor: ColumnTransformer,
                      problem_type: str, model_params: dict | None = None, random_state: int = 42) -> Pipeline
Returns   Fitted Pipeline with steps "preprocess" and "model"; fit on training data only

Why it matters
- .fit() runs on the train split only, so validation and test metrics stay honest
- One artifact for preprocessing + model: what you test is exactly what you deploy
- Model choice and hyperparameters come from config: swap models without rewriting code
- Fixed random seed: same data, same result

Tests     tests/test_train.py (stage 2)
"""
