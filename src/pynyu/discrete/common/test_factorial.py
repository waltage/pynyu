import math

from pynyu.discrete.common.factorial import Factorial
from pynyu.discrete.common.multiply_sequence import MultiplySequence


def test_factorial_basic():
    f = Factorial(10)
    assert str(f) == "10!"
    assert f.value == math.factorial(10)


def test_factorial_multipy_factorial():
    f1 = Factorial(5)
    f2 = Factorial(10)
    f3a = f1 * f2
    assert f3a.value == math.factorial(5) * math.factorial(10)
    assert str(f3a) == "5! * 10!"

    # check string invariant representation (sorted)
    f3b = f2 * f1
    assert f3b.value == math.factorial(5) * math.factorial(10)
    assert str(f3b) == "5! * 10!"

    # check integer multiplcation high
    f4 = f1 * 6
    assert f4.value == math.factorial(6)
    assert str(f4) == "6!"

    f4 = f1 * 3
    assert f4.value == math.factorial(5) * 3
    assert str(f4) == "5! * 3"

    s1 = MultiplySequence(3, 6)
    f5 = f1 * s1
    assert f5.value == math.factorial(5) * 3 * 4 * 5 * 6
    assert str(f5) == "5! * 6 * 5 * 4 * 3"
