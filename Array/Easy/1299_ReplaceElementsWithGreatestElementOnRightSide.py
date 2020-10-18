# Given an array arr, replace every element in that array with the greatest element
# among the elements to its right, and replace the last element with -1.
# After doing so, return the array.
# Example 1:
#   Input: arr = [17,18,5,4,6,1]
#   Output: [18,6,6,6,1,-1]


def replaceElements(arr):
    for i in range(len(arr)):
        if i != len(arr) - 1:
            arr[i] = max(arr[i + 1:])
        else:
            arr[i] = -1
    return arr


# -----------------mETHOD 2

def replace(arr):
    m = -1
    i = len(arr) - 1
    while i >= 0:
        temp = arr[i]
        arr[i] = m
        if temp > m:
            m = temp
        i -= 1
    return arr