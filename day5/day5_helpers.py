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
    position_dict = {}
    count = 0

    for i in range(len(data)):
        x1 = int(data[i].split(",")[0])
        y1 = int(data[i].split(",")[1].split("-")[0])
        x2 = int(data[i].split(">")[1].split(",")[0])
        y2 = int(data[i].split(">")[1].split(",")[1])

        if x1 == x2:
            position_dict = x1_eq_x2(position_dict, x1, y1, y2)
        elif y1 == y2:
            position_dict = y1_eq_y2(position_dict, y1, x1, x2)

    for key in position_dict.keys():
        if position_dict[key] > 1:
            count += 1
    return count


def part2(data):
    position_dict = {}

    for i in range(len(data)):
        x1 = int(data[i].split(",")[0])
        y1 = int(data[i].split(",")[1].split("-")[0])
        x2 = int(data[i].split(">")[1].split(",")[0])
        y2 = int(data[i].split(">")[1].split(",")[1])

        if x1 == x2:
            position_dict = x1_eq_x2(position_dict, x1, y1, y2)
        elif y1 == y2:
            position_dict = y1_eq_y2(position_dict, y1, x1, x2)
        elif (x1 > x2) and (y1 > y2):
            position_dict = x1_bigger_y1_bigger(position_dict, x1, x2, y1, y2)
        elif (x1 < x2) and (y1 < y2):
            position_dict = x1_smaller_y1_smaller(position_dict, x1, x2, y1, y2)
        elif (x1 > x2) and (y1 < y2):
            position_dict = x1_bigger_y1_smaller(position_dict, x1, x2, y1, y2)
        elif (x1 < x2) and (y1 > y2):
            position_dict = x1_smaller_y1_bigger(position_dict, x1, x2, y1, y2)

    count = 0
    for key in position_dict.keys():
        if position_dict[key] > 1:
            count += 1
    return count


def x1_eq_x2(position_dict, x1, y1, y2):
    max_y = max(y1, y2)
    min_y = min(y1, y2)
    while max_y >= min_y:
        if (x1, max_y) in position_dict.keys():
            position_dict[(x1, max_y)] += 1
        else:
            position_dict[(x1, max_y)] = 1
        max_y -= 1
    return position_dict


def y1_eq_y2(position_dict, y1, x1, x2):
    max_x = max(x1, x2)
    min_x = min(x1, x2)
    while max_x >= min_x:
        if (max_x, y1) in position_dict.keys():
            position_dict[(max_x, y1)] += 1
        else:
            position_dict[(max_x, y1)] = 1
        max_x -= 1
    return position_dict


def x1_bigger_y1_bigger(position_dict, x1, x2, y1, y2):
    while (x1 >= x2) and (y1 >= y2):
        if (x1, y1) in position_dict.keys():
            position_dict[(x1, y1)] += 1
        else:
            position_dict[(x1, y1)] = 1
        x1 -= 1
        y1 -= 1
    return position_dict


def x1_smaller_y1_smaller(position_dict, x1, x2, y1, y2):
    while (x2 >= x1) and (y2 >= y1):
        if (x2, y2) in position_dict.keys():
            position_dict[(x2, y2)] += 1
        else:
            position_dict[(x2, y2)] = 1
        x2 -= 1
        y2 -= 1
    return position_dict


def x1_bigger_y1_smaller(position_dict, x1, x2, y1, y2):
    while (x1 >= x2) and (y1 <= y2):
        if (x1, y1) in position_dict.keys():
            position_dict[(x1, y1)] += 1
        else:
            position_dict[(x1, y1)] = 1
        x1 -= 1
        y1 += 1
    return position_dict


def x1_smaller_y1_bigger(position_dict, x1, x2, y1, y2):
    while (x2 >= x1) and (y2 <= y1):
        if (x1, y1) in position_dict.keys():
            position_dict[(x1, y1)] += 1
        else:
            position_dict[(x1, y1)] = 1
        x1 += 1
        y1 -= 1
    return position_dict
