# logs/  [Run history, generated]

- **Stage 3:** Complete TODO: replace print with logging and add a configured log file
- **Why:** Keep timestamped run evidence for local debugging and automated checks

- **Purpose:** timestamped log files, e.g. `pipeline.log`, for post-run audit and debugging
- **Written by:** every module through `src/logger.py` (path and level set in `config.yaml`)
- **Git:** ignored. Console logs are visible on the host; a configured file keeps a local audit trail
