# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can
# only be used once).
# Return the sum of lengths of all good strings in words.
#
# Example 1:
#   Input: words = ["cat","bt","hat","tree"], chars = "atach"
#   Output: 6
#   Explanation:
#      The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#   Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
#   Output: 10
#   Explanation:
#      The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
# Note:
#   1 <= words.length <= 1000
#   1 <= words[i].length, chars.length <= 100
#   All strings contain lowercase English letters only.


def countCharacters(words, chars):
    prime_set = dict()
    for i in range(len(chars)):
        if chars[i] in prime_set:
            prime_set[chars[i]] += 1
        else:
            prime_set[chars[i]] = 1
    secondary_set = dict()
    for string in words:
        for index in range(len(string)):
            if string[index] in secondary_set:
                secondary_set[string[index]] += 1
            else:
                secondary_set[string[index]] = 1
        for key, value in secondary_set.items():
            if key in prime_set:
                if secondary_set[key] <= prime_set[key]:
                    continue


countCharacters(["cat","bt","hat","tree"], "atach")