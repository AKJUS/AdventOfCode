# Advent of Code 2016 - Day 2

instructions = []
test = ["ULL", "RRDDD", "LURDL", "UUUUD"]

with open("day2.txt") as puzzle:
    for line in puzzle:
        instructions.append(line.replace("\n", ""))

keypad = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8 ,9]]

# Start is at button 5
button = {"row": 1, "column": 1}
pin = []

# Part 1
for code in instructions:
    for char in code:
        if char == "U" and button["row"] > 0:
            button["row"] -= 1
        elif char == "D" and button["row"] < 2:
            button["row"] += 1
        elif char == "L" and button["column"] > 0:
            button["column"] -= 1
        elif char == "R" and button["column"] < 2:
            button["column"] += 1
    pin.append(keypad[button["row"]][button["column"]])

print(f"Pin for Part 1 = {pin}")

# Part 2
newKeypad = [[".", ".", "1", ".", "."],
             [".", "2", "3", "4", "."],
             ["5", "6", "7", "8", "9"],
             [".", "A", "B", "C", "."],
             [".", ".", "D", ".", "."]]

newButton = {"row": 2, "column": 0}
newPin = []

for code in instructions:
    for char in code:
        if char == "U" and newButton["row"] > 0 and newKeypad[newButton["row"]-1][newButton["column"]] != ".":
            newButton["row"] -= 1
        elif char == "D" and newButton["row"] < 4 and newKeypad[newButton["row"]+1][newButton["column"]] != ".":
            newButton["row"] += 1
        elif char == "L" and newButton["column"] > 0 and newKeypad[newButton["row"]][newButton["column"]-1] != ".":
            newButton["column"] -= 1
        elif char == "R" and newButton["column"] < 4 and newKeypad[newButton["row"]][newButton["column"]+1] != ".":
            newButton["column"] += 1
    newPin.append(newKeypad[newButton["row"]][newButton["column"]])

print(f"Pin for Part 2 = {newPin}")
