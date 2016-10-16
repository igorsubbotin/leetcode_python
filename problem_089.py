# Gray Code - https://leetcode.com/problems/gray-code/
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = self.grayCode(n-1)
        num = 1 << (n-1)
        for i in reversed(xrange(len(res))):
            res.append(num + res[i])
        return res