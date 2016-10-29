# Binary Tree Level Order Traversal II - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        s = []
        if root is not None:
            s.append((root, 0))
        while len(s) > 0:
            node, level = s.pop()
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.right is not None:
                s.append((node.right, level + 1))
            if node.left is not None:
                s.append((node.left, level + 1))
        res.reverse()
        return res