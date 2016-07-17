# Reverse Integer - https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = self.getSign(x)
        x = x / sign
        a = []
        while x != 0:
            a.append(x % 10)
            x /= 10
        res = 0
        a.reverse()
        i = 1
        for x in a:
            res += x * i
            i *= 10
        if res > 2147483647:
            return 0
        return res * sign
    
    def getSign(self, n):
        return n / abs(n)