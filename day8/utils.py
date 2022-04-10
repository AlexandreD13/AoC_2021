# Define functions in this file
import logging
import os
import sys


def import_input(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = file.read().split("\n")
            logging.info("Data successfully imported")
            return data
    else:
        logging.critical("File does not exist")
        sys.exit(1)


def split_data(data):
    input_data = [None] * len(data)
    output_data = [None] * len(data)
    try:
        for i in range(len(data)):
            input_data[i] = data[i].split("|")[0].split()
            output_data[i] = data[i].split("|")[1].split()
        logging.info("Data successfully split into input/output")
        return input_data, output_data
    except IndexError:
        logging.critical("File is of unsupported format")
        sys.exit(1)


def count_uniques(output_data):
    counter = 0
    for line in output_data:
        for item in line:
            if len(item) in [2, 3, 4, 7]:
                counter += 1
    logging.info("Part 1 - Number of unique values: %s", counter)


def parse_line(input_data):
    values_list = []
    for line in input_data:
        line.sort(key=len)
        values_dict = identify_values(line)
        values_list.append(values_dict)
    logging.info("Part 2 - Input has been deciphered for each line of data")
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


def len6(values_dict, item):
    if set(values_dict[1]).issubset(set(item)):
        if set(values_dict[4]).issubset(set(item)):
            values_dict[9] = item
        else:
            values_dict[0] = item
    else:
        values_dict[6] = item
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


def decipher_output(input_line, output_line):
    output_total = ""
    for output_item in output_line:
        for key, value in input_line.items():
            if set(value) == set(output_item):
                output_total += str(key)
    return int(output_total)
