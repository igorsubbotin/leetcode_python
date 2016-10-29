# Path Sum II - https://leetcode.com/problems/path-sum-ii/
from copy import copy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        s = [(root, root.val, [root.val])]
        while len(s) > 0:
            node, current_sum, path = s.pop()
            if node.left is None and node.right is None and current_sum == sum:
                res.append(path)
                continue
            if node.left is not None:
                s.append((node.left, current_sum + node.left.val, copy(path) + [node.left.val]))
            if node.right is not None:
                s.append((node.right, current_sum + node.right.val, copy(path) + [node.right.val]))
        return res