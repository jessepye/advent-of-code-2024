# import ipdb;

file = open("input.txt", "r")
numSafe = 0

def testLevelsForSafety(levels):
    pass

for line in file:
    lineIsSafe = True
    # ipdb.set_trace()
    levels = line.split()
    levels = [int(n) for n in levels]
    # edge cases of no numbers or 1 number
    if len(levels) < 1:
        continue
    if len(levels) == 1:
        numSafe += 1
        continue

    # handle the first 2 numbers as a special case:
    previousLevel = levels[0]
    previouslyIncreasing = None
    diff = levels[1] - previousLevel
    if abs(diff) >= 1 and abs(diff) <= 3:
        pass
    else:
        continue
    previouslyIncreasing = diff > 0
    previousLevel = levels[1]

    # continue checking from the third number
    for level in levels[2:]:
        # ipdb.set_trace()
        diff = level - previousLevel
        if (diff > 0 and previouslyIncreasing or diff < 0 and not previouslyIncreasing) \
        and abs(diff) >= 1 and abs(diff) <= 3:
            previouslyIncreasing = diff > 0
            previousLevel = level
        else:
            lineIsSafe = False
            break
    if lineIsSafe:
        numSafe += 1

print(numSafe)

