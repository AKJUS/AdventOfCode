# Advent of Code 2015 - Day 8

import re

# Escape characters used:
# \\ = \
# \" = "
# \xAB = single ASCII character

strings = []
codeLength = 0
valueLength = 0

with open("day8.txt") as puzzle:
    for line in puzzle:
        strings.append(line)

for line in strings:
    codeLength += len(line)
    line = line.replace(r"\\", "o")
    line = line.replace(r'\"', "o")
    match = re.findall(r"\\x..", line)
    for found in match:
        line = line.replace(found, "o")
    valueLength += len(line) - 2

print(codeLength - valueLength)
