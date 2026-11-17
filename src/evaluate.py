"""
evaluate.py  [Step 6: EVALUATE]
===============================
Purpose   Score the fitted pipeline on data it has never seen
Input     Fitted pipeline + X_eval, y_eval (validation split; test split once, at the end)
Output    Dictionary of plain numbers, e.g. {"pr_auc": 0.61, "roc_auc": 0.84}
Called by main.py          Feeds  the validation quality gate already checked inside main()

Contract  evaluate_model(model: Pipeline, X_eval: pd.DataFrame, y_eval: pd.Series,
                         problem_type: str) -> dict[str, float]
Returns   Dictionary of plain Python floats for the chosen problem type

Why it matters
- Never score on training data: it hides overfitting
- Metric choice follows the business goal and problem type passed from SETTINGS
- Plain numbers are easy to log, compare between runs and turn into a go/no-go decision

Tests     tests/test_evaluate.py (stage 2)
"""
