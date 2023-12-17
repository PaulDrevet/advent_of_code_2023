import sys

with open("data.txt") as f:
    lines = f.readlines()

energized = set()
known = set()


def laser(tile, direction):
    stack = [(tile, direction)]

    while stack:
        tile, direction = stack.pop()

        if tile[0] < 0 or tile[1] < 0 or tile[0] >= len(lines[0]) or tile[1] >= len(lines):
            continue

        if (tile, direction) in known:
            continue

        known.add((tile, direction))

        if tile not in energized:
            energized.add(tile)

        if lines[tile[1]][tile[0]] == "|" and (direction == "right" or direction == "left"):
            stack.append(((tile[0], tile[1] + 1), "down"))
            stack.append(((tile[0], tile[1] - 1), "up"))
        elif lines[tile[1]][tile[0]] == "-" and (direction == "up" or direction == "down"):
            stack.append(((tile[0] + 1, tile[1]), "right"))
            stack.append(((tile[0] - 1, tile[1]), "left"))
        elif lines[tile[1]][tile[0]] == "/" and direction == "up":
            stack.append(((tile[0] + 1, tile[1]), "right"))
        elif lines[tile[1]][tile[0]] == "/" and direction == "down":
            stack.append(((tile[0] - 1, tile[1]), "left"))
        elif lines[tile[1]][tile[0]] == "/" and direction == "left":
            stack.append(((tile[0], tile[1] + 1), "down"))
        elif lines[tile[1]][tile[0]] == "/" and direction == "right":
            stack.append(((tile[0], tile[1] - 1), "up"))
        elif lines[tile[1]][tile[0]] == "\\" and direction == "up":
            stack.append(((tile[0] - 1, tile[1]), "left"))
        elif lines[tile[1]][tile[0]] == "\\" and direction == "down":
            stack.append(((tile[0] + 1, tile[1]), "right"))
        elif lines[tile[1]][tile[0]] == "\\" and direction == "left":
            stack.append(((tile[0], tile[1] - 1), "up"))
        elif lines[tile[1]][tile[0]] == "\\" and direction == "right":
            stack.append(((tile[0], tile[1] + 1), "down"))
        elif direction == "up":
            stack.append(((tile[0], tile[1] - 1), "up"))
        elif direction == "down":
            stack.append(((tile[0], tile[1] + 1), "down"))
        elif direction == "left":
            stack.append(((tile[0] - 1, tile[1]), "left"))
        elif direction == "right":
            stack.append(((tile[0] + 1, tile[1]), "right"))


def print_map():
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1):
            if (j, i) in energized:
                print("#", end="")
            else:
                print(".", end="")
        print()


def solve():
    sys.setrecursionlimit(3000)
    laser((0, 0), "right")
    print(len(energized)-1)


solve()
