with open('data.txt') as f:
    lines = f.readlines()


def solve():
    start = (0, 0)
    tiles = []
    print(lines)
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                start = (i, j)
                tiles.append(start)
    print(start)

    for i in range(0, 64):
        newTiles = []
        print(tiles)
        for k in range(len(tiles)):
            t = tiles[k]
            if lines[t[0]-1][t[1]] != "#" and (t[0]-1, t[1]) not in newTiles:
                newTiles.append((t[0]-1, t[1]))
            if lines[t[0]+1][t[1]] != "#" and (t[0]+1, t[1]) not in newTiles:
                newTiles.append((t[0]+1, t[1]))
            if lines[t[0]][t[1]-1] != "#" and (t[0], t[1]-1) not in newTiles:
                newTiles.append((t[0], t[1]-1))
            if lines[t[0]][t[1]+1] != "#" and (t[0], t[1]+1) not in newTiles:
                newTiles.append((t[0], t[1]+1))
        tiles = newTiles

    print(len(tiles))




solve()
