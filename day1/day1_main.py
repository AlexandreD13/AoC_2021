# Advent Of Code 2021 - Day 1 - Sonar Sweep
from day1_helpers import import_input, part1, part2

if __name__ == "__main__":
    # Import input
    filename = "input.txt"
    data = import_input(filename)
    print("\nPart 1 :", part1(data))
    print("Part 2 :", part2(data))
