# Day 8 of Advent Of Code 2021
import logging.config

from utils import import_input, split_data, count_uniques, parse_line, decipher_output

if __name__ == "__main__":
    # Setup log file
    logging.basicConfig(filename="day8.log",
                        filemode="w",
                        level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info("|------------------- Advent of Code 2021 -------------------|")
    logging.info("Advent Of Code - Day 8: Seven Segment Search")
    logging.info("--------------------------------------------------------------")
    logging.info("Program started")

    # Import input
    filename = "input.txt"
    data = import_input(filename)
    del filename

    # Part 1
    input_data, output_data = split_data(data)
    logging.info("Part 1 - Counting values ...")
    count_uniques(output_data)

    # Part 2
    values_list = parse_line(input_data)
    logging.info("Part 2 - Solving output ...")
    line = 0
    total = 0
    for line_dict in values_list:
        total += decipher_output(line_dict, output_data[line])
        line += 1
    logging.info("Part 2 - Output values total: %s", total)

    logging.info("Program finished")
    logging.info("--------------------------------------------------------------\n")
