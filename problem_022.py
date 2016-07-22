# Generate Parentheses - https://leetcode.com/problems/generate-parentheses/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        opn = "("
        cls = ")"
        if n == 0:
            return []
        s = [(opn, n - 1, n)]
        res = []
        while len(s) > 0:
            d, i, j = s.pop()
            if i == 0 and j == 0:
                res.append(d)
                continue
            if i > 0:
                s.append((d + opn, i - 1, j))
            if j > 0 and j > i:
                s.append((d + cls, i, j - 1))
        return res