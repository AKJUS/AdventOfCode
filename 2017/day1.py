# Advent of Code 2017 - Day 1

def main():
    captcha = []

    with open("day1.txt") as puzzle:
        for input in puzzle:
            input = input.replace("\n", "")
            for num in input:
                captcha.append([int(num)])

    print(f"The sum for Part 1 = {part1(captcha)}")


def part1(list):
    sum = 0
    for index in range(len(list)):
        if index != len(list)-1:
            if list[index][0] == list[index+1][0]:
                sum += list[index][0]
        else:
            if list[index][0] == list[0][0]:
                sum += list[index][0]
    return sum


def part2():
    pass


if __name__ == "__main__":
    main()
