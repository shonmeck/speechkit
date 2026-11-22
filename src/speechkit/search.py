def make_snippet(speech: str, term: str, size: int = 3) -> str | None:
    speech_list = speech.split()
    for i, word in enumerate(speech_list):
        if term.lower() in word.lower():
            start = max(i - size, 0)
            return " ".join(speech_list[start : i + size + 1])
    return None

def get_hits(speech: str, term: str) -> int:
    return speech.lower().count(term.lower())
