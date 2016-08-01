# Longest Valid Parentheses - https://leetcode.com/problems/longest-valid-parentheses/
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [0] * (len(s) + 1)
        stk = []
        mx = 0
        for i in xrange(len(s)):
            x = s[i]
            if x == "(":
                stk.append(a[i])
            else:
                if len(stk) > 0:
                    v = stk.pop() + a[i] + 2
                    a[i+1] = v
                    mx = max(mx, v) 
        return mx