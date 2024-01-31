from jar import Jar


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"
"""    jar.deposit(11)
    jar.withdraw(9)
    assert str(jar) == '🍪🍪'"""
