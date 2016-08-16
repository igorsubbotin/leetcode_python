# Unique Paths II - https://leetcode.com/problems/unique-paths-ii/
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        grid = []
        for i in xrange(n):
            grid.append([0] * m)
        for i in reversed(xrange(n)):
            for j in reversed(xrange(m)):
                grid[i][j] = getScore(i, j, n, m, grid, obstacleGrid)
        return grid[0][0]
                
def getScore(i, j, n, m, grid, obstacleGrid):
    score = 0
    if obstacleGrid[i][j] == 1:
        return score
    if i == n - 1 and j == m - 1:
        return 1
    if i + 1 < n:
        score += grid[i + 1][j]
    if j + 1 < m:
        score += grid[i][j + 1]
    return score