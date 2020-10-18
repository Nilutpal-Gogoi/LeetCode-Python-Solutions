# Given an array nums, there is a sliding window of size k which is moving from the
# very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# ------------------ Solution 1 -------------------------------------------
def maxSlidingWindow(nums, k):
    result = []
    temp = []
    for i in range(len(nums)):
        if i < k:
            temp.append(nums[i])
            if i == k-1:
                result.append(max(temp))
        else:
            del temp[0:1]
            temp.append(nums[i])
            result.append(max(temp))
    return result


# ------------------ Solution 2 -------------------------------------------
def maxSlidingWindow1(nums, k):
    max = 0
    result = []
    for i in range(len(nums)-k+1):
        max = nums[i]
        for j in range(1,k):
            if nums[i+j] > max:
                max = nums[i+j]
        result.append(max)
    return result

print(maxSlidingWindow1([1,3,-1,-3,5,3,6,7], 3))

