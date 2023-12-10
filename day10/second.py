with open('data.txt') as f:
    lines = f.readlines()


def getStartingLocation():
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])-1):
            if lines[i][j] == "S":
                return i, j


def getSymbol(t):
    return lines[t[-1][0]][t[-1][1]]

def getSymbolByTuple(t):
    return lines[t[0]][t[1]]


def getPaths(currentLocation):
    firstPath = (0, 0)
    secondPath = (0, 0)
    top = lines[currentLocation[0]-1][currentLocation[1]]
    bottom = lines[currentLocation[0]+1][currentLocation[1]]
    left = lines[currentLocation[0]][currentLocation[1]-1]
    right = lines[currentLocation[0]][currentLocation[1]+1]
    if top == "7" or top == "F" or top == "|":
        if firstPath == (0, 0):
            firstPath = (currentLocation[0]-1, currentLocation[1])
            print("top fp")
        else:
            secondPath = (currentLocation[0]-1, currentLocation[1])
            print("top sp")
    if bottom == "L" or bottom == "J" or bottom == "|":
        if firstPath == (0, 0):
            firstPath = (currentLocation[0]+1, currentLocation[1])
            print("bottom fp")
        else:
            secondPath = (currentLocation[0]+1, currentLocation[1])
            print("bottom sp")
    if left == "-" or left == "L" or left == "F":
        if firstPath == (0, 0):
            firstPath = (currentLocation[0], currentLocation[1]-1)
            print("left fp")
        else:
            secondPath = (currentLocation[0], currentLocation[1]-1)
            print("left sp")
    if right == "-" or right == "J" or right == "7":
        if firstPath == (0, 0):
            firstPath = (currentLocation[0], currentLocation[1]+1)
            print("right fp")
        else:
            secondPath = (currentLocation[0], currentLocation[1]+1)
            print("right sp")
    return [firstPath, secondPath]


def comeFrom(path):
    if path[-1][0] == path[-2][0]+1:
        return "up"
    if path[-1][0] == path[-2][0]-1:
        return "down"
    if path[-1][1] == path[-2][1]+1:
        return "left"
    if path[-1][1] == path[-2][1]-1:
        return "right"


def getNextDirection(path):
    symbol = getSymbol(path)

    if symbol == "|":
        if comeFrom(path) == "up":
            return getNextLocation(path, "down")
        else:
            return getNextLocation(path, "up")
    if symbol == "-":
        if comeFrom(path) == "right":
            return getNextLocation(path, "left")
        else:
            return getNextLocation(path, "right")
    if symbol == "L":
        if comeFrom(path) == "up":
            return getNextLocation(path, "right")
        else:
            return getNextLocation(path, "up")
    if symbol == "J":
        if comeFrom(path) == "up":
            return getNextLocation(path, "left")
        else:
            return getNextLocation(path, "up")
    if symbol == "7":
        if comeFrom(path) == "left":
            return getNextLocation(path, "down")
        else:
            return getNextLocation(path, "left")
    if symbol == "F":
        if comeFrom(path) == "right":
            return getNextLocation(path, "down")
        else:
            return getNextLocation(path, "right")


def getNextLocation(path, direction):
    if direction == "up":
        return (path[-1][0]-1, path[-1][1])
    if direction == "down":
        return (path[-1][0]+1, path[-1][1])
    if direction == "left":
        return (path[-1][0], path[-1][1]-1)
    if direction == "right":
        return (path[-1][0], path[-1][1]+1)


def solve():
    currentLocation = getStartingLocation()
    paths = getPaths(currentLocation)
    path = [paths[0]]
    path.insert(0, currentLocation)

    while getSymbol(path) != "S":
        path.append(getNextDirection(path))

    print(len(path)//2)
    print(findInter(path))


def findInter(path):
    path.pop()
    print(path)

    res = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if (i, j) not in path:
                s = 0
                for k in range(j+1, len(lines[i])):
                    t = (i, k)
                    if t in path:
                        print(i, k, getSymbolByTuple(t))
                        if getSymbolByTuple(t) == "7" or getSymbolByTuple(t) == "J":
                            print()
                        else:
                            s += 1
                            k += 1
                            t = (i, k)

                        while k < len(lines[i]) and getSymbolByTuple(t) != "7" and getSymbolByTuple(t) != "J":
                            k += 1
                            t = (i, k)

                if s % 2 == 1:
                    res += 1
                    print(i, j, s, "res++", getSymbolByTuple((i,j)))
    return res



solve()
