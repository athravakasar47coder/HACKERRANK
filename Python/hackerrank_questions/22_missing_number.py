"""
Problem: Missing Number

Given an array containing numbers from 0 to n,
find the missing number.

Input:
nums = [3, 0, 1]

Output:
2

Concepts:
- Set
- Loop
- Searching
"""


def missing_number(nums):
    num_set = set(nums)

    for i in range(len(nums) + 1):
        if i not in num_set:
            return i


nums = [3, 0, 1]

print(missing_number(nums))