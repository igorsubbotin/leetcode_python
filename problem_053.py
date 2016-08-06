# Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        s = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] >= s + nums[i]:
                s = nums[i]
            else:
                s += nums[i]
            res = max(res, s)
        return res