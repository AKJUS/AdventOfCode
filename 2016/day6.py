# Advent of Code 2016 - Day 6

comRaw = []
columns = []
message = ""

with open("day6.txt") as puzzle:
    for line in puzzle:
        comRaw.append(line.replace("\n", ""))

# Fill columns with empty lists
for i in range (1, 9):
    columns.append([])

# Add each coms char in each of the lists
for snippets in comRaw:
    for index, char in enumerate(snippets):
        columns[index].append(char)

# Part 1
# Count how often each char appears in column
for col in columns:
    counter = {}
    for char in col:
        if char not in counter:
            occur = col.count(char)
            counter[char] = occur
    high = sorted(counter.values())
    key = [key for key, val in counter.items() if val == high[-1]]
    message += key[0]

print(f"The message for Part 1 = {message}")
