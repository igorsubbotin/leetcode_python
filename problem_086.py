# Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        left = dummy
        dummy_right = ListNode(0)
        right = dummy_right
        while head is not None:
            node = ListNode(head.val)
            if node.val < x:
                left.next = node
                left = node
            else:
                right.next = node
                right = node
            head = head.next
        left.next = dummy_right.next
        return dummy.next