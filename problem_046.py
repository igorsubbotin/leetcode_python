# Permutations - https://leetcode.com/problems/permutations/
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in xrange(len(nums)):
            n = nums[i]
            for j in self.permute(nums[:i] + nums[i + 1:]):
                res.append([n] + j)
        return res