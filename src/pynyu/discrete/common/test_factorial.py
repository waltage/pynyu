import math
from pynyu.discrete.common.factorial import MultiplySequence
from pynyu.discrete.common.factorial import Factorial
import pytest


def test_bad_sequence_non_positive():
    with pytest.raises(ValueError):
        MultiplySequence(-1, 100)


def test_bad_sequence_non_increasing():
    with pytest.raises(ValueError):
        MultiplySequence(10, 4)


def test_bad_sequence_types():
    with pytest.raises(TypeError):
        MultiplySequence(1.2, 4)

    with pytest.raises(TypeError):
        MultiplySequence(1, 20.3)


def test_sequence_str_true_factorial():
    seq = MultiplySequence(1, 10)
    assert str(seq) == "10!"


def test_sequence_str_mult_sequence():
    seq = MultiplySequence(3, 10)
    assert str(seq) == "10 * 9 * 8 * 7 * 6 * 5 * 4 * 3"


def test_sequence_value():
    seq = MultiplySequence(1, 5)
    assert seq.value == 5 * 4 * 3 * 2 * 1

    seq = MultiplySequence(2, 4)
    assert seq.value == 4 * 3 * 2


def test_factorial_basic():
    f = Factorial(10)
    assert str(f) == "10!"
    assert f.value == math.factorial(10)


def test_factorial_multipy_factorial():
    f1 = Factorial(5)
    f2 = Factorial(10)
    f3 = f1 * f2
    assert f3.value == math.factorial(5) * math.factorial(10)
    assert str(f3) == "5! * 10!"

    f4 = f1 * 6
    assert f4.value == math.factorial(6)
    assert str(f4) == "6!"

    s1 = MultiplySequence(3, 6)
    f5 = f1 * s1
    assert f5.value == math.factorial(5) * 3 * 4 * 5 * 6
    assert str(f5) == "5! * 6 * 5 * 4 * 3"
