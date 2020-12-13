# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


def maxDepth(s):
    count = 0
    temp = 0
    for i in s:
        if i == "(" or i == ")":
            if i == "(":
                if temp == count:
                    temp += 1
                    count += 1
                else:
                    temp += 1
            else:
                temp -= 1
    return count


# print(maxDepth("1"))

