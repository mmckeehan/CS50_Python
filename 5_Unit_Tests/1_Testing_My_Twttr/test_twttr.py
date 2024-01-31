from twttr import shorten


def test_shorten():
    assert shorten("hello!") == "hll!"
    assert shorten("German") == "Grmn"
    assert shorten("12345") == "12345"
    assert shorten("taAeEiIoOuUyYT") == "tyYT"
