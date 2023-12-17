with open("data.txt") as f:
    lines = f.readlines()


def solve():
    som = 0
    box = [0] * 256
    for i in range(len(box)):
        box[i] = {}
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(",")

    line = lines[0]
    for s in line:
        current = 0
        for c in s[:2]:
            current += ord(c)
            current *= 17
            current %= 256
        if s[2] == "=":
            box[current][s[:2]] = int(s[3])
        if s[2] == "-" and s[:2] in box[current]:
            del box[current][s[:2]]
    for i in range(len(box)):
        j = 1
        for k, v in box[i].items():
            som += ((i+1) * j * v)
            j += 1


solve()
