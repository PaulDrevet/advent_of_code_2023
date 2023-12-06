with open('data.txt') as f:
    lines = f.readlines()

times = lines[0].split(":")[1].rstrip().split(" ")
times = [ele for ele in times if ele.strip()]

distances = lines[1].split(":")[1].rstrip().split(" ")
distances = [ele for ele in distances if ele.strip()]


res = 1
for i in range(len(times)):
    s = 0
    time = int(times[i])
    distance = int(distances[i])
    for j in range(0, time):
        travel = (time - j) * j
        print(j, travel, distance)
        if travel > distance:
            print('here')
            s += 1
    print(time, distance)
    print(s)
    res = res * s
print(res)