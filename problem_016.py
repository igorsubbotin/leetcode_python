# 3Sum Closest - https://leetcode.com/problems/3sum-closest/
import sys
from bisect import bisect

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mn = sys.maxint
        res = 0
        c = {}
        d = {}
        for i in xrange(len(nums)):
            d[nums[i]] = i
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                sm = nums[i] + nums[j]
                s = target - sm
                if min(abs(s - nums[0]), abs(s - nums[len(nums)-1])) >= mn:
                    continue
                ix = bisect(nums, s)
                for k in xrange(max(0, ix - 2), min(len(nums), ix + 3)):
                    if k == i or k == j:
                        continue
                    s = sm + nums[k]
                    diff = abs(target - s)
                    if diff < mn:
                        mn = diff
                        res = s
        return res