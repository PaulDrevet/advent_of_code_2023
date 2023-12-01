import re
ret = 0

with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    numbers = re.findall(r'[\d+]', line)
    if len(numbers) == 1:
        ret += int(numbers[0] + numbers[0])
    else:
        ret += int(numbers[0] + numbers[len(numbers) - 1])
print(ret)
