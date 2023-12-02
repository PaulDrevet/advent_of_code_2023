red = 12
green = 13
blue = 14
res = 0


with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    valid = True
    lineCube = line.split(':')
    sets = lineCube[1].split(';')
    for s in sets:
        cubes = s.split(',')
        for cube in cubes:
            cube = cube.strip().split(" ")
            print(cube)
            if cube[1].startswith("g") and int(cube[0]) > green:
                valid = False
                break
            elif cube[1].startswith("r") and int(cube[0]) > red:
                valid = False
                break
            elif cube[1].startswith("b") and int(cube[0]) > blue:
                valid = False
                break
        if not valid:
            break
    if valid:
        res+= int(lineCube[0].split(" ")[1])

print(res)



