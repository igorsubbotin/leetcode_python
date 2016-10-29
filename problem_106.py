# Construct Binary Tree from Inorder and Postorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        if n == 0:
            return None
        d = {}
        for i in xrange(n):
            d[inorder[i]] = i
        postorder.reverse()
        res = TreeNode(postorder[0])
        s = [res]
        i = 1
        while i < n:
            node = TreeNode(postorder[i])
            head = peek(s)
            if d[node.val] > d[head.val]:
                head.right = node
            else:
                while True:
                    p = peek(s)
                    if p is None or d[p.val] < d[node.val]:
                        break
                    head = s.pop()
                head.left = node
            s.append(node)
            i += 1
        return res
        
def peek(s):
    if len(s) == 0:
        return None
    return s[len(s) - 1]