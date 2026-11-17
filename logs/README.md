# logs/  [Run history, generated]

- **Purpose:** timestamped log files, e.g. `pipeline.log`, for post-run audit and debugging
- **Written by:** every module through `src/logger.py` (path and level set in `config.yaml`)
- **Git:** ignored. Console logs are visible on the host; a configured file keeps a local audit trail
