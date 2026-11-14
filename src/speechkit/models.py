from dataclasses import dataclass

@dataclass(frozen=True)
class Speech:
    country: str
    session: int
    year: int
    text: str
    n_words: int

# s = Speech(country='FRA', session=14, year=1959, text='Example text.')
# print(s.speech)
