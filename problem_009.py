# Palindrome Number - https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        i = x
        ln = 0
        while i > 0:
            ln += 1
            i /= 10
        for i in xrange(ln / 2):
            right = (x / 10 ** i) % 10
            left = (x / 10 ** (ln - i - 1)) % 10
            if right != left:
                return False
        return True