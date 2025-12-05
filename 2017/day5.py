# Advent of Code 2017 - Day 5

def main():
    instructions = []
    with open("day5.txt") as puzzle:
        for row in puzzle:
            instructions.append(int(row.replace("\n", "")))
    
    # Part 1
    print(f"Part 1 takes {part1(instructions)} steps to exit")
    # Part 2
    print(f"Part 2 takes {part2(instructions)} steps to exit")


def part1(instructions):
    maze = list(instructions)
    index = 0
    steps = 0
    while True:
        try:
            if maze[index] == 0:
                maze[index] += 1
                steps += 1
            else:
                current = index
                index = index + maze[index]
                maze[current] += 1
                steps += 1
        except IndexError:
            break
    return steps


def part2(instructions):
    maze = list(instructions)
    index = 0
    steps = 0
    while True:
        try:
            if maze[index] == 0:
                maze[index] += 1
                steps += 1
            else:
                current = index
                if maze[index] >= 3:
                    index = index + maze[index]
                    maze[current] -= 1
                else:
                    index = index + maze[index]
                    maze[current] += 1
                steps += 1
        except IndexError:
            break
    return steps


if __name__ == "__main__":
    main()
