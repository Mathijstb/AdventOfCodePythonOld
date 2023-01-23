import os

from helpers.reader import DataReader
from parameterized import parameterized
import itertools


class Day2:

    def __init__(self, input_data):
        self.data = list([[int(i) for i in line.split()] for line in input_data])

    def solve1(self):
        return sum([max(numbers) - min(numbers) for numbers in self.data])

    def solve2(self):
        result = 0
        for row in self.data:
            for (a, b) in itertools.permutations(row, 2):
                if a % b == 0:
                    result += int(a / b)
        return result


if __name__ == "__main__":
    file = os.path.join('data/input2.csv')
    data = DataReader.from_file(file)
    P = Day2(data)
    print(P.solve1())
    print(P.solve2())


class Test:
    @parameterized.expand([
        ["5 1 9 5\n"
         "7 5 3\n"
         "2 4 6 8", 18]
    ])
    def test_part_1(self, sample, expected):
        p = Day2(DataReader.from_str(sample))
        assert p.solve1() == expected

    @parameterized.expand([
        ["5 9 2 8\n"
         "9 4 7 3\n"
         "3 8 6 5", 9]
    ])
    def test_part_2(self, sample, expected):
        p = Day2(DataReader.from_str(sample))
        assert p.solve2() == expected
