# Advent of Code 2016 - Day 3

triangles = []

with open("day3.txt") as puzzle:
    for line in puzzle:
        triangles.append(line.replace("\n", "").strip())

validTriangles = 0

for tri in triangles:
    sides = tri.split(",")
    sides = sides[0].split()
    a, b, c = int(sides[0]), int(sides[1]), int(sides[2])
    if(a+b > c) and (a+c > b) and (c+b > a):
        validTriangles += 1
print(validTriangles)
