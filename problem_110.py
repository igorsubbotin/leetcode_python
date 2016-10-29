# Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return getIsBalanced(root, 1)[0]
            
def getIsBalanced(node, depth):
    if node.left is None and node.right is None:
        return (True, depth)
    left_depth = depth
    left_balanced = True
    if node.left is not None:
        left_balanced, left_depth = getIsBalanced(node.left, depth + 1)
    right_depth = depth
    right_balanced = True
    if node.right is not None:
        right_balanced, right_depth = getIsBalanced(node.right, depth + 1)
    diff_balanced = abs(left_depth - right_depth) <= 1
    return (diff_balanced and left_balanced and right_balanced, max(left_depth, right_depth))