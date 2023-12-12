with open("data.txt") as f:
    lines = f.readlines()


def rec(springs, group):
    print(springs, group)
    if springs == "" and len(group) == 0:
        print("working")
        return 1
    if len(group) == 0 and springs[0] == ".":
        return rec(springs[1:], group)
    if len(group) == 0 or springs == "":
        return 0
    if springs[0] == ".":
        return rec(springs[1:], group)
    if springs[0] == "?":
        return rec("#" + springs[1:], group) + rec("." + springs[1:], group)
    if springs[0] == "#":
        i = 0
        while (springs[i] == "#" or springs[i] == "?") and i < len(springs)-1 and i < int(group[0]):
            i += 1
        if springs[i] == "#":
            i += 1
        print(i, int(group[0]))
        if i == int(group[0]):
            if i < len(springs):
                print("return 2")
                return rec("." + springs[int(group[0])+1:], group[1:])
            else:
                print("return 3")
                return rec(springs[int(group[0]):], group[1:])
        else:
            print("return 4")
            return 0


def solve():
    res = []
    for line in lines:
        springs = line.split(" ")[0]
        group = line.split(" ")[1].rstrip().split(",")

        s = rec(springs, group)
        res.append(s)
        print("\n\n\n\n")
    print(res)

solve()