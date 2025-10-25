# Advent of Code 2016 - Day 3

triangles = []

with open("day3.txt") as puzzle:
    for line in puzzle:
        triangles.append(line.replace("\n", "").strip())

# Part 1
validTriangles = 0
sideA = []
sideB = []
sideC = []

for tri in triangles:
    sides = tri.split(",")
    sides = sides[0].split()
    a, b, c = int(sides[0]), int(sides[1]), int(sides[2])
    sideA.append(a)
    sideB.append(b)
    sideC.append(c)
    if(a+b > c) and (a+c > b) and (c+b > a):
        validTriangles += 1
print(f"There are {validTriangles} for Part 1")

# Part 1
validVerticals = 0

newTriangles = []

def sourceColumns(source, target):
    while len(source) != 0:
        temp = []
        temp.append(source[0])
        temp.append(source[1])
        temp.append(source[2])
        source.remove(source[0])
        source.remove(source[0])
        source.remove(source[0])
        target.append(temp)
    return target

newTriangles = sourceColumns(sideA, newTriangles)
newTriangles = sourceColumns(sideB, newTriangles)
newTriangles = sourceColumns(sideC, newTriangles)

for lst in newTriangles:
    if lst[0]+lst[1] > lst[2] and lst[0]+lst[2] > lst[1] and lst[1]+lst[2] > lst[0]:
        validVerticals += 1
print(f"There are {validVerticals} for Part 2")
