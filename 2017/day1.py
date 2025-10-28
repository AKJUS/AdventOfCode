# Advent of Code 2017 - Day 1

def main():
    captcha = []
    test = [[1],[2],[1], [3], [1], [4], [15]]

    with open("day1.txt") as puzzle:
        for input in puzzle:
            input = input.replace("\n", "")
            for num in input:
                captcha.append([int(num)])

    print(f"The sum for Part 1 = {part1(captcha)}")
    print(f"The sum for Part 2 = {part2(captcha)}")



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


def part2(list):
    sum = 0
    indexJump = int(len(list) / 2)
    for index in range(len(list)):
        if index + indexJump > len(list)-1:
            wrap = index + indexJump - len(list)
            if list[index][0] == list[wrap][0]:
                sum += list[index][0]
        else:
            if list[index][0] == list[index + indexJump][0]:
                sum += list[index][0]
    return sum



if __name__ == "__main__":
    main()
