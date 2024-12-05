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
        if charMatchesAt('A', i, j):
            # M M
            #  A 
            # S S
            if charMatchesAt('M', i - 1, j - 1) and charMatchesAt('M', i - 1, j + 1) and charMatchesAt('S', i + 1, j - 1) and charMatchesAt('S', i + 1, j + 1):
                matches += 1

            # S M
            #  A 
            # S M
            if charMatchesAt('S', i - 1, j - 1) and charMatchesAt('M', i - 1, j + 1) and charMatchesAt('S', i + 1, j - 1) and charMatchesAt('M', i + 1, j + 1):
                matches += 1

            # S S
            #  A 
            # M M
            if charMatchesAt('S', i - 1, j - 1) and charMatchesAt('S', i - 1, j + 1) and charMatchesAt('M', i + 1, j - 1) and charMatchesAt('M', i + 1, j + 1):
                matches += 1

            # M S
            #  A 
            # M S
            if charMatchesAt('M', i - 1, j - 1) and charMatchesAt('S', i - 1, j + 1) and charMatchesAt('M', i + 1, j - 1) and charMatchesAt('S', i + 1, j + 1):
                matches += 1

print(matches)
