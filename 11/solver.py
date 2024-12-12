import ipdb
import copy
inputFile = "input.txt"
# inputFile = "example.txt"
with open(inputFile, "r") as file:
    stones =  [int(x) for x in file.read().strip().split()]
# stones = [0] # simplest example

def solve1(stones: list) -> int:
    def blink():
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                leftStone = int(str(stones[i])[:len(str(stones[i]))//2])
                rightStone = int(str(stones[i])[len(str(stones[i]))//2:])
                stones[i] = leftStone
                stones.insert(i+1, rightStone)
                i += 1 # extra increment of i to account for the new stone
            else:
                stones[i] *= 2024
            i += 1


    for blinkCount in range(25):
        blink()
        print(f"{blinkCount + 1} blinks")
    return len(stones)

def solve2(stones: list) -> int:
    # insight: order does not matter, all stones of value `0` or `1` or `n` are identical
    # keep the stones as a dict, with stoneValue as the key and count as the value.
    # starting with stones = [0], after 32 blinks, 357632 stones, but only 54 unique values
    stoneDict = {}
    for stone in stones:
        if stone in stoneDict:
            stoneDict[stone] += 1
        else:
            stoneDict[stone] = 1
    def blink(stoneDict):
        # we will be adding new keys during the loop, which isn't allowed "in-place";
        # imagine having 5 `0`s and 10 `1`s, what happens after we process the `0`s?
        newStones = {}
        for stone in stoneDict:
            if stone == 0:
                newVal = 1
                if newVal in newStones:
                    newStones[newVal] += stoneDict[stone]
                else:
                    newStones[newVal] = stoneDict[stone]
            elif len(str(stone)) % 2 == 0:
                leftStone = int(str(stone)[:len(str(stone))//2])
                rightStone = int(str(stone)[len(str(stone))//2:])
                if leftStone in newStones:
                    newStones[leftStone] += stoneDict[stone]
                else:
                    newStones[leftStone] = stoneDict[stone]
                if rightStone in newStones:
                    newStones[rightStone] += stoneDict[stone]
                else:
                    newStones[rightStone] = stoneDict[stone]
            else:
                newVal = stone * 2024
                if newVal in newStones:
                    newStones[newVal] += stoneDict[stone]
                else:
                    newStones[newVal] = stoneDict[stone]
        # print(f"newStones: {newStones}")
        return copy.copy(newStones)

    for blinkCount in range(75):
        stoneDict = blink(stoneDict)
        print(f"{blinkCount + 1} blinks")
    total = 0
    for stone in stoneDict:
        total += stoneDict[stone]
    return total

print(f"initial stones: {stones}")
print(solve1(stones))
print(solve2(stones))
