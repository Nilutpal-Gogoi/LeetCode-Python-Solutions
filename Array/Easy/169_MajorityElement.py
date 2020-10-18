# Given an array of size n, find the majority element. The majority element is the
# element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist
# in the array.
# Example 1:
#   Input: [3,2,3]
#   Output: 3
# Example 2:
#   Input: [2,2,1,1,1,2,2]
#   Output: 2


# ----------------- Brute Force -----------------------------------------
def majorityElement(nums):
    count = 1
    nums.sort()
    if len(nums) == 1:
        return nums[0]
    else:
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count += 1
                print(count)
                if count > len(nums) // 2:
                    return nums[i]
            else:
                count = 1


# print(majorityElement([1]))

# ------------------ Dictionary ---------------------------------------------
def majorityElement2(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
        if dic[num] > len(nums)//2:
             return num

print(majorityElement2([2,2,1,1,1,2,2]))



