# Advent of Code 2015 Day 9

cityNames = ["Faerun", "Norrath", "Tristram",
             "AlphaCentauri", "Arbre", "Snowdin", "Tambi"]
route = []
citiesPairs = []

with open("day9.txt") as puzzle:
    for line in puzzle:
        raw = line.strip("\n").split("=")
        cities = raw[0].split(" to ")
        cities[1] = cities[1].strip()
        cities.append(int(raw[1]))
        citiesPairs.append(cities)
