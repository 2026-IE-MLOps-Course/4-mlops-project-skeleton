"""
evaluate.py  [Step 6: EVALUATE]
===============================
Stage 3   Move the inline metric comparison from main() into check_quality_gate; main still stops the run
          Read its thresholds from config.yaml and log metrics so automated checks can reuse the decision
Purpose   Score the fitted pipeline on data it has never seen
Input     Fitted pipeline + X_eval, y_eval (validation split; test split once, at the end)
Output    Dictionary of plain numbers, e.g. {"pr_auc": 0.61, "roc_auc": 0.84}
Called by main.py          Feeds  the quality gate and experiment tracking
Gate      check_quality_gate compares the chosen metric with its configured minimum or maximum
Optional  evaluate_calibration reports probability calibration metrics and bins for tracking.py

Contract  evaluate_model(model: Pipeline, X_eval: pd.DataFrame, y_eval: pd.Series,
                         problem_type: str) -> dict[str, float]
Returns   Dictionary of plain Python floats for the chosen problem type

Why it matters
- Never score on training data: it hides overfitting
- Metric choice follows the business goal and problem type (set in config)
- Plain numbers are easy to log, compare between runs and turn into a go/no-go decision

Tests     tests/test_evaluate.py (stage 2)
"""
