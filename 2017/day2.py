# Advent of Code 2017 - Day 2

def main():
    puzzle = 312051

    # Find height and width of spiral
    sqroot = 0
    input = puzzle
    while True:
        sqroot = input**0.5
        if sqroot.is_integer():
            print(input)
            break
        else:
            input += 1


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    main()
