# Minimum Depth of Binary Tree - https://leetcode.com/problems/minimum-depth-of-binary-tree/
from Queue import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q = Queue()
        q.put((root, 1))
        while not q.empty():
            node, depth = q.get()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                q.put((node.left, depth + 1))
            if node.right is not None:
                q.put((node.right, depth + 1))