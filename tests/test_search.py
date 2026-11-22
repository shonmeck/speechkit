from speechkit.search import make_snippet, get_hits

speech = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def test_snippet():
    snip1 = make_snippet(speech=speech, term="lorem")
    assert snip1 == "Lorem ipsum dolor sit"

    snip2 = make_snippet(speech=speech, term="incididunt")
    assert snip2 == "do eiusmod tempor incididunt ut labore et"

    snip3 = make_snippet(speech=speech, term="laborum.")
    assert snip3 == "anim id est laborum."

def test_hits():
    hits1 = get_hits(speech="mississippi", term="iss")
    assert hits1 == 2

    hits2 = get_hits(speech="How again many AGAIN times aGaIn do I need again to ask AGAIN?",
                     term="again")
    assert hits2 == 5

    hits3 = get_hits(speech="You never know what someone will say.",
                     term="knowledge")
    assert hits3 == 0

