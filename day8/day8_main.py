# Advent Of Code 2021 - Day 8 - Seven Segment Search
from day8_helpers import import_input, split_data, part1, part2

if __name__ == "__main__":
    # Import input
    filename = "input.txt"
    data = import_input(filename)
    input_data, output_data = split_data(data)
    print("\nPart 1 :", part1(output_data))
    print("Part 2 :", part2(input_data, output_data))
