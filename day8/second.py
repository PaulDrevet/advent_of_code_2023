with open('data.txt') as f:
    lines = f.readlines()

instructions = lines[0].replace("L","0").replace("R","1")
print(instructions)
map = {}
res = 0

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
while not allZ:
    allZ = True
    for j in range(0, len(currents)):
        currents[j] = map[currents[j]][int(instructions[i % (len(instructions)-1)])]
        if currents[j][2] != "Z":
            allZ = False
    i += 1



print(currents)
print(i)
