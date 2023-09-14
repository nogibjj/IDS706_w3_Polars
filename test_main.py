"""
Test goes here, for four functions

"""

from mylib.calculator import *


def test_all():
    assert add(1, 2) == 3
    assert subtract(2, 1) == 1
    assert multiply(2,3) == 6
    assert divide(3,2) == 1.5
