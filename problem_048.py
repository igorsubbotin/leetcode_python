# Rotate Image - https://leetcode.com/problems/rotate-image/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in xrange(n / 2):
            shiftMatrixLevel(n, matrix, i)
        
def shiftMatrixLevel(n, matrix, level):
    for j in xrange(3):
        for i in xrange(n - level * 2 - 1):
            if j == 0:
                i1 = level
                j1 = level + i
                i2 = n - level - i - 1
                j2 = level
            elif j == 1:
                i1 = level + i + 1
                j1 = level
                i2 = n - level - 1
                j2 = level + i + 1
            elif j == 2:
                i1 = n - level - 1
                j1 = level + i + 1
                i2 = n - level - i - 2
                j2 = n - level - 1
            swap(matrix, i1, j1, i2, j2)
                
def swap(matrix, i1, j1, i2, j2):
    t = matrix[i1][j1]
    matrix[i1][j1] = matrix[i2][j2]
    matrix[i2][j2] = t