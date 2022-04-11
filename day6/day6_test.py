# Define tests in this file
from day6_helpers import SchoolOfFish

data = ["3", "4", "3", "1", "2"]
school_part1 = SchoolOfFish(data)
school_part2 = SchoolOfFish(data)


class TestClass:
    def test_day6_part1(self):
        nb_cycle_part1 = 18
        for _ in range(0, nb_cycle_part1):
            school_part1.update()
        assert school_part1.state() == 26

    def test_day6_part2(self):
        nb_cycle_part2 = 256
        for _ in range(0, nb_cycle_part2):
            school_part2.update()
        assert school_part2.state() == 26984457539
