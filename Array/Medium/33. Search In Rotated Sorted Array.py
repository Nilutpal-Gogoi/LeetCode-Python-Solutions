# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).
# Example 1:
#   Input: nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4
# Example 2:
#   Input: nums = [6,7,0], target = 3
#   Output: -1


def search(nums, target):
    low = 0
    high = len(nums)-1
    while low < high:
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[low]:
            if nums[low] == target:
                return low
            elif nums[low] > target:
                low = mid+1
        elif nums[mid] <= nums[high]:
            if nums[high] == target:
                return high
            elif nums[high] < target:
                high = mid-1
    return False

print(search([4,5,6,7,0,1,2], 0))


