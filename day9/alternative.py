with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

height_map = {}
for y, row in enumerate(lines):
    for x, height in enumerate(row):
        height_map[(x, y)] = int(height)

low_points = []
sum = 0
for coords, height in height_map.items():
    x, y = coords
    neighbours = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    lowest = True
    for neighbour in neighbours:
        if height_map.get(neighbour, 10) <= height:
            lowest = False
            break

    if lowest:
        low_points.append(coords)
        sum += height + 1

print(sum)