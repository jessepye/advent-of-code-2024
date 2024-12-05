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

print(rules)
print(updates)
