import os

from helpers.inputs import DataReader

class Day1():

    def __init__(self, data):
        self.data = data

    def solve1(self):
        return 3

    def solve2(self):
        return -1

sample = (
    "1122"
)

class Test1():
    def test_1(self):
        data = DataReader.from_str(sample)
        p = Day1(data)
        assert p.solve1() == 3

    def test_2(self):
        data = DataReader.from_str(sample)
        p = Day1(data)
        assert p.solve2() == -1


if __name__ == "__main__":
    f = os.path.join('data/input1.csv')
    data = DataReader.from_file(f)
    P = Day1(data)
    print(P.solve1())
    print(P.solve2())
