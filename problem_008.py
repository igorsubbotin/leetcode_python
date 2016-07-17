# String to Integer - https://leetcode.com/problems/string-to-integer-atoi/
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        sign, str = self.parseSign(str);
        str = self.normalize(str)
        if len(str) == 0:
            return 0
        res = sign * self.parseStr(str)
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res
        
    def parseSign(self, s):
        if len(s) == 0:
            return [1, s]
        c = s[0]
        if ord(c) == 43:
            return [1, s[1:]]
        elif ord(c) == 45:
            return [-1, s[1:]]
        else:
            return [1, s]
            
    def normalize(self, s):
        if len(s) == 0:
            return s
        res = ""
        for x in s:
            d = self.digitFromChar(x)
            if d < 0 or d > 9:
                return res
            res += x
        return res
    
    def parseStr(self, s):
        res = 0
        i = 1
        for x in reversed(s):
            res += self.digitFromChar(x) * i
            i *= 10
        return res
    
    def digitFromChar(self, c):
        return ord(c)-48