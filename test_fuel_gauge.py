from fuel_gauge import *
import pytest


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


def test_convert():
    assert convert(1, 4) == 25
    assert convert(3, 3) == 100 
    with pytest.raises(ValueError):
        convert(4, 3)
    with pytest.raises(ZeroDivisionError):
        convert(4, 0)