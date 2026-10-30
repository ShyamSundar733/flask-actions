from app import add, multiply, divide

def test_add():
    assert add(10,20) == 30

def test_multiply():
    assert multiply(5, 4) == 20

def test_divide():
    assert divide(10, 2) == 5