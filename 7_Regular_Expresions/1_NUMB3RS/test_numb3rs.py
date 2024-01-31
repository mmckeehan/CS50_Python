from numb3rs import validate

def test_validate_numb():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255") == False
    assert validate("256.1.1.1.1") == False

def test_validate_other():
    assert validate("4002:3c52:0b8e:0000:0000:3a6f:abcd") == False
    assert validate("cat.dog.frog.owl") == False

def test_validate_b1():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.1.1.1") == False

def test_validate_b2():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.256.1.1") == False

def test_validate_b3():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.1.256.1") == False

def test_validate_b4():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.256") == False
