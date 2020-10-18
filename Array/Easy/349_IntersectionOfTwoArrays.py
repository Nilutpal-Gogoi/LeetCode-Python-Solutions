# Given two arrays, write a function to compute their intersection.
# Example 1:
#   Input: nums1 = [1,2,2,1], nums2 = [2,2]
#   Output: [2]
# Example 2:
#   Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#   Output: [9,4]
# Note:
#   Each element in the result must be unique.
#   The result can be in any order.


# ------------------ Brute Force -----------------------------------------
def intersection(nums1, nums2):
    lis = []
    for i in nums1:
        for j in nums2:
            if i == j:
                if i not in lis:
                    lis.append(i)
    return lis

# ---------------- Using inbuilt sets ---------------------------------------


def intersection1(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return set1.intersection(set2)

# Time Complexity = O(n+m), O(n) time is used to convert nums1 into set, O(m) time
# is used to convert nums2
# Space Complexity = O(n+m) in the worst case when all the elements in the arrays
# are different.

