"""
test_infer.py  [Tests for src/infer.py]
=======================================
Stage 3   Keep index, schema and input-preservation tests while the API starts reusing inference
          Batch and live predictions must keep the same schema and one result per input row
Purpose   Prove src/infer.py does its one job, automatically, after every change
Run       pytest tests/test_infer.py   (CI runs all tests on every Pull Request)

What to check
- Output has the fixed columns (prediction, optional probability)
- Output index matches the input index
- Wrong input types or a broken model raise a clear error

Rule      Tests use small, fake in-memory data or temporary folders: never your real data files
"""
