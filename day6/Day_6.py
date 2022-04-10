# Day 6 of Advent Of Code 2021

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
        print("\nAfter {} days, there are {} fishes.".format(self.days_passed, sum(self.group.values())))

    def update(self):
        self.state()
        print(self.group)

        for key in self.group:
            if int(key) == 0:
                self.group["7"] += self.group[key]
                self.group["9"] += self.group[key]
                self.group["0"] = 0
            else:
                self.group[str(int(key) - 1)] += self.group[key]
                self.group[key] = 0

        self.days_passed += 1


if __name__ == "__main__":
    my_file = open("Day_6_input.txt", "r")
    content = my_file.read()
    n_list = content.split(',')

    del my_file, content

    school = SchoolOfFish(n_list)

    for i in range(0, 257):
        school.update()
