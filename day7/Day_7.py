# Day 7 of Advent Of Code 2021

import math


def main(list_of_positions):
    maximum = int(max(list_of_positions))

    min_cost = math.inf
    min_position = None
    for position in range(0, maximum):
        total_cost = fuel_cost_part_2(position, list_of_positions)
        if total_cost < min_cost:
            min_cost = total_cost
            min_position = position

    return min_cost, min_position


def fuel_cost_part_1(position, list_of_positions):
    total_cost = 0
    for i in range(len(list_of_positions)):
        total_cost += abs(int(list_of_positions[i]) - position)

    return total_cost


def fuel_cost_part_2(position, list_of_positions):
    total_cost = 0
    for i in range(len(list_of_positions)):
        difference = abs(int(list_of_positions[i]) - position)
        total_cost += sub_1(difference)

    return total_cost


def sub_1(difference):
    total = 0
    while difference > 0:
        total += difference
        difference -= 1

    return total


if __name__ == "__main__":
    my_file = open("Day_7_input.txt", "r")
    content = my_file.read()
    n_list = content.split(',')

    del my_file, content

    min_cost, min_position = main(n_list)

    print("\nMinimal gas consumption: ", min_cost)
    print("By moving to position: ", min_position)
