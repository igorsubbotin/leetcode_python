# Subsets - https://leetcode.com/problems/subsets/
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        c = []
        for _ in xrange(n + 1):
            c.append([])
        c[n].append([])
        for i in reversed(xrange(n)):
            a = [nums[i]]
            c[i].append(a)
            for j in xrange(i + 1, n):
                for x in c[j]:
                    c[i].append(a + x)
        res = []
        for x in c:
            res += x
        return res