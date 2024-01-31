from working import convert
import pytest

def test_convert_hours():
    with pytest.raises(ValueError):
        convert("09AM - 05:PM")
        convert("9:65 - 17:00")
    assert convert ("09:00 AM to 05:00 PM") == ("09:00 to 17:00")
