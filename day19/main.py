with open('data.txt') as f:
    lines = f.readlines()


def process(part, workflow):
    res = "in"
    part = [eval(i) for i in part]
    while res != "R" and res != "A":
        for i in range(len(workflow[res])-1):
            con = workflow[res][i]
            letter = con[0]
            comparator = con[1]
            number = con.split(":")[0][2:]
            r = con.split(":")[1]
            if letter == "x":
                partN = int(part[0])
                if comparator == ">":
                    if partN > int(number):
                        res = r
                        break
                elif comparator == "<":
                    if partN < int(number):
                        res = r
                        break
            elif letter == "m":
                partN = int(part[1])
                if comparator == ">":
                    if partN > int(number):
                        res = r
                        break
                elif comparator == "<":
                    if partN < int(number):
                        res = r
                        break
            elif letter == "a":
                partN = int(part[2])
                if comparator == ">":
                    if partN > int(number):
                        res = r
                        break
                elif comparator == "<":
                    if partN < int(number):
                        res = r
                        break
            elif letter == "s":
                partN = int(part[3])
                if comparator == ">":
                    if partN > int(number):
                        res = r
                        break
                elif comparator == "<":
                    if partN < int(number):
                        res = r
                        break

        if res != "R" and res != "A":
            res = workflow[res][-1]

        if res == "A":
            print(sum(part))
            return sum(part)

    return 0


def solve():
    workflow = {}
    i = 0
    while lines[i] != "\n":
        line = lines[i]
        if line == "\n":
            break
        name = line.split("{")[0]
        work = line.split("{")[1].split("}")[0].split(",")
        workflow[name] = work
        i += 1

    i += 1
    s = 0
    while i < len(lines):
        line = lines[i]
        part = line.split("{")[1].split("}")[0].replace("x", "").replace("m", "").replace("a", "").replace("s", "").replace("=", "").split(",")
        s += process(part, workflow)
        i += 1

    print(s)


solve()

