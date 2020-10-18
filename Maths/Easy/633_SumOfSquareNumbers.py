# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
# Example 1:
#   Input: 5
#   Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
#   Input: 3
#   Output: False


def judgeSquareSum(c):
    a = 0
    b = 0
    while a * a <= c:
        while b * b <= c:
            if (a * a) + (b * b) == c:
                return True
            b += 1
        b = 0
        a += 1
    return False

print(judgeSquareSum(999999999))