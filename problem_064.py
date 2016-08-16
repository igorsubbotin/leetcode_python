# Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        for i in xrange(n):
            for j in xrange(m):
                grid[i][j] += getMin(i, j, grid)
        return grid[n - 1][m - 1]
    
def getMin(i, j, grid):
    if i == 0 and j == 0:
        return 0
    if i - 1 < 0:
        return grid[i][j - 1]
    elif j - 1 < 0:
        return grid[i - 1][j]
    return min(grid[i][j - 1], grid[i - 1][j])