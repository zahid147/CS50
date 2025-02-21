import pytest
from fuel import convert, gauge

def test_correct():
    assert convert('3/4') == 75 and gauge(75) == "75%"
    assert convert('1/4') == 25 and gauge(25) == "25%"
    assert convert('1/100') == 1 and gauge(1) == "E"
    assert convert('99/100') == 99 and gauge(99) == "F"

def test_value_error():
    with pytest.raises(ValueError):
        assert convert('a/2')
        assert convert('2/a')
        assert convert('3/2')

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        assert convert('2/0')