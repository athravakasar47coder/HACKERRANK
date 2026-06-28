"""
Problem: Frequency Counter

Count the frequency of each element in a list.

Input:
nums = [1, 1, 2, 2, 2, 3, 4, 4]

Output:
{
    1: 2,
    2: 3,
    3: 1,
    4: 2
}

Concepts:
- Dictionary
- For Loop
- Counting Frequency
"""


def frequency_counter(nums):
    count_dict = {}

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    return count_dict


nums = [1, 1, 2, 2, 2, 3, 4, 4]

print(frequency_counter(nums))