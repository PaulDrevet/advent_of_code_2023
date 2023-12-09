with open('data.txt') as f:
    lines = f.readlines()

instructions = lines[0]
current = 'AAA'
map = {}

for i in range(2, len(lines)):
    node = lines[i].split(" ")[0]
    nodeLeft = lines[i].split(" ")[2].replace("(", "").replace(",", "")
    nodeRight = lines[i].split(" ")[3].replace(")", "").rstrip()
    print(node, nodeLeft, nodeRight)
    map[node] = [nodeLeft, nodeRight]

i = 0

while current != "ZZZ":

    if instructions[i % (len(instructions)-1)] == "L":
        current = map[current][0]
    else:
        current = map[current][1]

    i += 1
print(i)

