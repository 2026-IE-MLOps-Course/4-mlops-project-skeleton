"""
main.py  [Step 0: ORCHESTRATOR]
================================
Purpose   Run the whole pipeline, in order, with one command: python -m src.main
Owns      Step order, the split, SETTINGS and the validation quality gate before saving the model
Never     Cleaning, feature or model logic. main.py only CALLS other modules

Flow
                 SETTINGS here (config.yaml remains unused until stage 3)
                                      |
    data/raw --> load_data --> clean_data --> validate --> SPLIT (train / val / test)
                                                                   |
                           features (unfitted recipe) --> train (fit on train only)
                                                                   |
                                              evaluate (validation split)
                                                                   |
                              quality gate in main() --> save --> models/model.joblib
                                                                   |
    data/inference --> infer --> reports/predictions.csv

Contract  split_data(X: pd.DataFrame, y: pd.Series, test_size: float, val_size: float,
                     random_state: int, stratify: bool) -> tuple
Returns   X_train, X_val, X_test, y_train, y_val, y_test, in that order
Entry     main() -> None

Why it matters
- Split BEFORE anything is fitted, so no information leaks from test data into training
- Data passes as explicit variables between stateless steps: no hidden state
- One local entry point for you and your teammates; automated checks arrive in stage 3
- Keep print() messages with TODO: replace print with logging until stage 3

Tests     tests/test_main.py (stage 2)
"""
