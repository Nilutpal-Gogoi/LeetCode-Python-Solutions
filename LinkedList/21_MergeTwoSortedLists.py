# Merge two sorted linked lists and return it as a new sorted list. The new list should
# be made by splicing together the nodes of the first two lists.
# Example:
#   Input: 1->2->4, 1->3->4
#   Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = l1
        second = l2
        if not first:
            return second
        if not second:
            return first
        if first.val < second.val:
            third = last = first
            first = first.next
        else:
            third = last = second
            second = second.next
        while first and second:
            if first.val < second.val:
                last.next = first
                last = first
                first = first.next
            else:
                last.next = second
                last = second
                second = second.next
        if first != None:
            last.next = first
        else:
            last.next = second
        return third