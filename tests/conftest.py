import duckdb
import pytest

from speechkit.store import create_schema


@pytest.fixture
def con():
    with duckdb.connect(":memory:") as con:
        create_schema(con)
        yield con
