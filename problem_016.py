# 3Sum Closest - https://leetcode.com/problems/3sum-closest/
import sys

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
        for i in xrange(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = abs(target - s)
                if diff == 0:
                    return s
                if diff < mn:
                    mn = diff
                    res = s
                if s < target:
                    j += 1
                else:
                    k -= 1
        return res