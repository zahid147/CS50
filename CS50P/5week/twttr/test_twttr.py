from twttr import shorten

def test_vowel():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_consonent():
    assert shorten("myrrh") == "myrrh"
    assert shorten("MYRRH") == "MYRRH"

def test_number():
    assert shorten("420") == "420"

def test_punction():
    assert shorten("Hmm!?") == "Hmm!?"

def test_mixed():
    assert shorten("CS50!") == "CS50!cd"
    assert shorten("EngIn69") == "ngn69"