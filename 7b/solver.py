import ipdb;
import os

# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to input.txt relative to the script location
input_path = os.path.join(script_dir, "input.txt")

rawInputs = []
with open(input_path, "r") as file:
    rawInputs = file.read().strip().split('\n')
# print(rawInputs)

def canFindEquation(equationTotal: int, nums: list) -> bool:
    # print(f"running canFindEquation({equationTotal}, {nums})")
    if len(nums) < 1:
        return False, []
    if equationTotal < nums[0]:
        # print("--total too small, returning False--")
        return False, []
    if len(nums) == 1:
        if equationTotal == nums[0]:
            # print(f"--BASE CASE (True): equationTotal: {equationTotal} nums: {nums}--")
            return True, []
        else:
            # print(f"--BASE CASE (False): equationTotal: {equationTotal} nums: {nums}--")
            return False, []

    res = canFindEquation(equationTotal, [nums[0] * nums[1]] + nums[2:])
    if res == True:
        return True, res[1] + ['*']
    res = canFindEquation(equationTotal, [nums[0] + nums[1]] + nums[2:])
    if res == True:
        return True, res[1] + ['+']
    res = canFindEquation(equationTotal, [int(str(nums[0]) + str(nums[1]))] + nums[2:])
    if res == True:
        return True, res[1] + ['||']

sumOfTotals = 0
for equation in rawInputs:
    equationTotal = int(equation.split(":")[0])
    nums = [int(n) for n in equation.split(":")[1].split()]
    print(f"===========================================")
    print(f"equationTotal: {equationTotal} nums: {nums}")
    res = canFindEquation(equationTotal, nums)
    if res:
        print(f"Equation found:")
        print(f"equationTotal: {equationTotal} nums: {nums} operators: {res[1]}")
        sumOfTotals += equationTotal
    else:
        print(f"No equation found for equationTotal: {equationTotal} nums: {nums}")

print(sumOfTotals)
