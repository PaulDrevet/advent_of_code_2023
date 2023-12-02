res = 0

with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    red = 1
    green = 1
    blue = 1
    lineCube = line.split(':')
    sets = lineCube[1].split(';')
    for s in sets:
        cubes = s.split(',')
        for cube in cubes:
            cube = cube.strip().split(" ")
            if cube[1].startswith("g") and int(cube[0]) > green:
                green = int(cube[0])
            elif cube[1].startswith("r") and int(cube[0]) > red:
                red = int(cube[0])
            elif cube[1].startswith("b") and int(cube[0]) > blue:
                blue = int(cube[0])
    res += green * red * blue

print(res)



