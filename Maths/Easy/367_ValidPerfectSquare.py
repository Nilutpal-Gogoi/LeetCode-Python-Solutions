# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.
# Example 1:
#   Input: num = 16
#   Output: true
# Example 2:
#   Input: num = 14
#   Output: false


# -------------------- Linear Method ----------------------------------------
def isPerfectsquare(num):
    i = 1
    while i*i <= num:
        if num%i == 0 and num/i == i:
            return True
        i += 1
    return False

# --------------------- Newtons Method ---------------------------------------


def isPerfectsquare1(nums):
    r = nums
    while r*r > nums:
        r = (r+nums/r)//2
    return r*r==nums

# --------------------- Binary Search -------------------------------------------


def isPerfectsquare2(nums):
    start = 0
    end = nums
    while start <= end:
        mid = start+(end-start)//2
        if mid**2 == nums:
            return True
        elif mid**2 < nums:
            start = mid + 1
        else:
            end = mid - 1
    return False


print(isPerfectsquare2(67))