import duckdb
from collections.abc import Iterable
from speechkit.models import Speech

GROUPINGS = {
    "year": "year",
    "country": "country"
    }

def create_schema(con):
    with duckdb.connect("data/ungdcdb.duckdb") as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS un_speeches (
                country TEXT,
                session INT,
                year INT,
                text TEXT,
                n_words INT,
                PRIMARY KEY (country, year)
            )
        """)

def insert_speeches(con: duckdb.DuckDBPyConnection, speeches: Iterable[Speech]):
    count = 0
    with con.appender("un_speeches", action="upsert") as appender:
        for s in speeches:
            appender.append_row(s.country, s.session, s.year, s.text, s.n_words)
            count += 1
    return count

def get_stats(con: duckdb.DuckDBPyConnection,
              by: str = "year",
              start: int | None = None,
              end: int | None = None,
              country: str | None = None
              ) -> list[tuple[str, int]]:
    if by not in GROUPINGS:
        raise ValueError(f"by must be one of {sorted(GROUPINGS)}, not {by!r}")
    cols = GROUPINGS[by]
    sql = f'SELECT {cols}, count(*), count(DISTINCT country), sum(n_words) FROM un_speeches'
    params = []
    if start is not None:
        sql += " WHERE year >= ?"
        params.append(start)
    if end is not None:
        if start is not None:
            sql += " AND year <= ?"
        else:
            sql += " WHERE year <= ?"
        params.append(end)
    if country is not None:
        if start is not None or end is not None:
            sql += " AND country = ?"
        else:
            sql += " WHERE country = ?"
        params.append(country)
    sql += f" GROUP BY {cols} ORDER BY {cols}"        
    return con.execute(sql, params).fetchall()
