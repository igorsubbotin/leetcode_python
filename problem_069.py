# Sqrt(x) - https://leetcode.com/problems/sqrtx/
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return findSquare(x, 1, 47000)
        
def findSquare(n, left, right):
    mid = (left + right) / 2
    square = mid * mid
    if n < square:
        check = (mid - 1) * (mid - 1)
        if n >= check:
            return mid - 1
        return findSquare(n, left, mid)
    elif n > square:
        check = (mid + 1) * (mid + 1)
        if n == check:
            return mid + 1
        if n < check:
            return mid
        return findSquare(n, mid, right)
    else:
        return mid