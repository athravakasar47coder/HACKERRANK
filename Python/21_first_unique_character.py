"""
Problem: First Unique Character

Return the index of the first non-repeating
character in a string.

Input:
s = "leetcode"

Output:
0

Explanation:
'l' appears only once and is found at index 0.
"""


def first_unique_character(s):
    for char in s:
        if s.count(char) == 1:
            return s.index(char)

    return -1


s = "leetcode"

print(first_unique_character(s))