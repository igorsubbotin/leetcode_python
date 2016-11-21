# Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root is None:
            return res
        s = []
        i = 0
        s = [(root, "")]
        while i < len(s):
            node, path = s[i]
            path += str(node.val)
            if node.left is not None:
                s.append((node.left, path))
            if node.right is not None:
                s.append((node.right, path))
            if node.left is None and node.right is None:
                res += int(path)
            i += 1
        return res