"""
validate.py  [Step 3: VALIDATE, the data quality gate]
======================================================
Stage 3   Keep validation before expensive steps; main.py now passes rules from config.yaml
          Replace print() with shared logging and reuse validation for live API requests
Purpose   Check schema, types and business rules BEFORE expensive steps run
Input     Clean DataFrame + the rules (required columns, allowed target values, ranges)
Output    True if valid, otherwise a clear error that stops the pipeline
Called by main.py (training) and api.py (stage 3, every live request)
Next      the split in main.py

Baseline  validate_dataframe(df: pd.DataFrame, required_columns: list[str],
                             target_column: str | None = None) -> bool
Returns   True, or raises ValueError; validate data without changing it
Extra     Stage 3 may add optional checks with defaults; preserve the helper contract above

Why it matters
- Garbage in, garbage out: stop bad data at the door, not deep inside training
- Validate, never fix. Fixing belongs in clean_data.py
- Rules live in config, so they are versioned and easy to change

Tests     tests/test_validate.py (stage 2)
"""
