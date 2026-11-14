import duckdb
from collections.abc import Iterable
from speechkit.models import Speech

def create_schema(con):
    with duckdb.connect("data/ungdcdb.duckdb") as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS un_speeches (
                country TEXT,
                session INT,
                year INT,
                text TEXT,
                PRIMARY KEY (country, year)
            )
        """)

def insert_speeches(con: duckdb.DuckDBPyConnection, speeches: Iterable[Speech]):
    count = 0
    with con.appender("un_speeches", action="upsert") as appender:
        for s in speeches:
            appender.append_row(s.country, s.session, s.year, s.text)
            count += 1
    return count

def run_queries():
    return
