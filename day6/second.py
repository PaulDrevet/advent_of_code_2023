with open('data.txt') as f:
    lines = f.readlines()

time = lines[0].split(":")[1].replace(" ","")

distance = lines[1].split(":")[1].replace(" ","")
print(time)
print(distance)


m = 0
n = 0
time = int(time)
distance = int(distance)
for j in range(0, time):
    travel = (time - j) * j
    print(j, travel, distance)
    if travel > distance:
        print('here')
        n = j
        break
for j in range(time, 0, -1):
    travel = (time - j) * j
    print(j, travel, distance)
    if travel > distance:
        print('here')
        m = j
        break
print(str(m - n + 1))
