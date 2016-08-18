# Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/
from bisect import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        master = []
        for i in xrange(len(matrix)):
            master.append(matrix[i][0])
        line_ix = bisect(master, target) - 1
        if line_ix >= 0:
            ix = bisect(matrix[line_ix], target) - 1
            if ix >= 0:
                return matrix[line_ix][ix] == target
        return False