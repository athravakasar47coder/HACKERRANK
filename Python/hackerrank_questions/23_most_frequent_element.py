"""
Problem: Most Frequent Element

Find the element that appears the most times.

Input:
nums = [1, 1, 1, 2, 2, 3]

Output:
1

Concepts:
- Set
- Frequency Counting
- max()
"""


def most_frequent_element(nums):
    return max(set(nums), key=nums.count)


nums = [1, 1, 1, 2, 2, 3]

print(most_frequent_element(nums))