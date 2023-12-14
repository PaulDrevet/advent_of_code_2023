with open("data.txt") as f:
    lines = f.readlines()

def splitLines(text):
    res = []
    j = 0
    for i in range(0, len(text)-1):
        if text[i] == '\n':
            res += [text[:i+j]]
            print(text[:i])
            j = i
    res += [text[j+1:]]
    print(res)
    return res


def reformat(pattern):
    for i in range(0, len(pattern)):
        pattern[i] = pattern[i].rstrip()
    return pattern

def turn(pattern):
    newPattern = list(zip(*pattern[::-1]))
    return ["".join(x) for x in newPattern]





def getReflection(pattern):
    pattern = reformat(pattern)
    for i in range(1, len(pattern)):
        if i <= len(pattern)//2:
            p1 = pattern[:i]
            p2 = pattern[i:2*i]
            if p1 == p2:
                print("reflection")

    pattern.reverse()
    for i in range(1, len(pattern)):
        if i <= len(pattern)//2:
            p1 = pattern[:i]
            p2 = pattern[i:2*i]
            p2.reverse()
            if p1 == p2:
                print("reflection", len(pattern)-i)



    print("\n\n")




def solve():
    patterns = splitLines(lines)
    print(patterns)
    for p in patterns:
        getReflection(p)
        newP = turn(p)
    for a in newP:
        print(a)


solve()