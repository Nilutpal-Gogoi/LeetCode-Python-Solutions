# https://leetcode.com/problems/single-number/

# Brute force approach - Time Complexity: O(n2), Space Complexity: O(1)


def singleNumber(nums):
    flag = False
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] == nums[j] and i != j:
                flag = True
                break
        if not flag:
            return nums[i]
        flag = False
        continue
    return False


# Using Hash Table - Time Complexity: O(n), Space Complexity: O(n)


def singleNumber1(nums):
    dic = {}
    for i in range(0,len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    for key, value in dic.items():
        if value == 1:
            return key

# print(singleNumber1([1]))


# Using XOR - Time Complexity: O(n) and Space Complexity: O(1)
def singleNumber2(nums):
    result = 0
    for i in range(0, len(nums)):
        result = result ^ nums[i]
    return result

# print(singleNumber2([1]))
