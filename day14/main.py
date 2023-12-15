with open('data.txt') as f:
    lines = f.readlines()


def solve():
    s = 0
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                m = i
                while m > 0 :
                    m -= 1
                    if lines[m][j] != ".":
                        lines[i] = lines[i][:j] + "." + lines[i][j+1:]
                        lines[m+1] = lines[m+1][:j] + "O" + lines[m+1][j+1:]
                        break
                    if m == 0:
                        lines[i] = lines[i][:j] + "." + lines[i][j+1:]
                        lines[m] = lines[m][:j] + "O" + lines[m][j+1:]
                        break
    print("\n")
    for i in range(len(lines)):
        s += lines[i].count("O")*(len(lines)- i)
    print(s)



solve()