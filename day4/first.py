with open('data.txt') as f:
    lines = f.readlines()

s = 0
cardS = 0
for line in lines:
    card = line.split(":")[1]
    winningNumbers = card.split("|")[0].strip().split(" ")
    numbers = card.split("|")[1].strip().split(" ")
    for number in numbers:
        if number == "":
            numbers.remove(number)
    for number in numbers:
        if number in winningNumbers and number.isdigit():
            cardS = 1 if cardS == 0 else cardS * 2
    s += cardS
    cardS = 0

print(s)

