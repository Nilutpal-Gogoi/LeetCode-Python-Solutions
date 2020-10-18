# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
#   Input: [1,1,0,1,1,1]
#   Output: 3
#   Explanation: The first two digits or the last three digits are consecutive 1s.
#                The maximum number of consecutive 1s is 3.
# Note:
#   The input array will only contain 0 and 1.
#   The length of input array is a positive integer and will not exceed 10,000


# def findMaxConsecutiveOnes(nums):
#     curs_int = 0
#     max_one = 0
#     for i in range(len(nums)):
#         if nums[i] == 1:
#             curs_int += 1
#         else:
#             max_one = max(curs_int, max_one)
#             curs_int = 0
#     return max(curs_int, max_one)

def findMaxConsecutiveOnes(nums):
    count = 0
    lis = []
    for i in range(len(nums)):
        count = 0
        lis = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                lis.append(count)
                count = 0
        lis.append(count)
        return max(lis)


print(findMaxConsecutiveOnes([1,0,1,1,0,1]))