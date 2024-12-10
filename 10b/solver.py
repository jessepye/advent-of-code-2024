import copy
import ipdb

inputFile = "input.txt"
# inputFile = "example.txt"
with open(inputFile, "r") as file:
    map = [list(line) for line in file.read().strip().split("\n")]

for y in range(len(map)):
    for x in range(len(map[0])):
        map[y][x] = int(map[y][x])

# helper method to print maps:
def printMap(map):
    print("=====map=====")
    for line in map:
        for c in line:
            print(c, end="")
        print()

def countEndpoints(map, x, y, height):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return 0
    if map[y][x] != height:
        return 0
    # ipdb.set_trace()
    if height == 9 and map[y][x] == 9:
        return 1
    return countEndpoints(map, x - 1, y, height + 1) \
         + countEndpoints(map, x + 1, y, height + 1) \
         + countEndpoints(map, x, y - 1, height + 1) \
         + countEndpoints(map, x, y + 1, height + 1)

def findUniqueEndpoints(map, x, y, height):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return set()
    if map[y][x] != height:
        return set()
    # ipdb.set_trace()
    if height == 9 and map[y][x] == 9:
        return {(x,y)}
    return findUniqueEndpoints(map, x - 1, y, height + 1) \
         | findUniqueEndpoints(map, x + 1, y, height + 1) \
         | findUniqueEndpoints(map, x, y - 1, height + 1) \
         | findUniqueEndpoints(map, x, y + 1, height + 1)

score = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        score += countEndpoints(map, x, y, 0)
print(f"score: {score}")
