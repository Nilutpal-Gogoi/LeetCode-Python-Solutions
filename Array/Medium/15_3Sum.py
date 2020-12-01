# Given an array nums of n integers, are there elements a, b, c in nums such that
# a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
#   The solution set must not contain duplicate triplets.
# Example:
#   Given array nums = [-1, 0, 1, 2, -1, -4],
#   A solution set is:
#                       [
#                         [-1, 0, 1],
#                         [-1, -1, 2]
#                       ]


# ------------------------ Brute Force O(n3) ------------------------------------------
def threeSum(nums,n):
    lis = []
    nums.sort()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (nums[i]+nums[j]+nums[k])==0:
                    if [nums[i],nums[j],nums[k]] not in lis:
                        lis.append([nums[i],nums[j],nums[k]])
    return lis

# print(threeSum([-1, 0, 1, 2, -1, -4],6))

# ---------------------- Two Pointer Technique ----------------------------------------


def threeSum1(nums):
    nums.sort()
    triplets = []
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:    # for this case [-1,0,1,2,-1,-4]
            continue
        num = -nums[i]
        left = i+1
        right = len(nums)-1
        while left < right:
            current_sum = nums[left]+nums[right]
            if current_sum == num:   # Found the triplet
                triplets.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1       # Skip the same element to avoid duplicate triplets
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1      # Skip the same element to avoid duplicate triplets
            elif current_sum < num:
                left += 1
            else:
                right -= 1
    return triplets


print(threeSum1([-1,0,1,2,-1,-4]))

#  -4 -1 -1 0 1 2