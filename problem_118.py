# Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = []
        for i in xrange(numRows):
            a.append([1] * (i + 1))
            for j in xrange(i / 2):
                v = a[i - 1][j] + a[i - 1][j + 1]
                jx = j + 1
                a[i][jx] = v
                a[i][len(a[i]) - jx - 1] = v
        return a