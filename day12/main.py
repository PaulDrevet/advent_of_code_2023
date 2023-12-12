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
    for line in lines:
        springs = line.split(" ")[0]
        group = line.split(" ")[1].rstrip().split(",")

        getCompletedSpring(springs, group)


solve()