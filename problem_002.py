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
        x = self.getNumber(l1) + self.getNumber(l2)
        return self.getList(x)
        
    def getNumber(self, l):
        i = 1
        res = 0
        while l is not None:
            res += l.val * i
            i *= 10
            l = l.next
        return res
    
    def getList(self, n):
        l = ListNode(0)
        res = l
        while True:
            l.val = n % 10
            n /= 10
            if n == 0:
                return res
            l.next = ListNode(0)
            l = l.next