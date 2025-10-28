# Advent of Code 2017 - Day 2

def main():
    input = []

    with open("day2.txt") as puzzle:
        for line in puzzle:
            clean = line.replace("\n", "").split("\t")
            input.append(clean)

    print(f"The Chechsum for Part 1 = {part1(input)}")

def part1(list):
    sum = 0
    for ls in list:
        temp = []
        for digit in ls:
            temp.append(int(digit))
        sortedTemp = sorted(temp)
        sum += sortedTemp[-1] - sortedTemp[0]
    return sum

if __name__ == "__main__":
    main()
