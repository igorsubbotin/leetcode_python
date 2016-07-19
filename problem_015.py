# 3Sum - https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        p = []
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                p.append(([nums[i] + nums[j], i, j, nums[i], nums[j]]))
        d = {}
        for i in xrange(len(nums)):
            n = nums[i]
            if n not in d:
                d[n] = set()
            d[n].add(i)
        r = set()
        res = []
        for s, i, j, a, b in p:
            c = 0 - s
            if c in d:
                ix = d[c]
                ln = len(ix)
                if i in ix:
                    ln -= 1
                if j in ix:
                    ln -= 1
                if ln > 0:
                    l = [a, b, c]
                    l.sort()
                    t = tuple(l)
                    if t not in r:
                        r.add(t)
                        res.append(l)
        return res
        