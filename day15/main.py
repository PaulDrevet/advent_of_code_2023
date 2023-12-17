with open("data.txt") as f:
    lines = f.readlines()


def solve():
    som = 0
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(",")

    line = lines[0]
    for s in line:
        current = 0
        for c in s:
            current += ord(c)
            current *= 17
            current %= 256
        som += current
    print(som)


solve()
