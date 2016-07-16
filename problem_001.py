# Two Sum - https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            x = nums[i]
            for j in xrange(i + 1, len(nums)):
                y = nums[j]
                if x + y == target:
                    return [i, j]