# Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return isValidBSTRecursive(root)[0]

def isValidBSTRecursive(root):
    if root is None:
        return (True, None, None)
    valid = True
    minValue = root.val
    maxValue = root.val
    if root.left is not None:
        validLeft, mn, mx = isValidBSTRecursive(root.left)
        valid &= validLeft and root.val > mx
        maxValue = max(maxValue, mx)
        minValue = min(minValue, mn)
    if root.right is not None:
        validRight, mn, mx = isValidBSTRecursive(root.right)
        valid &= validRight and root.val < mn
        maxValue = max(maxValue, mx)
        minValue = min(minValue, mn)
    return (valid, minValue, maxValue)