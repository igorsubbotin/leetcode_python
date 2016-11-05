# Populating Next Right Pointers in Each Node II - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

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
        q = []
        q.append((root, 0))
        level = 0
        i = 0
        prev = None
        while i < len(q):
            node, l = q[i]
            if level == l and prev is not None:
                prev.next = node
            if node.left is not None:
                q.append((node.left, l + 1))
            if node.right is not None:
                q.append((node.right, l + 1))
            i += 1
            prev = node
            level = l