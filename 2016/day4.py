# Advent of Code 2016 - Day 4

encrypted = []

with open("day4.txt") as puzzle:
    for line in puzzle:
        encrypted.append(line.replace("\n", ""))

# Part 1
idSum = 0

for crypt in encrypted:
    counts = {}
    hash = crypt[-7:].replace("[", "").replace("]", "")
    id = crypt[-10:-7]
    wholeString = crypt.replace(hash, "").replace(id, "").replace("-", "").replace("[", "").replace("]", "")
    for char in wholeString:
        if char in counts:
            counts[char] += wholeString.count(char)
        else:
            counts[char] = wholeString.count(char)
        wholeString.replace(char, "")
    hashCheck = {}
    for char in hash:
        if char in counts:
            hashCheck[char] = counts[char]
        else:
            break
    if len(hashCheck) == 5:
        if hashCheck[hash[0]] >= hashCheck[hash[1]] >= hashCheck[hash[2]] >= hashCheck[hash[3]] >= hashCheck[hash[4]]:
            numbers = []
            target = []
            for number in hashCheck.values():
                numbers.append(number)
            for number in numbers:
                if numbers.count(number) > 1:
                    target.append(number)
            target = set(target)
            target = list(target)
            alpha = True
            for single in target:
                keys = [key for key, val in hashCheck.items() if val == single]
                if keys != sorted(keys):
                    alpha = False
            if alpha == True:
                idSum += int(id)

print(f"The sum of all valid room IDs = {idSum}")

# Part 2
# length 26
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for crypt in encrypted:
    solution = ""
    crypt = crypt[:-7]
    id = int(crypt[-3:])
    crypt = crypt[:-4].split("-")
    for word in crypt:
        for char in word:
            shift = id%26
            index = abc.index(char)
            newIndex = index+shift
            if newIndex > 25:
                newIndex = newIndex - 26
                solution += abc[newIndex]
            else:
                solution += abc[newIndex]
    if "north" in solution:
        print(f"The ID of the North Pole Objects = {id}")

