# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
# Return the number of negative numbers in grid.
# Example 1:
#   Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#   Output: 8
# Explanation: There are 8 negatives number in the matrix.
#
# Example 2:
#   Input: grid = [[3,2],[1,0]]
#   Output: 0
# Example 3:
#   Input: grid = [[1,-1],[-1,-1]]
#   Output: 3
# Example 4:
#   Input: grid = [[-1]]
#   Output: 1
#
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 100
#   -100 <= grid[i][j] <= 100

def binary(nums):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid]>0:
            low = mid+1
        elif nums[mid]<0:
            end = mid-1
    return len(nums)-low




