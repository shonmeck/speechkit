import duckdb
from speechkit.loader import load_speeches
from speechkit.store import create_schema, insert_speeches

def ingest():
    with duckdb.connect("data/ungdcdb.duckdb") as con:
        create_schema(con)
        n = insert_speeches(con, load_speeches("data/raw"))
        print(n, "speeches loaded")

def stats():
    return