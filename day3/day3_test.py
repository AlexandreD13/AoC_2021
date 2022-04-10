# Define tests in this file
from day3_helpers import part1, part2

data = ["00100", "11110", "10110", "10111",
        "10101", "01111", "00111", "11100",
        "10000", "11001", "00010", "01010"]


class TestClass:
    def test_day3_part1(self):
        assert part1(data) == 198

    def test_day3_part2(self):
        assert part2(data) == 230
