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

    refactorMaze()

    print(len(path)//2)
    print(findInter(path))


def refactorMaze():
    for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip()
        for j in range(0, len(lines[i])):
            if lines[i][j] == "S":
                lines[i] = lines[i].replace("S","7")
        print(lines[i])


def findInter(path):
    path.pop()
    print(path)

    res = 0
    for i in range(0, len(lines)):
        isInside = False
        for j in range(0, len(lines[i])):
            if (getSymbolByTuple((i, j)) == "F" or getSymbolByTuple((i, j)) == "7" or getSymbolByTuple((i, j)) == "|") and (i, j) in path:
                isInside = not isInside

            if isInside and ((i, j) not in path):
                print(i, j, getSymbolByTuple((i, j)))
                res += 1
    return res



solve()