# Container With Most Water - https://leetcode.com/problems/container-with-most-water/
from copy import copy

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = copy(height)
        a.sort()
        d = {}
        s = {}
        j = 0
        for i in xrange(len(a)):
            h = a[i]
            if h not in d:
                d[h] = j
                s[j] = h
                j += 1
        for i in xrange(len(height)):
            h = height[i]
            height[i] = d[h]
        left = [-1] * len(d) 
        right = [-1] * len(d)
        mx = 0
        for i in xrange(len(height)):
            h = height[i]
            for j in xrange(mx, h + 1):
                left[j] = i
            mx = max(mx, h + 1)
        mx = 0
        for i in xrange(len(height)):
            ix = len(height) - i - 1
            h = height[ix]
            for j in xrange(mx, h + 1):
                right[j] = ix
            mx = max(mx, h + 1)
        res = 0
        for i in xrange(len(d)):
            res = max(res, (right[i] - left[i]) * s[i]) 
        return res