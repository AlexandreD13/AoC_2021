# Define tests in this file
from day2_helpers import part1, part2

data = ["forward 5", "down 5",
        "forward 8", "up 3",
        "down 8", "forward 2"]


class TestClass:
    def test_day2_part1(self):
        assert part1(data) == 150

    def test_day2_part2(self):
        assert part2(data) == 900
