# Advent of Code 2017 - Day 6

def main():
    memory = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
    # memory = [0, 2, 7, 0]

    # Part 1
    partOne, partTwo = part1(memory)
    print(f"Part 1 used {partOne} redistribution cycles")
    # Part 2
    print(f"Part 2 used {partTwo} redistribution cycles")
    


def part1(memory):
    banks = list(memory)
    seen = []
    cyclesPartOne = 0

    while tuple(banks) not in seen:
        seen.append(tuple(banks))
        max_blocks = max(banks)
        index = banks.index(max_blocks)
        banks[index] = 0
        while max_blocks > 0:
            index = (index + 1) % len(banks)
            banks[index] += 1
            max_blocks -= 1

        cyclesPartOne += 1
    # Part 2
    item = list(seen)[-1]
    cyclesPartTwo = 0
    while seen.count(item) != 2:
        seen.append(tuple(banks))
        max_blocks = max(banks)
        index = banks.index(max_blocks)
        banks[index] = 0
        while max_blocks > 0:
            index = (index + 1) % len(banks)
            banks[index] += 1
            max_blocks -= 1

        cyclesPartTwo += 1

    return cyclesPartOne, cyclesPartTwo


if __name__ == "__main__":
    main()
