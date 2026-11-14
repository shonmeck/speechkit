import os

DB_PATH = os.environ.get("SPEECHKIT_DB", "data/ungdcdb.duckdb")
RAW_PATH = os.environ.get("SPEECHKIT_RAW", "raw/data")
LOG_LEVEL = os.environ.get("SPEECHKIT_LOG_LEVEL", "INFO")
