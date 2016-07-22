# Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        node = dummy
        q = PriorityQueue()
        for x in lists:
            if x is not None:
                q.put((x.val, x))
        while not q.empty():
            val, item = q.get()
            node.next = item
            node = node.next
            if item.next is not None:
                q.put((item.next.val, item.next))
        return dummy.next