"""
Problem: Move Zeroes

Move all zeroes to the end while maintaining
the order of non-zero elements.

Example:
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
"""


def move_zeroes(nums):
    zero_count = nums.count(0)

    result = [num for num in nums if num != 0]

    result.extend([0] * zero_count)

    return result


nums = [0, 1, 0, 3, 12]

print(move_zeroes(nums))