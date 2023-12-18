with open('data.txt') as f:
    lines = f.readlines()


def solve():
    position = (0, 0)
    positions = []
    for line in lines:
        hexa = line.split(" ")[2].rstrip()
        print(hexa[2:-1])
        print(hexa[-2:-1].replace("0", "R").replace("1", "D").replace("2", "L").replace("3","U"))
        meters = int(hexa[2:-1], 16)
        direction = hexa[-2:-1].replace("0", "R").replace("1", "D").replace("2", "L").replace("3","U")
        print(hexa, meters, direction)

        if direction == "U":
            position = (position[0], position[1]-meters)
        if direction == "D":
            position = (position[0], position[1]+meters)
        if direction == "L":
            position = (position[0]-meters, position[1])
        if direction == "R":
            position = (position[0]+meters, position[1])
        positions.append(position)
    maxX = max([x[1] for x in positions])
    maxY = max([x[0] for x in positions])
    minY = min([x[0] for x in positions])
    minX = min([x[1] for x in positions])
    ground = ["." * (maxY + abs(minY) + 1)] * (maxX + abs(minX) + 1)

    print("\n")

    y = abs(minY)
    x = abs(minX)
    print(minX, minY, maxY, maxX)
    for line in lines:
        direction = line.split(" ")[0]
        meters = int(line.split(" ")[1])

        if direction == "U":
            while meters != 0:
                ground[x] = ground[x][:y] + "#" + ground[x][y+1:]
                x -= 1
                meters -= 1

        if direction == "D":
            while meters != 0:
                ground[x] = ground[x][:y] + "#" + ground[x][y+1:]
                x += 1
                meters -= 1

        if direction == "L":
            while meters != 0:
                ground[x] = ground[x][:y] + "#" + ground[x][y+1:]
                y -= 1
                meters -= 1

        if direction == "R":
            while meters != 0:
                ground[x] = ground[x][:y] + "#" + ground[x][y+1:]
                y += 1
                meters -= 1

    s = 0

    for i in range(0, len(ground)):
        for j in range(0, len(ground[0])):
            if ground[i][j] == ".":
                c = 0
                for k in range(j+1, len(ground[0])):
                    if ground[i][k] == "#" and ground[i-1][k] == "#":
                        c += 1
                if c % 2 == 1:
                    ground[i] = ground[i][:j] + "1" + ground[i][j+1:]

    for i in range(len(ground)):
        for j in range(len(ground[0])):
            if ground[i][j] == "1" or ground[i][j] == "#":
                s += 1



    print(s)


solve()