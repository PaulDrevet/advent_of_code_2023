with open('data.txt') as f:
    lines = f.readlines()

graph = {}


def rec(pos, d="right", x=0):
    global graph
    v = graph[pos]
    adj = v[0]
    minD = v[2]
    path = v[3]
    for i in range(len(adj)):
        n = adj[i]
        if n[0] == pos[0]-1:
            direction = "up"
        if n[0] == pos[0]+1:
            direction = "down"
        if n[1] == pos[1]-1:
            direction = "left"
        if n[1] == pos[1]+1:
            direction = "right"

        if minD + graph[n][1] < graph[n][2] and (x < 3 or d != direction):
            graph[n][2] = minD + graph[n][1]
            graph[n][3] = path + [n]
            if d == direction:
                rec(n, direction, x+1)
            else:
                rec(n, direction)


def solve():
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        for j in range(len(lines[i])):
            if i == 0:
                if j == 0:
                    graph[(i, j)] = [[(i+1, j), (i, j+1)], int(lines[i][j]), int(lines[i][j]), [(i, j)]]
                if j == len(lines[i])-1:
                    graph[(i, j)] = [[(i+1, j), (i, j-1)], int(lines[i][j]), 1000000000000, []]
            if i == len(lines)-1:
                if j == 0:
                    graph[(i, j)] = [[(i-1, j), (i, j+1)], int(lines[i][j]), 1000000000000, []]
                if j == len(lines[i])-1:
                    graph[(i, j)] = [[(i-1, j), (i, j-1)], int(lines[i][j]), 1000000000000, []]
            if i == 0 and j != 0 and j != len(lines[i])-1:
                graph[(i, j)] = [[(i+1, j), (i, j+1), (i, j-1)], int(lines[i][j]), 1000000000000, []]
            if i == len(lines)-1 and j != 0 and j != len(lines[i])-1:
                graph[(i, j)] = [[(i-1, j), (i, j+1), (i, j-1)], int(lines[i][j]), 1000000000000, []]
            if j == 0 and i != 0 and i != len(lines)-1:
                graph[(i, j)] = [[(i+1, j), (i, j+1), (i-1, j)], int(lines[i][j]), 1000000000000, []]
            if j == len(lines[i])-1 and i != 0 and i != len(lines)-1:
                graph[(i, j)] = [[(i, j-1), (i+1, j), (i-1, j)], int(lines[i][j]), 1000000000000, []]
            if i != 0 and i != len(lines)-1 and j != 0 and j != len(lines[i])-1:
                graph[(i, j)] = [[(i, j-1), (i+1, j), (i, j+1), (i-1, j)], int(lines[i][j]), 1000000000000, []]

    print(graph[0, 0])
    rec((0, 0))
    print(graph)

    final = graph[(len(lines)-1, len(lines[0])-1)]
    s = 0
    for i in range(len(final[3])):
        print(graph[final[3][i]][1])
        s += graph[final[3][i]][1]
    print(s)


solve()