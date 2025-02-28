from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-1, -1) == -2

def test_sub():
    assert sub(3, 1)==2
    assert sub(5, 4)==1
    assert sub(10,11) == -1