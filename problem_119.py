# Pascal's Triangle II - https://leetcode.com/problems/pascals-triangle-ii/
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in xrange(rowIndex + 1):
            result.append(1)
            for j in reversed(xrange(i / 2)):
                v = result[j] + result[j+1]
                result[j+1] = v
                result[len(result) - j - 2] = v
        return result