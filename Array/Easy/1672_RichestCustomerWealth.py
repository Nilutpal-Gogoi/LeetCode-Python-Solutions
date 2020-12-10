# https://leetcode.com/problems/richest-customer-wealth/


def maximumWealth(accounts):
    result = []
    for i in range(len(accounts)):
        result.append(sum(accounts[i]))
    return max(result)