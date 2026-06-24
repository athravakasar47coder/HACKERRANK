"""
Problem: Sort Students by Marks

Sort students in ascending order
based on their marks.

Input:
students = [
    ("Atharva", 85),
    ("Rahul", 92),
    ("Amit", 78)
]

Output:
[
    ("Amit", 78),
    ("Atharva", 85),
    ("Rahul", 92)
]

Concepts:
- Tuples
- Lists
- sort()
- lambda
"""


students = [
    ("Atharva", 85),
    ("Rahul", 92),
    ("Amit", 78)
]

students.sort(key=lambda x: x[1])

print(students)