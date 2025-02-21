from bank import value

def test_vowel():
    assert value("Sup sir?") == 100
    assert value("Sup mam?") == 100

def test_consonent():
    assert value("Hey sir") == 20
    assert value("Hey mam") == 20

def test_number():
    assert value("Hello sir") == 0
    assert value("Hello mam") == 0