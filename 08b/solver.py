import ipdb;
import os

# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to input.txt relative to the script location
# input_path = os.path.join(script_dir, "example.txt")
input_path = os.path.join(script_dir, "input.txt")

# helper method to print maps:
def printMap(map):
    print("=====map=====")
    for line in map:
        for c in line:
            print(c, end="")
        print()


map = []
with open(input_path, "r") as file:
    map = [list(x) for x in file.read().strip().split('\n')]

# create a hash with key <frequency> and val <list of (x,y) coordinates>
freqLocs = {}
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] != '.':
            if map[y][x] in freqLocs:
                freqLocs[map[y][x]].append((x,y))
            else:            
                freqLocs[map[y][x]] = [(x,y)]

# for each Frequency, Loop over each pairing of them
# add to the total if the coordinate lands inside the map boundary
def addAntinodesToMap(coordinates: list, xLen: int, yLen: int, antinodeMap: list) -> int:
    print(f"addAntinodesToMap(coordinates: {coordinates})")
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            # look at two pairs of coordinates, (x1, y1) and (x2, y2)
            x1 = coordinates[i][0]
            y1 = coordinates[i][1]
            x2 = coordinates[j][0]
            y2 = coordinates[j][1]

            # there's a better place to add the antinodes but this will work for now
            antinodeMap[y1][x1] = '#'
            antinodeMap[y2][x2] = '#'

            print(f"comparing ({x1},{y1}) and ({x2},{y2})")

            dx = x2 - x1
            dy = y2 - y1

            # antinode 1 (there are now many of these extending in the (-dx, -dy) direction)
            ax1 = x1 - dx
            ay1 = y1 - dy

            while ax1 >= 0 and ax1 < xLen and ay1 >= 0 and ay1 < yLen:
                print(f"antiNode found at ({ax1}, {ay1})")
                antinodeMap[ay1][ax1] = '#'
                ax1 = ax1 - dx
                ay1 = ay1 - dy
                # printMap(antinodeMap)
            print(f"antiNode out of bounds at ({ax1}, {ay1})")

            # antinode 2 (there are now many of these extending in the (dx, dy) direction)
            ax2 = x2 + dx
            ay2 = y2 + dy
            while ax2 >= 0 and ax2 < xLen and ay2 >= 0 and ay2 < yLen:
                print(f"antiNode found at ({ax2}, {ay2})")
                antinodeMap[ay2][ax2] = '#'
                # printMap(antinodeMap)
                ax2 = ax2 + dx
                ay2 = ay2 + dy
            print(f"antiNode out of bounds at ({ax2}, {ay2})")

    return antinodeMap

def countAntinodes(map):
    count = 0
    for line in map:
        for c in line:
            if c=="#":
                count +=1
    return count


totalAntinodes = 0

antinodeMap = [['.'] * len(map[0]) for _ in range(len(map))]

for f in freqLocs:
    print(f"====================================")
    print(f"checking locations for frequency {f}")
    antinodeMap = addAntinodesToMap(freqLocs[f], len(map[0]), len(map), antinodeMap)
printMap(map)
printMap(antinodeMap)

print(countAntinodes(antinodeMap))
