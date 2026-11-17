# reports/  [Pipeline outputs, generated]

- **Stage 3:** Keep batch prediction files and log experiment plots through tracking.py
- **Why:** Separate local outputs from shared run history without changing the prediction schema

- **Purpose:** batch predictions (`predictions.csv`); experiment plots are logged through `tracking.py`
- **Written by:** `src/main.py` (predictions come from `src/infer.py`)
- **Rule:** keep the ID column so every prediction can be joined back to its source record
