# https://leetcode.com/problems/spiral-matrix-ii/


def generateMatrix(n):
    arr = []
    for i in range(1, (n*n)+1):
        arr.append(i)
    top, left = 0, 0
    right, bottom = n-1, n-1
    index = 0
    matrix = [[0] * n for i in range(n)]
    while n*n > index:
        if left > right:
            break

        for i in range(left, right+1):
            matrix[top][i] = arr[index]
            index += 1
        top += 1

        if top > bottom:
            break

        for i in range(top, bottom+1):
            matrix[i][right] = arr[index]
            index += 1
        right -= 1

        if left > right:
            break

        for i in range(right, left-1, -1):
            matrix[bottom][i] = arr[index]
            index += 1
        bottom -= 1

        if top > bottom:
            break

        for i in range(bottom, top-1, -1):
            matrix[i][left] = arr[index]
            index += 1
        left += 1
    return matrix

print(generateMatrix(3))



