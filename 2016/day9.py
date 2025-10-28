# Advent of Code 2016 - Day 9
import re

def main():
    rawString = ""
    with open("day9.txt") as puzzle:
        for line in puzzle:
            rawString += line

    part1(rawString)


def part1(string):
    # Regex to find all (1x6) groups
    regexAll = r'\(\d*\dx\d*\d\)'
    allMatches = re.findall(regexAll, string)
    # Regex to find only (1x6) with out any following (1x6) group
    regex = r'\(\d*\dx\d*\d\)(?!\()'
    matches = re.findall(regex, string)


def part2(string):
    pass


if __name__ == "__main__":
    main()
