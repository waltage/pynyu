from __future__ import annotations

from fractions import Fraction
from math import factorial

from pynyu.discrete.common.combinatorial_number import CombinatorialNumber
from pynyu.discrete.common.multiply_sequence import MultiplySequence


def test_simplify():
    c1 = CombinatorialNumber()
    c1.numerator = [MultiplySequence(2, 5), MultiplySequence(7, 10)]
    c1.denominator = [MultiplySequence(4, 8)]

    c1.simplify()
    assert c1.value == (2 * 3 * 4 * 5 * 7 * 8 * 9 * 10) / (4 * 5 * 6 * 7 * 8)
    assert str(c1) == "(3! * 10 * 9) / (6)"

    c2 = CombinatorialNumber()
    c2.numerator = [
        MultiplySequence(2, 10),
        MultiplySequence(2, 12),
        MultiplySequence(2, 14),
    ]
    c2.simplify()
    assert str(c2) == "14! * 12! * 10!"


def test_multiply_c_c():
    c1 = CombinatorialNumber()
    c1.numerator = [MultiplySequence(2, 5)]
    c1n = 2 * 3 * 4 * 5
    c1.denominator = [MultiplySequence(2, 8)]
    c1d = 2 * 3 * 4 * 5 * 6 * 7 * 8

    c2 = CombinatorialNumber()
    c2.numerator = [MultiplySequence(5, 10)]
    c2n = 5 * 6 * 7 * 8 * 9 * 10
    c2.denominator = [MultiplySequence(2, 4)]
    c2d = 2 * 3 * 4
    c3 = c2 * c1

    assert c3.value == (c1n * c2n) / (c1d * c2d)
    assert str(c3) == "(5 * 10 * 9) / (4!)"


def test_divide_c_c():
    c1 = CombinatorialNumber()
    c1.numerator = [MultiplySequence(2, 5)]
    c1n = 2 * 3 * 4 * 5
    c1.denominator = [MultiplySequence(2, 8)]
    c1d = 2 * 3 * 4 * 5 * 6 * 7 * 8

    c2 = CombinatorialNumber()
    c2.numerator = [MultiplySequence(5, 10)]
    c2n = 5 * 6 * 7 * 8 * 9 * 10
    c2.denominator = [MultiplySequence(2, 4)]
    c2d = 2 * 3 * 4

    c3 = c2 / c1
    assert c3.value == Fraction(c2n * c1d, c1n * c2d)
    assert str(c3) == "(10 * 9 * 8 * 7 * 6 * 5 * 8 * 7 * 6) / (4!)"


def test_multiply_c_ms():
    c1 = CombinatorialNumber()
    c1.numerator = [MultiplySequence(2, 5)]

    ms1 = MultiplySequence(2, 10)

    x = c1 * ms1
    assert x.value == factorial(5) * factorial(10)
    assert str(x) == "10! * 5!"


def test_divide_c_ms():
    c1 = CombinatorialNumber()
    c1.numerator = [MultiplySequence(2, 5)]
    ms1 = MultiplySequence(2, 10)

    x = c1 / ms1
    assert x.value == Fraction(factorial(5), factorial(10))
    assert str(x) == "1 / (10 * 9 * 8 * 7 * 6)"


def test_multiply_c_i():
    c1 = CombinatorialNumber()
    c1.numerator = [MultiplySequence(2, 5)]

    c2 = c1 * 6
    assert c2.value == factorial(6)
    assert str(c2) == "6!"


def test_divide_c_i():
    c1 = CombinatorialNumber()
    c1.numerator = [MultiplySequence(2, 5)]

    c2 = c1 / 5
    assert c2.value == factorial(4)
    assert str(c2) == "4!"
