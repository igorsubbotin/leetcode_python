# Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/
from Queue import PriorityQueue
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        q = PriorityQueue()
        q.put((0, 0, grid[0][0]))
        v = set()
        while not q.empty():
            i, j, p = q.get()
            if i == n - 1 and j == m - 1:
                return p
            if (i, j) in v:
                continue
            v.add((i, j))
            if i + 1 < n:
                q.put((i + 1, j, p + grid[i + 1][j]))
            if j + 1 < m:
                q.put((i, j + 1, p + grid[i][j + 1]))