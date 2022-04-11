# Define tests in this file
from day3_helpers import import_input, part1, part2

filename = "data/input_test.txt"
data = import_input(filename)


class TestClass:
    def test_day3_part1(self):
        assert part1(data) == 198

    def test_day3_part2(self):
        assert part2(data) == 230
