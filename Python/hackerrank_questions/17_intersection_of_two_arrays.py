"""
Problem: Intersection of Two Arrays

Return all unique elements that appear
in both arrays.

Example:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

Output:
[2]
"""


def intersection(nums1, nums2):
    common = []

    for i in range(len(nums2)):
        for j in range(len(nums1)):
            if nums2[i] == nums1[j]:
                common.append(nums2[i])

    return list(set(common))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))