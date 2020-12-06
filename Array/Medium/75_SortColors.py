# https://leetcode.com/problems/sort-colors/

# The brute force approach will be using any sorting method- Time Complexity: O(nlogn) and Space Complexity: O(1)


def sortColors(nums):
    return sorted(nums)

# print(sortColors([2,0,2,1,1,0]))

# Better Approach: This will be by using TWO POINTER method. Time Complexity: O(n) and Space Complexity: O(1)


def sortColors1(nums):
    i = 0
    low = 0
    high = len(nums)-1
    while i <= high:
        if nums[i] == 0:
            nums[i], nums[low] = nums[low], nums[i]
            i += 1
            low += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
    return nums
