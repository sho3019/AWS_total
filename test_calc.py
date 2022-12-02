import pytest

from Python.calc import calc

def test_calc():
    assert calc("plus", 1, 1) == 2
    assert calc("minus", 3, 5) == -2
    assert calc("cross", 2, 9) == 18
    assert calc("devision", 7, 2) == 3.5
    assert calc("plus", 1, -1) == 0
    assert calc("aa", 1, 4) == "error"