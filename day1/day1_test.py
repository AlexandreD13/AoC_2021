# Define tests in this file
from day1_helpers import part1, part2

data = ["199", "200", "208", "210",
        "200", "207", "240", "269",
        "260", "263"]


class TestClass:
    def test_day1_part1(self):
        assert part1(data) == 7

    def test_day1_part2(self):
        assert part2(data) == 5
