# https://leetcode.com/problems/valid-palindrome/


def isPalindrome(s):
    if s == "":
        return True
    result = ""
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57:
            result += s[i]
    left = 0
    right = len(result) - 1
    while left <= right:
        if result[left].lower() != result[right].lower():
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))