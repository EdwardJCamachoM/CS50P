from plates import *

def test_is_length():
    assert is_length("AA") == True
    assert is_length("AAAAAAA") == False

def test_is_start():
    assert is_start("AA") == True
    assert is_start("11") == False

def test_is_numbers_last():
    assert is_numbers_last("11") == True
    assert is_numbers_last("1A") == False

def test_no_leading_zero():
    assert no_leading_zero("0") ==  False
    assert no_leading_zero("1") == True

def test_is_no_punctuation():
    assert is_no_punctuation("234ac.") == False
    assert is_no_punctuation("AA123") == True