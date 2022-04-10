# Define functions in this file
import os
import sys


def import_input(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = file.read().split("\n")
            return data
    else:
        sys.exit(1)


def part1(data):
    depth = 0
    horizontal = 0
    for index in range(len(data)):
        instruction, units = data[index].split()
        units = int(units)
        if instruction == "forward":
            horizontal += units
        elif instruction == "down":
            depth += units
        elif instruction == "up":
            depth -= units
    return horizontal * depth


def part2(data):
    depth = 0
    horizontal = 0
    aim = 0
    for i in range(len(data)):
        instruction, units = data[i].split()
        units = int(units)
        if instruction == "forward":
            horizontal += units
            depth += aim * units
        elif instruction == "down":
            aim += units
        elif instruction == "up":
            aim -= units
    return horizontal * depth
