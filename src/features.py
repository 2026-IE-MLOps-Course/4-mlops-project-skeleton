"""
features.py  [Step 4: FEATURE RECIPE]
=====================================
Stage 3   Keep the unfitted recipe; main.py now passes feature lists from config.yaml instead of SETTINGS
          Replace print() with shared logging without changing the agreed transformations
Purpose   Define HOW raw columns become model inputs (impute, bin, encode, scale)
Input     Lists of column names per transformation (from config)
Output    An UNFITTED scikit-learn ColumnTransformer (a recipe, not transformed data)
Called by main.py          Used by train.py (fits it) and infer.py (applies it, inside the saved model)

Contract  get_feature_preprocessor(<column lists named in TEAM_BRIEF.md>) -> ColumnTransformer
Returns   An UNFITTED recipe; parameter names come from the agreed notebook feature groups

Why it matters
- Never call .fit() here. Fitting happens in train.py on the train split only: no data leakage
- One recipe for training AND inference, so both process data identically
- Swap features through config lists, not code edits

Tests     tests/test_features.py (stage 2)
"""
