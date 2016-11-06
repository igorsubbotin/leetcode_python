# Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = -sys.maxint
        if root is None:
            return res
        q = [root]
        i = 0
        while i < len(q):
            node = q[i]
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            i += 1
        for node in reversed(q):
            left = 0
            if node.left is not None:
                left = node.left.val
            right = 0
            if node.right is not None:
                right = node.right.val
            res = max(res, node.val + left + right, node.val, node.val + left, node.val + right)
            node.val = max(node.val + left, node.val + right, node.val)
        return res