from math import lcm


with open('data.txt') as f:
    lines = f.readlines()

instructions = lines[0].replace("L","0").replace("R","1")
map = {}

for i in range(2, len(lines)):
    node = lines[i].split(" ")[0]
    nodeLeft = lines[i].split(" ")[2].replace("(", "").replace(",", "")
    nodeRight = lines[i].split(" ")[3].replace(")", "").rstrip()
    map[node] = [nodeLeft, nodeRight]

currents = []
for key in map:
    if key[2] == "A":
        currents.append(key)

print(currents)

i = 0
allZ = False
results = []
alreadyFound = []
while not allZ:
    allZ = True
    for j in range(0, len(currents)):
        if currents[j][2] != "Z":
            currents[j] = map[currents[j]][int(instructions[i % (len(instructions)-1)])]
            allZ = False
        elif currents[j] not in alreadyFound:
            alreadyFound.append(currents[j])
            results.append(i)
    i += 1
print(lcm(results[0], results[1], results[2], results[3], results[4], results[5]))
