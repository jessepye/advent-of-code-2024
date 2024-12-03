import re
# import ipdb;

file = open("modified_input.txt", "r")

text = file.read()
pattern = r"mul\(\d{1,3},\d{1,3}\)"
muls = re.findall(pattern, text)

total = 0
for mul in muls:
    pattern = r"\d{1,3}"
    nums = re.findall(pattern, mul)
    nums = [int(n) for n in nums]
    total += nums[0] * nums[1]

print(total)

