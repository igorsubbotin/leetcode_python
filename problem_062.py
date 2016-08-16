# Unique Paths - https://leetcode.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = n + m - 2
        k = m - 1
        return factorial(N) / (factorial(k) * factorial(N - k))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return n * factorial(n - 1)