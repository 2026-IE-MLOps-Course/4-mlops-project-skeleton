"""
test_train.py  [Tests for src/train.py]
=======================================
Stage 3   Keep training and seed tests; add training-only calibration checks if calibration is enabled
          Keep validation independent of every fitted transformation, including calibration
Purpose   Prove src/train.py does its one job, automatically, after every change
Run       pytest tests/test_train.py   (CI runs all tests on every Pull Request)

What to check
- It returns a fitted pipeline that can predict
- Same data + same seed gives the same model
- Optional calibration uses cross-validation on training data only
- Empty data or mismatched X and y raise a clear error

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
