import threading
with open('data.txt') as f:
    lines = f.readlines()

a = {}
res = 10000000000000000000000000000000
seeds2 =[]

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

def seedToLocation(seed, length):
    res = 1000000000000000000000000000000000000000000000000000000000000000000000000
    print("Thread started" + str(seed))
    for j in range(seed, seed+length):
        for m in a:
            for mapLine in a[m]:
                if int(mapLine[1]) <= j <= int(mapLine[1])+int(mapLine[2]):
                    j = int(mapLine[0]) + (j - int(mapLine[1]))
                    break
            if m == "humidity-to-location map:":
                if j < res:
                    res = j
    print(res)


for i in range(0, len(seeds), 2):
    seed = int(seeds[i])
    length = int(seeds[i+1])
    threading.Thread(target=seedToLocation, args=(seed, length)).start()



