# Advent of Code 2016 - Day 8

# Screen
# -------------------------------------------------
# |                                                |
# |                   50 x 6                       |
# |                                                |
# --------------------------------------------------


def main():
    instructions = []

    with open("day8.txt") as puzzle:
        for line in puzzle:
            instructions.append(line.replace("\n", ""))

    # Create Display as list
    # 6 rows and 50 columns
    display = []
    for r in range(6):
        row = []
        for c in range(50):
            c = "."
            row.append(c)
        display.append(row)

    print(f"In Part 1 {part1(instructions, display)} Pixels are active")
    #part1(["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4"], display)
    print(f"The Code for Part 2 is {part2()}")


def printDisplay(display):
    for row in display:
        displayRow = ""
        for pixel in row:
            displayRow += pixel
        print(displayRow)


def part1(instructions, display):
    for action in instructions:
        # RECT
        if "rect" in action:
            y = int(action.split(" ")[1].split("x")[0])
            x = int(action.split(" ")[1].split("x")[1])
            for r in range(x):
                for c in range(y):
                    display[r][c] = "#"

        # COLUMN SHIFT
        elif "column" in action:
            shift = int(action.split("column")[1].split(" by ")[1])
            x = int(action.split("column")[1].split(" by ")[0].replace(" x=", ""))
            found = []
            shifted = []
            for r in range(5):
                if display[r][x] == "#":
                    found.append(r)
            for y in found:
                # no wrapping
                if y + shift < 6:
                    display[y+shift][x] = "#"
                    shifted.append(y+shift)
                    if y not in shifted:
                        display[y][x] = "."
                # wrapping
                else:
                    newY = y + shift - 6
                    display[newY][x] = "#"
                    shifted.append(newY)
                    if y not in shifted:
                        display[y][x] = "."

        # ROW SHIFT
        elif "row" in action:
            y = int(action.replace("rotate row y=", "").split(" by ")[0])
            shift = int(action.replace("rotate row y=", "").split(" by ")[1])
            found = []
            shifted = []
            for x in range(50):
                if display[y][x] == "#":
                    found.append(x)
            for x in found:
                # no wrapping
                if x + shift < 50:
                    display[y][x+shift] = "#"
                    shifted.append(x+shift)
                    if x not in shifted:
                        display[y][x] = "."
                # wrapping
                else:
                    newX = x + shift - 50
                    display[y][newX] = "#"
                    shifted.append(newX)
                    if x not in shifted:
                        display[y][x] = "."

    printDisplay(display)
    # Count active Pixel
    count = 0
    for row in display:
        for pixel in row:
            if pixel == "#":
                count += 1
    return count


def part2():
    return "UPOJFLBCEZ"


if __name__ == "__main__":
    main()
