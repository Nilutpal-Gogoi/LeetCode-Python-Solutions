# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


# Brute force approach - Time Complexity: O(n2) and Space Complexity: O(1)


def findDisappearedNumbers(nums):
    result = []
    for j in range(1, len(nums)+1):
        flag = False
        for i in range(len(nums)):
            if j == nums[i]:
                flag = True
                break
        if not flag:
            result.append(j)
    print(result)

# findDisappearedNumbers([4,3,2,7,8,2,3,1])

# Using Sorting we can reduce the Time Complexity to nlog(n).
# Using HashTable we can reduce the Time Complexity to n but the space complexity increases to O(n)


def findDisappearedNumbers1(nums):
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    result = []
    for i in range(1, len(nums)+1):
        if i not in dic:
            result.append(i)
    return result

# print(findDisappearedNumbers1([4,3,2,7,8,2,3,1]))

# Better Approach - Time Complexity: O(n) and Space Complexity: O(1)


def findDisappearedNumbers2(nums):
    result = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        nums[idx] = -abs(nums[idx])
    for i in range(len(nums)):
        if nums[i]<0:       # To bring the input back to its original state
            nums[i] = -nums[i]
        else:               # Found the missing number
            result.append(i+1)
    return result


print(findDisappearedNumbers2([4, 3, 2, 7, 8, 2, 3, 1]))