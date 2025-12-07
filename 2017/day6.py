# Advent of Code 2017 - Day 6

def main():
    memory = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
    # memory = [0, 2, 7, 0]

    # Part 1
    print(f"Part 1 used {part1(memory)} redistribution cycles")


def part1(memory):
    banks = list(memory)
    seen = set()
    cycles = 0

    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        max_blocks = max(banks)
        index = banks.index(max_blocks)
        banks[index] = 0
        while max_blocks > 0:
            index = (index + 1) % len(banks)
            banks[index] += 1
            max_blocks -= 1

        cycles += 1

    return cycles



def part2():
    pass


if __name__ == "__main__":
    main()
