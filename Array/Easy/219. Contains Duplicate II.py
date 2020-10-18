# Given an array of integers and an integer k, find out whether there are two distinct
# indices i and j in the array such that nums[i] = nums[j] and the absolute difference
# between i and j is at most k.
#
# Example 1:
#   Input: nums = [1,2,3,1], k = 3
#   Output: true
# Example 2:
#   Input: nums = [1,0,1,1], k = 1
#   Output: true
# Example 3:
#   Input: nums = [1,2,3,1,2,3], k = 2
#   Output: false


# ----------------------- Solution 1 : Brute Force ---------------------------------
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and j-i <= k:
                return True
    return False

# Time Complexity - O(n2) , space Complexity - O(1)

# ----------------------- Solution 2 :  ------------------
def containsNearbyDuplicate2(nums, k):
    temp = {}
    for i in range(len(nums)):
        if nums[i] not in temp:
            temp[nums[i]] = 1
        else:
            for j in range(1,k+1):          # Solution by Vipin bhaiya, reverse socho
                if nums[i] == nums[i-j] and i-(i-j) <= k:
                    return True
    return False

print(containsNearbyDuplicate2([1,2,3,1],3))