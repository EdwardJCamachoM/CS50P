from bank import value

def test_hello():
    greeting = "hello"
    assert value(greeting) == 0

def test_h():
    assert value("how are you") == 20
    assert value("hi there") == 20

def test_no_h():
    assert value("what's up") == 100
    assert value("good morning") == 100

def test_empty():
    assert value("") == 100

def test_upper():
    assert value("SUP MY NIG") == 100