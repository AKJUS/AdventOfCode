# Advent of Code 2016 - Day 7

# Switching to proper python structure for code
import re

def main():
    # 2000 IPs
    ips = []

    with open("day7.txt") as puzzle:
        for line in puzzle:
            ips.append(line.replace("\n", ""))
    # Part 1
    print(f"Part 1 found {part1(ips)} valid IPs")


def part1(ips):
    validIPCounter = 0

    def searchForPattern(string):
        for i in range(len(string) - 3):
            if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
                return True
        return False


    for ip in ips:
        hyperContains = False
        # Find all bracket enclosed hypernets
        regex = r'\[([^\]]+)\]'
        hypernets = re.findall(regex, ip)

        # Remove all hypernets from ip and remove brackets
        for hyper in hypernets:
            hyper = "["+hyper+"]"
            ip = ip.replace(hyper, " ")

        # Check if hypernets contain pattern
        for hyper in hypernets:
            if searchForPattern(hyper) != False:
                hyperContains = True
                break
        if hyperContains == False and searchForPattern(ip) == True:
            validIPCounter += 1
    return validIPCounter


def part2(ips):
    pass


if __name__ == "__main__":
    main()
