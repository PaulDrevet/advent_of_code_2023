ranking = 5

with open('data.txt') as f:
    lines = f.readlines()


def greaterThan(a, b):
    for i in range(0, len(a)):
        if a[i] == b[i]:
            continue
        if a[i] == "A" and b[i] not in ["A"]:
            return True
        if a[i] == "K" and b[i] not in ["A", "K"]:
            return True
        if a[i] == "Q" and b[i] not in ["A", "K", "Q"]:
            return True
        if a[i] == "J" and b[i] not in ["A,", "K", "Q", "J"]:
            return True
        if a[i] == "T" and b[i] not in ["A", "K", "Q", "J", "T"]:
            return True
        if a[i] > b[i] and a[i].isdigit() and b[i].isdigit():
            return True
        return False


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if greaterThan(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array


def sortHand(value, dictHands):
    currentHands = []
    for dictHand in dictHands:
        if dictHands.get(dictHand) == value:
            currentHands.append(dictHand)
    return bubble_sort(currentHands)


def getCardValue():
    hands = {}
    d = {}
    for line in lines:
        d = d.fromkeys(d, 0)
        hand = line.split(" ")[0]
        bid = line.split(" ")[1]
        for card in hand:
            if card in d:
                d[card] += 1
            else:
                d[card] = 1
        keys = [k for k, v in d.items() if v == 2]
        power = 0
        if 5 in d.values():
            power = 6
        elif 4 in d.values():
            power = 5
        elif 3 in d.values() and 2 in d.values():
            power = 4
        elif 3 in d.values():
            power = 3
        elif len(keys) == 2:
            power = 2
        elif 2 in d.values():
            power = 1
        hands[hand + "b"] = bid.rstrip()
        hands[hand] = power
    return hands


def getSum(hands, sortedHand):

    s = 0
    sortedHand = sortedHand[::-1]
    print(sortedHand)

    for i in range(0, len(sortedHand)):
        bid = int(hands.get(sortedHand[i] + "b"))
        value = bid * (i+1)
        print(sortedHand[i], bid, i, value)
        s = s + value
    return s


def solve():
    hands = getCardValue()
    sortedHand = []
    for i in range(6, -1, -1):
        sortedHand.extend(sortHand(i, hands)[::-1])
    print(getSum(hands, sortedHand))

solve()
