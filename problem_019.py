# Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        a = []
        while node is not None:
            a.append(node)
            node = node.next
        ix = len(a) - n
        if ix == 0:
            return head.next
        a[ix-1].next = None
        if ix < len(a) - 1:
            a[ix-1].next = a[ix+1]
        return head