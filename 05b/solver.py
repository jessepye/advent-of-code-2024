import ipdb;
import os

# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to input.txt relative to the script location
input_path = os.path.join(script_dir, "input.txt")

rules = []
updates = []

with open(input_path, "r") as file:
    inRulesSection = True
    for line in file:
        if inRulesSection:
            if len(line) > 1:
                # ipdb.set_trace()
                nums = [int(n) for n in line.strip().split("|")]
                rules.append(nums)
            else:
                inRulesSection = False
        if not inRulesSection:
            if len(line) > 1:
                nums = [int(n) for n in line.strip().split(",")]
                updates.append(nums)

# These functions rely on the list `rules` from the global scope

def isValid(update):
    for rule in rules:
        # ipdb.set_trace()
        if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
            print(f"update {update} breaks rule {rule}")
            return False
    return True

# bubble sort
def fixUpdate(update):
    for outer in range(1, len(update)):
        for i in range(len(update) - outer):
            if [update[i+1], update[i]] in rules:
                update[i], update[i+1] = update[i+1], update[i]

total = 0
for update in updates:
    if not isValid(update):
        fixUpdate(update)
        print(f"Fix attempted. valid? {isValid(update)}")
        print(f"fixed: {update}")
        mid = update[int((len(update) - 1)/2)]
        total += mid
        print(f"mid {mid} new total {total}")
        

print(total)

