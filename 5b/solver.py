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


total = 0


for update in updates:
    followsRules = True
    for rule in rules:
        # ipdb.set_trace()
        if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
            print(f"update {update} breaks rule {rule}")
            followsRules = False
            break
    if followsRules:
        mid = update[int((len(update) - 1) / 2)]
        total += mid
        print(f"update {update} follows all rules; mid {mid}; total {total}")

print(total)
