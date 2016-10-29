# Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        s = []
        if root is not None:
            s.append((root, 1))
        while len(s) > 0:
            node, level = s.pop()
            res = max(level, res)
            if node.left is not None:
                s.append((node.left, level + 1))
            if node.right is not None:
                s.append((node.right, level + 1))
        return res