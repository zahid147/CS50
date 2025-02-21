from um import count

def test():
    assert count('um') == 1
    assert count('um, hello, um, world') == 2
    assert count('yummy') == 0
    assert count('Um, thanks, um...') == 2