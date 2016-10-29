# Flatten Binary Tree to Linked List - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.head = TreeNode(0)
        self.visit(root)
        
    def visit(self, node):
        if node is None:
            return
        self.head.right = node
        self.head = node
        left = node.left
        right = node.right
        node.left = None
        node.right = None
        self.visit(left)
        self.visit(right)