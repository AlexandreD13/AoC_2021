# Define functions in this file
import os
import sys


def import_input(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = [int(line) for line in file]
            return data
    else:
        sys.exit(1)


def part1(data):
    count = 0
    for index in range(1, len(data)):
        if data[index] > data[index - 1]:
            count += 1
    return count


def part2(data):
    count = 0
    for index in range(2, len(data) - 1):
        window_a = int(data[index - 2]) + int(data[index - 1]) + int(data[index])
        window_b = int(data[index - 1]) + int(data[index]) + int(data[index + 1])
        if window_b > window_a:
            count += 1
    return count
