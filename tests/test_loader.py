import logging

import pytest

from speechkit.loader import load_speeches


@pytest.fixture
def sample_folder(tmp_path):
    (tmp_path / "ITA_47_1992.txt").write_text(
        "Spaghetti is not the only pasta.", encoding="utf-8"
    )
    (tmp_path / "YUG_1992.txt").write_text(
        "The non-alignment movement was awesome.", encoding="utf-8"
    )
    nested = tmp_path / "Session 2" / "Way Down in the Hole"
    nested.mkdir(parents=True)
    (nested / "ALB_2_1967.txt").write_text("Burek is not only for Turks.")
    (tmp_path / ".DS_Store-to-UTF-8.txt").write_text(
        "Dysfunction is for all.", encoding="utf-8"
    )
    return tmp_path


def test_loads_valid_file(sample_folder):
    speeches = list(load_speeches(str(sample_folder)))

    assert len(speeches) == 2

    assert speeches[0].country == "ITA"
    assert speeches[1].country == "ALB"

    assert speeches[0].year == 1992
    assert speeches[1].year == 1967

    assert speeches[0].session == 47
    assert speeches[1].session == 2

    assert speeches[0].text == "Spaghetti is not the only pasta."
    assert speeches[1].text == "Burek is not only for Turks."


def test_logs_skipped_files(sample_folder, caplog):
    caplog.set_level(logging.WARNING)

    list(load_speeches(str(sample_folder)))

    assert len(caplog.records) == 2
    assert ".DS_Store-to-UTF-8.txt" in caplog.text
