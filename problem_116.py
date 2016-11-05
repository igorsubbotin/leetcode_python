# Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        level = 0
        prev = None
        q = []
        q.append((root, 0))
        i = 0
        while i < len(q):
            node, l = q[i]
            if l == level and prev is not None:
                prev.next = node
            if node.left is not None:
                q.append((node.left, l + 1))
            if node.right is not None:
                q.append((node.right, l + 1))
            prev = node
            level = l
            i += 1