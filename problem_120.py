# Triangle - https://leetcode.com/problems/triangle/
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in xrange(1, n):
            for j in xrange(len(triangle[i])):
                v1 = triangle[i-1][max(0, j-1)]
                v2 = triangle[i-1][min(len(triangle[i-1])-1,j)]
                triangle[i][j] = min(triangle[i][j] + v1, triangle[i][j] + v2)
        return min(triangle[n-1])