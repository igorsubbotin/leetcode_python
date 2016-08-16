# Spiral Matrix - https://leetcode.com/problems/spiral-matrix/
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        c = 0
        i = 0
        j = 0
        borders = [0, n - 1, m - 1, 0]
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        k = 0
        while c < m * n:
            res.append(matrix[i][j])
            if i + d[k][0] < borders[0] or j + d[k][1] > borders[1] or i + d[k][0] > borders[2] or j + d[k][1] < borders[3]:
                borders[k] += (-1) ** (((k % 3) + 2) / 3)
                k = (k + 1) % 4
            i += d[k][0]
            j += d[k][1]
            c += 1
        return res