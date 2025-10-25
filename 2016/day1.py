# Advent of Code 2016 - Day 1

route = []
visited = []
firstTwice = []
test = ["R2", "L3"]
lastMove = "N"
position = {"x": 0, "y": 0}
origin = {"x": 0, "y": 0}
blocks = 0

with open("day1.txt") as puzzle:
    instructions = puzzle.read().replace("\n", "")
    route = instructions.split(", ")


# Part 1
for turn in route:
    moves = int(turn[1:])
    if turn[0] == "R" and lastMove == "N":
        for i in range(1, moves+1):
            position["x"] += 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "E"
    elif turn[0] == "L" and lastMove == "N":
        for i in range(1, moves+1):
            position["x"] -= 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "W"
    elif turn[0] == "R" and lastMove == "E":
        for i in range(1, moves+1):
            position["y"] -= 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "S"
    elif turn[0] == "L" and lastMove == "E":
        for i in range(1, moves+1):
            position["y"] += 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "N"
    elif turn[0] == "R" and lastMove == "S":
        for i in range(1, moves+1):
            position["x"] -= 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "W"
    elif turn[0] == "L" and lastMove == "S":
        for i in range(1, moves+1):
            position["x"] += 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "E"
    elif turn[0] == "R" and lastMove == "W":
        for i in range(1, moves+1):
            position["y"] += 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "N"
    elif turn[0] == "L" and lastMove == "W":
        for i in range(1, moves+1):
            position["y"] -= 1
            if position.copy() in visited and len(firstTwice) == 0:
                firstTwice.append(position.copy())
                visited.append(position.copy())
            else:
                visited.append(position.copy())
        lastMove = "S"

print(f"Target Coordinates are: {position}")

print(f"Shortest Distance in Blocks = {
      abs(position["x"]) + abs(position["y"])}")

print(f"First block visited twice is at = {firstTwice[0]}")

print(f"Shortest Distance to first block visited twice = {abs(firstTwice[0]["x"]) + abs(firstTwice[0]["y"])}")
