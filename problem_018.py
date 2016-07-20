# 4Sum - https://leetcode.com/problems/4sum/
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        p = []
        d = {}
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                s = nums[i] + nums[j]
                a = (s, i, j)
                p.append(a)
                if s not in d:
                    d[s] = []
                d[s].append(a)
        r = set()
        res = []
        for s, i, j in p:
            x = target - s
            if x in d:
                for s2, k, l in d[x]:
                    if i != k and i != l and j != k and j != l:
                        lst = [nums[i], nums[j], nums[k], nums[l]]
                        lst.sort()
                        t = tuple(lst)
                        if t not in r:
                            r.add(t)
                            res.append(lst)
        return res   