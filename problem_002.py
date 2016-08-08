# Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
        shift = 0
        while l1 is not None or l2 is not None:
            a1 = 0
            if l1 is not None:
                a1 = l1.val
                l1 = l1.next
            a2 = 0
            if l2 is not None:
                a2 = l2.val
                l2 = l2.next
            sm = a1 + a2 + shift
            shift = sm / 10
            head.next = ListNode(sm % 10)
            head = head.next
        if shift > 0:
            head.next = ListNode(shift)
        return dummy.next