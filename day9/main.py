# Day 9 of Advent Of Code 2021
import logging.config

from utils import import_input, risk_level

if __name__ == "__main__":
    # Setup log file
    logging.basicConfig(filename="day9.log",
                        filemode="w",
                        level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info("|------------------- Advent of Code 2021 -------------------|")
    logging.info("Advent Of Code - Day 9: Smoke Basin")
    logging.info("--------------------------------------------------------------")
    logging.info("Program started")

    # Import input
    filename = "input.txt"
    heightmap = import_input(filename)
    del filename

    # Part 1
    logging.info("Part 1 - Calculating risk level ...")
    total_risk = risk_level(heightmap)

    logging.info("Program finished")
    logging.info("--------------------------------------------------------------\n")
