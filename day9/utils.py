# Define functions in this file
import logging
import os
import sys


def import_input(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            heightmap = file.read().split("\n")
            logging.info("Data successfully imported")
        temp = heightmap
        index = 0
        for line in temp:
            heightmap[index] = list(line)
            index += 1
        logging.info("Data converted to list of lists")
        logging.info("Format - heightmap[line][column]")
        return heightmap
    else:
        logging.critical("File does not exist")
        sys.exit(1)


# Use get method for dictionary
def risk_level(heightmap):
    total_risk = 0
    for index_line in range(len(heightmap)):
        for index_column in range(len(heightmap[index_line]) - 1):
            if heightmap[index_line][index_column] < heightmap[index_line][index_column + 1] and \
                    heightmap[index_line][index_column] < heightmap[index_line][index_column - 1] and \
                    heightmap[index_line][index_column] < heightmap[index_line + 1][index_column] and \
                    heightmap[index_line][index_column] < heightmap[index_line - 1][index_column]:
                total_risk += int(heightmap[index_line][index_column]) + 1
                logging.info("Part 1 - Low point at Index: %s, Column: %s, Value: %s",
                             index_line, index_column,
                             int(heightmap[index_line][index_column]))
                logging.info("Part 1 - Total risk level now at: %s",
                             total_risk)
