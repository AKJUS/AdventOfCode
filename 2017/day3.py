# Advent of Code 2017 - Day 3

import math

def main():
    puzzle = 312051
    lastRow, sideLength = findSquare(puzzle)
    midPoint = math.floor(sideLength/2)
    radius = midPoint
    # Part 1
    distance = (lastRow - midPoint) - puzzle + radius
    print(f"The Distance to the origin is {distance}")

def findSquare(puzzle):
    currentSquare = puzzle
    while math.sqrt(currentSquare).is_integer() == False:
        currentSquare += 1
    return currentSquare, math.sqrt(currentSquare)

if __name__ == "__main__":
    main()
