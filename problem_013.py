# Roman to Integer - https://leetcode.com/problems/roman-to-integer/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        if len(s) == 0:
            return 0
        a = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        i = 0
        while len(s) > 0:
            c = s.pop()
            n = a[c]
            if n < i:
                res -= n
            else:
                i = n
                res += n
        return res