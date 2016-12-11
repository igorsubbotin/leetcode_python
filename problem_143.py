# Reorder List - https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        n = 0
        node = head
        while node is not None:
            n += 1
            node = node.next
        i = 0
        mid = (n - 1) / 2
        node = head
        while i != mid:
            node = node.next
            i += 1
        head2 = reverse(node.next)
        node.next = None
        dummy = ListNode(0)
        node = dummy
        first = True
        while True:
            if head is None and head2 is None:
                break
            if first:
                node.next = head
                head = head.next
            else:
                node.next = head2
                head2 = head2.next
            first = not first
            node = node.next
            
def reverse(head):
    if head is None:
        return None
    prev = head
    node = head.next
    head.next = None
    while node is not None:
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt
    return prev