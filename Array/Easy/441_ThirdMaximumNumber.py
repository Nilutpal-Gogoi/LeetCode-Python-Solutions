# https://leetcode.com/problems/third-maximum-number/


def thirdMax(nums):
    n, T = list(set(nums)), [float('-inf')] * 3
    for i in n:
        if i > T[0]:
            T = [i, T[0], T[1]]
        elif i > T[1]:
            T = [T[0], i, T[1]]
        elif i > T[2]:
            T = [T[0], T[1], i]
    return T[2] if T[2] != float('-inf') else T[0]


print(thirdMax([3, 2, 1, 5]))


