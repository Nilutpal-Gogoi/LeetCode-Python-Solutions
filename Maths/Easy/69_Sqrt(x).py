# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative
# integer. Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# Example 1:
#   Input: 4
#   Output: 2
# Example 2:
#   Input: 8
#   Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.


# --------------------- Newton Method -----------------------------------
def mySqrt(num):
    r = num
    while r*r > num:
        r = (r+num//r)//2
    return r

# ------------------- Binary search -----------------------------------------


def mySqrt1(num):
    low = 0
    high = num
    while low<high:
        mid = low + (high-low)//2
        if mid*mid == num:
            return mid
        elif mid*mid > num:
            high = mid -1
        else:
            low = mid + 1
        return high-1

print(mySqrt1(8))