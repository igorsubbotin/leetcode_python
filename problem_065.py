# Valid Number - https://leetcode.com/problems/valid-number/
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if "e" in s:
            t = s.split("e");
            return len(t) <= 2 and isValidNumber(t[0], True) and isValidNumber(t[1], False)
        return isValidNumber(s, True)
    
def isValidNumber(s, allowDecimalDelimiter):
    if len(s) == 0:
        return False
    i = 0
    if s[0] == "-" or s[0] == "+":
        i = 1
    if i == len(s):
        return False
    if len(s) == i + 1 and s[i] == ".":
        return False
    delimiter = False
    while i < len(s):
        if not (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            if s[i] == ".":
                if delimiter or not allowDecimalDelimiter:
                    return False
                delimiter = True
            else:
                return False
        i += 1
    return True