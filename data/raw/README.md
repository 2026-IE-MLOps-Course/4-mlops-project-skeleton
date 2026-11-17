# data/raw/  [Original data, read only]

- **Stage 3:** The path moves from SETTINGS to config.yaml and DVC records the input version
- **Why:** Restore the recorded file before loading it, so every run starts from the same bytes

- **Purpose:** the dataset exactly as received
- **Read by:** `src/load_data.py` (path set in `config.yaml`)
- **Rule:** never edit or overwrite these files. Every run starts from them
- **Git:** Versioned with DVC (Data Version Control): Git keeps `opioid_raw_data.csv.dvc`, a pointer with the file's md5; the file lives on DagsHub. `dvc pull` downloads the exact bytes; never re-save it (line endings change the md5)
