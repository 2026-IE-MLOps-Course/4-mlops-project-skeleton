"""
validate.py  [Step 3: VALIDATE, the data quality gate]
======================================================
Purpose   Check schema, types and business rules BEFORE expensive steps run
Input     Clean DataFrame + the rules (required columns, allowed target values, ranges)
Output    True if valid, otherwise a clear error that stops the pipeline
Called by main.py (training) and api.py (stage 3, every live request)
Next      the split in main.py

Contract  validate_dataframe(df: pd.DataFrame, required_columns: list[str],
                             target_column: str | None = None) -> bool
Returns   True, or raises ValueError; validate data without changing it
Extra     Business rules may add parameters with defaults, agreed in TEAM_BRIEF.md

Why it matters
- Garbage in, garbage out: stop bad data at the door, not deep inside training
- Validate, never fix. Fixing belongs in clean_data.py
- main.py passes rules from SETTINGS; extra rule parameters have defaults

Tests     tests/test_validate.py (stage 2)
"""
