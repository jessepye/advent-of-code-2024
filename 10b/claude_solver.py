import copy

def printMap(map):
    print("=====map=====")
    for line in map:
        for c in line:
            print(c, end="")
        print()

def countEndpoints(map, x, y, prev_height, visited):
    # Check bounds
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return 0
    
    # Get current position
    current_height = map[y][x]
    
    # Check if this is a valid next step
    if current_height != prev_height + 1:
        return 0
    
    # Position has been visited
    if (x, y) in visited:
        return 0
        
    # Found a valid endpoint
    if current_height == 9:
        return 1
        
    # Mark current position as visited
    visited.add((x, y))
    
    # Try all directions
    total = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        total += countEndpoints(map, x + dx, y + dy, current_height, visited.copy())
    
    return total

def solve(map):
    score = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 0:  # Only start from trailheads (height 0)
                score += countEndpoints(map, x, y, -1, set())
    return score

# Read and parse input
with open("example.txt", "r") as file:
    map = [[int(c) for c in line.strip()] for line in file.read().strip().split("\n")]

score = solve(map)
print(f"score: {score}")
