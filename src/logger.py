"""
logger.py  [One logging setup]
==============================
Purpose   Configure logging ONCE: timestamp, level, module name, to console and a log file
Called by main.py and api.py at startup (only the entry points)
Used by   every module through: logger = logging.getLogger(__name__)
Settings  config.yaml (log level, log file path)

Why it matters
- Replaces print(): every message has a time, a severity and a source
- Console logs show up in Docker and the cloud host; the file keeps an audit trail per run
"""
