# Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        result = dummy
        node = head
        n = None
        while node is not None:
            if node.val != n:
                n = node.val
                result.next = ListNode(n)
                result = result.next
            node = node.next   
        return dummy.next