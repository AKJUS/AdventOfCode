# Advent of Code 2017 - Day 7

def main():
    progs = []
    with open("day7.txt") as puzzle:
        for row in puzzle:
            progs.append(row.replace("\n", ""))

    # Part1:
    print(f"The base for Part 1 = {part1(progs)}")


def part1(progs):
    input = progs
    topLevel = []
    base = []
    for item in progs:
        if "->" not in item:
            topLevel.append(item.split(" ")[0])

    def findBase(current):
        base.append(current)
        for item in input:
            if "->" in item and current in item.split("->")[1]:
                if isinstance(item.split(" ")[0], str):
                    return findBase(item.split(" ")[0])

    findBase(topLevel[1])
    return base[-1]

def part2():
    pass


if __name__ == "__main__":
    main()
