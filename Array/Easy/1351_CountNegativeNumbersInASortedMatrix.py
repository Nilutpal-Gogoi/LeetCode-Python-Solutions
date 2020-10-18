# Given a m * n matrix grid which is sorted in non-increasing order both row-wise
# and column-wise.
# Return the number of negative numbers in grid.
# Example 1:
#   Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#   Output: 8
#   Explanation: There are 8 negatives number in the matrix.
# Example 2:
#   Input: grid = [[3,2],[1,0]]
#   Output: 0
# Example 3:
#   Input: grid = [[1,-1],[-1,-1]]
#   Output: 3
# Example 4:
#   Input: grid = [[-1]]
#   Output: 1


def countNegatives(grid):
    count = 0
    for row in grid:
        count += binarySearch(row)
    return count


def binarySearch(List):
    start = 0
    end = len(List)
    while start<end:
        mid = start+(end-start)//2
        if List[mid] < 0:
            end = mid
        else:
            start = mid + 1
    return len(List)-start

print(countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
