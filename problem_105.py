# Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        res = []
        if len(preorder) == 0 or len(inorder) == 0:
            return res
        d = {}
        for i in xrange(len(inorder)):
            d[inorder[i]] = i
        res = TreeNode(preorder[0])
        s = [res]
        i = 1
        while i < len(preorder):
            node = TreeNode(preorder[i])
            head = peek(s)
            if d[head.val] > d[node.val]:
                head.left = node
            else:
                while True:
                    p = peek(s)
                    if p is None or d[p.val] > d[node.val]:
                        break
                    head = s.pop()
                head.right = node
            s.append(node)
            i += 1
        return res
        
def peek(s):
    if len(s) == 0:
        return None
    return s[len(s) - 1]