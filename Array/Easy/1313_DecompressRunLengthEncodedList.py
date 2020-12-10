# https://leetcode.com/problems/decompress-run-length-encoded-list/


def decompressRLElist(nums):
    result = []
    for i in range(0,len(nums)-1,2):
        for j in range(nums[i]):
            result.append(nums[i+1])
    return result


print(decompressRLElist([1,1,2,3]))