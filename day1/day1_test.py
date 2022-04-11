# Define tests in this file
from day1_helpers import import_input, part1, part2

filename = "data/input_test.txt"
data = import_input(filename)


class TestClass:
    def test_day1_part1(self):
        assert part1(data) == 7

    def test_day1_part2(self):
        assert part2(data) == 5
