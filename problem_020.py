# Valid Parentheses - https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for c in s:
            code = self.getCode(c)
            if code > 0:
                a.append(code)
            else:
                if len(a) == 0 or code + a.pop() != 0:
                    return False
        return len(a) == 0
        
    def getCode(self, c):
        if c == "(":
            return 1
        if c == ")":
            return -1
        if c == "[":
            return 2
        if c == "]":
            return -2
        if c == "{":
            return 3
        if c == "}":
            return -3