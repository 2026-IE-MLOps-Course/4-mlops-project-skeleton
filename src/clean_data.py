"""
clean_data.py  [Step 2: CLEAN]
==============================
Purpose   Make raw data consistent so every later step behaves predictably
Input     Raw DataFrame + target column name
Output    Clean DataFrame; target required in training, every row preserved during inference
Called by main.py (training) and api.py (stage 3, same cleaning for live requests)
Next      validate.py

Contract  clean_dataframe(df_raw: pd.DataFrame, target_column: str | None = None) -> pd.DataFrame
Modes     Target given: training, require the target; None: inference, never drop rows

Why it matters
- Stateless fixes only: normalize headers and reset the index
- Training may remove duplicates and missing targets; inference never drops rows
- Nothing that LEARNS from data (means, bins, scaling): that belongs in features.py, after the split
- Same input always gives the same output, so it is safe to rerun
- Report how many rows were dropped: a sudden jump signals an upstream problem

Tests     tests/test_clean_data.py (stage 2)
"""
