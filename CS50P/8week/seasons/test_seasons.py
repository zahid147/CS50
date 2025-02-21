from seasons import func
import pytest

def test_format():
    with pytest.raises(SystemExit):
        assert func("2002/06/29") == "Invalid date"
    with pytest.raises(SystemExit):
        assert func("29/06/2002") == "Invalid date"
    assert func("2002-06-29") == "Eleven million, ninety-six thousand, six hundred forty"

def test_output():
    assert func("2002-06-29") == "Eleven million, ninety-six thousand, six hundred forty"
    assert func("2004-01-04") == "Ten million, two hundred ninety-eight thousand, eight hundred eighty"