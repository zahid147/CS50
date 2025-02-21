from numb3rs import validate

def test_dot():
    assert validate("10:12:134:123") == False
    assert validate("255.0.10.66") == True

def test_alpha():
    assert validate("a.b.c.d") == False
    assert validate("a.22.b.13") == False
    assert validate("111.222.111.222") == True
    assert validate("cat") == False

def test_out_of_ange():
    assert validate("256.256.256.256") == False
    assert validate("256.255.0.1") == False
    assert validate("255.111.222.500") == False
    assert validate("255.233.211.222") == True