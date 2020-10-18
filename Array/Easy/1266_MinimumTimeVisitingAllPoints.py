# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your
# task is to find the minimum time in seconds to visit all points.
#
# You can move according to the next rules:
# In one second always you can either move vertically, horizontally by one unit or
#   diagonally (it means to move one unit vertically and one unit horizontally in
#   one second).
# You have to visit the points in the same order as they appear in the array.
#
#
# Example 1:
#   Input: points = [[1,1],[3,4],[-1,0]]
#   Output: 7
#   Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
#   Time from [1,1] to [3,4] = 3 seconds
#   Time from [3,4] to [-1,0] = 4 seconds
#   Total time = 7 seconds


def minTimeToVisitAllPoints(points):
    horizontal = 0
    vertical = 0
    time = 0
    for i in range(1, len(points)):
        for j in range(len(points[i])):
            if j % 2 == 0:
                horizontal = points[i][j] - points[i - 1][j]
                if horizontal<0:
                    horizontal = 0-horizontal
            else:
                vertical = points[i][j] - points[i - 1][j]
                if vertical<0:
                    vertical = 0- vertical
        if horizontal < vertical:
            time += vertical
        elif horizontal > vertical:
            time += horizontal
        else:
            time += horizontal
    return time

print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))