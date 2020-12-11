# Remove all elements from a linked list of integers that have value val.
# Example:
#   Input:  1->2->6->3->4->5->6, val = 6
#   Output: 1->2->3->4->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def removeElements(head, val):
    cursor = head
    prev = None
    while cursor:
        if cursor.val == val:
            if prev:
                prev.next = cursor.next
                cursor = prev
            else:
                head = head.next
        else:
            prev = cursor
        cursor = cursor.next
    return head
