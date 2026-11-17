"""
infer.py  [Step 7: INFER]
=========================
Purpose   Turn new, unseen records into predictions with the saved pipeline
Input     Fitted pipeline + new data (DataFrame, same feature columns, no target)
Output    DataFrame with a fixed schema: "prediction" (+ optional "probability"), same index as input
Called by main.py (batch, writes reports/predictions.csv) and api.py (stage 3, live requests)

Contract  run_inference(model: Pipeline, X_infer: pd.DataFrame, include_proba: bool = False) -> pd.DataFrame
Returns   Same index as X_infer, input unchanged; "prediction" and optional "probability" columns

Why it matters
- No training here: inference is reused unchanged by the API, so batch and live results match
- Fixed output columns: downstream teams can rely on them
- Keep the input index (and ID) so predictions join back to source records

Tests     tests/test_infer.py (stage 2)
"""
