from plates import is_valid

def test_correct_length():
    assert is_valid("AA3456") == True
    assert is_valid("A") == False
    assert is_valid("ABCDE12") == False

def test_no_punction():
    assert is_valid("Asse10") == True
    assert is_valid("Asser!") == False

def test_first_two_digit():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False

def test_no_alpha_after_number():
    assert is_valid("AA123") == True
    assert is_valid("AA12A") == False

def test_the_first_number():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
