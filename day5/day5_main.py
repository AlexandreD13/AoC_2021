# Advent Of Code 2021 - Day 5 - Hydrothermal Venture
from day5_helpers import import_input, part1, part2

if __name__ == "__main__":
    # Import input
    filename = "data/input.txt"
    data = import_input(filename)
    print("\nPart 1 : ", part1(data))
    print("Part 2 : ", part2(data))