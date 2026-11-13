import duckdb
from collections.abc import Iterable
from speechkit.models import Speech

def create_schema():
    with duckdb.connect("ungdcdb.duckdb") as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS un_speeches (
                country TEXT,
                session INT,
                year INT,
                text TEXT,
                PRIMARY KEY (country, year)
            )
        """)

def insert_speeches(speeches: Iterable[Speech]):
    with duckdb.connect("ungdcdb.duckdb") as con:
        with con.appender("un_speeches") as appender:
            appender.append_rows((s.country, s.session, s.year, s.text) for s in speeches)

def run_queries():
    return