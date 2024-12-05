# import ipdb;
import os

# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to input.txt relative to the script location
input_path = os.path.join(script_dir, "input.txt")

textArray = []
with open(input_path, "r") as file:
    for line in file:
        textArray.append(line)

# Uses textArray from the global scope
def charMatchesAt(c, i, j):
    return i >= 0 and i < len(textArray) \
       and j >= 0 and j < len(textArray[i]) \
       and textArray[i][j] == c

matches = 0
# ipdb.set_trace()
for i in range(len(textArray)):
    for j in range(len(textArray[i])):
        if charMatchesAt('X', i, j):
            # Check up
            if charMatchesAt('M', i - 1, j) and charMatchesAt('A', i - 2, j) and charMatchesAt('S', i - 3, j):
                matches += 1

            # Check up-right
            if charMatchesAt('M', i - 1, j + 1) and charMatchesAt('A', i - 2, j + 2) and charMatchesAt('S', i - 3, j + 3):
                matches += 1

            # Check right
            if charMatchesAt('M', i, j + 1) and charMatchesAt('A', i, j + 2) and charMatchesAt('S', i, j + 3):
                matches += 1

            # Check right-down
            if charMatchesAt('M', i + 1, j + 1) and charMatchesAt('A', i + 2, j + 2) and charMatchesAt('S', i + 3, j + 3):
                matches += 1

            # Check down
            if charMatchesAt('M', i + 1, j) and charMatchesAt('A', i + 2, j) and charMatchesAt('S', i + 3, j):
                matches += 1

            # Check down-left
            if charMatchesAt('M', i + 1, j - 1) and charMatchesAt('A', i + 2, j - 2) and charMatchesAt('S', i + 3, j - 3):
                matches += 1

            # Check left
            if charMatchesAt('M', i, j - 1) and charMatchesAt('A', i, j - 2) and charMatchesAt('S', i, j - 3):
                matches += 1

            # Check left - up
            if charMatchesAt('M', i - 1, j - 1) and charMatchesAt('A', i - 2, j - 2) and charMatchesAt('S', i - 3, j - 3):
                matches += 1

print(matches)
