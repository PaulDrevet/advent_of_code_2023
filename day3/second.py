with open('data.txt') as f:
    lines = f.readlines()

currentNumber = ""
currentNumbers = []
valid = 0
s = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        ks = []
        ms = []
        if lines[i][j] == "*":
            for k in range(i - 1, i + 2):
                for m in range(j - 1, j + 2):
                    if (0 <= k < len(lines)) and (0 <=m < len(lines[k])):
                        if lines[k][m].isdigit():
                            if not (k in ks and m in ms):
                                valid += 1
                                ks.append(k)
                                ms.append(m)
                                mLeft = m-1
                                mRight = m+1
                                currentNumber = lines[k][m]
                                while mLeft >= 0 and lines[k][mLeft].isdigit():
                                    currentNumber = lines[k][mLeft] + currentNumber
                                    ms.append(mLeft)
                                    mLeft = mLeft - 1
                                while mRight < len(lines[k]) and lines[k][mRight].isdigit():
                                    currentNumber = currentNumber + lines[k][mRight]
                                    ms.append(mRight)
                                    mRight += 1

                                currentNumbers.append(currentNumber)
                                print(currentNumbers)
        else:
            if valid == 2:
                print(currentNumbers)
                s += int(currentNumbers[0])*int(currentNumbers[1])
            valid = 0
            ks = []
            ms = []
            currentNumber = ""
            currentNumbers = []

print(s)
