# data/raw/  [Original data, read only]

- **Purpose:** the dataset exactly as received
- **Read by:** `src/load_data.py` (path set in `config.yaml`)
- **Rule:** never edit or overwrite these files. Every run starts from them
- **Git:** Versioned with DVC (Data Version Control): Git keeps `opioid_raw_data.csv.dvc`, a pointer with the file's md5; the file lives on DagsHub. `dvc pull` downloads the exact bytes; never re-save it (line endings change the md5)
