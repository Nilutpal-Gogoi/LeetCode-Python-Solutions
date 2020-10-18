# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#
# Example 1:
#   Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
#   Output: [15]
#   Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
# Example 2:
#   Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
#   Output: [12]
#   Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:
#   Input: matrix = [[7,8],[1,2]]
#   Output: [7]


def luckyNumbers(lis):
    m = len(lis)
    n = len(lis[0])
    min_list = []
    max_list = []
    max_l = float("-inf")
    for i in range(m):
        min_list.append(min(lis[i]))
    for j in range(n):
        for i in range(m):
            max_l = max(max_l, lis[i][j])
        max_list.append(max_l)
        max_l = float("-inf")
    dic = {}
    for i in min_list:
        dic[i] = 1
    for i in max_list:
        if i in dic:
            return [i]


print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))