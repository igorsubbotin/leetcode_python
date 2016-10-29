# Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
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
        for i in xrange(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        return res