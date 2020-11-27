# https://leetcode.com/problems/two-sum/


# Brute Force Approach Will be by using Two loops: Time Complexity: O(n2) and Space Complexity: O(1)
# Also can be solved using sorting technique and two pointer: Time Complexity: O(nlogn) and Space Complexity: O(1)

# Using Hash Tables: Time Complexity: O(n) and Space Complexity: O(n)
def twoSum(nums, target):
    dic = {}
    for key, value in enumerate(nums):
        item = target - value
        if item not in dic:
            dic[value] = 1
        else:
            return [min(key, nums.index(item)), max(key, nums.index(item))]
    return [-1, -1]