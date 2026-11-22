import pytest

from speechkit.models import Speech
from speechkit.store import insert_speeches, get_stats, get_search

@pytest.fixture
def speeches():
    return [
        Speech(country="USA", session=1, year=2000, text="One two three", n_words=3),
        Speech(country="CUB", session=1, year=2000, text="Four five", n_words=2),
        Speech(country="CYP", session=2, year=2001, text="Six", n_words=1),
    ]


def test_insert_returns_count(con, speeches):
    n = insert_speeches(con, speeches)

    assert n == 3
    assert con.execute("SELECT count(*) FROM un_speeches").fetchone()[0] == 3


def test_reinsert_returns_same(con, speeches):
    n = insert_speeches(con, speeches)
    o = insert_speeches(con, speeches)

    assert n == 3, o == 3
    assert con.execute("SELECT count(*) FROM un_speeches").fetchone()[0] == 3


def test_by_year(con, speeches):
    insert_speeches(con, speeches)
    # rows = get_stats(con, by="year")
    # print(rows)
    total_2000 = get_stats(con, by="year", start=2000, end=2000)
    assert total_2000[0][3] == 5


def test_filter(con, speeches):
    insert_speeches(con, speeches)
    rows = get_stats(con, by="country", start=2000, end=2000)
    assert rows[1][0] == "USA"


def test_raises_valueError(con):
    with pytest.raises(ValueError):
        get_stats(con, by="city")

def test_get_search(con, speeches):
    insert_speeches(con, speeches)
    rows = get_search(con, term="two")
    assert rows[0][2] == "One two three"

