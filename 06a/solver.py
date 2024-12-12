import ipdb;
import os

# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to input.txt relative to the script location
input_path = os.path.join(script_dir, "input.txt")

room = []

def printRoom():
    for line in room:
        for c in line:
            print(c, end="")
        print()

with open(input_path, "r") as file:
    room = [list(line) for line in file.read().strip().split("\n")]

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))  # dx, dy
currentDir = 0 # (0, -1), which represents North

# find the starting position
x, y = 0, 0
for y in range(len(room)):
    if '^' in room[y]:
        x = room[y].index('^')
        break

print(x, y)

while True:
    room[y][x] = 'X'
    # printRoom()
    nextX = x + dirs[currentDir][0]
    nextY = y + dirs[currentDir][1]
    # Are we still in the room?
    # ipdb.set_trace()
    if nextX < 0 or nextX >= len(room[y]) or nextY < 0 or nextY >= len(room):
        print("we have left the room")
        break
    nextLoc = room[nextY][nextX]
    if nextLoc == '#':
        currentDir = (currentDir + 1) % (len(dirs))
        continue
    if nextLoc == '.' or nextLoc == 'X':
        x = nextX
        y = nextY
        continue
    print("we shouldn't be here...")

total = sum(line.count('X') for line in room)
printRoom()
print(total)

