import sys

with open("data.txt") as f:
    lines = f.readlines()

energized = []
known = []



def laser(tile, direction):
    if tile[0] < 0 or tile[1] < 0 or tile[0] >= len(lines[0]) or tile[1] >= len(lines):
        return
    if (tile, direction) in known:
        return
    known.append((tile, direction))
    if tile not in energized:
        energized.append(tile)

    if lines[tile[1]][tile[0]] == "|" and (direction == "right" or direction == "left"):
        laser((tile[0], tile[1] + 1), "down")
        laser((tile[0], tile[1] - 1), "up")
        return
    if lines[tile[1]][tile[0]] == "-" and (direction == "up" or direction == "down"):
        laser((tile[0] + 1, tile[1]), "right")
        laser((tile[0] - 1, tile[1]), "left")
        return
    if lines[tile[1]][tile[0]] == "/" and direction == "up":
        laser((tile[0] + 1, tile[1]), "right")
        return
    if lines[tile[1]][tile[0]] == "/" and direction == "down":
        laser((tile[0] - 1, tile[1]), "left")
        return
    if lines[tile[1]][tile[0]] == "/" and direction == "left":
        laser((tile[0], tile[1] + 1), "down")
        return
    if lines[tile[1]][tile[0]] == "/" and direction == "right":
        laser((tile[0], tile[1] - 1), "up")
        return
    if lines[tile[1]][tile[0]] == "\\" and direction == "up":
        laser((tile[0] - 1, tile[1]), "left")
        return
    if lines[tile[1]][tile[0]] == "\\" and direction == "down":
        laser((tile[0] + 1, tile[1]), "right")
        return
    if lines[tile[1]][tile[0]] == "\\" and direction == "left":
        laser((tile[0], tile[1] - 1), "up")
        return
    if lines[tile[1]][tile[0]] == "\\" and direction == "right":
        laser((tile[0], tile[1] + 1), "down")
        return
    if direction == "up":
        laser((tile[0], tile[1] - 1), "up")
        return
    if direction == "down":
        laser((tile[0], tile[1] + 1), "down")
        return
    if direction == "left":
        laser((tile[0] - 1, tile[1]), "left")
        return
    if direction == "right":
        laser((tile[0] + 1, tile[1]), "right")
        return


def print_map():
    for i in range(len(lines)):
        for j in range(len(lines[0])-1):
            if (j, i) in energized:
                print("#", end="")
            else:
                print(".", end="")
        print()


def solve():
    sys.setrecursionlimit(10000)
    laser((0, 0), "right")
    print(len(energized))


solve()