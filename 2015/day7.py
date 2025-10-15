# Advent of Code 2015 - Day 7
# All found values
values = {}
commands = []

# Open Puzzle
with open("day7.txt") as puzzle:
    for line in puzzle:
        commands.append(line.replace("\n", "").split(" "))

# Look for straight declaration of values
for command in commands:
    if command[0].isdigit() and command[1] == "->":
        values[command[2]] = int(command[0])

# Uncomment out for Part 2
# values["b"] = 956


while True:
    try:
        print(values["a"])
        break
    except KeyError:
        pass

    for command in commands:
        # Direct assignement
        if command[0].isalpha() and command[1] == "->":
            if command[0] in values:
                values[command[2]] = values[command[0]]
        # AND
        if "AND" in command:
            if command[0].isdigit() and command[1] == "AND" and command[2] in values:
                values[command[4]] = int(command[0]) & int(values[command[2]])
            if command[0] in values and command[2] in values:
                values[command[4]] = int(
                    values[command[0]]) & int(values[command[2]])
        # OR
        if "OR" in command:
            if command[0] in values and command[2] in values:
                values[command[4]] = int(
                    values[command[0]]) | int(values[command[2]])
        # LSHIFT
        if "LSHIFT" in command:
            if command[0] in values:
                values[command[4]] = int(
                    values[command[0]]) << int(command[2])
        # RSHIFT
        if "RSHIFT" in command:
            if command[0] in values:
                values[command[4]] = int(
                    values[command[0]]) >> int(command[2])
        # NOT
        if "NOT" in command:
            if command[1] in values:
                values[command[3]] = ~int(values[command[1]]) & 65535
