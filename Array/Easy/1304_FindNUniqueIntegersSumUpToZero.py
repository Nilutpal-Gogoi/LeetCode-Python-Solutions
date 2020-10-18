# Given an integer n, return any array containing n unique integers such that they
# add up to 0.
# Example 1:
#   Input: n = 5
#   Output: [-7,-1,1,3,4]
#   Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
#   Input: n = 3
#   Output: [-1,0,1]
# Example 3:
#   Input: n = 1
#   Output: [0]


def sumZero(n):
    L, rem = n // 2, n % 2
    if rem != 0:
        arr = [0]
    else:
        arr = []
    for i in range(1, L + 1):
        arr.append(-i)
        arr.append(i)
    return arr