# Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.add(i)
                    if j not in cols:
                        cols.add(j)
        for ix in rows:
            zeroRow(matrix, ix)
        for ix in cols:
            zeroColumn(matrix, ix)
            
def zeroRow(matrix, ix):
    for i in xrange(len(matrix[0])):
        matrix[ix][i] = 0

def zeroColumn(matrix, ix):
    for i in xrange(len(matrix)):
        matrix[i][ix] = 0