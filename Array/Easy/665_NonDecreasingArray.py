# https://leetcode.com/problems/non-decreasing-array/


def checkPossibility(nums):
    count = 0
    for i in range(1, len(nums)):
        if count <= 1:
            if nums[i-1] > nums[i]:
                count += 1
                if i-2 < 0 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
    return count <= 1



print(checkPossibility([5,7,1,8]))