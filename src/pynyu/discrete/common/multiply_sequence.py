from __future__ import annotations


class MultiplySequence(object):
    def __init__(self, low: int, high: int):
        if low < 1:
            raise ValueError("sequence must be over positive integers")
        if high < low:
            raise ValueError("sequence must be monotonic increasing")
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
