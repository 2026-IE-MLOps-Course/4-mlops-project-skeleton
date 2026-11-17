# data/inference/  [New data to score]

- **Stage 3:** DVC now records the batch input version alongside the training data
- **Why:** Restore the recorded file before scoring, so predictions can be traced to their inputs

- **Purpose:** new, unlabelled records the trained model has never seen
- **Read by:** `src/main.py`, then passed to `src/infer.py`
- **Rule:** same columns as training data, without the target
- **Git:** Versioned with DVC (Data Version Control): Git keeps `opioid_infer_01.csv.dvc`, a pointer with the file's md5; the file lives on DagsHub. `dvc pull` downloads the exact bytes; never re-save it (line endings change the md5)
