# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#   Input: [-2, 0, 1, 2], target=2


def threeSumClosest(nums, target):
    nums.sort()
    smallestDiff = float("inf")
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            targetDiff = target - nums[i] - nums[left] - nums[right]
            if targetDiff == 0: # found the triplet with an exact sum
                return target-targetDiff
            if abs(targetDiff) < abs(smallestDiff) or (abs(targetDiff) == abs(smallestDiff) and targetDiff > smallestDiff):
                smallestDiff = targetDiff
            if targetDiff > 0:
                left += 1
            else:
                right -= 1
    return target-smallestDiff