# 3Sum - https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        r = set()
        res = []
        for i in xrange(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    l = [nums[i], nums[j], nums[k]]
                    l.sort()
                    t = tuple(l)
                    if t not in r:
                        r.add(t)
                        res.append(l)
                    j += 1
                    continue
                if s < 0:
                    j += 1
                else:
                    k -= 1
        return res
        