# Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n, tail = getLengthAndTail(head)
        if n < 2:
            return head
        k = k % n
        if k == 0:
            return head
        tail.next = head
        node = head
        for _ in xrange(n - k - 1):
            node = node.next
        res = node.next
        node.next = None
        return res
        
def getLengthAndTail(l):
    n = 0
    tail = None
    while l is not None:
        n += 1
        tail = l
        l = l.next
    return n, tail