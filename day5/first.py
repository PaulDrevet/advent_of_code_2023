with open('data.txt') as f:
    lines = f.readlines()

a = {}
res = 10000000000000000000000000000000

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

for seed in seeds:
    seed = int(seed)
    for m in a:
        for mapLine in a[m]:
            if int(mapLine[1]) <= seed <= int(mapLine[1])+int(mapLine[2]):
                seed = int(mapLine[0]) + (seed - int(mapLine[1]))
                break
        if m == "humidity-to-location map:":
            if seed < res:
                res = seed

print(res)

