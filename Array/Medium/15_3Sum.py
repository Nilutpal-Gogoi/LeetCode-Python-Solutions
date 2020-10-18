# Given an array nums of n integers, are there elements a, b, c in nums such that
# a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
#   The solution set must not contain duplicate triplets.
# Example:
#   Given array nums = [-1, 0, 1, 2, -1, -4],
#   A solution set is:
#                       [
#                         [-1, 0, 1],
#                         [-1, -1, 2]
#                       ]


# ------------------------ Brute Force O(n3) ------------------------------------------
def threeSum(nums,n):
    lis = []
    nums.sort()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (nums[i]+nums[j]+nums[k])==0:
                    if [nums[i],nums[j],nums[k]] not in lis:
                        lis.append([nums[i],nums[j],nums[k]])
    return lis

# print(threeSum([-1, 0, 1, 2, -1, -4],6))

# ---------------------- Two Pointer Technique ----------------------------------------


def threeSum1(nums, n):
    nums.sort()
    for i in range(n-2):
        if twoSum(nums, -nums[i], i+1):
            return True
    return False


def twoSum(nums, x, i):
    j = len(nums)-1
    while i<j:
        if (nums[i]+nums[j]) < x:
            i += 1
        elif (nums[i]+nums[j]) > x:
            j -= 1
        else:
            return True
    return False


# print(threeSum1([-3, -1, 0, 4, 6, 7], 6))

# ------------------------


def binary(arr, k):
    l = 0
    h = len(arr)-1
    while l<h:
        if arr[l] + arr[h] == k:
            return [arr[l], arr[h]]
        elif arr[l]+arr[h] < k:
            l += 1
        else:
            h -= 1
    return False


def sumOfThreeElements2(arr, k):
    n = len(arr)
    left = 0
    right = n-1
    arr.sort()
    main = []
    for i in range(n-2):
        result = k-arr[i]
        lis = binary(arr[i+1:n], result)
        if lis:
            lis.insert(0, arr[i])
            main.append(lis)
    if main:
        return main
    else:
        return False


print(sumOfThreeElements2([-1, 0, 1, 2, -1, -4], 0))

