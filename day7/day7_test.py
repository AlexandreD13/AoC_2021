# Define tests in this file
from day7_helpers import part1, part2

data = ["16", "1", "2", "0", "4", "2", "7", "1", "2", "14"]


class TestClass:
    def test_day7_part1(self):
        assert part1(data) == 37

    def test_day7_part2(self):
        assert part2(data) == 168
