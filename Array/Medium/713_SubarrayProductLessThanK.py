# https://leetcode.com/problems/subarray-product-less-than-k/

# Brute Force Approach- Time Complexity: O(n2) and Space Complexity: O(1)


def numSubarrayProductLessThanK(nums, k):
    count = 0
    for i in range(len(nums)):
        if nums[i] < k:
            count += 1
        mul = nums[i]
        for j in range(i+1, len(nums)):
            mul = mul * nums[j]
            if mul < k:
                count += 1
            else:
                break
    return count


# Sliding Window Technique

def numSubarrayProductLessThanK1(nums, k):


print(numSubarrayProductLessThanK1([10, 5, 2, 6], 100))

# [2, 5, 6, 10]