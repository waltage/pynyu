from __future__ import annotations

from copy import deepcopy
from fractions import Fraction

from pynyu.discrete.common.multiply_sequence import MultiplySequence

SequenceComponents = dict[int, int]


class CombinatorialNumber(object):
    def __init__(self, initial: int | MultiplySequence | CombinatorialNumber = None):
        self.numerator: list[MultiplySequence] = []
        self.denominator: list[MultiplySequence] = []
        if initial:
            if isinstance(initial, int):
                self.numerator = [MultiplySequence(initial, initial)]
            elif isinstance(initial, MultiplySequence):
                self.numerator = [deepcopy(initial)]
            elif isinstance(initial, CombinatorialNumber):
                self.numerator = deepcopy(initial.numerator)
                self.denominator = deepcopy(initial.denominator)
            else:
                raise TypeError(
                    "initial must be an int, MultiplySequence, or CombinatorialNumber"
                )

    def __rmul__(
        self, other: int | MultiplySequence | CombinatorialNumber
    ) -> CombinatorialNumber:
        print("r")
        return self.__mul__(other)

    def __mul__(
        self, other: int | MultiplySequence | CombinatorialNumber
    ) -> CombinatorialNumber:
        print("m")
        result = deepcopy(self)
        if isinstance(other, int):
            result.numerator.append(MultiplySequence(other, other))
        elif isinstance(other, MultiplySequence):
            result.numerator.append(deepcopy(other))
        elif isinstance(other, CombinatorialNumber):
            result.numerator.extend(deepcopy(other.numerator))
            result.denominator.extend(deepcopy(other.denominator))

        result.numerator.sort(key=lambda x: (x.low, x.high))
        result.denominator.sort(key=lambda x: (x.low, x.high))
        print("pre:", result)
        result.simplify()
        print("post:", result)
        return result

    def __truediv__(
        self, other: int | MultiplySequence | CombinatorialNumber
    ) -> CombinatorialNumber:
        result = deepcopy(self)
        print("div")
        if isinstance(other, int):
            result.denominator.append(MultiplySequence(other, other))
        elif isinstance(other, MultiplySequence):
            result.denominator.append(deepcopy(other))
        elif isinstance(other, CombinatorialNumber):
            result.numerator.extend(deepcopy(other.denominator))
            result.denominator.extend(deepcopy(other.numerator))

        result.numerator.sort(key=lambda x: (x.low, x.high))
        result.denominator.sort(key=lambda x: (x.low, x.high))
        result.simplify()
        return result

    @staticmethod
    def __collect_sequence_range(
        sequence: list[MultiplySequence],
    ) -> SequenceComponents:
        """Calculates the unique integers, and their frequency, of a list of MultiplySequences."""
        result_dict = dict()
        for part in sequence:
            for i in range(part.low, part.high + 1):
                if i not in result_dict:
                    result_dict[i] = 0
                result_dict[i] += 1
        return result_dict

    def __cancel_numer_denom(self) -> tuple[SequenceComponents, SequenceComponents]:
        """Reduces any shared components in the numerator and denominator (cancellation)."""
        numer = CombinatorialNumber.__collect_sequence_range(self.numerator)
        denom = CombinatorialNumber.__collect_sequence_range(self.denominator)
        all_keys = set(numer.keys()).union(set(denom.keys()))
        for i in all_keys:
            num_count = numer.get(i, 0)
            den_count = denom.get(i, 0)
            if num_count > 0 and den_count > 0:
                numer[i] -= 1
                if numer[i] == 0:
                    del numer[i]
                denom[i] -= 1
                if denom[i] == 0:
                    del denom[i]
        return numer, denom

    @staticmethod
    def __split_sequence_range(seq: SequenceComponents) -> list[MultiplySequence]:
        """Converts SequenceComponents to a list of contiguous MultiplySequences."""
        result = []
        if len(seq) == 0:
            return result

        while len(seq) > 0:
            next_seq = None
            for i in sorted(seq.keys()):
                if not next_seq:
                    # first value
                    next_seq = MultiplySequence(i, i)
                elif next_seq.high == i - 1:
                    # contiguous, extend the current sequence
                    next_seq.high = i
                else:
                    # non-contiguous, add the prior sequence and create new from i
                    result.append(next_seq)
                    next_seq = MultiplySequence(i, i)

                seq[i] -= 1
                if seq[i] == 0:
                    del seq[i]
            if next_seq:
                result.append(next_seq)
        return result

    def simplify(self):
        """Reduce the numerator and denominator through cancellation and range simplification."""
        num_dict, den_dict = self.__cancel_numer_denom()
        self.numerator = CombinatorialNumber.__split_sequence_range(num_dict)
        self.denominator = CombinatorialNumber.__split_sequence_range(den_dict)

    @property
    def value(self) -> Fraction:
        num_result = 1
        for part in self.numerator:
            num_result *= part.value
        den_result = 1
        for part in self.denominator:
            den_result *= part.value
        return Fraction(num_result, den_result)

    def __str__(self):
        num = " * ".join([str(_) for _ in self.numerator])
        den = " * ".join([str(_) for _ in self.denominator])
        if len(self.numerator) > 0 and len(self.denominator) > 0:
            return f"({num}) / ({den})"
        elif len(self.numerator) == 0 and len(self.denominator) > 0:
            return f"1 / ({den})"
        elif len(self.numerator) > 0 and len(self.denominator) == 0:
            return f"{num}"
