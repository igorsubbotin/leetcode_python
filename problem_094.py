# Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        s = []
        s.append((root, False))
        while len(s) > 0:
            node, v = s.pop()
            if node is None:
                continue
            if v:
                res.append(node.val)
                continue
            if node.right is not None:
                s.append((node.right, False))
            s.append((node, True))
            if node.left is not None:
                s.append((node.left, False))
        return res