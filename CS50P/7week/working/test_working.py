from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        assert convert('09:00 AM - 17:00 PM')
    assert convert('9 AM to 5 PM') == "09:00 to 17:00"

def test_minute():
    with pytest.raises(ValueError):
        assert convert('9:60 AM to 5:30 PM')
    with pytest.raises(ValueError):
        assert convert('9 AM to 5:90 PM')
    assert convert('10:30 PM to 8:50 AM') == "22:30 to 08:50"
