# Advent of Code 2016 - Day 1

route = []
test = ["R2", "L3"]
heading = 0
position = {"x": 0, "y": 0}
origin = {"x": 0, "y": 0}

with open("day1.txt") as puzzle:
    for instructions in puzzle:
        instructions = instructions.strip("\n")
        route = instructions.split(", ")


print(position)
