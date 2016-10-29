# Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        s = [(root, root.val)]
        while len(s) > 0:
            node, current_sum = s.pop()
            if node.left is None and node.right is None and current_sum == sum:
                return True
            if node.left is not None:
                s.append((node.left, current_sum + node.left.val))
            if node.right is not None:
                s.append((node.right, current_sum + node.right.val))
        return False