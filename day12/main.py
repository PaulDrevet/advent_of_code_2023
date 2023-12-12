with open("data.txt") as f:
    lines = f.readlines()


def check(springs, group):
    springs = springs.split(".")
    while ("" in springs):
        springs.remove("")
    if len(springs) != len(group):
        return False
    for i in range(len(springs)):
        if len(springs[i]) != int(group[i]):
            return False
    return True


def rec(springs, group):
    if springs == "" and len(group) == 0:
        return 1
    if springs == "" or len(group) == 0:
        print(springs, group)
        return 0
    if springs[0] == ".":
        return rec(springs[1:], group)
    if springs[0] == "?":
        return rec("#" + springs[1:], group) + rec("." + springs[1:], group)
    if springs[0] == "#":
        i = 0
        while springs[i] == "#" and i < len(springs)-1:
            i += 1
        if i >= int(group[0]):
            return rec(springs[i:], group[1:])
        else:
            return rec(springs[1:], group)



def getCompletedSpring(springs, group):
    springTest = ""
    print(springs)

    for i in range(len(springs)):
        if springs[i] == "?":
            springTest = springs[:i] + "#" + springs[i+1:]
            for j in range(i, len(springs)):
                if springs[j] == "?":
                    springTest = springTest[:j] + "#" + springTest[j+1:]
                    print(springTest)
        if springs[i] == "?":
            for j in range(i, len(springs)):
                if springs[j] == "?":
                    springTest = springTest[:j] + "#" + springTest[j+1:]
                    print(springTest)
    print()




def solve():
    res = 0
    for line in lines:
        springs = line.split(" ")[0]
        group = line.split(" ")[1].rstrip().split(",")

        s = rec(springs, group)
        print(s)
        res =+ s
    print(res)

solve()