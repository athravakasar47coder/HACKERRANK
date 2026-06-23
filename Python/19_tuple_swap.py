"""
Problem: Swap Two Variables

Swap two values without using
a third variable.

Example:
a = 10
b = 20

Output:
a = 20
b = 10
"""


a = 10
b = 20

print(f"Before Swap -> a = {a}, b = {b}")

a, b = b, a

print(f"After Swap  -> a = {a}, b = {b}")