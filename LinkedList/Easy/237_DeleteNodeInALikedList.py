# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
# Given linked list -- head = [4,5,1,9], which looks like following:
# Example 1:
#   Input: head = [4,5,1,9], node = 5
#   Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should
# become 4 -> 1 -> 9 after calling your function.
# Example 2:
#   Input: head = [4,5,1,9], node = 1
#   Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should
# become 4 -> 5 -> 9 after calling your function.
# Note:
#  > The linked list will have at least two elements.
#  > All of the nodes' values will be unique.
#  > The given node will not be the tail and it will always be a valid node of the
#    linked list.
#  > Do not return anything from your function.


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList:
    def deleteNode(self, node):
        while node:
            if node.next:
                node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                temp = node
                node.next = temp.next.next
                return

# In this question the head node is not given, so we copy the next element into that
# node and then delete the last node.


