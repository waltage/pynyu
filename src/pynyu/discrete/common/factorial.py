from __future__ import annotations

from copy import deepcopy

from pynyu.discrete.common.multiply_sequence import MultiplySequence


class Factorial(object):
    def __init__(self, value: int):
        self.__sequences = [MultiplySequence(2, value)]

    def __str__(self):
        return " * ".join([f"{s}" for s in self.__sequences])

    @property
    def value(self) -> int:
        result = 1
        for _ in self.__sequences:
            result *= _.value
        return result

    def __rmul__(self, other: Factorial | MultiplySequence | int) -> Factorial:
        return self.__mul__(other)

    def __mul__(self, other: Factorial | MultiplySequence | int) -> Factorial:
        result = deepcopy(self)
        if isinstance(other, Factorial):
            result.__sequences.extend(other.__sequences)
            result.__sequences.sort(key=lambda x: (x.low, x.high))
            return result
        elif isinstance(other, MultiplySequence):
            result.__sequences.append(other)
            result.__sequences.sort(key=lambda x: (x.low, x.high))
            return result
        elif isinstance(other, int):
            # find if this int can be extended on one of the sequences
            for _ in result.__sequences:
                if other == _.low - 1:
                    _.low -= 1
                    result.__sequences.sort(key=lambda x: (x.low, x.high))
                    return result
                elif other == _.high + 1:
                    _.high += 1
                    result.__sequences.sort(key=lambda x: (x.low, x.high))
                    return result
            # not contiguous, create a new one
            result.__sequences.append(MultiplySequence(other, other))
            result.__sequences.sort(key=lambda x: (x.low, x.high))
            return result
        raise TypeError(
            "can only multiply Factorial with Factorial, MultipleSequence, or int"
        )
