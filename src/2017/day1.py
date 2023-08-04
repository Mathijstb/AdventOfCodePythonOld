import os
from unittest import TestCase

from parameterized import parameterized
import regex


class Day1:

    def __init__(self, data):
        self.data = data

    def solve1(self):
        pattern = regex.compile(r"(.)\1")
        matches = regex.findall(pattern, self.data, overlapped=True)
        if self.data[0] == self.data[-1]:
            matches.append(self.data[0])
        return sum(int(i) for i in matches)

    def solve2(self):
        length = len(self.data)
        shift = int(length / 2)
        matches = []
        for i, value in enumerate(self.data):
            other = self.data[(i + shift) % length]
            if value == other:
                matches.append(value)
        return sum(int(i) for i in matches)


if __name__ == "__main__":
    print(Day1('1234').solve1())
    print(Day1('1234').solve2())


class Test(TestCase):
    @parameterized.expand([
        ["1122", 3],
        ["1111", 4],
        ["1234", 0],
        ["91212129", 9]
    ])
    def test_part_1(self, sample, expected):
        p = Day1(sample)
        assert p.solve1() == expected

    @parameterized.expand([
        ["1212", 6],
        ["1221", 0],
        ["123425", 4],
        ["123123", 12],
        ["12131415", 4]
    ])
    def test_part_2(self, sample, expected):
        p = Day1(sample)
        assert p.solve2() == expected
