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


def split_data(data):
    input_data = [None] * len(data)
    output_data = [None] * len(data)
    try:
        for i in range(len(data)):
            input_data[i] = data[i].split("|")[0].split()
            output_data[i] = data[i].split("|")[1].split()
        return input_data, output_data
    except IndexError:
        sys.exit(1)


def parse_line(input_data):
    values_list = []
    for line in input_data:
        line.sort(key=len)
        values_dict = identify_values(line)
        values_list.append(values_dict)
    return values_list


def identify_values(line):
    values_dict = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "",
                   6: "", 7: "", 8: "", 9: ""}

    for item in line:
        if len(item) == 2:
            values_dict[1] = item
        elif len(item) == 3:
            values_dict[7] = item
        elif len(item) == 4:
            values_dict[4] = item
        elif len(item) == 5:
            values_dict = len5(values_dict, item)
        elif len(item) == 6:
            values_dict = len6(values_dict, item)
        else:
            values_dict[8] = item
    return values_dict


def len5(values_dict, item):
    if set(values_dict[1]).issubset(set(item)):
        values_dict[3] = item
    else:
        temp = list(item)
        for letter in values_dict[4]:
            if letter in temp:
                del temp[temp.index(letter)]
        if len(temp) == 2:
            values_dict[5] = item
        else:
            values_dict[2] = item
    return values_dict


def len6(values_dict, item):
    if set(values_dict[1]).issubset(set(item)):
        if set(values_dict[4]).issubset(set(item)):
            values_dict[9] = item
        else:
            values_dict[0] = item
    else:
        values_dict[6] = item
    return values_dict


def decipher_output(input_line, output_line):
    output_total = ""
    for output_item in output_line:
        for key, value in input_line.items():
            if set(value) == set(output_item):
                output_total += str(key)
    return int(output_total)


def part1(output_data):
    counter = 0
    for line in output_data:
        for item in line:
            if len(item) in [2, 3, 4, 7]:
                counter += 1
    return counter


def part2(input_data, output_data):
    values_list = parse_line(input_data)
    line = 0
    total = 0
    for line_dict in values_list:
        total += decipher_output(line_dict, output_data[line])
        line += 1
    return total
