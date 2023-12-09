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
    print(history)
    j = 0
    while (not all_equal(history[-1])) or history[-1][0] != 0:
        current = history[j]
        nextLine = []
        for i in range(1, len(current)):
            diff = int(current[i]) - int(current[i-1])
            nextLine.append(diff)
        history.append(nextLine)
        j += 1

    history[-1].append(0)

    for i in range(len(history)-2, -1, -1):
        history[i].append(history[i][-1] + history[i+1][-1])
    s += (history[0][-1])

print(s)


