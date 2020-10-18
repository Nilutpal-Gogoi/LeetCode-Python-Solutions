# Given an array A of non-negative integers, return an array consisting of all the
# even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.
# Example 1:
#   Input: [3,1,2,4]
#   Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


def sortArrayByParity(A):
    start = 0
    end = len(A) - 1
    while start < end:
        if A[start] % 2 != 0 and A[end] % 2 == 0:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
        elif A[start] % 2 == 0 and A[end] % 2 != 0:
            start += 1
            end -= 1
        elif A[start] % 2 == 0 and A[end] % 2 == 0:
            start += 1
        else:
            end -= 1
    return A

