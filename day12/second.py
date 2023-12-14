with open("data.txt") as f:
    lines = f.readlines()



def aRec(springs, group):
    if springs == "" and len(group) == 0:
        return 1
    if len(group) == 0 and springs[0] == ".":
        return aRec(springs[1:], group)
    if len(group) == 0 and springs[0] == "?":
        return aRec(springs[1:], group)
    if len(group) == 0 or springs == "":
        return 0
    if int(group[0]) > len(springs):
        return 0
    if springs[0] == ".":
        return aRec(springs[1:], group)
    if springs[0] == "?":
        return aRec("#" + springs[1:], group) + aRec("." + springs[1:], group)
    if springs[0] == "#":
        ok = True
        for i in range(0, int(group[0])):
            if springs[i] == ".":
                ok = False
        if int(group[0]) < len(springs):
            if springs[int(group[0])] == "#":
                ok = False
        if ok:
            return aRec("." + springs[int(group[0])+1:], group[1:])
        else:
            return 0


def solve():
    res = []
    i = 0
    for line in lines:
        print("Ligne " + str(i) + " : " + line)
        springs = (line.split(" ")[0])
        group = (line.split(" ")[1].rstrip().split(",")) * 5
        for i in range(0, 4):
            springs = (springs + "?" + (line.split(" ")[0]))
        s = aRec(springs, group)
        res.append(s)
        i += 1


    print(res)
    print(sum(res))


solve()