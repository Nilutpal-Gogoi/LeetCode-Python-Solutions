# Given a non-empty, singly linked list with head node head, return a middle node
# of linked list. If there are two middle nodes, return the second middle node.
# Example 1:
#   Input: [1,2,3,4,5]
#   Output: Node 3 from this list (Serialization: [3,4,5])
#   The returned node has value 3.  (The judge's serialization of this node is
#   [3,4,5]).
#   Note that we returned a ListNode object ans, such that:
#   ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and
#   ans.next.next.next = NULL.
# Example 2:
#   Input: [1,2,3,4,5,6]
#   Output: Node 4 from this list (Serialization: [4,5,6])
#   Since the list has two middle nodes with values 3 and 4, we return the second
#   one.
# Note:
#   The number of nodes in the given list will be between 1 and 100.


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
        return

    def middleNode1(self):    # In this 123456 , 4 is the middle element
        slow = self.head
        fast = self.head
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        return slow.data

    def find_mid(self):
        fast = self.head
        slow = self.head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            if fast:
                slow = slow.next
        return slow.data


lst = LinkedList()
lst.insertAtHead(6)
lst.insertAtHead(5)
lst.insertAtHead(4)
lst.insertAtHead(3)
lst.insertAtHead(2)
lst.insertAtHead(1)
print(lst.find_mid())


