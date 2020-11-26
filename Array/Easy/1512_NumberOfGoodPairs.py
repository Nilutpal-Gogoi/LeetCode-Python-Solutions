# https://leetcode.com/problems/number-of-good-pairs/

# Brute Force Approach - Time Complexity: O(n) , Space Complexity: O(1)


def numIdenticalPairs(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                result += 1
    return result

print(numIdenticalPairs([1,2,3]))