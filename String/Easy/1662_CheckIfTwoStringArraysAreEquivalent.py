# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


def arrayStringsAreEqual(word1, word2):
    result1 = ""
    result2 = ""
    for i in range(len(word1)):
        result1 += word1[i]
    for i in range(len(word2)):
        result2 += word2[i]
    if len(result1) != len(result2):
        return False
    else:
        for i in range(len(result1)):
            if result1[i] != result2[i]:
                return False
            else:
                continue
    return True


print(arrayStringsAreEqual(["a", "cb"],["ab", "c"]))