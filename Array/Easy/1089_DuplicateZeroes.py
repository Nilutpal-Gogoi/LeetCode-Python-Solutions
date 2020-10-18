# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything
# from your function.
# Example 1:
#   Input: [1,0,2,3,0,4,5,0]
#   Output: null
#   Explanation: After calling your function, the input array is modified
#                to: [1,0,0,2,3,0,0,4]
# Example 2:
#   Input: [1,2,3]
#   Output: null
#   Explanation: After calling your function, the input array is modified to: [1,2,3]

# -------------------------- Method - 1 --------------------------------------
def duplicateZeros(arr):
    length = len(arr)
    i = 0
    while i < length:
        if arr[i]==0:
            arr.insert(i,0)
            i += 2
        else:
            i += 1
    return arr[:length]


print(duplicateZeros([1,0,2,3,0,4,5,0]))

# -------------------- Method 2 ------------------------------------------------


def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    ignore_next = False
    for i in range(len(arr) - 1):
        if arr[i] == 0 and not ignore_next:
            arr[i + 2:] = arr[i + 1:-1]
            arr[i + 1] = 0
            ignore_next = True
        else:
            ignore_next = False



