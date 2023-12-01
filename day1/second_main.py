import re

ret = 0
word_digit_pairs = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')
]

with open('data.txt') as f:
    lines = f.readlines()


for line in lines:
    numbers = re.findall(r'[\d+]|one|two|three|four|five|six|seven|eight|nine', line)
    print(line)
    print(numbers)

    if len(numbers) == 1:
        n = numbers[0]
        if n in [word for word, digit in word_digit_pairs]:
            for word, digit in word_digit_pairs:
                n = n.replace(word, digit)
        s = n + n
        ret += int(s)

    else:
        n = numbers[0]
        n1 = numbers[len(numbers) - 1]

        if n in [word for word, digit in word_digit_pairs]:
            for word, digit in word_digit_pairs:
                n = n.replace(word, digit)
        if n1 in [word for word, digit in word_digit_pairs]:
            for word, digit in word_digit_pairs:
                n1 = n1.replace(word, digit)
        s = n + n1
        ret += int(s)

print(ret)
