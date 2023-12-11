with open('data.txt') as f:
    lines = f.readlines()


def expand(galaxy):
    horizontal = []
    vertical = []
    for i in range(0, len(galaxy)):
        empty = True
        galaxy[i] = galaxy[i].rstrip()
        for j in range(0, len(galaxy[i])):
            if galaxy[i][j] == "#":
                empty = False
                vertical.append(j)
        if empty:
            horizontal.append(i + len(horizontal))

    for x in horizontal:
        galaxy.insert(x+1, "." * (len(galaxy[x])))

    a = 0
    for i in range(0,len(galaxy[0])):
        if i in vertical:
            continue
        else:
            for j in range(0, len(galaxy)):
                galaxy[j] = galaxy[j][:i+a] + "." + galaxy[j][i+a:]
            a += 1

    return galaxy


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


def findShortestPath(pairs):
    res = 0
    for pair in pairs:
        s = abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])
        res += s
        print(pair, s)

    return res


def solve():
    galaxy = expand(lines)
    pairs = getPairs(galaxy)
    print(findShortestPath(pairs))


solve()