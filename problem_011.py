# Container With Most Water - https://leetcode.com/problems/container-with-most-water/
from copy import copy

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        res = 0
        for i in xrange(len(height)):
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res