from twttr import chop

def test_vowels():
    assert chop("avenue") == "vn"
    assert chop("AVENUE") == "VN"

def test_absolutes():
    assert chop("pty") == "pty"
    assert chop("aeiou") == ""

def test_symbols_numbers():
    assert chop("cs50") == "cs50"

def test_empty():
    assert chop("") == ""