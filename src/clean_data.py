"""
clean_data.py  [Step 2: CLEAN]
==============================
Stage 3   Keep the helper contract, including every inference row; also reuse it in the API
          Replace print() with shared logging so batch and live cleaning stay traceable
Purpose   Make raw data consistent so every later step behaves predictably
Input     Raw DataFrame + target column name
Output    Clean DataFrame; target required only in training, no rows dropped during inference
Called by main.py (training) and api.py (stage 3, same cleaning for live requests)
Next      validate.py

Contract  clean_dataframe(df_raw: pd.DataFrame, target_column: str | None = None) -> pd.DataFrame
Modes     Target given: training, require the target; None: inference, never drop rows

Why it matters
- Stateless fixes only: column names and index reset; duplicates and missing targets filtered in training only
- Nothing that LEARNS from data (means, bins, scaling): that belongs in features.py, after the split
- Same input always gives the same output, so it is safe to rerun
- Report how many rows were dropped: a sudden jump signals an upstream problem

Tests     tests/test_clean_data.py (stage 2)
"""
