"""
Problem: Coordinate Distance

Calculate the Euclidean distance between two points.

Example:
p1 = (2, 3)
p2 = (5, 7)

Output:
5.0
"""

from math import sqrt


def coordinate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


p1 = (2, 3)
p2 = (5, 7)

print(coordinate_distance(p1, p2))