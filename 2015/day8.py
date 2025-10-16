# Advent of Code 2015 - Day 8

import re

# Escape characters used:
# \\ = \
# \" = "
# \xAB = single ASCII character

# Part 1
strings = []
codeLength = 0
valueLength = 0


def getPuzzle():
    with open("day8.txt") as puzzle:
        for line in puzzle:
            strings.append(line)


getPuzzle()

for line in strings:
    codeLength += len(line)
    line = line.replace(r"\\", "o")
    line = line.replace(r'\"', "o")
    match = re.findall(r"\\x..", line)
    for found in match:
        line = line.replace(found, "o")
    valueLength += len(line) - 2
strings = []

print(f"Solution Part 1: {codeLength - valueLength}")

# Part 2
getPuzzle()
# Part 2 - Corrected Logic
strings = []

getPuzzle()

original_length = 0
encoded_length = 0

for line in strings:
    original_length += len(line)
    new_len = len(line)
    new_len += 2
    new_len += line.count('\\')
    new_len += line.count('"')
    encoded_length += new_len

print(f"Solution Part 2: {encoded_length - original_length}")
