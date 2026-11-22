import logging
from collections.abc import Iterator
from pathlib import Path

from speechkit.models import Speech

logger = logging.getLogger(__name__)


def load_speeches(folder: str) -> Iterator[Speech]:
    for path in sorted(Path(folder).rglob("*.txt")):
        try:
            country, session, year = path.stem.split("_")
            session = int(session)
            year = int(year)
            text = path.read_text(encoding="utf-8")
            n_words = len(text.split())
        except (ValueError, UnicodeDecodeError, OSError) as err:
            logger.warning("Skipping %s: %s", path, err)
            continue
        yield Speech(
            country=country, session=session, year=year, text=text, n_words=n_words
        )
