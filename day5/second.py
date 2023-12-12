import threading
with open('data.txt') as f:
    lines = f.readlines()

a = {}
res = 10000000000000000000000000000000
seeds2 =[]

def seedToLocation(j):
    res = 1000000000000000000000000000000000000000000000000000000000000000000000000
    for m in a:
        for mapLine in a[m]:
            if int(mapLine[1]) <= j <= int(mapLine[1])+int(mapLine[2]):
                j = int(mapLine[0]) + (j - int(mapLine[1]))
                break
        if m == "humidity-to-location map:":
            if j < res:
                res = j
    return res


seeds = lines[0].split(":")[1].strip().split(" ")
for i in range(1, len(lines)):
    if lines[i][0].isalpha():
        key = lines[i].rstrip()
        a[key] = []
        i += 1
        while lines[i][0] != "\n" and i < len(lines)-1:
            aLine = lines[i].rstrip().split(" ")
            a[key] += [aLine]
            i += 1



min = 1000000000000000000000000000000000000000000000000000000000000000000
bigMin = 1000000000000000000000000000000000000000000000000000000000000000000
for i in range(0, len(seeds), 2):
    inter = 12

    seed = int(seeds[i])
    length = int(seeds[i+1])
    for j in range(seed, seed+length, inter):
        res = seedToLocation(seed+j)
        if res < min:
            min = res
            minInterval = (seed+j-inter, seed+j)
            print(minInterval)
            print(min, "\n")
    if min < bigMin:
        bigMin = min
print(minInterval)
print(bigMin)

for i in range(minInterval[0], minInterval[1]):
    res = seedToLocation(i)
    if res < bigMin:
        bigMin = res
print(bigMin)





