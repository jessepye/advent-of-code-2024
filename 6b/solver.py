import ipdb
import os
import copy

# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to input.txt relative to the script location
input_path = os.path.join(script_dir, "input.txt")
solved_room_path = os.path.join(script_dir, "solved_room.txt")

def printRoom(room):
    for line in room:
        for c in line:
            print(c, end="")
        print()

originalRoom = []

with open(input_path, "r") as file:
    originalRoom = [list(line) for line in file.read().strip().split("\n")]

solvedRoom = []

with open(solved_room_path, "r") as file:
    solvedRoom = [list(line) for line in file.read().strip().split("\n")]


# find the starting position
x, y = 0, 0
for y in range(len(originalRoom)):
    if '^' in originalRoom[y]:
        x = originalRoom[y].index('^')
        break

startingX , startingY = x, y
# print(f"starting position ({x}, {y})")

def producesLoop(room, x, y) -> bool:
    dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))  # dx, dy
    currentDir = 0 # (0, -1), which represents North
    numSteps = 0
    # TODO: more effecient loop detection
    maxPossibleSteps = len(room) * len(room[0]) * 4
    while True:
        # room[y][x] = 'X'
        numSteps += 1

        if numSteps > maxPossibleSteps:
            return True

        nextX = x + dirs[currentDir][0]
        nextY = y + dirs[currentDir][1]

        # Are we still in the room?
        if nextX < 0 or nextX >= len(room[y]) or nextY < 0 or nextY >= len(room):
            # print("we have left the room")
            return False

        nextLoc = room[nextY][nextX]

        # found wall, rotate
        if nextLoc == '#': 
            currentDir = (currentDir + 1) % (len(dirs))
            continue
        else:
            x = nextX
            y = nextY
            continue

# print(f"Original Room:")
# printRoom(originalRoom)
#
# print(f"Solved Room")
# printRoom(solvedRoom)

# Change each 'X' one at a time to a '#' and see if it produces a loop

total = 0

for y in range(len(solvedRoom)):
    for x in range(len(solvedRoom[y])):
        if solvedRoom[y][x] == 'X':
            modifiedRoom = copy.deepcopy(originalRoom)
            modifiedRoom[y][x] = '#'
            if producesLoop(modifiedRoom, startingX, startingY):
                total += 1
                # print(f"Found a loop when placing a wall at {x}, {y}. New total: {total}")

print(total)

