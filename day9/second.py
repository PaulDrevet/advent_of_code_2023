from itertools import groupby

s = 0
with open('data.txt') as f:
    lines = f.readlines()

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


for line in lines:
    history = [line.rstrip().split(" ")]
    history = [[int(x) for x in history[0]]]
    j = 0
    while (not all_equal(history[-1])) or history[-1][0] != 0:
        current = history[j]
        nextLine = []
        for i in range(1, len(current)):
            diff = int(current[i]) - int(current[i-1])
            nextLine.append(diff)
        history.append(nextLine)
        j += 1

    history[-1].insert(0, 0)
    print(history)

    for i in range(len(history)-2, -1, -1):
        history[i].insert(0,(history[i][0] - history[i+1][0]))
    s += (history[0][0])

    print(history)
    print("\n")

print(s)


