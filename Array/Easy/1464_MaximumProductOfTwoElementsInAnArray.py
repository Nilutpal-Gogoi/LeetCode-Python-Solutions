# Given the array of integers nums, you will choose two different indices i and j of
# that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
# Example 1:
#   Input: nums = [3,4,5,2]
#   Output: 12
#   Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will
#   get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.


def maxProduct(nums):
    max_num = float('-inf')
    max_index = 0
    for i in range(len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
            max_index = i
    sec_max_num = float('-inf')
    sec_max_index = 0
    for i in range(len(nums)):
        if i != max_index and nums[i]>sec_max_num:
            sec_max_num = nums[i]
            sec_max_index = i
    return ((max_num - 1) * (sec_max_num - 1))

print(maxProduct([10,2,5,2]))