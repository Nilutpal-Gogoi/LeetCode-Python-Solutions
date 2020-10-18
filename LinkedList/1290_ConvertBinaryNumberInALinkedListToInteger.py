# Given head which is a reference node to a singly-linked list. The value of each node
# in the linked list is either 0 or 1. The linked list holds the binary representation
# of a number.
# Return the decimal value of the number in the linked list.


def getDecimalValue(self, head):
    result = 0
    length = 0
    cursor = head
    while cursor:
        length += 1
        cursor = cursor.next
    cursor = head
    length = length - 1
    while length >= 0:
        result = result + cursor.val * (2 ** length)
        cursor = cursor.next
        length -= 1
    return result

