# Define tests in this file
from day5_helpers import part1, part2

data = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1",
        "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4",
        "0,0 -> 8,8", "5,5 -> 8,2"]


class TestClass:
    def test_day5_part1(self):
        assert part1(data) == 5

    def test_day5_part2(self):
        assert part2(data) == 12
