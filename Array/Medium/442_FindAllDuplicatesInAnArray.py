# https://leetcode.com/problems/find-all-duplicates-in-an-array/


# Brute Force Approach - Time Complexity: O(n2) and Space Complexity: O(1)
def findDuplicates(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                result.append(nums[i])
                break
    return result


# print(findDuplicates([4,3,2,7,8,2,3,1]))

# This can be also solved using sorting. The time complexity will be reduced to O(nlogn) and space complexity will remain
# same.

# Using hashing will reduce the time complexity to O(n) and space complexity will increase by O(n)
def findDuplicates1(nums):
    dic = {}
    result = []
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    for key, value in dic.items():
        if value > 1:
            result.append(key)
    return result

# print(findDuplicates1([4,3,2,7,8,2,3,1]))


# Better Approach- Time Complexity: O(n) and Space Complexity: O(1)
def findDuplicates2(nums):
    result = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = - nums[index]
        else:
            result.append(index+1)
        print(nums)
    print(result)


findDuplicates2([4, 3, 2, 7, 8, 2, 3, 1])

