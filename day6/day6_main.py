# Advent Of Code 2021 - Day 6 - Lanternfish
from day6_helpers import import_input, SchoolOfFish

if __name__ == "__main__":
    # Import input
    filename = "input.txt"
    data = import_input(filename)
    school_part1 = SchoolOfFish(data)
    school_part2 = SchoolOfFish(data)

    NB_CYCLE_PART1 = 80
    NB_CYCLE_PART2 = 256

    for i in range(0, NB_CYCLE_PART1):
        school_part1.update()

    for i in range(0, NB_CYCLE_PART2):
        school_part2.update()

    print("\nPart 1 :", school_part1.state())
    print("Part 2 :", school_part2.state())
