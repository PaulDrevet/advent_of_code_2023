with open('data.txt') as f:
    lines = f.readlines()

symbols = ["*", "#", "+", "$", "%", "&", "!", "?", "£", "€", "§", "(", ")", "[", "]", "{", "}", "<", ">", ":", ";", ",",
           "-", "_", "=", "'", '"', " ", "@","/","\\"]
currentNumber = ""
valid = False
s = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if not lines[i][j].isdigit():
            if valid:
                s += int(currentNumber)
                print("1 :" + currentNumber)
            currentNumber = ""
            valid = False
        else:
            currentNumber += lines[i][j]
            print("2 :" + currentNumber)
            for k in range(i - 1, i + 2):
                for m in range(j - 1, j + 2):
                    if not (k < 0 or k > len(lines) - 1 or m < 0 or m > len(lines[k]) - 1):
                        if lines[k][m] in symbols:
                            valid = True

print(s)
