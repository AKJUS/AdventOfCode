# Advent of Code 2017 - Day 2

def main():
    input = []

    with open("day2.txt") as puzzle:
        for line in puzzle:
            clean = line.replace("\n", "").split("\t")
            input.append(clean)

    print(f"The Chechsum for Part 1 = {part1(input)}")
    print(f"The sum of the even divisons in Part 2 are = {part2(input)}")


def part1(list):
    sum = 0
    for ls in list:
        temp = []
        for digit in ls:
            temp.append(int(digit))
        sortedTemp = sorted(temp)
        sum += sortedTemp[-1] - sortedTemp[0]
    return sum


def part2(list):
    sum = 0
    for ls in list:
        temp = []
        for digit in ls:
            temp.append(int(digit))
        sortedTemp = sorted(temp, reverse=True)
        for number in temp:
            for i in range(len(temp)):
                if number != temp[i]:
                    if number%temp[i] == 0:
                        sum += number/temp[i]
    return sum



if __name__ == "__main__":
    main()
