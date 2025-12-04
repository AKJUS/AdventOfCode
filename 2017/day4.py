# Advent of Code 2017 - Day 4

def main():
    phrases = []
    with open("day4.txt") as puzzle:
        for row in puzzle:
            phrases.append(row.replace("\n", ""))
    
    # Part 1
    print(f"Part 1 found {part1(phrases)} valid passphrases")


def part1(phrases):
    valid = 0
    for phrase in phrases:
        seen = []
        current = phrase.split(" ")
        for word in current:
            if word not in seen:
                seen.append(word)
        if len(seen) == len(current):
            valid += 1
    return valid


def part2():
    pass


if __name__ == "__main__":
    main()
