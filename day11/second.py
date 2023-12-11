with open('data.txt') as f:
    lines = f.readlines()


def getVerticalHorizontal(galaxy):
    horizontal = []
    verticalFull = []
    vertical = []
    for i in range(0, len(galaxy)):
        empty = True
        galaxy[i] = galaxy[i].rstrip()
        for j in range(0, len(galaxy[i])):
            if galaxy[i][j] == "#":
                empty = False
                verticalFull.append(j)
        if empty:
            horizontal.append(i)

    for i in range(0, len(galaxy)):
        if i not in verticalFull:
            vertical.append(i)
    print(horizontal)
    print(vertical)

    return (horizontal, vertical)



def getPairs(galaxy):
    planets = []
    pairs = []
    for i in range(0, len(galaxy)):
        for j in range(0, len(galaxy[i])):
            if galaxy[i][j] == "#":
                planets.append((i, j))
    for i in range(0, len(planets)):
        for j in range(i+1, len(planets)):
            pairs.append((planets[i], planets[j]))
    return pairs


def findShortestPath(pairs, VH):
    res = 0
    e = 1000000-1

    for pair in pairs:
        expand = 0
        for v in VH[0]:
            if pair[0][0] < v < pair[1][0] or pair[1][0] < v < pair[0][0]:
                expand += 1
        for h in VH[1]:
            if pair[0][1] < h < pair[1][1] or pair[1][1] < h < pair[0][1]:
                expand += 1
        s = abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1]) + expand * e
        print(pair, expand, s)
        res += s
    return res


def solve():
    galaxy = lines
    VH = getVerticalHorizontal(lines)
    pairs = getPairs(galaxy)
    print(findShortestPath(pairs, VH))


solve()