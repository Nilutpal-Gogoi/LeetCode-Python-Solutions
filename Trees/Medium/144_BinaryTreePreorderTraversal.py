# https://leetcode.com/problems/binary-tree-preorder-traversal/


class TreeNode:
    def __init__(self, value = 0, left=None, right = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root
        