# Define functions in this file
import math
import os
import sys


def import_input(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = [int(line) for line in file.read().split(",")]
            return data
    else:
        sys.exit(1)


def part1(data):
    maximum = int(max(data))
    min_cost = math.inf
    for position in range(0, maximum):
        total_cost = 0
        for index in range(len(data)):
            total_cost += abs(int(data[index]) - position)
        if total_cost < min_cost:
            min_cost = total_cost
    return min_cost


def part2(data):
    maximum = int(max(data))
    min_cost = math.inf
    for position in range(0, maximum):
        total_cost = 0
        for index in range(len(data)):
            difference = abs(int(data[index]) - position)
            total_cost += sub_1(difference)
        if total_cost < min_cost:
            min_cost = total_cost
    return min_cost


def sub_1(difference):
    total = 0
    while difference > 0:
        total += difference
        difference -= 1
    return total
