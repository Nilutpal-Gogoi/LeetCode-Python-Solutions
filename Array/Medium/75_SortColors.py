# https://leetcode.com/problems/sort-colors/

# The brute force approach will be using any sorting method- Time Complexity: O(nlogn) and Space Complexity: O(1)


def sortColors(nums):
    return sorted(nums)

# print(sortColors([2,0,2,1,1,0]))

# Better Approach: This will be by using TWO POINTER method. Time Complexity: O(n) and Space Complexity: O(1)


def sortColors1(nums):
