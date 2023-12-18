with open("data.txt") as f:
    lines = f.readlines()

def splitLines(text):
    res = []
    j = 0
    for i in range(0, len(text)-1):
        if text[i] == '\n':
            res += [text[:i+j]]
            j = i
    res += [text[j+1:]]
    return res


def reformat(pattern):
    for i in range(0, len(pattern)):
        pattern[i] = pattern[i].rstrip()
    return pattern


def turn(pattern):
    newP = []
    print(pattern)
    for i in range(len(pattern[0])):
        a = ""
        for j in range(len(pattern)):
            if pattern[j] != "":
                a += pattern[j][i]
        newP.append(a)
    return newP


def getReflection(pattern):
    print(pattern)
    for i in range(1, len(pattern)):
        if i <= len(pattern)//2:
            p1 = pattern[:i]
            p2 = pattern[i:2*i]
            if p1 == p2:
                print("reflection")
                return i

    pattern.reverse()
    for i in range(1, len(pattern)):
        if i <= len(pattern)//2:
            p1 = pattern[:i]
            p2 = pattern[i:2*i]
            p2.reverse()
            if p1 == p2:
                print("reflection", len(pattern)-i)
                return len(pattern)-i
    return 0


def solve():
    col = []
    row = []
    s = 0
    patterns = splitLines(lines)
    for p in patterns:
        p = reformat(p)

        col.append(getReflection(p))
        row.append(getReflection(turn(p)))
        print("\n")
    print(col)
    s += sum(col * 100)
    s += sum(row)
    print(s)


solve()