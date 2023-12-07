ranking = 5

with open('data.txt') as f:
    lines = f.readlines()


def isFive(hand):
    for i in hand:
        if hand.count(i) == 5 or (hand.count(i) + hand.count('J') == 5 and i != 'J'):
            return True
    return False


def isFour(hand):
    for i in hand:
        if hand.count(i) == 4 or (hand.count(i) + hand.count('J') == 4 and i != 'J'):
            return True
    return False


def isForOfKind(hand):
    for i in hand:
        if hand.count(i) == 4 or (hand.count(i) + hand.count('J') == 4 and i != 'J'):
            return True
    return False


def isFull(hand):
    diff = {}
    for i in hand:
        if i != 'J':
            diff[i] = hand.count(i)
    if len(diff) > 2:
        return False
    return True


def isThree(hand):
    for i in hand:
        if hand.count(i) == 3 or (hand.count(i) + hand.count('J') == 3 and i != 'J'):
            return True
    return False


def isTwoPair(hand):
    previous = ""
    for i in hand:
        if hand.count(i) == 2 and i != previous and previous != "":
            return True
        elif hand.count(i) == 2 and previous == "":
            previous = i
    return False


def isOnePair(hand):
    for i in hand:
        if hand.count(i) == 2 or (hand.count(i) + hand.count('J') == 2 and i != 'J'):
            return True
    return False

def getValue(hand):
    if isFive(hand):
        return 6
    elif isFour(hand):
        return 5
    elif isFull(hand):
        return 4
    elif isThree(hand):
        return 3
    elif isTwoPair(hand):
        return 2
    elif isOnePair(hand):
        return 1
    else: return 0

def greaterThan(a, b):
    for i in range(0, len(a)):
        if a[i] == b[i]:
            continue
        if a[i] == "A":
            return True
        if a[i] == "K" and b[i] not in ["A"]:
            return True
        if a[i] == "Q" and b[i] not in ["A", "K"]:
            return True
        if a[i] == "T" and b[i] not in ["A", "K", "Q"]:
            return True
        if a[i] > b[i] and a[i].isdigit() and b[i].isdigit():
            return True
        if b[i] == "J":
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

        hands[hand] = getValue(hand)
        hands[hand + "b"] = bid.rstrip()
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
