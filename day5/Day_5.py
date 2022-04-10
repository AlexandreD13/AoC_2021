my_file = open("Day_5_input.txt", "r")
content = my_file.read()
content_list = content.split("\n")

del my_file, content

# ---------------------------------------------------------------------------------------------------------------------
# Part 1:
position_dict = {}

for i in range(len(content_list)):
    x1 = int(content_list[i].split(",")[0])
    y1 = int(content_list[i].split(",")[1].split("-")[0])

    x2 = int(content_list[i].split(">")[1].split(",")[0])
    y2 = int(content_list[i].split(">")[1].split(",")[1])

    if x1 == x2:
        max_y = max(y1, y2)
        min_y = min(y1, y2)
        while max_y >= min_y:
            if (x1, max_y) in position_dict.keys():
                position_dict[(x1, max_y)] += 1
            else:
                position_dict[(x1, max_y)] = 1
            max_y -= 1
    elif y1 == y2:
        max_x = max(x1, x2)
        min_x = min(x1, x2)
        while max_x >= min_x:
            if (max_x, y1) in position_dict.keys():
                position_dict[(max_x, y1)] += 1
            else:
                position_dict[(max_x, y1)] = 1
            max_x -= 1

count = 0
for key in position_dict.keys():
    if position_dict[key] > 1:
        count += 1
print(count)
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# Part 2:
position_dict = {}

for i in range(len(content_list)):
    x1 = int(content_list[i].split(",")[0])
    y1 = int(content_list[i].split(",")[1].split("-")[0])

    x2 = int(content_list[i].split(">")[1].split(",")[0])
    y2 = int(content_list[i].split(">")[1].split(",")[1])

    max_y = max(y1, y2)
    min_y = min(y1, y2)
    max_x = max(x1, x2)
    min_x = min(x1, x2)

    if x1 == x2:
        while max_y >= min_y:
            if (x1, max_y) in position_dict.keys():
                position_dict[(x1, max_y)] += 1
            else:
                position_dict[(x1, max_y)] = 1
            max_y -= 1
    elif y1 == y2:
        while max_x >= min_x:
            if (max_x, y1) in position_dict.keys():
                position_dict[(max_x, y1)] += 1
            else:
                position_dict[(max_x, y1)] = 1
            max_x -= 1
    elif (x1 > x2) and (y1 > y2):
        while (x1 >= x2) and (y1 >= y2):
            if (x1, y1) in position_dict.keys():
                position_dict[(x1, y1)] += 1
            else:
                position_dict[(x1, y1)] = 1
            x1 -= 1
            y1 -= 1
    elif (x2 > x1) and (y2 > y1):
        while (x2 >= x1) and (y2 >= y1):
            if (x2, y2) in position_dict.keys():
                position_dict[(x2, y2)] += 1
            else:
                position_dict[(x2, y2)] = 1
            x2 -= 1
            y2 -= 1
    elif (x1 > x2) and (y1 < y2):
        while (x1 >= x2) and (y1 <= y2):
            if (x1, y1) in position_dict.keys():
                position_dict[(x1, y1)] += 1
            else:
                position_dict[(x1, y1)] = 1
            x1 -= 1
            y1 += 1
    elif (x1 < x2) and (y1 > y2):
        while (x2 >= x1) and (y2 <= y1):
            if (x1, y1) in position_dict.keys():
                position_dict[(x1, y1)] += 1
            else:
                position_dict[(x1, y1)] = 1
            x1 += 1
            y1 -= 1

count = 0
for key in position_dict.keys():
    if position_dict[key] > 1:
        count += 1
print(count)