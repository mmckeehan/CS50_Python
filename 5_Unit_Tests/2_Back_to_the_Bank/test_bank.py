from bank import value

def test_value_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("hiya") == 20

def test_value_no_h():
    assert value("bonjor") == 100
    assert value("Wasssssa") == 100
    assert value("sup") == 100

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
