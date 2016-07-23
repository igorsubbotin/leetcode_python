# Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k < 2:
            return head
        ln = 0
        node = head
        while node is not None:
            node = node.next
            ln += 1
        dummy = ListNode(0)
        dummy.next = head
        end = dummy
        last = dummy
        t = ln / k
        for i in xrange(t):
            j = k
            head = end.next
            end = head
            while j > 1:
                next = end.next
                end.next = next.next
                next.next = head
                head = next
                j -= 1
            last.next = head
            last = end
        return dummy.next