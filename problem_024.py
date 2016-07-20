# Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        node = head
        while node is not None:
            if node.next is None:
                break
            first = node
            second = node.next
            third = second.next
            t = second
            second = first
            first = t
            prev.next = first
            first.next = second
            second.next = third
            prev = second
            node = third
        return dummy.next