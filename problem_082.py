# Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
        d = {}
        node = head
        while node is not None:
            if node.val not in d:
                d[node.val] = 0
            d[node.val] += 1
            node = node.next
        dummy = ListNode(0)
        result = dummy
        node = head
        while node is not None:
            if d[node.val] == 1:
                result.next = ListNode(node.val)
                result = result.next
            node = node.next
        return dummy.next