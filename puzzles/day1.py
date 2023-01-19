import os

from helpers.inputs import AocData, DataParser
from helpers.types import MyRange

class Day1():

    def __init__(self, data):
        p = DataParser(MyRange.from_str, MyRange.from_str, sep=',')
        self.pairs = p.parse_data(data)

    def solve1(self):
        fully_contained = lambda r1, r2: r1.fully_contains(r2) or r2.fully_contains(r1)
        return sum(fully_contained(*r) for r in self.pairs)

    def solve2(self):
        return sum(r1.overlap(r2).size > 0 for r1,r2 in self.pairs)



sample = (
    "    [D]    \n"
    "[N] [C]    \n"
    "[Z] [M] [P]\n"
    " 1   2   3 \n"
    "\n"
    "move 1 from 2 to 1\n"
    "move 3 from 1 to 3\n"
    "move 2 from 2 to 1\n"
    "move 1 from 1 to 2"
)

class Test1():
    def test_1(self):
        data = AocData.from_str(sample)
        p = Day1(data)
        assert p.solve1() == 'CMZ'

    def test_2(self):
        data = AocData.from_str(sample)
        p = Day1(data)
        assert p.solve2() == 'MCD'


if __name__ == "__main__":
    f = os.path.join('data/1')
    data = AocData.from_file(f)
    P1 = Day1(data)
    print(P1.solve1())
    P2 = Day1(data)
    print(P2.solve2())
