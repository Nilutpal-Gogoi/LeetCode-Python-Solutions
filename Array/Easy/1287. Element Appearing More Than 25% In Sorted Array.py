# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than
# 25% of the time.
# Return that integer.
#
# Example 1:
#   Input: arr = [1,2,2,6,6,6,6,7,10]
#   Output: 6
# Constraints:
#   1 <= arr.length <= 10^4
#   0 <= arr[i] <= 10^5


def findSpecialInteger(arr):
    n = (1/4)*len(arr)
    temp = {}
    for i in range(len(arr)):
        if arr[i] in temp:
            temp[arr[i]] += 1
        else:
            temp[arr[i]] = 1
    print(temp)
    for key, value in temp.items():
        if value > n:
            return key


print(findSpecialInteger([1,2,3,3]))