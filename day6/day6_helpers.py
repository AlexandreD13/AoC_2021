# Define functions in this file
import os
import sys


def import_input(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = file.read().split(",")
            return data
    else:
        sys.exit(1)


class SchoolOfFish:
    def __init__(self, initial_state):
        self.group = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
                      "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

        for i in range(len(initial_state)):
            if initial_state[i] in self.group:
                self.group[initial_state[i]] += 1
            else:
                self.group[initial_state[i]] = 1

        self.days_passed = 0

    def state(self):
        return sum(self.group.values())

    def update(self):
        for key in self.group:
            if int(key) == 0:
                self.group["7"] += self.group[key]
                self.group["9"] += self.group[key]
                self.group["0"] = 0
            else:
                self.group[str(int(key) - 1)] += self.group[key]
                self.group[key] = 0

        self.days_passed += 1
