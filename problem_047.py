# Permutations II - https://leetcode.com/problems/permutations-ii/
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        n = {}
        for i in xrange(len(nums)):
            if nums[i] not in n:
                n[nums[i]] = i
        for x in n:
            i = n[x]
            for j in self.permuteUnique(nums[:i] + nums[i + 1:]):
                v = [x] + j
                res.append(v)
        return res