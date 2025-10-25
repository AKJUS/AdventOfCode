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

print(pin)
