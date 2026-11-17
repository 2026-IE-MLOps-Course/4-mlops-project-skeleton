"""
features.py  [Step 4: FEATURE RECIPE]
=====================================
Purpose   Define HOW raw columns become model inputs (impute, bin, encode, scale)
Input     Column lists agreed in TEAM_BRIEF.md, passed from SETTINGS in main.py
Output    An UNFITTED scikit-learn ColumnTransformer (a recipe, not transformed data)
Called by main.py          Used by train.py (fits it) and infer.py (applies it, inside the saved model)

Contract  get_feature_preprocessor(<column lists named in TEAM_BRIEF.md>) -> ColumnTransformer
Returns   An UNFITTED recipe; parameter names come from the agreed notebook feature groups

Why it matters
- Never call .fit() here. Fitting happens in train.py on the train split only: no data leakage
- One recipe for training AND inference, so both process data identically
- main.py passes the agreed feature lists from SETTINGS; do not invent shared parameter names

Tests     tests/test_features.py (stage 2)
"""
