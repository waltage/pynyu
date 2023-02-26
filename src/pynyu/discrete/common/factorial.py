from __future__ import annotations

from copy import deepcopy


class MultiplySequence(object):
    def __init__(self, low: int, high: int):
        if low < 1:
            raise ValueError("sequence must be over positive integers")
        if high <= low:
            raise ValueError("sequence must be strictly increasing")
        if not isinstance(low, int) or not isinstance(high, int):
            raise TypeError("sequence must be over integers")
        self.low = low
        self.high = high

    @property
    def value(self) -> int:
        result = 1
        for i in range(self.low, self.high + 1):
            result *= i
        return result

    def __str__(self) -> str:
        if self.low <= 2:
            return f"{self.high}!"
        else:
            return " * ".join([f"{i}" for i in range(self.high, self.low - 1, -1)])


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
            result.__sequences.sort(lambda x: (x.low, x.high))
            return result
        elif isinstance(other, MultiplySequence):
            result.__sequences.append(other)
            result.__sequences.sort(lambda x: (x.low, x.high))
            return result
        elif isinstance(other, int):
            # find if this int can be extended on one of the sequences
            for _ in result.__sequences:
                if other == _.low - 1:
                    _.low -= 1
                    result.__sequences.sort(lambda x: (x.low, x.high))
                    return result
                elif other == _.high + 1:
                    _.high += 1
                    result.__sequences.sort(lambda x: (x.low, x.high))
                    return result
            # not contiguous, create a new one
            result.__sequences.append(MultiplySequence(other, other))
            result.__sequences.sort(lambda x: (x.low, x.high))
            return result
        raise TypeError(
            "can only multiply Factorial with Factorial, MultipleSequence, or int"
        )
