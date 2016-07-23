# Count and Say - https://leetcode.com/problems/count-and-say/
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1x"
        res = "1"
        for _ in xrange(n - 1):
            c = 1
            res = ""
            for i in xrange(len(s) - 1):
                if s[i] != s[i + 1]:
                    res += str(c) + s[i]
                    c = 0
                c += 1
            s = res + "x"
        return res