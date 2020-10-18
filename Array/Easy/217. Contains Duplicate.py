# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# Example 1:
#   Input: [1,2,3,1]
#   Output: true
# Example 2:
#   Input: [1,2,3,4]
#   Output: false
# Example 3:
#   Input: [1,1,1,3,3,4,3,2,4,2]
#   Output: true


# ---------------------------- Solution 1: Brute Force -----------------------------------------------------------------
def CheckDuplicatesInArray(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# Time Complexity - O(n2), space complexity - O(1)

# ---------------------------- Solution 2: Using Sorting Technique (Improved Time Complexity) -------------------------


def CheckDuplicatesInArray2(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False

# Time COmplexity - O(nlogn) , Space Complexity - O(1)

# ------------------------ Solution 3: Using HashTable -----------------------------


def CheckDuplicatesInArray3(arr):
    temp = {}
    for i in range(len(arr)):
        if arr[i] not in temp:
            temp[arr[i]] = 1
        else:
            return True
    return False

# Time COmplexity - O(n) , Space Complexity - O(n)
print(CheckDuplicatesInArray3([1,2,3,1]))