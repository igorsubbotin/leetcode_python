# Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        i = 1
        dummy = ListNode(0)
        node = head
        cur = dummy
        internal = None
        internal_tail = None
        while node is not None:
            nxt = node.next
            if i < m or i > n:
                cur.next = node
                cur = node
            if i == m:
                internal_head = node
                internal_tail = node
                node.next = None
            if i > m and i < n:
                node.next = internal_head
                internal_head = node
            if i == n:
                node.next = internal_head
                cur.next = node
                cur = internal_tail
            i += 1
            node = nxt
        return dummy.next