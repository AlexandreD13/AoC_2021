# Define tests in this file
from day5_helpers import import_input, part1, part2

filename = "data/input_test.txt"
data = import_input(filename)


class TestClass:
    def test_day5_part1(self):
        assert part1(data) == 5

    def test_day5_part2(self):
        assert part2(data) == 12
