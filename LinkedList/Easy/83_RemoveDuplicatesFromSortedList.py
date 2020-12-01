# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


def deleteDuplicates(head):
    cursor = head
    prev = None
    duplicates = dict()
    while cursor:
        if cursor.val in duplicates:
            prev.next = cursor.next
            cursor = None
        else:
            duplicates[cursor.val] = 1
            prev = cursor
        cursor = prev.next
    return head