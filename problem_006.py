# ZigZag Conversion - https://leetcode.com/problems/zigzag-conversion/
from Queue import Queue

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ""
        step = numRows * 2 - 2
        for i in xrange(numRows):
            j = i
            while j < len(s):
                res += s[j]
                if i != 0 and i != numRows - 1:
                    mid = j + step - i * 2
                    if mid < len(s):
                        res += s[mid]
                j += step
                
        return res