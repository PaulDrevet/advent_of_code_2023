with open('test.txt') as f:
    lines = f.readlines()

a = {}
res = 10000000000000000000000000000000

seeds = lines[0].split(":")[1].strip().split(" ")
for i in range(1, len(lines)):
    if lines[i][0].isalpha():
        key = lines[i].rstrip()
        a[key] = []
        i += 1
        while i < (len(lines)) and lines[i][0] != "\n" :
            aLine = lines[i].rstrip().split(" ")
            a[key] += [aLine]
            i += 1


print("\n")
a = dict(reversed(list(a.items())))
notFound = True
placement = 0
i = 0
print(a)
while notFound:
    placement = i
    for m in a:
        for mapLine in a[m]:
            if int(mapLine[1]) <= placement <= int(mapLine[1])+int(mapLine[2]):
                placement = int(mapLine[0]) - (placement - int(mapLine[1]))
                break
    print(placement)
    if placement in seeds:
        print(placement)
        notFound = False
    else:
        i += 1

print(res)

