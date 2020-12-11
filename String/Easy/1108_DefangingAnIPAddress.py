# https://leetcode.com/problems/defanging-an-ip-address/


def defangIPaddr(address):     # T.C : O(N) , S.C: O(n)
    result = ""
    for i in range(len(address)):
        if address[i] != ".":
            result += address[i]
        else:
            result += "[.]"
    return result


def defangIPAddr1(address):        # T.C : O(n) and S.C: O(1)
    return address.replace(".","[.]")

print(defangIPAddr1("255.100.50.0"))