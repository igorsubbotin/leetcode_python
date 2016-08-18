# Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return fib(n)
        
c = {}
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in c:
        c[n] = fib(n - 1) + fib(n - 2)
    return c[n]