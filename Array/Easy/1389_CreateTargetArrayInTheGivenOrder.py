# https://leetcode.com/problems/create-target-array-in-the-given-order/


def createTargetArray(nums, index):
    target = []
    n = len(nums)
    i = 0
    while i < n:
        target.insert(index[i],nums[i])
        i += 1
        print("target", target, "i", i)
    return target

print(createTargetArray([0,1,2,3,4],[0,1,2,2,1]))