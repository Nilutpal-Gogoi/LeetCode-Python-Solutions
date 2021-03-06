# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
#   Given linked list: 1->2->3->4->5, and n = 2.
#   After removing the second node from the end, the linked list becomes 1->2->3->5.


def removeNthFromEnd(self, head, n):
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
    if not fast:
        return slow.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head