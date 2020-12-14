# https://leetcode.com/problems/spiral-matrix/


def spiralOrder(matrix):
    left = 0
    top = 0
    bottom = len(matrix)-1
    m = bottom+1
    right = len(matrix[0])-1
    n = right+1
    index = 0
    result = [0] * (m*n)
    while m*n > index:
        if left > right:
            break

        for i in range(left, right+1):
            result[index] = matrix[top][i]
            index += 1
        top += 1

        if top > bottom:
            break

        for i in range(top, bottom+1):
            result[index] = matrix[i][right]
            index += 1
        right -= 1

        if left > right:
            break

        for i in range(right, left-1, -1):
            result[index] = matrix[bottom][i]
            index += 1
        bottom -= 1

        if top > bottom:
            break

        for i in range(bottom, top-1, -1):
            result[index] = matrix[i][left]
            index += 1
        left += 1
    return result


print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))