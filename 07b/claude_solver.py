import os

# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to input.txt relative to the script location
input_path = os.path.join(script_dir, "input.txt")

rawInputs = []
with open(input_path, "r") as file:
    rawInputs = file.read().strip().split('\n')

def canFindEquation(equationTotal: int, nums: list) -> tuple[bool, list]:
    if len(nums) < 1:
        return False, []
    if equationTotal < nums[0]:
        return False, []
    if len(nums) == 1:
        if equationTotal == nums[0]:
            return True, []
        else:
            return False, []

    # Try multiplication
    mul_nums = [nums[0] * nums[1]] + nums[2:]
    found, operators = canFindEquation(equationTotal, mul_nums)
    if found:
        return True, ['*'] + operators

    # Try addition
    add_nums = [nums[0] + nums[1]] + nums[2:]
    found, operators = canFindEquation(equationTotal, add_nums)
    if found:
        return True, ['+'] + operators

    # Try concatenation
    concat_nums = [int(str(nums[0]) + str(nums[1]))] + nums[2:]
    found, operators = canFindEquation(equationTotal, concat_nums)
    if found:
        return True, ['||'] + operators

    return False, []

def printEquation(nums: list, operators: list) -> str:
    result = str(nums[0])
    for i in range(len(operators)):
        result += f" {operators[i]} {nums[i+1]}"
    return result

sumOfTotals = 0
for equation in rawInputs:
    equationTotal = int(equation.split(":")[0])
    nums = [int(n) for n in equation.split(":")[1].split()]
    print(f"===========================================")
    print(f"equationTotal: {equationTotal} nums: {nums}")
    found, operators = canFindEquation(equationTotal, nums)
    if found:
        print(f"Equation found:")
        print(f"{printEquation(nums, operators)} = {equationTotal}")
        sumOfTotals += equationTotal
    else:
        print(f"No equation found for equationTotal: {equationTotal} nums: {nums}")

print(f"Total sum: {sumOfTotals}")
