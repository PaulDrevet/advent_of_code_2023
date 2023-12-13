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


def getReflection(pattern):
    pattern = reformat(pattern)
    print(pattern)
    for i in range(0, len(pattern)):
        if i < len(pattern)//2:
            print(pattern[:i],  "|||" ,pattern[i+1:])
            if pattern[:i] == pattern[i+1:]:
                print("reflection")
                return
        else:
            print(pattern[:i],  "|||" ,pattern[i+1:])





def solve():
    patterns = splitLines(lines)
    for p in patterns:
        getReflection(p)


solve()