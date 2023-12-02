classicList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven",
               "eight",
               "nine"]
reversedList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves",
                "thgie", "enin"]

matchingList = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8),
                ("nine", 9)]

s = 0
m = 0
n = 0
with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    current = ""
    for c in line:
        current = current + c
        if any((match := substring) in current for substring in classicList):
            n = match
            break
    current = ""
    for c in reversed(line):
        current = current + c
        if any((match := substring) in current for substring in reversedList):
            m = match[::-1]
            break
    if not n.isdigit():
        for word, digit in matchingList:
            n = n.replace(word, str(digit))
    if not m.isdigit():
        for word, digit in matchingList:
            m = m.replace(word, str(digit))
    s = s + int(n+m)

print(s)