# Symmetric Tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return iterative(root)
        #return recursive(root)
        
def iterative(root):
    if root is None: return True
    a = [root.left]
    b = [root.right]
    while len(a) > 0 or len(b) > 0:
        ax = a.pop()
        bx = b.pop()
        if ax is None and bx is None:
            continue
        if ax is None or bx is None or ax.val != bx.val:
            return False
        a.append(ax.left)
        a.append(ax.right)
        b.append(bx.right)
        b.append(bx.left)
    return True
        
def recursive(root):
    if root is None: return True
    return traverseNode(root.left, False) == traverseNode(root.right, True)
        
def traverseNode(node, rev):
    res = []
    if node is None:
        res += [None]
    else:
        res += [node.val]
        left = traverseNode(node.left, rev)
        right = traverseNode(node.right, rev)
        if rev:
            res += right + left
        else:
            res += left + right
    return res