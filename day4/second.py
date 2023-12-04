with open('data.txt') as f:
    lines = f.readlines()

s = 0
cardS = 0
tab = [1] * len(lines)
for i in range(len(lines)):
    card = lines[i].split(":")[1]
    winningNumbers = card.split("|")[0].strip().split(" ")
    numbers = card.split("|")[1].strip().split(" ")
    for number in numbers:
        if number == "":
            numbers.remove(number)
    for number in numbers:
        if number in winningNumbers and number.isdigit():
            cardS += 1
    for j in range(i+1, i+cardS+1):
        tab[j] += 1 * tab[i]

    cardS = 0

print(sum(tab))

