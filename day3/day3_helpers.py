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
    gamma = ""
    epsilon = ""
    ones = 0
    zeros = 0
    for j in range(len(data[0])):
        for i in range(len(data)):
            if data[i][j] == "1":
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        ones = 0
        zeros = 0
    return int(epsilon, 2) * int(gamma, 2)


def part2(data):
    o2 = data.copy()
    co2 = data.copy()
    length = len(data[0])
    for j in range(length):
        ones = 0
        zeros = 0
        for i in range(len(o2)):
            if o2[i][j] == "1":
                ones += 1
            else:
                zeros += 1

        index_o2 = []
        if len(o2) > 1:
            for i in range(len(o2)):
                if ones >= zeros:
                    if o2[i][j] == "0":
                        index_o2.append(o2[i])
                else:
                    if o2[i][j] == "1":
                        index_o2.append(o2[i])

        index_o2.sort(reverse=True)
        for index in index_o2:
            o2.remove(index)

    for j in range(length):
        ones = 0
        zeros = 0
        for i in range(len(co2)):
            if co2[i][j] == "1":
                ones += 1
            else:
                zeros += 1

        index_co2 = []

        if len(co2) > 1:
            for i in range(len(co2)):
                if ones >= zeros:
                    if co2[i][j] == "1":
                        index_co2.append(co2[i])
                else:
                    if co2[i][j] == "0":
                        index_co2.append(co2[i])

        index_co2.sort(reverse=True)
        for index in index_co2:
            co2.remove(index)
    return int(o2[0], 2) * int(co2[0], 2)
