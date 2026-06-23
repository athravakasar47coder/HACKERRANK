"""
Problem: Two Sum

Given a list of integers and a target value,
return the indices of two numbers whose sum equals the target.

Example:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))