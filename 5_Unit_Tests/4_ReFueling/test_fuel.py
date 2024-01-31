from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("100/100") == 100
    assert convert("50/100") == 50
    assert convert("0/100") == 0
    with pytest.raises(ValueError):
        convert("cat/100")
        convert("101/100")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
