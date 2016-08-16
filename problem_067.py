# Add Binary - https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        overflow = False
        res = ""
        i = 0
        while i < max(len(a), len(b)):
            v = getValue(i, a) + getValue(i, b)
            if overflow:
                v += 1
            overflow = False
            if v / 2 > 0:
                overflow = True
            v = v % 2
            res = str(v) + res
            i += 1
        if overflow:
            res = str(1) + res
        return res
        
def getValue(i, s):
    n = len(s)
    ix = n - i - 1
    if ix < 0:
        return 0
    return int(s[ix])