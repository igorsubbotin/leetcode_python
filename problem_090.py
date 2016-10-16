# Subsets II - https://leetcode.com/problems/subsets-ii/
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cache = {}
        nums.sort()
        return [[]] + subset(cache, nums, 0)

def subset(cache, nums, start):
    if start not in cache:
        r = set()
        res = []
        n = nums[start:]
        for i in xrange(len(n)):
            c = [n[i]]
            add(c, r, res)
            for j in xrange(i + 1, len(n)):
                for k in subset(cache, n, j):
                    add(k, r, res)
                    add(c + k, r, res)
        cache[start] = res
    return cache[start]
    
def add(c, r, res):
    t = tuple(c)
    if t not in r:
        r.add(t)
        res.append(c)