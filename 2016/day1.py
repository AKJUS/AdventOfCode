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
    if turn[0] == "R" and lastMove == "N":
        position["x"] += int(turn.replace("R", ""))
        visited.append(position.copy())
        lastMove = "E"
    elif turn[0] == "L" and lastMove == "N":
        position["x"] -= int(turn.replace("L", ""))
        visited.append(position.copy())
        lastMove = "W"
    elif turn[0] == "R" and lastMove == "E":
        position["y"] -= int(turn.replace("R", ""))
        visited.append(position.copy())
        lastMove = "S"
    elif turn[0] == "L" and lastMove == "E":
        position["y"] += int(turn.replace("L", ""))
        visited.append(position.copy())
        lastMove = "N"
    elif turn[0] == "R" and lastMove == "S":
        position["x"] -= int(turn.replace("R", ""))
        visited.append(position.copy())
        lastMove = "W"
    elif turn[0] == "L" and lastMove == "S":
        position["x"] += int(turn.replace("L", ""))
        visited.append(position.copy())
        lastMove = "E"
    elif turn[0] == "R" and lastMove == "W":
        position["y"] += int(turn.replace("R", ""))
        visited.append(position.copy())
        lastMove = "N"
    elif turn[0] == "L" and lastMove == "W":
        position["y"] -= int(turn.replace("L", ""))
        visited.append(position.copy())
        lastMove = "S"

print(f"Target Coordinates are: {position}")

print(f"Shortest Distance in Blocks = {
      abs(position["x"]) + abs(position["y"])}")
