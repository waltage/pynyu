from pynyu.discrete.common.factorial import MultiplySequence

import pytest


def test_bad_sequence_non_positive():
    with pytest.raises(ValueError):
        MultiplySequence(-1, 100)


def test_bad_sequence_non_monotonic_increasing():
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
