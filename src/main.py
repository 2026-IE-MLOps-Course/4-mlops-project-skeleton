"""
main.py  [Step 0: ORCHESTRATOR]
================================
Stage 3   Move SETTINGS to config.yaml and replace print() with logging; keep the existing quality-gate decision
          Add tracking around the same pipeline so data versions and automated runs remain traceable
Purpose   Run the whole training pipeline, in order, with one command: python -m src.main
Owns      Step order, train/validation/test split, the quality gate decision, passing data between steps
Never     Config parsing (config.py), logging setup details (logger.py), tracking details (tracking.py),
          or any cleaning, feature or model logic

Flow
    config.yaml + .env --> config.py, logger.py, tracking.py (start run)
                                      |
    data/raw --> load_data --> clean_data --> validate --> SPLIT (train / val / test)
                                                                   |
                           features (unfitted recipe) --> train (fit on train only)
                                                                   |
                                         evaluate (validation) --> QUALITY GATE
                                                                   | fail: stop, nothing saved
                                                                   v pass
                         test audit (once) --> save models/model.joblib + register (tracking.py)
                                                                   |
    data/inference --> load -> clean -> validate -> infer --> reports/predictions.csv
                                                                   |
                                                      tracking.py (finish run)

Contract  split_data(X: pd.DataFrame, y: pd.Series, test_size: float, val_size: float,
                     random_state: int, stratify: bool) -> tuple
Returns   X_train, X_val, X_test, y_train, y_val, y_test, in that order
Entry     main() -> None

Why it matters
- Split BEFORE anything is fitted: no leakage. Validation decides, test only audits
- A model that fails the gate is never saved, so it can never be deployed
- One entry point: you, your teammates and CI run exactly the same command

Tests     tests/test_main.py
"""
