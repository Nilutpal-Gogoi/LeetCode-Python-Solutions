# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.
#
# Example 1:
#   Input: [4,2,5,7]
#   Output: [4,5,2,7]
#   Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
# Note:
#   2 <= A.length <= 20000
#   A.length % 2 == 0
#   0 <= A[i] <= 1000


def sortArrayByParityII(A):
    start = 0
    end = len(A)-1
    while start < end:
        if start % 2 == 0 and A[start] % 2 == 0:
            start += 1
            continue
        elif start % 2 != 0 and A[start] % 2 != 0:
            start += 1
            continue
        elif start % 2 == 0 and A[start] % 2 != 0:
            if A[end] % 2 == 0:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            else:
                while A[end] % 2 != 0:
                    end -= 1
                A[start], A[end] = A[end], A[start]
                start += 1
            end = len(A)-1
            continue
        elif start % 2 != 0 and A[start] % 2 == 0:
            if A[end] % 2 != 0:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            else:
                while A[end] % 2 == 0:
                    end -= 1
                A[start], A[end] = A[end], A[start]
                start += 1
            end = len(A)-1
            continue
    return A

# print(sortArrayByParityII([4,1,1,0,1,0]))



# ------------------ Simple Way ---------------------

def sortByParity2(A):
    out = [0]*len(A)
    j = 0
    k = 1
    for i in A:
        if i%2==0:
            out[j] = i
            j += 2
        else:
            out[k] = i
            k += 2
    return out

print(sortArrayByParityII([4,1,1,0,1,0]))
