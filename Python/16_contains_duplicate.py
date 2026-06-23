"""
Problem: Contains Duplicate

Return True if any value appears
more than once in the list.

Example:
Input:  [1, 2, 3, 1]
Output: True
"""


def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


nums = [1, 2, 3, 1]

print(contains_duplicate(nums))