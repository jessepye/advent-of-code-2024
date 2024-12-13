import ipdb
import copy
# inputFile = "input.txt"
inputFile = "example.txt"
with open(inputFile, "r") as file:
    map = [list(line) for line in file.read().strip().split('\n')]

# helper method to print maps:
def printMap(map):
    print("=====map=====")
    for line in map:
        for c in line:
            print(c, end="")
        print()

def solve1(map):
    markableMap = copy.deepcopy(map)
    def markPlotAndFindAreaPerimeter(map, x, y): # Is it a good idea to pass in `map` here? Or just use closures
        # is this the right place to put our recursive floodFill function? Feels weird to nest twice
        def floodFill(map, x, y, plotVal): # returns a set of all the points we've filled
            if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
                return set()
            if map[y][x] != plotVal:
                return set()
            plotSet = {(x,y)}
            map[y][x] = '.'
            return plotSet | floodFill(map, x - 1, y, plotVal) \
             | floodFill(map, x + 1, y, plotVal) \
             | floodFill(map, x, y - 1, plotVal) \
             | floodFill(map, x, y + 1, plotVal)

        if map[y][x] == '.':
            return map, 0, 0
        plotSet = floodFill(map, x, y, map[y][x])
        area = len(plotSet)
        perimeter = 0
        for coord in plotSet:
            if (coord[0] - 1, coord[1]) not in plotSet:
                perimeter += 1
            if (coord[0] + 1, coord[1]) not in plotSet:
                perimeter += 1
            if (coord[0], coord[1] - 1) not in plotSet:
                perimeter += 1
            if (coord[0], coord[1] + 1) not in plotSet:
                perimeter += 1
        # printMap(map)
        return map, area, perimeter

    totalCost = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            # we will replace the plot with `.`s so we don't double count, is there a more elegant way of doing this?
            markableMap, area, perimeter = markPlotAndFindAreaPerimeter(markableMap, x, y) 
            totalCost += area * perimeter
    return totalCost

def solve2(map):
    def markPlotAndFindAreaAndSides(map, x, y): # Is it a good idea to pass in `map` here? Or just use closures
        # is this the right place to put our recursive floodFill function? Feels weird to nest twice
        def floodFill(map, x, y, plotVal): # returns a set of all the points we've filled
            if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
                return set()
            if map[y][x] != plotVal:
                return set()
            plotSet = {(x,y)}
            map[y][x] = '.'
            return plotSet | floodFill(map, x - 1, y, plotVal) \
             | floodFill(map, x + 1, y, plotVal) \
             | floodFill(map, x, y - 1, plotVal) \
             | floodFill(map, x, y + 1, plotVal)

        if map[y][x] == '.':
            return map, 0, 0
        plotSet = floodFill(map, x, y, map[y][x])
        area = len(plotSet)
        sides = 0
        # trick: corners == sides... but are easier to count

        for coord in plotSet:
            # check each of the 4 corners of this coordinate.
            # if the one at `corner` is in, the other 3 need to be out
            # if the one at `corner` is out, the other 3 need to be in
            for cornerDir in {(-1, -1), (-1, 1), (1, -1), (1, 1)}:
                cornerIsIn = (coord[0] + cornerDir[0], coord[1] + cornerDir[1]) in plotSet
                otherCornerDirs = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
                otherCornerDirs.remove(cornerDir)
                otherCorners = []
                for otherCornerDir in otherCornerDirs:
                    otherCorners.add()

        return map, area, sides

    totalCost = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            # we will replace the plot with `.`s so we don't double count, is there a more elegant way of doing this?
            map, area, sides = markPlotAndFindAreaAndSides(map, x, y) 
            totalCost += area * sides
    return totalCost

print(f"initial map:")
printMap(map)

print(solve1(map))
print(solve2(map))
