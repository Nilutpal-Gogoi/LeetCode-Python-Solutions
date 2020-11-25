# https://leetcode.com/problems/set-mismatch/

# Brute Force Approach - Time Complexity: O(n2) and Space Complexity: O(1)

def findErrorNums(nums):
    dup = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                dup = nums[i]
    result = 0
    for i in range(0, len(nums)):
        result = result ^ nums[i]
    for i in range(1, len(nums) + 1):
        result = result ^ i
    result = result ^ dup
    return [dup, result]

# print(findErrorNums([1,2,2,4]))

# Using Hash Table/Dictionary - Time Complexity: O(n) and Space Complexity: O(1)


def findErrorNums1(nums):
    dic = {}
    dup = 0
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    for key, value in dic.items():
        if value == 2:
            dup = key
    result = 0
    for i in range(0, len(nums)):
        result = result ^ nums[i]
    for i in range(1, len(nums) + 1):
        result = result ^ i
    result = result ^ dup
    return [dup, result]

# print(findErrorNums1([1,2,2,4]))

# Using Maths - Time Complexity: O(1), Space Complexity: O(1)


def findErrorNums2(nums):
    n = len(nums)
    s = n*(n+1)//2
    miss = s - sum(set(nums))
    duplicate = sum(nums)+miss-s
    return [duplicate, miss]